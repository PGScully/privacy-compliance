# European Union — audit checklist (GDPR, AI Act, Data Act)

Control-by-control audit procedures for an EU audit. Use with `references/audit.md`
(methodology, ratings, reporting) and the obligation references `references/eu/gdpr.md`,
`references/eu/ai-act.md` and `references/eu/data-act.md`.

Determine first whether each regulation applies (GDPR Art 3; AI Act Art 2; Data Act
Art 1) and mark non-applicable controls with the basis.

## Applying this checklist at each stage

These controls apply at every stage; only the evidence and procedure change (see
`references/audit.md`). For example:

- **Requirements:** assess Art 5(1)(c) minimisation and the Art 6 lawful basis
  against the planned data elements; require the Art 13/14 notice content; ask where
  data will be hosted (Art 44–49); require retention rules (Art 5(1)(e)); classify AI
  systems (AI Act Art 5/6).
- **Design:** confirm Art 25 data protection by design and by default, Art 32 security
  design, Art 22 automated-decision safeguards, and AI Act Art 14 human oversight.
- **Build / operation:** inspect code and config, re-perform rights requests and
  deletion in a test environment, and test operating effectiveness from records
  (ROPA, DPAs, DPIA, access reviews, breach register).

## GDPR — principles and lawfulness

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| Art 5(1)(a) | Is processing lawful, fair and transparent? | Bases, notices, DPAs | Each activity has a basis and notice |
| Art 5(1)(b) | Is processing purpose-limited? | ROPA, lineage, tags | No incompatible secondary use |
| Art 5(1)(c) | Is data minimised? | Schemas, payloads | Fields necessary for the purpose |
| Art 5(1)(d) | Is data accurate? | Validation, correction flow | Accuracy controls and rectification |
| Art 5(1)(e) | Is storage limited? | Retention schedule, deletion jobs | Retention enforced and documented |
| Art 5(1)(f) | Integrity and confidentiality? | Security config (Art 32) | Appropriate safeguards |
| Art 5(2) | Accountability demonstrated? | Policies, records, evidence | Compliance can be evidenced |
| Art 6 | Is there a valid legal basis per activity? | ROPA, consent records, LIAs | Recorded basis; legitimate-interest assessments |
| Art 7 | Is consent demonstrable, granular and withdrawable? | Consent records, preference centre | Freely given; withdrawal as easy as giving |
| Art 9 | Are special-category data covered by a condition? | Sensitive fields, conditions, explicit consent | Art 9(2) condition per item |
| Art 10 | Is criminal-conviction data controlled? | Data flows, official-authority basis | Official control or lawful authorisation |

## GDPR — rights

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| Art 12 | Is information concise, accessible and timely? | Notice, request workflow, SLA | One-month clock; free of charge |
| Art 13/14 | Is required information provided, and by when? | Notice content; source data | All Art 13/14 items present |
| Art 15–20 | Are access, rectification, erasure, restriction, portability supported? | Endpoints, runbooks, exports | Each right operable |
| Art 19 | Are recipients notified of changes? | Notification mechanism | Recipients informed where required |
| Art 21 | Can individuals object, including to marketing? | Objection flow, suppression | Absolute marketing objection honoured |
| Art 22 | Are automated decisions controlled? | Logic docs, human review | Rights to intervention/contest supported |

## GDPR — controller/processor and security

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| Art 24 | Are appropriate measures implemented and reviewed? | Governance, policies | Measures documented and current |
| Art 25 | Data protection by design and by default? | Design docs, defaults, pseudonymisation | Principles embedded; safe defaults |
| Art 26 | Are joint-controller roles defined? | Arrangement, published essence | Roles defined and available |
| Art 27 | Is an EU representative designated where required? | Representative details | Designated and published |
| Art 28 | Are processor contracts complete, incl. sub-processors? | DPAs, subprocessor list | Art 28(3) terms; authorisations |
| Art 30 | Is a record of processing activities maintained? | ROPA | Required fields present; available on request |
| Art 32 | Are risk-appropriate security measures in place? | Encryption, resilience, testing | Measures match risk; tested |
| Art 33 | Is breach notification to the authority timely? | Runbook, 72-hour clock, register | ≤72h or reasons documented; log kept |
| Art 34 | Are high-risk breaches communicated to individuals? | Templates, criteria | High-risk communication process |
| Art 35 | Are DPIAs performed for high-risk processing? | DPIAs, trigger criteria | DPIA for each high-risk activity |
| Art 36 | Is prior consultation done where residual risk is high? | Consultation records | Performed where required |
| Art 37–39 | Is a DPO designated and positioned correctly? | Designation, reporting line | Criteria met; independence |

## GDPR — transfers

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| Art 44–45 | Are transfers covered by adequacy? | Adequacy decisions, regions | Destination adequate |
| Art 46–47 | Are appropriate safeguards in place otherwise? | SCCs, BCRs, TIAs | Executed and assessed |
| Art 48–49 | Are judgments and derogations handled correctly? | Legal basis, consent | Permitted basis only |

## AI Act

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| Art 5 | Are prohibited practices absent? | Feature specs, model use | None of Art 5(1)(a)–(h) present |
| Art 6 / Annex III | Are high-risk systems classified? | Classification records | Correctly classified; profiling always high-risk |
| Art 9–15 | Do high-risk systems meet the requirements? | Risk mgmt, data governance, docs, logs, oversight, accuracy | Requirements evidenced |
| Art 16 | Are provider obligations met? | QMS, conformity, CE, registration | Complete |
| Art 26 | Are deployer obligations met? | Oversight, logs, worker information | Complete |
| Art 27 | Is a fundamental rights impact assessment done? | FRIA | Done where required |
| Art 50 | Are transparency obligations met? | AI notices, synthetic-content marking | Disclosed/marked |
| Art 51–53 | Are GPAI obligations met? | Documentation, training-data summary | Complete; systemic-risk notification |

## Data Act

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| Art 3–4 | Is user access to product/service data by default? | Product design, access features | Easily, securely, free, machine-readable |
| Art 4(12)/5(7) | Is personal data shared only on a GDPR basis? | Legal basis, consent | Valid Art 6/9 basis |
| Art 5–6 | Is third-party sharing controlled? | Purpose limits, contracts | Agreed purpose; no prohibited use |
| Art 17 | Are public-sector requests justified and minimised? | Requests, pseudonymisation | Exceptional need, minimised, notified |
| Art 30 | Is cloud switching supported? | Open interfaces, export | Compliant export/switching |
| Art 32 | Are safeguards against foreign access in place? | Contracts, customer notice | Measures and notice present |

## Audit evidence index

Record results using the format in `references/audit.md` (section 7), citing the
specific file, config path or document section for each control.
