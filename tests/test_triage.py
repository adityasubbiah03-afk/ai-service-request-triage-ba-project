"""Acceptance-style tests mapped to user stories (see docs/06 and docs/16).

Run with:  python -m unittest discover -s tests -v
"""
import unittest

from sklearn.model_selection import train_test_split

from src.config import CATEGORIES, RANDOM_SEED, ROUTING
from src.generate_data import generate
from src.train_model import build_pipeline
from src.triage import (
    ACTION_AUTO,
    ACTION_MANUAL,
    ACTION_PRIORITY,
    ACTION_SAFETY,
    TriageService,
)


class TriageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        df = generate(n_rows=2000, seed=RANDOM_SEED)
        cls.train, cls.test = train_test_split(df, test_size=0.25, stratify=df["category"], random_state=RANDOM_SEED)
        model = build_pipeline().fit(cls.train["text"], cls.train["category"])
        cls.service = TriageService(model=model)

    # US-01 / FR-02: routing suggestions
    def test_clear_account_access_request_is_routed(self):
        r = self.service.triage("I am locked out of my online account and cannot log in.")
        self.assertEqual(r.category, "ACCOUNT_ACCESS")
        self.assertEqual(r.action, ACTION_AUTO)
        self.assertEqual(r.team, ROUTING["ACCOUNT_ACCESS"][0])

    def test_every_result_has_a_valid_category(self):
        for text in self.test["text"].head(50):
            self.assertIn(self.service.triage(text).category, CATEGORIES)

    # US-03 / FR-04: low confidence goes to humans
    def test_low_confidence_goes_to_manual_queue(self):
        r = self.service.triage("hello")
        self.assertEqual(r.action, ACTION_MANUAL)
        self.assertIn("LOW_CONFIDENCE", r.flags)

    # US-04 / FR-05: hardship is always escalated to a human
    def test_hardship_rule_overrides_routine_routing(self):
        r = self.service.triage("My payment is late and I have no food for the kids.")
        self.assertEqual(r.action, ACTION_PRIORITY)
        self.assertEqual(r.category, "HARDSHIP_URGENT")

    # US-05 / FR-06: life safety is escalated immediately
    def test_life_safety_phrase_is_escalated_immediately(self):
        r = self.service.triage("I am not safe at home and need help.")
        self.assertEqual(r.action, ACTION_SAFETY)
        self.assertEqual(r.sla_business_days, 0)

    # US-06 / FR-07: explanation is provided
    def test_explanation_terms_are_returned(self):
        r = self.service.triage("I received a debt notice for $412 and want to dispute it.")
        self.assertTrue(len(r.reasons) > 0)

    # NFR: the service never raises on odd input
    def test_handles_empty_and_odd_input(self):
        for text in ["", "   ", "12345", "!!!???", "x" * 5000]:
            r = self.service.triage(text)
            self.assertIn(r.action, {ACTION_AUTO, ACTION_MANUAL, ACTION_PRIORITY, ACTION_SAFETY})

    # US-07: minimum quality bar on synthetic data
    def test_overall_accuracy_meets_minimum_bar(self):
        preds = [self.service.triage(t).category for t in self.test["text"]]
        acc = sum(p == y for p, y in zip(preds, self.test["category"])) / len(preds)
        self.assertGreaterEqual(acc, 0.85)


if __name__ == "__main__":
    unittest.main()
