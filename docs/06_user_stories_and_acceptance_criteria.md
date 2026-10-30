# 06 · User Stories and Acceptance Criteria

*Simulated engagement. Story IDs trace to requirements in [doc 04](04_business_requirements.md) and [doc 05](05_functional_requirements.md), and to tests in [`tests/test_triage.py`](../tests/test_triage.py). Sprint planning is in [doc 09](09_backlog_and_sprint_plan.md).*

**Definition of Ready:** story has persona, value, acceptance criteria, traced requirement, estimate, and no unresolved dependency.

**Definition of Done:** acceptance criteria met and demonstrated; tests pass; documentation updated; no open high-severity defects; product owner accepts.

## Summary

| ID | Epic | Persona | Priority | Points | Sprint | Status |
|---|---|---|---|---|---|---|
| US-01 | E1 Triage suggestion | triage officer | Must | 5 | 1 | Done (prototype) |
| US-02 | E1 Triage suggestion | triage officer | Must | 2 | 1 | Done (prototype) |
| US-03 | E1 Triage suggestion | team leader | Must | 3 | 1 | Done (prototype) |
| US-04 | E2 Safety and priority | Priority Case Team manager | Must | 5 | 1 | Done (prototype) |
| US-05 | E2 Safety and priority | Priority Case Team manager | Must | 3 | 1 | Done (prototype) |
| US-06 | E3 Transparency | triage officer | Must | 3 | 1 | Done (prototype) |
| US-07 | E3 Transparency | Director, Contact Centre Operations | Must | 5 | 2 | Done (prototype) |
| US-08 | E4 Governance and monitoring | AI Governance Committee member | Should | 5 | 2 | Done (prototype) |
| US-09 | E5 Staff workflow | triage officer | Should | 5 | Pilot backlog | Backlog (needs production build) |
| US-10 | E4 Governance and monitoring | Legal and oversight reviewer | Must | 5 | Pilot backlog | Backlog (needs production build) |
| US-11 | E4 Governance and monitoring | Director, Contact Centre Operations | Should | 3 | 2 | Partial (config file only) |
| US-12 | E4 Governance and monitoring | Data Science Lead | Should | 5 | Pilot backlog | Backlog (needs production build) |
| US-13 | E2 Safety and priority | triage officer | Must | 3 | Pilot backlog | Backlog (needs production build) |
| US-14 | E2 Safety and priority | Chief Counsel | Must | 2 | 1 | Done by design |
| US-15 | E5 Staff workflow | receiving team manager | Could | 2 | Pilot backlog | Backlog (needs production build) |
| US-16 | E4 Governance and monitoring | Privacy Officer | Must | 5 | Pilot backlog | Backlog (needs production build) |

**Story points by plan:** Sprint 1 = 23, Sprint 2 = 13, Pilot backlog = 25. Enabler tasks (analysis and governance work that is not a user story) are tracked in [doc 09](09_backlog_and_sprint_plan.md).

## Stories

### US-01 · The system to suggest which team should handle each incoming request

**As a** triage officer, **I want** the system to suggest which team should handle each incoming request, **so that** I can route requests faster and more consistently.

- **Epic:** E1 Triage suggestion · **Priority:** Must · **Estimate:** 5 pts · **Sprint:** 1
- **Traces to:** BR-01, BR-02 / FR-01, FR-02
- **Status:** Done (prototype)
- **Test evidence:** test_clear_account_access_request_is_routed; test_every_result_has_a_valid_category

**Acceptance criteria**

1. **Given** a new request containing free text, **when** it is processed, **then** exactly one of the seven categories is suggested together with the receiving team and service-level target.
2. **Given** a clear single-topic request (e.g. locked out of account), **when** processed, **then** the suggested team is Account Support Team.
3. **Given** any request, **then** the output never states or implies a decision about eligibility, payment or debt.

### US-02 · To see how confident the system is in each suggestion

