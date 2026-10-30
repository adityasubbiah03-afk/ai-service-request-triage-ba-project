# 00 · Project Charter

| | |
|---|---|
| **Project** | AI-Assisted Triage of Citizen Service Requests |
| **Client (fictional)** | Department of Citizen Services Delivery (DCSD) |
| **Document owner** | Aditya Subbiah Sudar, Business Analyst (simulated engagement) |
| **Version / date** | 1.0 · October 2026 |
| **Status** | Approved for discovery and prototype (simulated) |

> **Simulation notice.** DCSD is a fictional agency. All stakeholders, interviews, workshop outcomes, volumes and costs in this repository are **simulated or assumed** for portfolio purposes and are labelled as such. No real citizen data is used. See the [README](../README.md).

## 1. Purpose
Define the scope, objectives, governance and approach for a discovery-to-pilot-readiness engagement exploring whether machine learning can help DCSD triage inbound citizen service requests faster and more consistently, **without removing human judgement from decisions that affect people**.

## 2. Background
DCSD receives free-text service requests through web forms, email and phone transcripts. Triage officers read each request and manually route it to one of seven specialist teams. Discovery (docs 02 and 03) indicates this is slow at peak times, inconsistent between officers, and risks urgent hardship cases waiting in the same queue as routine enquiries.

## 3. Problem statement
Manual reading and routing of every request delays response times, causes misrouting and re-handling, and offers no systematic way to surface people in urgent need. DCSD wants to understand whether AI-assisted triage is feasible, safe, lawful and worthwhile before committing to a build.

## 4. Objectives (SMART)
| ID | Objective | Measure | Target for pilot go/no-go |
|----|-----------|---------|---------------------------|
| O1 | Reduce time to first routing | Median minutes from lodgement to routed | ≥ 50% reduction vs. baseline |
| O2 | Improve routing accuracy | % requests reaching the correct team first time | ≥ 95% on suggested routes |
| O3 | Protect urgent cases | % genuine hardship / safety requests reaching a human priority queue within 1 business day | ≥ 99% |
| O4 | Keep decisions human | % AI outputs reviewed by a triage officer during pilot | 100% |
| O5 | Treat people fairly | Max accuracy gap between writing-style, region and channel groups | ≤ 5 percentage points |

## 5. Scope
**In scope:** discovery; requirements; process redesign; a proof-of-concept classifier on synthetic data; governance, privacy and AI impact analysis; business case; pilot roadmap.

**Out of scope:** production build; integration with real DCSD systems; use of real citizen data; any automated decision on eligibility, payments or debts; voice/phone audio processing; non-English languages (flagged for future).

## 6. Deliverables
All deliverables are in [`/docs`](.) and [`/src`](../src). See the index in the README and the [traceability matrix](16_traceability_matrix.md).

## 7. Approach
Agile-iterative delivery in two two-week sprints following a short discovery: stakeholder analysis → interviews → workshop → requirements → backlog → prototype → governance and business case. Ceremonies and cadence are in [doc 09](09_backlog_and_sprint_plan.md).

## 8. Governance (RACI)
| Activity | Sponsor (EGM Service Delivery) | Business owner (Dir. Contact Centre) | Delivery Lead | BA | Data Science Lead | Privacy / Legal / Security | AI Governance Committee |
|---|---|---|---|---|---|---|---|
| Approve scope & charter | **A** | C | R | R | C | I | I |
| Requirements sign-off | A | **R** | C | **R** | C | C | I |
| Prototype build & evaluation | I | C | A | C | **R** | I | I |
| Privacy & security review | I | C | C | C | C | **A/R** | I |
| AI impact assessment | C | R | C | **R** (draft) | C | C | **A** |
| Pilot go/no-go | **A** | R | R | C | C | C | **R** |

R = Responsible · A = Accountable · C = Consulted · I = Informed

## 9. Assumptions and constraints (summary)
Full list in the [RAID log](08_raid_log.md). Key ones: data would be hosted in an Australian, appropriately security-assessed environment; the model only suggests routes; the agency's accountable use case owner is named before any pilot.

## 10. Glossary
| Term | Meaning |
|---|---|
| **Triage** | Reading an incoming request and deciding which team should handle it, and how urgently |
| **Triage officer** | DCSD staff member who performs triage |
| **Confidence** | The model's own probability for its top suggestion (not a guarantee of correctness) |
| **Shadow mode** | The model makes suggestions in the background; staff do not see or act on them, so performance can be measured safely |
| **Human in the loop (HITL)** | A person reviews and can override every AI output before action |
| **RAID** | Risks, Assumptions, Issues, Dependencies |
| **PIA** | Privacy Impact Assessment |
| **APP** | Australian Privacy Principle (Privacy Act 1988) |
| **PSPF / ISM** | Protective Security Policy Framework / Information Security Manual |
| **TF-IDF** | A way of turning text into numbers by weighting words that are distinctive to a request |
