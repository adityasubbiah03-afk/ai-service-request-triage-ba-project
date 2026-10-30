# 03 · Requirements Workshop: Plan, Facilitation and Outcomes

*The plan and facilitation materials are reusable. Section 6 records the outcomes of a **simulated** workshop with role-based participants, written to demonstrate how outcomes are captured and converted into requirements.*

## 1. Workshop objectives
1. Agree the problem statement and the boundary of the first release.
2. Prioritise requirements using MoSCoW.
3. Agree safety, privacy and human-oversight principles for the pilot.
4. Identify risks, assumptions and decisions needed.

## 2. Participants and roles
| Role | Represented by |
|---|---|
| Facilitator and scribe | BA |
| Decision maker | Director, Contact Centre Operations (S02) |
| Subject experts | Triage officers (×3), receiving team managers (×2) |
| Technical | Data Science Lead, IT Delivery representative |
| Assurance | Privacy Officer, Security Advisor, Legal (observer) |
| Voice of customer | Customer advocacy representative |

## 3. Logistics
- Duration 3 hours, in person with a remote option, 10–12 participants.
- Pre-read (sent 2 days prior): charter, as-is process map ([doc 07](07_process_maps.md)), interview themes ([doc 02](02_stakeholder_interview_guide.md)).
- Materials: process map printed A1, sticky notes, dot stickers, MoSCoW board, parking-lot sheet, decision log.

## 4. Agenda
| Time | Item | Technique | Output |
|---|---|---|---|
| 0:00–0:10 | Welcome, ground rules, objectives | Check-in | Shared purpose |
| 0:10–0:30 | Current-state walkthrough | Process walkthrough on printed map | Validated as-is map and pain points |
| 0:30–1:00 | Pain points and impact | Affinity grouping, dot voting | Ranked pain points |
| 1:00–1:15 | Break | | |
| 1:15–1:55 | Future-state principles | "How might we…", pre-mortem ("it's 12 months later and this failed, why?") | Design principles, failure modes |
| 1:55–2:35 | Prioritise requirements | MoSCoW with dot allocation | Prioritised list |
| 2:35–2:50 | Risks, assumptions, decisions | RAID capture | RAID entries and decisions |
| 2:50–3:00 | Recap and next steps | Read-back | Actions and owners |

## 5. Facilitation notes
- Start with the process, not the technology, to keep the conversation on the problem.
- Use the pre-mortem to give sceptics a constructive outlet.
- Capture *decisions* and *actions* visibly; park out-of-scope items without dismissing them.
- Check every requirement for: who needs it, why, how we would know it is met.
- Quiet-voice tactic: silent writing before discussion so triage officers are heard alongside senior staff.

## 6. Simulated outcomes
### 6.1 Ranked pain points (dot votes)
| Rank | Pain point | Votes |
|---|---|---|
| 1 | Urgent hardship cases hard to spot in a long queue | 14 |
| 2 | Monday and post-holiday backlog | 11 |
| 3 | Misrouted requests bounce between teams | 9 |
| 4 | Inconsistent routing between officers | 6 |
| 5 | No reliable data on why requests arrive | 3 |

### 6.2 Pre-mortem: why might this fail?
| Failure mode | Mitigation adopted |
|---|---|
| An urgent person is missed because the model was confident and wrong | Hardship and safety rules run first; every pilot suggestion is reviewed by a human (RAID R-01) |
| Staff ignore or distrust suggestions | Show reasons; capture overrides; co-design with officers (R-04) |
| Model performs worse for some customer groups | Group fairness testing and thresholds (R-05) |
| Real data cannot be used because approvals stall | Prototype on synthetic data; PIA started early (R-07) |
| Staff see it as a cost-cutting tool | Early consultation with staff representatives (I-02) |

### 6.3 MoSCoW outcome
| Priority | Requirements |
|---|---|
| **Must** | Suggest team routing (BR-01); route low-confidence to manual queue (BR-03); never auto-queue hardship as routine (BR-04, BR-05); human review of all outputs in pilot (BR-07); explain suggestions (BR-06); audit log (BR-09); privacy and security approvals before real data (BR-08) |
| **Should** | Fairness reporting by group (BR-10); confidence threshold configurable (BR-11); officer override capture (BR-12) |
| **Could** | Suggested SLA and priority label; trend dashboard of request themes |
| **Won't (this release)** | Automated responses to citizens; any eligibility, payment or debt decision; non-English languages; voice audio |

### 6.4 Decisions
| ID | Decision | Owner |
|---|---|---|
| DEC-01 | The tool suggests routes only; it never makes or communicates decisions | Director, Contact Centre Ops |
| DEC-02 | Safety and hardship rules take precedence over model output | Director, Contact Centre Ops |
| DEC-03 | Proof of concept uses synthetic data only | Privacy Officer |
| DEC-04 | Pilot begins in shadow mode before any staff-facing suggestions | Sponsor |
| DEC-05 | Fairness gap threshold of 5 percentage points triggers review | AI Governance Committee |

### 6.5 Actions
| # | Action | Owner | Due |
|---|---|---|---|
| A1 | Start PIA threshold assessment | Privacy Officer | Sprint 2 |
| A2 | Confirm hosting and classification options | Security Advisor | Sprint 2 |
| A3 | Provide anonymised triage volumes and timings | Contact Centre Ops | Sprint 1 |
| A4 | Draft hardship and safety phrase list for clinical/welfare review | Priority Case Team manager | Sprint 2 |
| A5 | Brief staff representatives | Sponsor | Sprint 1 |

### 6.6 Parking lot
Multilingual support; auto-acknowledgement emails to citizens; integration with case management; trend analytics for policy teams.