**As a** triage officer, **I want** to see how confident the system is in each suggestion, **so that** I know when to look more carefully.

- **Epic:** E1 Triage suggestion · **Priority:** Must · **Estimate:** 2 pts · **Sprint:** 1
- **Traces to:** BR-06 / FR-03
- **Status:** Done (prototype)
- **Test evidence:** Covered in test_clear_account_access_request_is_routed (confidence returned)

**Acceptance criteria**

1. **Given** a suggestion, **then** a confidence value between 0 and 1 is shown.
2. **Given** confidence below the threshold, **then** the suggestion is visibly flagged as low confidence.

### US-03 · Uncertain requests to go to a manual triage queue instead of being guessed

**As a** team leader, **I want** uncertain requests to go to a manual triage queue instead of being guessed, **so that** routine errors do not reach the wrong team.

- **Epic:** E1 Triage suggestion · **Priority:** Must · **Estimate:** 3 pts · **Sprint:** 1
- **Traces to:** BR-03 / FR-04
- **Status:** Done (prototype)
- **Test evidence:** test_low_confidence_goes_to_manual_queue

**Acceptance criteria**

1. **Given** model confidence below the configured threshold, **when** processed, **then** the request is placed in the manual triage queue with the flag LOW_CONFIDENCE.
2. **Given** a vague or empty message, **then** it is never auto-suggested to a team.
3. **Given** the threshold, **then** the share of requests sent to the manual queue is reported.

### US-04 · Requests that mention financial hardship to be escalated to my team regardless of the model's category

**As a** Priority Case Team manager, **I want** requests that mention financial hardship to be escalated to my team regardless of the model's category, **so that** people in urgent need are not left in a routine queue.

- **Epic:** E2 Safety and priority · **Priority:** Must · **Estimate:** 5 pts · **Sprint:** 1
- **Traces to:** BR-04, BR-05 / FR-05
- **Status:** Done (prototype)
- **Test evidence:** test_hardship_rule_overrides_routine_routing

**Acceptance criteria**

1. **Given** a request containing a hardship phrase on the agreed list (e.g. no food, eviction), **when** processed, **then** the action is PRIORITY_HUMAN_ESCALATION and the team is Priority Case Team, even if the model predicts another category.
2. **Given** a mixed request (late payment AND no food), **then** it is escalated as hardship.
3. **Given** a hardship escalation, **then** it is never auto-closed or auto-answered.

### US-05 · Requests that indicate risk to personal safety to be escalated immediately

**As a** Priority Case Team manager, **I want** requests that indicate risk to personal safety to be escalated immediately, **so that** a person can be contacted without delay under agency procedures.

- **Epic:** E2 Safety and priority · **Priority:** Must · **Estimate:** 3 pts · **Sprint:** 1
- **Traces to:** BR-05 / FR-06
- **Status:** Done (prototype)
- **Test evidence:** test_life_safety_phrase_is_escalated_immediately

**Acceptance criteria**

1. **Given** a request matching a life-safety phrase, **then** the action is IMMEDIATE_SAFETY_ESCALATION with a service-level target of zero days.
2. **Given** such a match, **then** the model output cannot downgrade the escalation.
3. **Given** the phrase list, **then** it is owned and reviewed by welfare specialists, not data scientists.

### US-06 · A plain-language reason for each suggestion

**As a** triage officer, **I want** a plain-language reason for each suggestion, **so that** I can judge whether to accept or override it.

- **Epic:** E3 Transparency · **Priority:** Must · **Estimate:** 3 pts · **Sprint:** 1
- **Traces to:** BR-06 / FR-07
- **Status:** Done (prototype)
- **Test evidence:** test_explanation_terms_are_returned

**Acceptance criteria**

1. **Given** a model-based suggestion, **then** up to five words or phrases from the request that most influenced the suggestion are returned.
2. **Given** a rule-based escalation, **then** the reason states which rule matched.
3. **Given** the explanation, **then** it contains no jargon (no coefficients, no probabilities beyond confidence).

