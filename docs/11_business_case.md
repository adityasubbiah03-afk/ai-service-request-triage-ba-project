# 11 · Business Case

| | |
|---|---|
| **Project** | AI-Assisted Triage of Citizen Service Requests |
| **Prepared by** | Aditya Subbiah Sudar, Business Analyst (simulated engagement) |
| **Version** | 1.0 · October 2026 |
| **Decision sought** | Approve Phase 0–1 funding (approvals and shadow mode) |

> **Read this first.** Volumes, hourly cost, build and run costs and rule-based coverage are **planning assumptions** (see [RAID](08_raid_log.md) A-01, A-07) chosen to be plausible for a mid-sized agency. They must be replaced with agency data (I-01). Model performance figures come from synthetic data. The arithmetic is shown so the case can be re-run with real inputs.

## 1. Strategic fit
Faster, fairer service; better protection for people in hardship; responsible adoption of AI in line with government policy; better data for service improvement.

## 2. Problem and opportunity
At an assumed 600,000 requests per year and 2.5 minutes of manual triage each, triage consumes about **25,000 officer hours a year (about $1.5 million at an assumed $60 loaded hourly cost)**. Misrouting, inconsistent decisions and the risk of urgent cases waiting add service and reputational cost that is not valued here.

## 3. Options
| Option | Description |
|---|---|
| 0. Do nothing | Continue manual triage |
| 1. Rules-only routing | Keyword and rule-based routing maintained by staff |
| 2. AI-assisted triage, human in the loop (**recommended, staged**) | Safety rules plus ML suggestion; humans review all outputs in the pilot |
| 3. Full automation | Model routes and acts without review (**rejected**: fails DEC-01, legal and ethical tests) |

### Multi-criteria assessment
Scores are 1 (poor) to 5 (strong), assigned by the BA and tested in the simulated workshop. They are judgement, not measurement.

| Criterion | Weight | 0 Do nothing | 1 Rules-only routing | 2 AI-assisted, human in the loop | 3 Full automation |
|---|---|---|---|---|---|
| Service outcomes (speed, accuracy) | 25% | 1 | 3 | 4 | 5 |
| Risk to people (higher = safer) | 25% | 2 | 4 | 3 | 1 |
| Value for money | 20% | 1 | 3 | 4 | 5 |
| Adaptability | 10% | 1 | 2 | 4 | 4 |
| Explainability | 10% | 5 | 5 | 4 | 2 |
| Delivery complexity (higher = simpler) | 10% | 5 | 4 | 3 | 2 |
| **Weighted score (out of 5)** | 100% | **2.05** | **3.45** | **3.65** | **3.30** |

Option 3 scores highest on speed and cost, but any option that removes human review fails the mandatory requirements (BR-07, BR-13) and is excluded regardless of score.

## 4. Financial analysis (undiscounted, 3 years)
**Assumptions**
| Assumption | Value | Note |
|---|---|---|
| Requests per year | 600,000 | A-01 |
| Manual triage time | 2.5 min | A-01 |
| Officer review time when a suggestion is shown | 0.5 min | Officer still reviews |
| Loaded cost per hour | $60 | A-07 |
| Share of requests with a suggested route (Option 2) | 86.6% | Prototype result on synthetic data |
| Share with suggested route (Option 1) | 55% | Unvalidated assumption; test in shadow pilot |
| Benefit ramp-up Option 2 | 15% / 80% / 100% | Year 1 includes shadow mode, so little benefit |
| Benefit ramp-up Option 1 | 10% / 80% / 100% | |

**Option 2 cost estimate (assumed):** Year 1 build $650,000 (delivery team $380k, integration $120k, assurance including PIA and security $90k, change and training $60k) plus $120,000 running; $180,000 per year running thereafter.
**Option 1 cost estimate (assumed):** $250,000 build; $60,000 per year running from Year 2.

