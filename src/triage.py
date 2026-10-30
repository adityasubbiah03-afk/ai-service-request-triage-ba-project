"""Triage service: safety rules first, then a model suggestion, then routing.

Design principle (see docs/14_ai_governance_assessment.md): the system SUGGESTS a route to a
human triage officer. It never decides eligibility, payments or debts.

Usage:
    python -m src.triage "I have no food and my payment has not arrived"
"""
import re
import sys
from dataclasses import asdict, dataclass, field

import joblib
import numpy as np

from .config import (
    CONFIDENCE_THRESHOLD,
    HARDSHIP_PATTERNS,
    LIFE_SAFETY_PATTERNS,
    MODEL_PATH,
    ROUTING,
)

ACTION_AUTO = "SUGGEST_ROUTE"
ACTION_MANUAL = "MANUAL_TRIAGE_QUEUE"
ACTION_PRIORITY = "PRIORITY_HUMAN_ESCALATION"
ACTION_SAFETY = "IMMEDIATE_SAFETY_ESCALATION"


@dataclass
class TriageResult:
    action: str
    category: str
    team: str
    sla_business_days: int
    confidence: float
    reasons: list = field(default_factory=list)
    flags: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


def _matches(patterns, text: str) -> list:
    return [p for p in patterns if re.search(p, text, flags=re.IGNORECASE)]


class TriageService:
    def __init__(self, model=None, threshold: float = CONFIDENCE_THRESHOLD):
        self.model = model if model is not None else joblib.load(MODEL_PATH)
        self.threshold = threshold

    def _top_terms(self, text: str, class_idx: int, k: int = 5) -> list:
        """Terms that pushed the model towards the predicted class (plain-language explanation)."""
        vec = self.model.named_steps["tfidf"]
        clf = self.model.named_steps["clf"]
        x = vec.transform([text])
        contrib = x.multiply(clf.coef_[class_idx]).toarray().ravel()
        names = np.array(vec.get_feature_names_out())
        top = np.argsort(contrib)[::-1][:k]
        return [str(names[i]) for i in top if contrib[i] > 0]

    def triage(self, text: str) -> TriageResult:
        # 1. Life-safety rules always win.
        if _matches(LIFE_SAFETY_PATTERNS, text):
            team, sla = ROUTING["HARDSHIP_URGENT"]
            return TriageResult(
                ACTION_SAFETY, "HARDSHIP_URGENT", team, 0, 1.0,
                reasons=["Matched life-safety rule"], flags=["LIFE_SAFETY"],
            )

        proba = self.model.predict_proba([text])[0]
        idx = int(np.argmax(proba))
        category = str(self.model.classes_[idx])
        confidence = float(proba[idx])
        reasons = self._top_terms(text, idx)

        # 2. Hardship rules override the model so urgent cases are never auto-queued as routine.
        if _matches(HARDSHIP_PATTERNS, text) or category == "HARDSHIP_URGENT":
            team, sla = ROUTING["HARDSHIP_URGENT"]
            flags = ["HARDSHIP_RULE"] if _matches(HARDSHIP_PATTERNS, text) else ["MODEL_HARDSHIP"]
            return TriageResult(
                ACTION_PRIORITY, "HARDSHIP_URGENT", team, sla, confidence,
                reasons=reasons, flags=flags,
            )

        # 3. Low confidence goes to a human, not to a guess.
        team, sla = ROUTING[category]
        if confidence < self.threshold:
            return TriageResult(
                ACTION_MANUAL, category, "Manual Triage Queue", sla, confidence,
                reasons=reasons, flags=["LOW_CONFIDENCE"],
            )
        return TriageResult(ACTION_AUTO, category, team, sla, confidence, reasons=reasons)


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python -m src.triage "your request text"')
        sys.exit(1)
    result = TriageService().triage(" ".join(sys.argv[1:]))
    for k, v in result.to_dict().items():
        print(f"{k:>18}: {v}")


if __name__ == "__main__":
    main()