### US-07 · An evaluation report showing how well the classifier performs and how it compares with simple baselines

**As a** Director, Contact Centre Operations, **I want** an evaluation report showing how well the classifier performs and how it compares with simple baselines, **so that** I can make an evidence-based go/no-go decision.

- **Epic:** E3 Transparency · **Priority:** Must · **Estimate:** 5 pts · **Sprint:** 2
- **Traces to:** BR-02, BR-03 / FR-01
- **Status:** Done (prototype)
- **Test evidence:** test_overall_accuracy_meets_minimum_bar

**Acceptance criteria**

1. **Given** a training run, **then** accuracy, macro F1, per-category precision and recall, and a confusion matrix are produced.
2. **Given** the evaluation, **then** results are compared with a majority-class baseline and an alternative model.
3. **Given** the threshold, **then** a coverage-versus-accuracy trade-off table is produced.
4. **Given** the automated test suite, **then** it fails if accuracy on the synthetic test set drops below 85%.

### US-08 · Performance reported separately for different writing styles, regions and channels

**As a** AI Governance Committee member, **I want** performance reported separately for different writing styles, regions and channels, **so that** we can see whether any group is served worse.

- **Epic:** E4 Governance and monitoring · **Priority:** Should · **Estimate:** 5 pts · **Sprint:** 2
- **Traces to:** BR-10 / FR-11
- **Status:** Done (prototype)
- **Test evidence:** Output reviewed: reports/fairness_by_group.csv

**Acceptance criteria**

1. **Given** an evaluation run, **then** accuracy and macro F1 are reported for each group in writing style, region and channel.
2. **Given** a gap above 5 percentage points between the best and any other group, **then** it is highlighted for review.
3. **Given** small groups, **then** the group size is reported so results are read with appropriate caution.

### US-09 · To accept or override a suggestion and record a reason

**As a** triage officer, **I want** to accept or override a suggestion and record a reason, **so that** my expertise corrects the system and improves it safely over time.

- **Epic:** E5 Staff workflow · **Priority:** Should · **Estimate:** 5 pts · **Sprint:** Pilot backlog
- **Traces to:** BR-12 / FR-10
- **Status:** Backlog (needs production build)
- **Test evidence:** Not in prototype

**Acceptance criteria**

1. **Given** a suggestion, **when** I accept or choose a different team, **then** my action and an optional reason code are stored against the request.
2. **Given** overrides, **then** the override rate is reported by category and officer team (not by individual) monthly.
3. **Given** an override, **then** the model is never retrained automatically from it without data-science review.

### US-10 · A complete audit record for each triaged request

**As a** Legal and oversight reviewer, **I want** a complete audit record for each triaged request, **so that** any outcome can be explained and reviewed later.

- **Epic:** E4 Governance and monitoring · **Priority:** Must · **Estimate:** 5 pts · **Sprint:** Pilot backlog
- **Traces to:** BR-09 / FR-09
- **Status:** Backlog (needs production build)
- **Test evidence:** Not in prototype

**Acceptance criteria**

1. **Given** a processed request, **then** the log stores request ID, timestamp, model version, rule matches, suggestion, confidence, reasons and officer action.
2. **Given** the log, **then** personal information is masked or minimised per the privacy assessment.
3. **Given** the retention schedule, **then** logs are retained and disposed of in line with records obligations.

### US-11 · To adjust the confidence threshold and review the phrase lists without a code release

**As a** Director, Contact Centre Operations, **I want** to adjust the confidence threshold and review the phrase lists without a code release, **so that** the service can respond to changing risk appetite quickly.

- **Epic:** E4 Governance and monitoring · **Priority:** Should · **Estimate:** 3 pts · **Sprint:** 2
- **Traces to:** BR-11 / FR-08
- **Status:** Partial (config file only)
- **Test evidence:** Configuration in src/config.py