| Scenario | Annual benefit at full run rate | Year 1 net | Year 2 net | Year 3 net | **3-year cumulative net** |
|---|---|---|---|---|---|
| Option 1 base | $660,000 (11,000 h) | -$184,000 | $468,000 | $600,000 | **$884,000** |
| **Option 2 base** | **$1,039,200 (17,320 h)** | -$614,120 | $651,360 | $859,200 | **$896,440** |
| Option 2 pessimistic (70% coverage, 0.8 min review, slower ramp, higher cost) | $714,000 | -$878,600 | $208,400 | $351,200 | **-$319,000** |
| Option 2 optimistic (90% coverage, 0.4 min review) | $1,134,000 | -$483,200 | $860,600 | $974,000 | **$1,351,400** |

### What the numbers say, honestly
1. **In the base case Options 1 and 2 are financially close** ($884k vs $896k over three years). The financial case alone does not decide between them.
2. **Option 2 is riskier**: in the pessimistic case it loses money over three years. Option 1 has not been stress-tested because its coverage figure is itself unvalidated.
3. **"Savings" are released capacity, not cash.** Officer time is redirected to complex, urgent and quality work; headcount reduction is not part of this case and would require separate consultation (C-02).
4. Option 2's advantages are non-financial: it can cover more request types, adapts to new phrasing, produces structured data, and improves with monitoring, at the price of governance effort and model risk.

## 5. Non-financial benefits
Earlier identification of hardship cases; consistent routing; fewer re-routes (workshop rank 3 pain point); data on why people contact DCSD; staff time for complex work; evidence base for responsible AI use.

## 6. Risks
See [RAID log](08_raid_log.md). Highest: R-08 (synthetic results overstate), R-05 (group fairness), R-02 (automation bias), R-01 (urgent case missed).

## 7. Recommendation
Approve a **staged** path for Option 2, with Option 1 evaluated alongside as the fallback:

| Phase | Duration (indicative) | What happens | Funding |
|---|---|---|---|
| 0. Approvals | 8 weeks | PIA, security authorisation, AI use case assessment, accountable owner, staff consultation | Requested now |
| 1. Shadow mode | 8 weeks | Model runs on real requests in the background; nothing shown to staff; rule-based baseline measured too | Requested now |
| 2. Assisted mode | 12 weeks | Suggestions shown to officers in low-risk categories; 100% human review | Subject to Gate 2 |
| 3. Review | 4 weeks | Evaluate; decide scale, hold or stop | Subject to Gate 3 |

Indicative funding requested now: **$220,000** for Phases 0 and 1 (portion of the Option 2 Year 1 estimate).

### Decision gates
| Gate | Criteria |
|---|---|
| G1 end of Phase 0 | PIA, security authorisation and AI use case assessment approved; use case owner named; staff consultation completed |
| G2 end of Phase 1 | On real data and a sample reviewed by senior officers: accuracy of suggested routes ≥ 95%; hardship and safety recall ≥ 99% on cleaned labels; group accuracy gap ≤ 5 points; Option 2 materially better than the rule-based baseline; no unresolved high findings |
| G3 end of Phase 2 | Median time to route down ≥ 50%; override rate and staff survey acceptable; no severe incidents |

**Stop conditions:** failure to meet G2 after one remediation cycle; any severe incident involving a missed urgent case; withdrawal of required approvals.

## 8. Benefits realisation
| Benefit | Measure | Baseline source | Owner | Reviewed |
|---|---|---|---|---|
| Faster routing | Median minutes to route | Operational data (D-03) | Contact Centre Ops | Monthly |
| First-time accuracy | % routed correctly first time | Re-route rate | Team managers | Monthly |
| Urgent case protection | Time to priority queue; recall on sample | Audit log | Priority Case Team | Monthly |
| Fairness | Group accuracy gaps | Monitoring | AI Governance Committee | Quarterly |
| Staff experience | Survey | Pilot survey | Team leaders | Per phase |
