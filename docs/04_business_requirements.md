# 04 · Business Requirements Document (BRD)

| | |
|---|---|
| **Project** | AI-Assisted Triage of Citizen Service Requests |
| **Client (fictional)** | Department of Citizen Services Delivery (DCSD) |
| **Version** | 1.0 · October 2026 |
| **Author** | Aditya Subbiah Sudar, Business Analyst (simulated engagement) |
| **Approver (simulated)** | Director, Contact Centre Operations |

> Simulated engagement. Volumes, timings and costs are assumptions unless stated otherwise. The model results quoted come from the synthetic dataset in this repository.

## 1. Executive summary
DCSD triages every inbound service request by hand. This is slow at peak times, inconsistent, and puts people in urgent need at risk of waiting in routine queues. This BRD sets out the business requirements for an AI-assisted triage capability that **suggests** a receiving team and flags urgency, while keeping decisions with people.

## 2. Business context and problem
| Item | Description |
|---|---|
| Current state | Triage officers read each request and route it to one of seven teams (see as-is map, [doc 07](07_process_maps.md)) |
| Assumed volume | 600,000 requests per year (planning assumption) |
| Assumed handling time | 2.5 minutes of triage per request (planning assumption) → about 25,000 hours per year |
| Pain points | Peak backlogs; misrouting and re-handling; inconsistent decisions; hardship cases hard to spot (ranked in [doc 03](03_workshop_plan_and_outcomes.md)) |
| Drivers | Service standards, public trust, workforce capacity, government policy on responsible AI |

## 3. Business objectives
See charter objectives O1–O5 ([doc 00](00_project_charter.md)). Targets are for the pilot go/no-go decision, not claims about the prototype.

## 4. Scope
| In scope | Out of scope |
|---|---|
| Free-text service requests in English received by web form, email, phone transcript | Voice audio, languages other than English |
| Classification into seven categories; routing suggestion; urgency flagging | Eligibility, payment, debt or any other decision |
| Human review workflow, audit, monitoring | Automated replies to citizens |
| Privacy, security, fairness and governance requirements | Integration build with production case-management systems |

## 5. Business requirements
Priority uses MoSCoW as agreed in the workshop.

| ID | Requirement | Priority | Source | Success measure |
|----|-------------|----------|--------|-----------------|
| BR-01 | The business shall receive a suggested receiving team for each incoming request | Must | T1, S02, S03 | Suggested route available for ≥ 85% of requests (rest go to manual queue) |
| BR-02 | The solution shall reduce the time taken to route routine requests | Must | T1, O1 | ≥ 50% reduction in median time to route (pilot measure) |
| BR-03 | Requests the system is unsure about shall go to a human queue rather than being guessed | Must | T2, T5 | Accuracy of suggested routes ≥ 95%; 100% of low-confidence requests in manual queue |
| BR-04 | Requests indicating financial hardship shall be escalated to the Priority Case Team and never queued as routine | Must | T3, S10 | ≥ 99% of genuine hardship requests reach a human priority queue within 1 business day |
| BR-05 | Requests indicating a risk to personal safety shall be escalated immediately | Must | T3, S10 | 100% of matched requests escalated with zero-day service level |
| BR-06 | Every suggestion shall be explained in plain language | Must | T5, S03, S08 | Officers can see reasons for 100% of suggestions; ≥ 80% of officers rate them useful in pilot survey |
| BR-07 | A person shall review every output during the pilot; the solution shall not make or communicate decisions | Must | T4, T8, DEC-01 | 100% reviewed; zero automated decisions or citizen communications |
| BR-08 | Privacy and security approvals shall be completed before any real citizen data is used | Must | T6, DEC-03 | PIA and security authorisation recorded before data access |
| BR-09 | Each suggestion and each human action shall be recorded in an audit log | Must | S08, S15 | 100% of requests have a complete audit record |
| BR-10 | Performance shall be monitored for different customer groups to detect unfair outcomes | Should | T7, S10 | Max accuracy gap between groups ≤ 5 percentage points |
| BR-11 | The confidence threshold and urgency phrase lists shall be adjustable under change control | Should | S02, DEC-05 | Changes versioned, approved, logged |
| BR-12 | Officers shall be able to override a suggestion and record why | Should | S03 | Override captured for 100% of overrides |
| BR-13 | The solution shall meet government AI policy and privacy obligations, including an AI use case assessment and a named accountable use case owner | Must | S08, S09 | Assessments approved; use case registered before pilot |
| BR-14 | Performance, group gaps and drift shall be monitored after go-live | Should | S05, S09 | Monthly report; alert thresholds defined |

## 6. Stakeholders
See [doc 01](01_stakeholder_map.md).

## 7. Assumptions, constraints, dependencies
| Type | Statement | Ref |
|---|---|---|
| Assumption | Request volume and handling times are as stated in section 2 and will be validated with operational data | A-01 |
| Assumption | Historical triage labels exist but contain some errors (assumed ~2%); this prototype injects 2% label noise to test robustness | A-02 |
| Assumption | A named accountable use case owner will be appointed before the pilot | A-04 |
| Constraint | Request text may contain sensitive personal information; classification and hosting constraints apply | C-01 |
| Constraint | Staff consultation obligations apply before role changes | C-02 |
| Dependency | Privacy, security and AI governance approvals before real data use | D-01, D-02 |
| Dependency | Operational data (volumes, timings, re-route rates) from Contact Centre Operations | D-03 |

Full list in [RAID log](08_raid_log.md).

## 8. Benefits (summary)
Capacity released for complex and urgent work, faster routing, more consistent decisions, earlier visibility of hardship, and better data on why people contact DCSD. Figures and options analysis are in [doc 11](11_business_case.md).

## 9. Acceptance and success criteria for the pilot
1. All Must requirements met in a controlled pilot.
2. Suggested-route accuracy ≥ 95% on a sample reviewed by senior officers.
3. Hardship and safety escalation meets BR-04 and BR-05 on a sample including real-world phrasing variety.
4. No unresolved high-severity privacy, security or fairness findings.
5. Staff survey shows officers understand and trust the explanations.

## 10. Sign-off
| Role | Name | Status |
|---|---|---|
| Business owner | Director, Contact Centre Operations | Approved (simulated) |
| Sponsor | EGM, Service Delivery | Approved (simulated) |
| Privacy Officer | n/a | Consulted |
| Data Science Lead | n/a | Consulted |