**Acceptance criteria**

1. **Given** an authorised user, **when** they change the threshold, **then** the change is versioned, approved and logged.
2. **Given** a proposed threshold, **then** the expected share sent to manual review is shown before approval.

### US-12 · Monthly monitoring of accuracy, group gaps, override rate and data drift

**As a** Data Science Lead, **I want** monthly monitoring of accuracy, group gaps, override rate and data drift, **so that** degradation is detected before it harms people.

- **Epic:** E4 Governance and monitoring · **Priority:** Should · **Estimate:** 5 pts · **Sprint:** Pilot backlog
- **Traces to:** BR-14 / FR-12
- **Status:** Backlog (needs production build)
- **Test evidence:** Not in prototype

**Acceptance criteria**

1. **Given** a monthly sample reviewed by humans, **then** accuracy and hardship recall are computed.
2. **Given** accuracy dropping more than 3 percentage points, or any group gap above 5 points, **then** an alert goes to the use case owner.
3. **Given** an alert, **then** the incident process in doc 14 is triggered.

### US-13 · The system to fail safe by sending requests to the manual queue if anything goes wrong

**As a** triage officer, **I want** the system to fail safe by sending requests to the manual queue if anything goes wrong, **so that** no request is lost or silently mishandled.

- **Epic:** E2 Safety and priority · **Priority:** Must · **Estimate:** 3 pts · **Sprint:** Pilot backlog
- **Traces to:** BR-03 / FR-15
- **Status:** Backlog (needs production build)
- **Test evidence:** test_handles_empty_and_odd_input (odd input only)

**Acceptance criteria**

1. **Given** an empty, very long or malformed request, **then** the service returns a valid result and does not fail.
2. **Given** a service outage, **then** all new requests flow to the manual queue and an alert is raised.
3. **Given** recovery, **then** requests received during the outage are not re-processed automatically.

### US-14 · Certainty that the tool cannot take decisions or contact citizens

**As a** Chief Counsel, **I want** certainty that the tool cannot take decisions or contact citizens, **so that** administrative-law and automated-decision risks are contained.

- **Epic:** E2 Safety and priority · **Priority:** Must · **Estimate:** 2 pts · **Sprint:** 1
- **Traces to:** BR-07, BR-13 / FR-14
- **Status:** Done by design
- **Test evidence:** Prototype exposes no outbound or decision interface

**Acceptance criteria**

1. **Given** the architecture, **then** the tool has read-only access to request text and write access only to its own suggestion record.
2. **Given** any output, **then** it is labelled 'suggestion for human review'.

### US-15 · Referred requests to arrive with the category and the reason for routing

**As a** receiving team manager, **I want** referred requests to arrive with the category and the reason for routing, **so that** my team can start work without re-reading everything.

- **Epic:** E5 Staff workflow · **Priority:** Could · **Estimate:** 2 pts · **Sprint:** Pilot backlog
- **Traces to:** BR-01, BR-06 / FR-13
- **Status:** Backlog (needs production build)
- **Test evidence:** Not in prototype

**Acceptance criteria**

1. **Given** a routed request, **then** my queue shows the suggested category, reasons and any flags.

### US-16 · Personal information minimised and masked in logs and training data

**As a** Privacy Officer, **I want** personal information minimised and masked in logs and training data, **so that** the initiative complies with the Australian Privacy Principles.

- **Epic:** E4 Governance and monitoring · **Priority:** Must · **Estimate:** 5 pts · **Sprint:** Pilot backlog
- **Traces to:** BR-08 / FR-09
- **Status:** Backlog (needs production build)
- **Test evidence:** Not in prototype (synthetic data only)

**Acceptance criteria**

1. **Given** request text, **then** names, addresses, phone numbers, emails and reference numbers are masked before storage in logs.
2. **Given** real data for training, **then** use only starts after the PIA and security approvals are recorded.
