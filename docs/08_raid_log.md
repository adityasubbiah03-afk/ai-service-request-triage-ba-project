# 08 · RAID Log (Risks, Assumptions, Issues, Dependencies) and Decision Log

*Simulated engagement. Status as at the end of Sprint 2. Ratings: Likelihood (L) and Impact (I) each 1–5; Score = L × I. 1–6 Low · 7–12 Medium · 13–19 High · 20–25 Very high.*

## Risks
| ID | Risk | L | I | Score | Mitigation | Owner | Status |
|----|------|---|---|-------|------------|-------|--------|
| R-01 | An urgent hardship or safety case is missed or delayed because phrasing is not covered by rules or the model | 3 | 5 | 15 High | Rules run before model; 100% human review in pilot; welfare-owned phrase list; shadow mode first; hardship recall monitored monthly | Priority Case Team manager | Open |
| R-02 | Automation bias: officers accept suggestions without checking | 4 | 4 | 16 High | Show confidence and reasons; training; random blind audits; override-rate monitoring | Contact Centre Ops | Open |
| R-03 | Model drifts as policies, payment types or language change | 3 | 3 | 9 Medium | Monthly monitoring; quarterly retraining review; change control | Data Science Lead | Open |
| R-04 | Staff distrust or reject suggestions | 3 | 3 | 9 Medium | Co-design with officers; explanations; feedback loop; transparent metrics | BA / Team leaders | Open |
| R-05 | Unequal performance across customer groups | 4 | 4 | 16 High | Group fairness testing; 5-point threshold; data augmentation; human review; advocacy consultation. **Prototype shows an 8.2-point writing-style gap (I-03)** | AI Governance Committee | Open, being treated |
| R-06 | Privacy breach or over-collection of personal information in logs or training | 2 | 5 | 10 Medium | Data minimisation; masking; PIA; synthetic data for PoC; access controls | Privacy Officer | Open |
| R-07 | PIA, security or AI governance approvals delay the pilot | 3 | 3 | 9 Medium | Start approvals in Sprint 2; early engagement; phased scope | BA / Delivery Lead | Open |
| R-08 | Synthetic-data results overstate real-world performance | 5 | 4 | 20 Very high | Treat PoC as feasibility only; shadow-mode evaluation on real data after approvals; expect lower accuracy and more variety in real language | Data Science Lead | Open |
| R-09 | Scope creep toward automated decisions or citizen-facing responses | 2 | 5 | 10 Medium | DEC-01; legal review; no outbound interface by design | Sponsor | Open |
| R-10 | Benefits overstated; released time is capacity, not cashable savings | 3 | 3 | 9 Medium | Present benefits as capacity; sensitivity analysis; validate with operational data | BA | Open |
| R-11 | Hosting or tooling constraints limit the solution | 2 | 3 | 6 Low | Early architecture and security engagement | Enterprise Architecture | Open |
| R-12 | Historical labels are inconsistent or wrong | 4 | 3 | 12 Medium | Labelling guidelines; double review of a sample; relabel before training (see I-04) | Data Science Lead | Open |
| R-13 | People game phrasing to gain priority | 2 | 3 | 6 Low | Human verification of all priority cases; rules reviewed regularly | Priority Case Team manager | Open |

## Assumptions
| ID | Assumption | How to validate | Owner |
|----|------------|-----------------|-------|
| A-01 | 600,000 requests per year and 2.5 minutes of triage per request | Operational data (D-03) | Contact Centre Ops |
| A-02 | About 2% of historical triage labels are wrong | Double-review a sample | Data Science Lead |
| A-03 | Requests are in English for this release | Check language mix in intake data | BA |
| A-04 | A named accountable use case owner will exist before the pilot | Confirm with AI Accountable Official | Sponsor |
| A-05 | Officers will review 100% of outputs in the pilot | Pilot design and compliance checks | Contact Centre Ops |
| A-06 | An Australian-hosted environment suitable for the data classification is available | Security assessment | Security Advisor |
| A-07 | Loaded cost of $60 per officer hour is representative | Finance validation | Finance partner |

## Constraints
| ID | Constraint |
|----|------------|
| C-01 | Request text may contain sensitive personal information, so classification, hosting and access controls apply |
| C-02 | Consultation obligations with staff and their representatives apply before role changes |
| C-03 | Government AI policy and Privacy Act obligations apply (see doc 14) |

## Issues
| ID | Issue | Impact | Action | Owner | Status |
|----|-------|--------|--------|-------|--------|
| I-01 | Operational baseline data (volumes, timings, re-route rate) not yet supplied | Business case rests on assumptions | Chase action A3; replace assumptions with data | Contact Centre Ops | Open |
| I-02 | Staff and staff-representative consultation has not started | Risk to trust and to compliance | Sponsor to brief representatives (action A5); plan consultation | Sponsor | Open |
| I-03 | Accuracy gap by writing style is 8.2 points on synthetic data (formal 89.1%, ESL-style 89.7%, plain 92.2%, terse 97.3%), above the 5-point threshold | Fails NFR-06 and BR-10 target | Investigate cause; add training variety; retest; do not proceed to pilot until resolved on real data | Data Science Lead | Open |
| I-04 | In the test set, all 4 hardship cases not escalated were records whose recorded label contradicted their text (label noise) | Evidence that label quality affects measured recall | Introduce labelling guidelines and double review; report recall on cleaned labels | Data Science Lead | Open |

## Dependencies
| ID | Dependency | Needed by | Owner | Status |
|----|------------|-----------|-------|--------|
| D-01 | Privacy Impact Assessment | Before any real data | Privacy Officer | Not started |
| D-02 | Security authorisation and hosting decision | Before any real data | Security Advisor | Not started |
| D-03 | Operational data from Contact Centre Ops | Business case validation | Contact Centre Ops | Requested |
| D-04 | Appointment of accountable use case owner | Before pilot | Sponsor | Not started |
| D-05 | AI Governance Committee meeting slot | Pilot go/no-go | AI Governance Committee | Proposed |
| D-06 | Case-management system capability to hold a suggestion field | Assisted mode | Enterprise Architecture | Unknown |

## Decision log
| ID | Decision | Date | Decided by | Rationale |
|----|----------|------|------------|-----------|
| DEC-01 | Tool suggests only; never decides or contacts citizens | Workshop | Director, Contact Centre Ops | Legal and ethical risk; staff trust |
| DEC-02 | Safety and hardship rules take precedence over the model | Workshop | Director, Contact Centre Ops | Protect people in urgent need |
| DEC-03 | PoC uses synthetic data only | Workshop | Privacy Officer | No approvals yet for real data |
| DEC-04 | Pilot starts in shadow mode | Workshop | Sponsor | Measure safely before exposure |
| DEC-05 | 5-point group accuracy gap triggers review | Workshop | AI Governance Committee | Fairness control |
| DEC-06 | Use TF-IDF with logistic regression | Sprint 1 | Data Science Lead | Matches Naive Bayes accuracy in testing and gives inspectable term weights for explanations |
| DEC-07 | Prototype confidence threshold set at 0.60 | Sprint 1 | Data Science Lead | Sends about 5% of requests to manual review while accuracy of suggestions rises vs. no threshold; to be re-set on real data |
