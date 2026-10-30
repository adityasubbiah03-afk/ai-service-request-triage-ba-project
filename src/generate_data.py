"""Generate a SYNTHETIC dataset of citizen service requests.

No real citizen data is used anywhere in this project. Requests are assembled from
hand-written templates for a fictional agency, then deliberately made messy:

* four writing styles (plain, formal, terse, esl) so group fairness can be tested
* ~12% multi-intent messages (a second topic is appended; the label stays the primary one)
* ~2% label noise (simulating human mis-triage in historical data)
* PII-like tokens are fake reference numbers only

Usage:  python -m src.generate_data
"""
import random
import re

import pandas as pd

from .config import CATEGORIES, DATA_PATH, RANDOM_SEED

N_ROWS = 4000
CLASS_WEIGHTS = {
    "PAYMENT_ENQUIRY": 24,
    "DEBT_DISPUTE": 16,
    "ACCOUNT_ACCESS": 16,
    "UPDATE_DETAILS": 14,
    "COMPLAINT": 11,
    "TECHNICAL_FAULT": 12,
    "HARDSHIP_URGENT": 7,
}

CORE = {
    "PAYMENT_ENQUIRY": [
        "I have not received my payment this fortnight and I would like to know why.",
        "Can you tell me when my next payment will be deposited?",
        "My payment amount looks lower than usual, can someone explain the change?",
        "I want to confirm what payment I am entitled to as a carer.",
        "My payment was due {days} ago and it still has not arrived in my account.",
        "Please check why my payment of {amount} was delayed.",
        "How is my payment calculated and what is my payment date?",
        "I applied for a payment {days} ago and want an update on the claim.",
        "Is my payment going to be paid on time over the public holiday?",
        "I think my payment was only part paid, I expected {amount}.",
        "Can you send me a statement showing my last few payments?",
        "Do I qualify for a higher rate of payment now that my situation has changed?",
    ],
    "DEBT_DISPUTE": [
        "I received a debt notice for {amount} and I do not think it is correct.",
        "I want to dispute the overpayment letter I was sent.",
        "Please explain how you calculated the debt of {amount}.",
        "I would like to set up a repayment plan for my debt.",
        "I was told I owe money but I have never been overpaid.",
        "Can I request a review of my debt decision?",
        "The debt notice says I must repay by {date} but I need more time.",
        "I am appealing the overpayment because my income was reported correctly.",
        "Why are you taking money from my payment to recover a debt?",
        "I want to see the evidence behind the debt raised against me.",
        "Can the debt be waived because the error was not my fault?",
    ],
    "ACCOUNT_ACCESS": [
        "I am locked out of my online account and cannot log in.",
        "I need to reset my password but the reset email never arrives.",
        "The verification code is not being sent to my phone.",
        "I think someone else may have accessed my account without permission.",
        "My login keeps saying my details are incorrect.",
        "I lost my phone and cannot complete the two step sign in.",
        "How do I recover access to my account after changing my number?",
        "My account has been suspended after too many sign in attempts.",
        "I cannot link my identity to my online account.",
        "Please unlock my account, I have tried to log in many times.",
        "I forgot my username and need to get back into my account.",
    ],
    "UPDATE_DETAILS": [
        "I have moved house and need to update my address.",
        "Please change my bank account details to the new account.",
        "My partner has moved in and I need to report the change.",
        "I started a new job and my income has changed.",
        "I need to update my name after getting married.",
        "My phone number has changed, please update my contact details.",
        "I want to add my child to my record.",
        "Please update my details, I am now living with a housemate.",
        "I am going overseas for {days} and need to report my travel.",
        "I need to tell you that my hours at work have been reduced.",
        "Can you record my new postal address as of {date}?",
    ],
    "COMPLAINT": [
        "I want to make a complaint about the way a staff member spoke to me.",
        "I waited over an hour on the phone and then the call dropped.",
        "Nobody has called me back even though I was promised a call.",
        "I am very unhappy with how my case has been handled.",
        "The service centre staff were rude and unhelpful.",
        "I was given different information by three different people.",
        "I submitted a request {days} ago and nobody has responded to me.",
        "This is the third time I have had to explain my situation and I am frustrated.",
        "I would like to lodge a formal complaint about the delays.",
        "Your staff made an error and have not apologised or fixed it.",
        "The process is confusing and the service I received was poor.",
    ],
    "TECHNICAL_FAULT": [
        "The app crashes every time I try to open it.",
        "The upload button on the website does not work.",
        "I get an error message when I try to submit my form.",
        "The page will not load on my {device}.",
        "My document upload fails every time at {pct} percent.",
        "The website timed out and I lost everything I typed.",
        "I see error code {code} when I try to view my statement.",
        "The online form will not let me press submit.",
        "The app shows a blank screen after I sign in.",
        "I cannot download my payment summary, the link is broken.",
        "The website is not working properly on my {device}.",
    ],
    "HARDSHIP_URGENT": [
        "I have no money for food and my payment has not arrived.",
        "I received an eviction notice and I will be homeless next week.",
        "I cannot afford my medication this week and need urgent help.",
        "My power will be cut off on {date} and I have no money to pay.",
        "I have nothing to eat and my children are going hungry.",
        "I am sleeping in my car and need emergency support.",
        "I cannot pay my rent and the landlord says I must leave.",
        "I need an urgent payment, I have run out of money for essentials.",
        "We are in a crisis, there is no food in the house.",
        "I am about to be evicted and do not know where to go.",
        "I can't afford to buy food until my next payment.",
    ],
}

