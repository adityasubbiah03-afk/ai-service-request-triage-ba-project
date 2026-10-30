"""Train, evaluate and report on the triage classifier.

Outputs (all written to reports/):
  metrics.json, classification_report.txt, confusion_matrix.png,
  threshold_tradeoff.csv/.png, fairness_by_group.csv, baseline_comparison.csv,
  top_terms_by_category.csv

Usage:  python -m src.train_model
"""
import json

import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    f1_score,
    recall_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from .config import (
    CATEGORIES,
    CONFIDENCE_THRESHOLD,
    DATA_PATH,
    MODEL_PATH,
    RANDOM_SEED,
    REPORTS_DIR,
)
from .generate_data import generate
from .triage import ACTION_AUTO, ACTION_MANUAL, ACTION_PRIORITY, ACTION_SAFETY, TriageService


def build_pipeline(classifier=None) -> Pipeline:
    return Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True, lowercase=True)),
            ("clf", classifier or LogisticRegression(max_iter=1000, C=4.0, class_weight="balanced")),
        ]
    )


def load_data() -> pd.DataFrame:
    if not DATA_PATH.exists():
        DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        generate().to_csv(DATA_PATH, index=False)
    return pd.read_csv(DATA_PATH)


def threshold_tradeoff(y_true, proba, classes) -> pd.DataFrame:
    pred = classes[np.argmax(proba, axis=1)]
    conf = proba.max(axis=1)
    rows = []
    for t in np.arange(0.30, 0.96, 0.05):
        mask = conf >= t
        rows.append(
            {
                "threshold": round(float(t), 2),
                "auto_suggest_coverage": round(float(mask.mean()), 4),
                "accuracy_when_suggested": round(float(accuracy_score(y_true[mask], pred[mask])), 4) if mask.any() else np.nan,
                "sent_to_manual_queue": round(float(1 - mask.mean()), 4),
            }
        )
    return pd.DataFrame(rows)


def fairness_table(test_df: pd.DataFrame, pred: np.ndarray) -> pd.DataFrame:
    rows = []
    for col in ["writing_style", "region", "channel"]:
        for group, sub in test_df.assign(pred=pred).groupby(col):
            rows.append(
                {
                    "attribute": col,
                    "group": group,
                    "n": len(sub),
                    "accuracy": round(accuracy_score(sub["category"], sub["pred"]), 4),
                    "macro_f1": round(f1_score(sub["category"], sub["pred"], average="macro"), 4),
                }
            )
    out = pd.DataFrame(rows)
    out["accuracy_gap_vs_best_in_attribute"] = out.groupby("attribute")["accuracy"].transform(lambda s: (s.max() - s).round(4))
    return out


def top_terms(model: Pipeline, k: int = 8) -> pd.DataFrame:
    vec, clf = model.named_steps["tfidf"], model.named_steps["clf"]
    names = np.array(vec.get_feature_names_out())
    rows = []
    for i, cls in enumerate(clf.classes_):
        for rank, j in enumerate(np.argsort(clf.coef_[i])[::-1][:k], start=1):
            rows.append({"category": cls, "rank": rank, "term": names[j], "weight": round(float(clf.coef_[i][j]), 3)})
    return pd.DataFrame(rows)


