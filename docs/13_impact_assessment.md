# 13 · Impact Assessment (AI Use Case, Privacy, Security, Stakeholders)

*Simulated engagement. This is a BA-drafted assessment structured around the themes in the Digital Transformation Agency's (DTA) Policy for the responsible use of AI in government (v2.0, effective 15 December 2025) and Australian privacy and security obligations. **A real agency would complete its official AI impact assessment tool and PIA; this document is a working draft that shows the analysis such assessments need.** Legal conclusions are for the agency's Legal and Privacy teams to confirm.*

## 1. Use case description
| Item | Description |
|---|---|
| Name | AI-assisted triage of citizen service requests |
| Purpose | Suggest a receiving team and flag urgency for each incoming free-text request |
| System type | Text classifier (TF-IDF with logistic regression) plus rule-based safety layer |
| Level of autonomy | Assistive. Output is a suggestion; a human decides. No decisions about entitlements, payments, debts or services |
| Users | Triage officers, team leaders, Priority Case Team |
| People affected | Anyone who contacts DCSD, including people in hardship, regional and remote residents, and culturally and linguistically diverse (CALD) customers |
| Data | Request text, channel, request ID. Prototype uses synthetic data only |
| Proposed owner | Accountable use case owner to be nominated (RAID D-04) |

## 2. Indicative risk assessment
| Dimension | Assessment | Reasoning |
|---|---|---|
| Effect on legal rights or entitlements | Low (indirect) | Suggestion only; humans decide; but a mis-route can delay a response |
| Potential harm if wrong | Medium to High for urgent cases | A missed hardship or safety request can cause serious harm |
| Vulnerable groups affected | Yes | People in hardship are over-represented in the urgent category |
| Data sensitivity | High | Free text can contain health, financial and family information |
| Scale | High | Hundreds of thousands of requests per year (assumed) |
| Reversibility | High | Mis-routes can be corrected; delay cannot be undone |
| Transparency to affected people | To be designed | Public transparency statement and notice needed |
| Human oversight | Strong by design | 100% review in pilot; safety rules first |
| **Indicative overall rating** | **Medium, with the hardship and safety pathway treated as elevated** | To be confirmed by the AI Accountable Official; reassess as higher risk if human review is reduced or removed |

**Triggers for re-assessment:** removing or sampling human review; extending to eligibility or payment decisions; adding new categories or languages; any severe incident; material model change.

## 3. Benefits and harms
| | Benefit | Harm | Mitigation |
|---|---|---|---|
| Citizens | Faster routing; hardship flagged earlier | Urgent case missed; unfair treatment by writing style; privacy intrusion | Rules before model; human review; fairness testing; PIA |
| Staff | Less repetitive reading; time for complex work | Deskilling; over-trust; fear of replacement; monitoring concerns | Role redesign; training; blind audits; consultation; override data not used to assess individuals |
| Agency | Capacity, consistency, data insight | Reputational harm from error or bias; legal risk | Governance gates; transparency; incident process |
| Society | Responsible government use of AI | Erosion of trust if poorly handled | Public AI transparency statement; accountable owner; oversight |

## 4. Privacy analysis (Privacy Act 1988, Australian Privacy Principles)
| APP | Consideration | Initial position |
|---|---|---|
| APP 1 Open and transparent management | Privacy policy and public AI transparency statement should describe AI-assisted triage | Update required before pilot |
| APP 3 Collection | Use only what is necessary; request text is already collected for handling the request | No new collection; avoid adding attributes |
| APP 5 Notification | People should be told that AI assists in handling requests | Add to collection notice |
| APP 6 Use and disclosure | Using request text to train or evaluate a model may be a secondary use; needs assessment | **Legal and Privacy to advise before real data used for training** |
| APP 8 Cross-border disclosure | Avoid offshore processing | Require onshore hosting |
| APP 10 Quality | Accuracy of labels and outputs | Labelling guidelines; double review; monitoring |
| APP 11 Security and destruction | Protect and dispose of data | Controls in section 5; retention schedule |
| APP 12 and 13 Access and correction | Logs about a person may be personal information subject to access and correction | Design logs to be retrievable and correctable |

**PIA:** because free text may include sensitive information and the use is new and large-scale, a full Privacy Impact Assessment is recommended, and agencies are generally expected to complete one for high privacy risk projects under the Privacy (Australian Government Agencies, Governance) APP Code. Privacy Officer to determine (D-01).

**Data minimisation controls (design):** mask names, addresses, phone numbers, email addresses and reference numbers in logs; do not store full text in monitoring dashboards; restrict access by role; do not use real data for training before approvals; no use of group attributes beyond those approved for fairness testing.

## 5. Security
| Area | Requirement |
|---|---|
| Classification | Determine classification of request text and outputs under the Protective Security Policy Framework (PSPF); assume at least a sensitive handling requirement until assessed |
| Hosting | Australian hosting in an environment assessed for the classification; follow the Information Security Manual (ISM) controls |
| Access | Role-based; least privilege; multi-factor authentication; separation of model development and production |
| Data protection | Encryption in transit and at rest; logging and alerting |
| Supply chain | Review third-party libraries and any hosted services |
| Resilience | Fail-safe to manual queue (NFR-10) |

## 6. Legal and administrative law notes (for Legal to confirm)
- The design avoids automated decision-making by keeping a human as decision maker and by prohibiting any outbound decision or communication (DEC-01, FR-14).
- Where a statute governs the downstream decision, the human decision maker must still consider each case on its merits; the tool must not fetter that discretion. Officer training should say so.
- Records: audit logs and suggestions may be Commonwealth records under the Archives Act 1983; retention to be set with the records manager.
- Accessibility and discrimination: monitor for indirect discrimination in outputs (see fairness analysis in doc 14).

## 7. Stakeholder impact summary
| Group | Impact | Consultation |
|---|---|---|
| Triage officers | Role shifts toward review and exceptions | Co-design; staff representatives; training |
| Receiving teams | Fewer mis-routes; new data in referrals | Workshop; pilot metrics |
| Priority Case Team | Owns safety phrase list; may see more flagged cases | Direct involvement |
| Customers in hardship | Earlier visibility; risk if missed | Advocacy consultation; human review |
| CALD and remote customers | Risk of lower accuracy | Group testing; plain-language review; future language support |
| Privacy, security, legal | Assurance obligations | Gated approvals |

## 8. Residual risk and conditions of approval
Approval to proceed to shadow mode should be conditional on: nominated use case owner; PIA and security authorisation complete; staff consultation under way; group-gap treatment plan accepted; welfare-owned hardship phrase list; incident process agreed.