OPENERS = ["", "", "", "Hi,", "Hello,", "To whom it may concern,", "Good morning,", "Hi team,"]
CLOSERS = ["", "", "", "Thanks.", "Thank you.", "Please help.", "Regards,", "Kind regards.", "Please advise."]
CONTEXT = [
    "", "", "", "My reference is {ref}.", "Ref {ref}.", "I called earlier today.",
    "I have been a customer for {years} years.", "This has been going on since {date}.",
]
DATES = ["Monday", "next Friday", "the 14th", "15 March", "last week", "the end of the month", "1 July"]
DAYS = ["2 days", "3 days", "a week", "two weeks", "10 days", "a month"]
AMOUNTS = ["$212.40", "$412.50", "$1,050", "$87.15", "$640", "$2,300.80", "$155"]
DEVICES = ["phone", "laptop", "tablet", "computer"]

STYLE_WEIGHTS = {"plain": 60, "formal": 15, "terse": 15, "esl": 10}
REGION_WEIGHTS = {"metro": 60, "regional": 30, "remote": 10}
CHANNEL_WEIGHTS = {"web_form": 50, "email": 30, "phone_transcript": 20}


def _fill(template: str, rng: random.Random) -> str:
    return template.format(
        days=rng.choice(DAYS),
        amount=rng.choice(AMOUNTS),
        date=rng.choice(DATES),
        device=rng.choice(DEVICES),
        pct=rng.choice([30, 60, 90, 99]),
        code=rng.choice(["500", "403", "E-1042", "7001"]),
        ref="".join(rng.choices("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", k=8)),
        years=rng.randint(1, 20),
    )


def _style_formal(text: str) -> str:
    text = text.replace("I want", "I would like").replace("Can you", "Could you kindly")
    text = text.replace("Please", "I would be grateful if you could").replace("cannot", "am unable to")
    return "I am writing to formally request assistance. " + text


def _style_terse(text: str, rng: random.Random) -> str:
    text = text.lower()
    text = re.sub(r"[.,!?]", "", text)
    swaps = {"please": "pls", "payment": "pmt", "account": "acct", "because": "bc", "you": "u", "thanks": "thx"}
    for k, v in swaps.items():
        if rng.random() < 0.6:
            text = re.sub(rf"\b{k}\b", v, text)
    words = text.split()
    return " ".join(words[: max(6, int(len(words) * 0.8))])


def _style_esl(text: str, rng: random.Random) -> str:
    text = re.sub(r"\b(the|a|an)\b ", "", text, flags=re.I)
    text = text.replace("I am", "I").replace("has not", "not").replace("have not", "not have")
    text = text.replace("I would like", "I want").replace("my payment", "payment my") if rng.random() < 0.3 else text
    return text


def _apply_style(text: str, style: str, rng: random.Random) -> str:
    if style == "formal":
        return _style_formal(text)
    if style == "terse":
        return _style_terse(text, rng)
    if style == "esl":
        return _style_esl(text, rng)
    return text


def generate(n_rows: int = N_ROWS, seed: int = RANDOM_SEED) -> pd.DataFrame:
    rng = random.Random(seed)
    cats = list(CLASS_WEIGHTS)
    rows = []
    for i in range(n_rows):
        label = rng.choices(cats, weights=[CLASS_WEIGHTS[c] for c in cats])[0]
        style = rng.choices(list(STYLE_WEIGHTS), weights=list(STYLE_WEIGHTS.values()))[0]
        region = rng.choices(list(REGION_WEIGHTS), weights=list(REGION_WEIGHTS.values()))[0]
        channel = rng.choices(list(CHANNEL_WEIGHTS), weights=list(CHANNEL_WEIGHTS.values()))[0]

        parts = [rng.choice(OPENERS), _fill(rng.choice(CORE[label]), rng)]
        if rng.random() < 0.12:  # multi-intent: append a sentence from a different category
            other = rng.choice([c for c in cats if c != label])
            parts.append(_fill(rng.choice(CORE[other]), rng))
        parts += [_fill(rng.choice(CONTEXT), rng), rng.choice(CLOSERS)]
        text = " ".join(p for p in parts if p).strip()
        text = _apply_style(text, style, rng)

        recorded_label = label
        if rng.random() < 0.02:  # historical mis-triage
            recorded_label = rng.choice([c for c in cats if c != label])

        rows.append(
            {
                "request_id": f"SR-{100000 + i}",
                "text": text,
                "category": recorded_label,
                "writing_style": style,
                "region": region,
                "channel": channel,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    df = generate()
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PATH, index=False)
    print(f"Wrote {len(df)} synthetic requests to {DATA_PATH}")
    print(df["category"].value_counts().to_string())


if __name__ == "__main__":
    main()