def main() -> None:
    REPORTS_DIR.mkdir(exist_ok=True)
    df = load_data()
    train_df, test_df = train_test_split(df, test_size=0.25, stratify=df["category"], random_state=RANDOM_SEED)

    # Baselines to show the model adds value
    baselines = {}
    for name, clf in {
        "Majority class (dummy)": DummyClassifier(strategy="most_frequent"),
        "Naive Bayes (TF-IDF)": MultinomialNB(alpha=0.3),
        "Logistic regression (TF-IDF) [chosen]": None,
    }.items():
        pipe = build_pipeline(clf)
        pipe.fit(train_df["text"], train_df["category"])
        p = pipe.predict(test_df["text"])
        baselines[name] = {
            "accuracy": round(accuracy_score(test_df["category"], p), 4),
            "macro_f1": round(f1_score(test_df["category"], p, average="macro"), 4),
        }
    pd.DataFrame(baselines).T.rename_axis("model").to_csv(REPORTS_DIR / "baseline_comparison.csv")

    model = build_pipeline()
    cv = cross_val_score(
        model, train_df["text"], train_df["category"],
        cv=StratifiedKFold(5, shuffle=True, random_state=RANDOM_SEED), scoring="f1_macro",
    )
    model.fit(train_df["text"], train_df["category"])
    proba = model.predict_proba(test_df["text"])
    classes = model.classes_
    pred = classes[np.argmax(proba, axis=1)]
    y = test_df["category"].to_numpy()

    report_txt = classification_report(y, pred, labels=CATEGORIES, digits=3)
    (REPORTS_DIR / "classification_report.txt").write_text(report_txt)

    fig, ax = plt.subplots(figsize=(8, 7))
    ConfusionMatrixDisplay.from_predictions(y, pred, labels=CATEGORIES, xticks_rotation=45, ax=ax, colorbar=False, cmap="Blues")
    ax.set_title("Confusion matrix (synthetic test set)")
    fig.tight_layout()
    fig.savefig(REPORTS_DIR / "confusion_matrix.png", dpi=150)
    plt.close(fig)

    tt = threshold_tradeoff(y, proba, classes)
    tt.to_csv(REPORTS_DIR / "threshold_tradeoff.csv", index=False)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(tt["threshold"], tt["auto_suggest_coverage"], marker="o", label="Share auto-suggested")
    ax.plot(tt["threshold"], tt["accuracy_when_suggested"], marker="s", label="Accuracy when suggested")
    ax.axvline(CONFIDENCE_THRESHOLD, color="grey", linestyle="--", label=f"Chosen threshold ({CONFIDENCE_THRESHOLD})")
    ax.set_xlabel("Confidence threshold")
    ax.set_ylabel("Proportion")
    ax.set_title("Coverage vs accuracy trade-off")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(REPORTS_DIR / "threshold_tradeoff.png", dpi=150)
    plt.close(fig)

    fair = fairness_table(test_df, pred)
    fair.to_csv(REPORTS_DIR / "fairness_by_group.csv", index=False)
    top_terms(model).to_csv(REPORTS_DIR / "top_terms_by_category.csv", index=False)

    chosen = tt.loc[np.isclose(tt["threshold"], CONFIDENCE_THRESHOLD)].iloc[0].to_dict()
    metrics = {
        "dataset": {"rows": int(len(df)), "train_rows": int(len(train_df)), "test_rows": int(len(test_df)), "synthetic": True},
        "test_accuracy": round(accuracy_score(y, pred), 4),
        "test_macro_f1": round(f1_score(y, pred, average="macro"), 4),
        "cv_macro_f1_mean": round(float(cv.mean()), 4),
        "cv_macro_f1_std": round(float(cv.std()), 4),
        "hardship_recall_model_only": round(recall_score(y, pred, labels=["HARDSHIP_URGENT"], average="macro"), 4),
        "chosen_threshold": CONFIDENCE_THRESHOLD,
        "at_chosen_threshold": chosen,
        "max_accuracy_gap_by_attribute": fair.groupby("attribute")["accuracy_gap_vs_best_in_attribute"].max().to_dict(),
    }
    (REPORTS_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2, default=float))

    # End-to-end evaluation of the full triage service (safety rules + model + threshold)
    service = TriageService(model=model)
    results = [service.triage(t) for t in test_df["text"]]
    actions = pd.Series([r.action for r in results], index=test_df.index)
    cats = pd.Series([r.category for r in results], index=test_df.index)
    is_h = test_df["category"] == "HARDSHIP_URGENT"
    escalated = actions.isin([ACTION_PRIORITY, ACTION_SAFETY])
    suggested = actions == ACTION_AUTO
    e2e = {
        "share_suggest_route": round(float(suggested.mean()), 4),
        "share_manual_queue": round(float((actions == ACTION_MANUAL).mean()), 4),
        "share_priority_escalation": round(float(escalated.mean()), 4),
        "hardship_recall_end_to_end": round(float(escalated[is_h].mean()), 4),
        "hardship_cases_missed": int((~escalated[is_h]).sum()),
        "hardship_cases_total": int(is_h.sum()),
        "false_escalation_rate_non_hardship": round(float(escalated[~is_h].mean()), 4),
        "accuracy_of_suggested_routes": round(float((cats[suggested] == test_df.loc[suggested, "category"]).mean()), 4),
    }
    metrics["end_to_end"] = e2e
    (REPORTS_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2, default=float))

    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(report_txt)
    print(json.dumps(metrics, indent=2, default=float))


if __name__ == "__main__":
    main()
