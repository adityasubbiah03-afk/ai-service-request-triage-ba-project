"""Central configuration: categories, routing table, thresholds and safety rules.

Everything here is FICTIONAL and for demonstration only. The "Department of Citizen
Services Delivery (DCSD)" does not exist.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "synthetic_requests.csv"
MODEL_PATH = ROOT / "models" / "triage_model.joblib"
REPORTS_DIR = ROOT / "reports"

RANDOM_SEED = 42

# category -> (receiving team, service-level target in business days)
ROUTING = {
    "PAYMENT_ENQUIRY": ("Payments Team", 3),
    "DEBT_DISPUTE": ("Debt Review Team", 5),
    "ACCOUNT_ACCESS": ("Account Support Team", 2),
    "UPDATE_DETAILS": ("Records Team", 5),
    "COMPLAINT": ("Feedback and Complaints Team", 10),
    "TECHNICAL_FAULT": ("Digital Support Team", 3),
    "HARDSHIP_URGENT": ("Priority Case Team", 1),
}
CATEGORIES = list(ROUTING)

# Below this model confidence the request goes to the manual triage queue.
# Chosen from the threshold trade-off analysis in reports/threshold_tradeoff.csv.
CONFIDENCE_THRESHOLD = 0.60

# Safety rules run BEFORE the model and can never be overridden by it.
# Any match sends the request to a human immediately.
LIFE_SAFETY_PATTERNS = [
    r"\bsuicid\w*",
    r"\bkill (myself|me)\b",
    r"\bend (my|it all|my life)\b",
    r"\bself[- ]?harm\b",
    r"\bnot safe\b",
    r"\bunsafe\b",
    r"\b(family|domestic) violence\b",
    r"\bhe (hits|hurts|threatens) me\b",
]
HARDSHIP_PATTERNS = [
    r"\bno (money|food)\b",
    r"\b(can'?t|cannot|unable to) (afford|buy|pay for) (food|rent|medication|medicine|power|electricity)\b",
    r"\bhomeless\w*",
    r"\bevict\w*",
    r"\bnothing to eat\b",
    r"\bpower (will be|has been|got) (cut|disconnected)\b",
    r"\bsleeping in (my|the) car\b",
]
