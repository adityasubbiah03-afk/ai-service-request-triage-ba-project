# 16 · Requirements Traceability Matrix

*Shows how each business requirement is carried through functional requirements, user stories, evidence and documents. "Evidence" distinguishes automated tests, generated reports and design-only items.*

## 1. Business requirements to evidence
| BR | Requirement (short) | FR / NFR | User stories | Evidence | Status |
|----|---------------------|----------|--------------|----------|--------|
| BR-01 | Suggest receiving team | FR-01, FR-02 | US-01, US-15 | `test_clear_account_access_request_is_routed`, `test_every_result_has_a_valid_category`; `reports/classification_report.txt` | Prototype done |
| BR-02 | Reduce time to route | FR-01, NFR-01 | US-01, US-07 | Business case time model ([doc 11](11_business_case.md)); **time saving not measured, needs pilot** | Assumed |
| BR-03 | Uncertain goes to human | FR-04, FR-15, NFR-10 | US-03, US-13 | `test_low_confidence_goes_to_manual_queue`, `test_handles_empty_and_odd_input`; `reports/threshold_tradeoff.csv` | Prototype done; fail-safe is design |
| BR-04 | Hardship escalation | FR-05 | US-04 | `test_hardship_rule_overrides_routine_routing`; end-to-end recall in `reports/metrics.json` | Prototype done; real-data recall unproven |
| BR-05 | Life-safety escalation | FR-06 | US-05 | `test_life_safety_phrase_is_escalated_immediately` | Prototype done |
| BR-06 | Explain suggestions | FR-03, FR-07, FR-13, NFR-05 | US-02, US-06, US-15 | `test_explanation_terms_are_returned`; `reports/top_terms_by_category.csv` | Prototype done; UI is design |
| BR-07 | Human review; no decisions | FR-14, FR-13 | US-14 | No outbound interface in `/src`; DEC-01 | Done by design |
| BR-08 | Privacy and security first | NFR-03, NFR-04 | US-16 | Synthetic data only (DEC-03); [doc 13](13_impact_assessment.md) | Design |
| BR-09 | Audit log | FR-09, NFR-08 | US-10 | Seeded, reproducible reports; production log is design | Design |
| BR-10 | Fairness monitoring | FR-11, NFR-06 | US-08 | `reports/fairness_by_group.csv`; I-03 raised | Prototype done; gap above threshold |
| BR-11 | Adjustable threshold and rules | FR-08 | US-11 | `src/config.py` | Partial |
| BR-12 | Override capture | FR-10 | US-09 | none | Design |
| BR-13 | Policy and privacy compliance | NFR-03, NFR-04 | US-14 | [doc 13](13_impact_assessment.md), [doc 14](14_ai_governance_assessment.md) | Draft assessments |
| BR-14 | Post-go-live monitoring | FR-12, NFR-09 | US-12 | Monitoring plan in doc 14 | Design |

## 2. Objectives to requirements
| Objective | Requirements | Measured where |
|---|---|---|
| O1 Reduce time to routing | BR-01, BR-02 | Pilot (Phase 2) |
| O2 Routing accuracy ≥ 95% | BR-01, BR-03 | `reports/metrics.json` (synthetic: 95.0%); pilot sample |
| O3 Protect urgent cases ≥ 99% | BR-04, BR-05 | Prototype 94.6% (label noise explains misses); pilot sample |
| O4 Human review 100% | BR-07 | Pilot compliance checks |
| O5 Fairness gap ≤ 5 points | BR-10 | `reports/fairness_by_group.csv` (currently 8.2 on writing style) |

## 3. Document-to-requirement map
| Document | Purpose in the engagement |
|---|---|
| 00 Charter | Objectives, scope, governance |
| 01 Stakeholder map | Who, influence, engagement |
| 02 Interview guide | Elicitation approach; themes T1–T8 |
| 03 Workshop | Facilitation; MoSCoW; decisions DEC-01..05 |
| 04 BRD | BR-01..BR-14 |
| 05 FRD | FR-01..FR-15, NFR-01..NFR-10 |
| 06 User stories | US-01..US-16 with acceptance criteria |
| 07 Process maps | As-is, to-be, role changes |
| 08 RAID | Risks, assumptions, issues, dependencies, decisions |
| 09 Backlog and sprint plan | Agile delivery, ceremonies, roadmap |
| 10 Status report | Project reporting |
| 11 Business case | Options, financials, gates |
| 12 Briefing paper | Executive decision paper |
| 13 Impact assessment | Privacy, security, legal, stakeholder impact |
| 14 Governance assessment | Model card, fairness, monitoring, ethics alignment |
| 15 Explainer | Communication to non-technical stakeholders |

## 4. Gaps and what they need
| Gap | Needed to close |
|---|---|
| Time saving unmeasured | Operational baseline data and pilot |
| Real-data performance unknown | PIA, security authorisation, shadow mode |
| Audit log, override capture, monitoring, officer UI | Production build in pilot backlog |
| Fairness gap above threshold | Real-data retest and treatment plan (I-03) |
