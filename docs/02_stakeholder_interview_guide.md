# 02 · Stakeholder Interview Guide and Synthesis

*The guide in sections 1–4 is a reusable working document. Section 5 is a **simulated** synthesis written for this portfolio from role-based personas; it represents plausible hypotheses to test, not research data.*

## 1. Purpose and approach
Understand the current triage process, pain points, constraints and success criteria; surface concerns early; validate assumptions before the workshop.
- **Format:** 30–45 minute semi-structured interviews, one stakeholder at a time (small group for team managers).
- **Sample:** at least one person from each of S01–S10 and three triage officers.
- **Record:** notes only, with consent; anonymise quotes in reporting.

## 2. Opening script
"Thanks for your time. We're exploring whether technology could help route service requests faster and more fairly. Nothing has been decided. I'm here to learn how triage works today and what would make a change useful or risky. I'll take notes; comments will be reported without names. Is that okay?"

## 3. Question bank
**A. Everyone (context)**
1. Describe your role and how you interact with incoming service requests.
2. What does a good outcome look like for a citizen, and for your team?
3. What worries you most about changing how triage works?

**B. Triage officers and team leaders (S03)**
4. Walk me through the last request you triaged, from opening it to routing it.
5. How do you decide which team and how urgent? What cues do you look for?
6. How often are requests misrouted or bounced back? What causes it?
7. What do you do when a request mentions hardship or safety?
8. Which parts of the job would you be happy to hand to a tool? Which never?
9. What would you need to see to trust a suggestion from a system?

**C. Receiving team managers (S04)**
10. What makes a referral easy or hard to handle?
11. What does a misrouted request cost you in time and rework?
12. How do you currently know whether the queue contains urgent cases?

**D. Operations and sponsor (S01, S02)**
13. Which metrics do you report on, and where are the gaps?
14. What would make you stop this initiative?
15. What level of risk is acceptable for a pilot?

**E. Privacy, security, legal, governance (S06–S09)**
16. What classification and hosting constraints apply to request text?
17. When does a tool like this become an automated decision under our obligations?
18. What assessments and approvals are mandatory before a pilot?
19. What would you need to see to approve a risk rating?

**F. Advocacy and staff representatives (S10, S11)**
20. Which citizen groups are most at risk of being misunderstood by a text classifier?
21. What consultation do you expect before any change to roles?
22. What transparency would you expect to be published?

## 4. Note-taking template
| Field | Notes |
|---|---|
| Interviewee role / date | |
| Key facts about current process | |
| Pain points (with examples) | |
| Needs and success criteria | |
| Concerns and risks | |
| Quotes (anonymised) | |
| Follow-ups / documents requested | |

## 5. Simulated interview synthesis
*Personas based on typical government contact-centre operations. Figures marked "assumed" are planning assumptions, not measured data, and would be validated in discovery.*

### 5.1 Themes
| # | Theme | Evidence (simulated) | Source roles | Requirement link |
|---|---|---|---|---|
| T1 | Every request is read manually; Monday and post-holiday peaks create backlogs | "Mondays are a wall." Backlog clears mid-week | S02, S03 | BR-01, BR-02 |
| T2 | Misrouting causes rework (assumed ~10–15% of requests are re-routed at least once) | Team managers describe returning requests to the triage queue | S03, S04 | BR-03 |
| T3 | Urgent hardship cases can sit in the general queue because urgency cues are buried in long messages | Officers rely on spotting keywords while skimming | S02, S03, S10 | BR-04, BR-05 |
| T4 | Officers want suggestions but fear replacement | "If it's a suggestion I can overrule, fine. If it replaces me, no." | S03, S11 | BR-07, BR-09 |
| T5 | Trust depends on seeing *why* the tool suggested something | Officers want highlighted words, not a black box | S03, S08 | BR-06 |
| T6 | Privacy and security approvals gate any use of real text | PIA and hosting decisions needed before data use | S06, S07 | BR-08 |
| T7 | Risk of unequal performance for non-native English, very short, or very formal messages | Advocacy reps want group-level testing and published results | S10 | BR-10 |
| T8 | Legal wants clarity that the tool suggests, not decides | Automated decision-making obligations if outputs affect rights | S08, S09 | BR-07, BR-13 |

### 5.2 Insights that shaped the design
1. **Suggest, never decide.** All outputs are advisory (T4, T8).
2. **Safety rules sit in front of the model** and cannot be overridden by it (T3).
3. **Low confidence means a human, not a guess** (T2, T5).
4. **Explain every suggestion in plain language** (T5).
5. **Measure fairness by group from day one** (T7).

### 5.3 Open questions carried to the workshop
- What confidence threshold balances workload relief and accuracy? (answered with data in doc 14)
- Which phrases must always trigger priority escalation, and who owns that list?
- How will officer overrides be captured to improve the model safely?
