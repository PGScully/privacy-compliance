# Privacy compliance audit

Use this when asked to **audit** for compliance with privacy legislation, as opposed
to a one-off review. An audit is a structured, evidence-based assessment against
defined criteria that produces a report with traceable findings and an overall
opinion.

Audits apply at **every lifecycle stage** — at requirements gathering before any code
exists, through design and build, at release, in operation, and for later changes.
The stage determines the artefacts available and the nature of the findings.

## Audit vs review

| | Review (Task A) | Audit (Task C) |
|---|---|---|
| Trigger | A change, design or question | A request for assurance over a defined scope |
| Input | The artefact in front of you | A scope (systems + documentation) and criteria |
| Output | Findings list | Report, control matrix, evidence index, opinion |
| Coverage | Whatever is relevant | Every in-scope control, each rated |
| Evidence | Cited inline | Indexed and retained |

A review can be one step of an audit; the audit adds planning, complete control
coverage, ratings, and reporting.

## 1. Plan the audit

Record, in writing, before testing:

- **Stage(s) in scope** — requirements, design, build, pre-release, operation, or
  change. State which are included and excluded; a change audit is scoped to the
  delta introduced by the change. Findings are framed accordingly: pre-code stages
  yield **requirements/design gaps** (add a requirement or control), later stages
  yield implementation or operating defects.
- **Objective and scope** — which requirements/design sets, repositories, services,
  environments, systems and documentation; the period covered; and explicit
  **exclusions**.
- **Criteria** — the exact legislation and version being audited against (for
  example Privacy Act 1988 (Cth) as at compilation No. 104; GDPR; AI Act; Data Act;
  CCPA and its regulations), plus any codes (registered APP codes, CR code) or
  contractual commitments.
- **Approach** — compliance audit against the criteria, evidence-based. State the
  limits: pre-implementation audits assess **by design** and cannot evidence
  operating effectiveness; later audits may test operation.
- **Materiality and risk** — prioritise high-risk processing (sensitive data,
  large scale, automated decisions, cross-border, children).
- **Roles** — who owns the requirements/design/codebase/docs, who provides missing
  information, and where legal sign-off is required.

### Stage selection guide

| Stage | Primary artefacts | Audit focus |
|---|---|---|
| Requirements / discovery | requirements, user stories, acceptance criteria, process and data-flow descriptions, business case, RFP | Is the planned processing lawful, necessary and proportionate? What privacy requirements must be added? |
| Design / architecture | architecture and data models, API contracts, IaC plans, vendor selection, threat model, DPIA draft | Are the required controls designed in? |
| Development / build | code, config, migrations, tests, CI | Are the controls actually implemented? |
| Pre-release / readiness | release checklist, notices, runbooks, training | Can obligations be met from day one? |
| Post-deployment / operation | logs, access reviews, DSR records, breach register, retention jobs, monitoring | Do controls operate effectively over time? |
| Change / update | change requests, PRs, release notes, migrations, new data/vendors | Does the change preserve or improve compliance, or add new processing? |

## 2. Collect evidence

Enumerate the evidence that exists **at the stage in scope** before concluding.
Pre-code evidence is often documentary; later stages add system and operational
artefacts. Typical sources:

| Domain | Evidence to inspect |
|---|---|
| Requirements/design | Requirements, user stories and acceptance criteria, process/data-flow diagrams, architecture and data models (planned), vendor selection, DPIA drafts, privacy requirements register |
| Data inventory | Schemas, migrations, ORM models, data dictionaries, ROPA |
| Collection | Forms, API payloads, SDKs, trackers, imports/enrichment |
| Consent | Preference centre, consent records, cookie/consent config, withdrawal path |
| Transparency | Privacy policy/notice, collection notices, version/date |
| Access control | IAM roles/policies, authz code, admin access, least privilege |
| Security | TLS config, encryption at rest, KMS/key rotation, secrets management |
| Retention/deletion | TTLs, cron/lifecycle jobs, backup retention, de-identification |
| Cross-border | Cloud regions, subprocessor lists, DPA/SCC/BCR documents, consent text |
| Rights | Access/export/correction/delete endpoints or runbooks, SLAs |
| Logging/monitoring | Log configuration, PII in logs, alerting, audit trails |
| Incidents | Breach runbook, breach register, notification templates, 30-day/72-hour clocks |
| Vendors | Contracts, processor terms, subprocessor authorisations |
| Governance | Policies, procedures, training records, complaint handling, DPIAs |

