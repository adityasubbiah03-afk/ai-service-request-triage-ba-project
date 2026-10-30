# 10 · Project Status Report

| | |
|---|---|
| **Project** | AI-Assisted Triage of Citizen Service Requests (simulated engagement) |
| **Reporting period** | Sprint 2 (5–18 October 2026) |
| **Prepared by** | Aditya Subbiah Sudar, Business Analyst |
| **Audience** | Sponsor (EGM Service Delivery), Director Contact Centre Operations, AI Governance Committee |

## 1. Overall status
| Dimension | RAG | Comment |
|---|---|---|
| Scope | 🟢 Green | In scope delivered; no change requests |
| Schedule | 🟢 Green | Both sprints completed at planned capacity (30 points each) |
| Quality / readiness for pilot | 🟠 Amber | Fairness gap above threshold (I-03); results are on synthetic data only (R-08) |
| Risk | 🟠 Amber | Two High risks open (R-02 automation bias, R-05 group fairness) and one Very high (R-08) |
| Stakeholders | 🟠 Amber | Staff consultation not yet started (I-02) |

**Overall: AMBER.** The concept is feasible on synthetic data and the design is safe by construction, but the evidence is not yet strong enough to recommend a pilot without the approval and shadow-mode steps in the business case.

## 2. Accomplishments this period
- Completed stakeholder analysis, interviews, workshop, BRD/FRD, 16 user stories and process maps.
- Built and tested a proof-of-concept triage service (8 automated tests passing).
- Evaluated the classifier against baselines and produced coverage, accuracy and fairness reports.
- Completed options analysis and business case, AI impact assessment and governance assessment.

## 3. Key metrics (synthetic data, seed 42; reproducible with `python -m src.train_model`)
| Measure | Result | Pilot target | Comment |
|---|---|---|---|
| Overall accuracy (1,000-request test set) | 92.3% | n/a | Majority-class baseline: 24.8% |
| Macro F1 | 0.915 | n/a | 5-fold CV mean 0.912 ± 0.005 |
| Share of requests given a suggested route | 86.6% | ≥ 85% | Meets BR-01 measure |
| Accuracy of suggested routes | 95.0% | ≥ 95% | Meets target on synthetic data; unproven on real data |
| Share sent to manual queue | 4.5% | n/a | Low-confidence requests |
| Share escalated as priority | 8.9% | n/a | Includes 2.1% false escalation of non-hardship requests (acceptable cost of caution) |
| Hardship escalation recall | 94.6% (70 of 74) | ≥ 99% | The 4 misses were mislabelled records (I-04); real-data recall unproven |
| Max accuracy gap, writing style | 8.2 points | ≤ 5 points | **Breach (I-03)** |
| Max accuracy gap, region / channel | 3.1 / 2.2 points | ≤ 5 points | Within threshold; small groups, interpret with caution |

## 4. Planned next period
| Item | Owner |
|---|---|
| Obtain operational baseline data (I-01) | Contact Centre Ops |
| Begin PIA and security assessment (D-01, D-02) | Privacy Officer, Security Advisor |
| Start staff and representative consultation (I-02) | Sponsor |
| Investigate and treat the writing-style gap (I-03) | Data Science Lead |
| Submit AI use case assessment to the AI Governance Committee | BA, AI Governance Committee |

## 5. Top risks and issues
| ID | Item | Rating | Action |
|---|---|---|---|
| R-08 | Synthetic results overstate real-world performance | Very high | Shadow mode on real data before any staff exposure |
| R-05 / I-03 | Unequal performance across writing styles | High | Treat before pilot; retest on real data |
| R-02 | Automation bias | High | Training, blind audits, override monitoring |

## 6. Decisions required
1. Approve funding for Phases 0 and 1 only (approvals and shadow mode), per [doc 11](11_business_case.md).
2. Nominate an accountable use case owner (D-04).
3. Endorse starting staff consultation (I-02).

## 7. Effort and budget
Effort tracked at 60 points across two sprints against a plan of 60. No financial budget was allocated to this simulated discovery.