For each item, record **where** it is (file:line, config path, document section) so
the finding is reproducible.

## 3. Test each control

For every in-scope control in the jurisdiction checklist, apply the procedure that
fits the stage:

- **At requirements:** challenge the planned processing — is each data element
  necessary, is the purpose stated, is there a lawful basis, what notice/consent is
  required, what happens on access/correction/deletion, where will data go
  (including offshore), how long is it kept? Record the requirement to be added.
- **At design:** inspect the design artefacts to confirm the required controls are
  designed in (minimisation, security, retention, DPbD, oversight).
- **At build and later:** **inspect** the artefact (schema, config, policy clause);
  **walk through** the end-to-end flow; **re-perform** in a test environment when
  safe (for example, trigger an export or deletion and observe the result); and
  **test a sample** where volume makes full inspection impractical, and say so.

Record a result for every control — including *Not tested* with the reason. Do not
leave controls unaddressed.

## 4. Rate conformity and severity

**Conformity rating per control:**

| Rating | Meaning |
|---|---|
| Conforms | Requirement met, with evidence |
| Partially conforms | Met in some respects or some scope, with gaps |
| Does not conform | Requirement not met |
| Not applicable | Control does not apply (state the basis) |
| Not tested | Not assessed (state why) |

**Finding severity** uses the same scale as reviews:

- **Critical** — likely serious interference/breach, prohibited practice, an
  unreported notifiable breach, or sensitive/special-category processing without a
  lawful basis.
- **High** — clear breach of a specific provision with real harm potential.
- **Medium** — likely breach in some circumstances, or a missing required control.
- **Low** — documentation/transparency improvement.

**Overall opinion:** *Reasonable assurance*, *Qualified* (exceptions noted),
*Adverse* (widespread non-conformity), or *Insufficient evidence*.

## 5. Finding format

```
### [Severity] Short title
- **Stage:** requirements / design / build / pre-release / operation / change.
- **Criteria:** the provision breached, e.g. APP 11.1; GDPR Art 32; AI Act Art 26(7).
- **Condition:** what actually exists (or is planned, at pre-code stages).
- **Evidence:** file:line / config path / document section / requirement ID.
- **Cause:** why it exists (design, omission, drift, unclear ownership).
- **Effect:** the risk to individuals and to the entity (penalties, harm).
- **Recommendation:** a concrete, testable remediation or the requirement to add,
  ideally with priority.
- **Management response:** [to be completed by the auditee]
```

## 6. Report structure

1. **Cover** — objective, **stage(s) in scope**, scope, exclusions, criteria, period,
   date, auditor.
2. **Executive summary** — overall opinion and the most significant findings.
3. **Summary of findings** — counts by severity and by domain; control matrix.
4. **Detailed findings** — one entry per finding in the format above.
5. **Control results** — every control with its rating and evidence reference.
6. **Limitations** — what was not tested, the stage limits (design-only assurance at
   pre-code stages; no operating-effectiveness testing), reliance on provided
   artefacts, AI-assisted analysis, and the need for legal/human review.
7. **Appendices** — evidence index, documents reviewed, open information requests.

Use `assets/audit-report-template.md` as the starting point.

## 7. Evidence index (workpapers)

Retain a table mapping each control and finding to its evidence, so a third party
can re-perform the audit:

| ID | Control | Evidence | Location | Result |
|---|---|---|---|---|
| [E1] | [APP 11.1] | [encryption config] | [path/to/config] | Conforms |

## 8. Limitations

- This is an AI-assisted compliance audit, not a statutory financial or legal audit,
  and not a penetration test.
- Pre-implementation audits give assurance over requirements and design only, not
  over operating effectiveness.
- It cannot confirm operating effectiveness without observation over time and
  system access beyond the artefacts provided.
- Recommendations are risk-based; the auditee and legal counsel decide on
  applicability and remediation.
