# Australia — audit checklist (Privacy Act 1988 (Cth))

Control-by-control audit procedures for an Australian privacy audit. For each
control: what to test, the evidence to inspect, and the condition for a "conforms"
rating. Use with `references/audit.md` (methodology, ratings, reporting) and
`references/australia/apps.md` (obligation detail).

## Applying this checklist at each stage

These controls apply at every stage; only the evidence and procedure change (see
`references/audit.md`). For example:

- **Requirements:** assess APP 3 by challenging each planned data element and its
  purpose; require an APP 1.4 policy and an APP 5 collection notice; ask APP 8 where
  data will be hosted; require an APP 11.2 retention and deletion rule.
- **Design:** assess APP 11 by confirming the security design (encryption, access
  control); design the APP 4 unsolicited-data disposition; design the APP 12/13
  rights workflow and the Part IIIC breach process.
- **Build / operation:** inspect config and code, re-perform rights requests in a
  test environment, and test operating effectiveness from records (access reviews,
  DSR logs, breach register, retention jobs).

## Governance and transparency

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| APP 1.2 | Are there practices, procedures and systems to ensure APP compliance and handle inquiries/complaints? | Privacy program docs, owners, procedures, ticket queues, complaints log | Documented, assigned, operating |
| APP 1.3 | Is there a clearly expressed, up-to-date APP privacy policy? | `references/australia/privacy-policy.md` checklist; policy version/date | Present, current, covers actual processing |
| APP 1.4 | Does the policy contain all of 1.4(a)–(g)? | Policy text vs APP 1.4 checklist | All seven elements present |
| APP 1.5–1.6 | Is the policy available free of charge and in a requested form? | Website/links, request handling | Reachable and provided on request |
| APP 5.2 | Are the collection-notice matters given at or before collection? | Collection screens, notices, API docs | All applicable matters notified |

## Collection and dealing with data

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| APP 3.1–3.2 | Is each collected field reasonably necessary (and, for agencies, directly related)? | Schemas, forms, event payloads, data dictionary | Every field justified; no over-collection |
| APP 3.3 | Is sensitive information collected only with consent or a 3.4 exception? | Sensitive-data fields, consent records, exceptions used | Consent or documented exception per item |
| APP 3.5 | Is collection by lawful and fair means? | Collection code, trackers, enrichment | No covert/unfair collection |
| APP 3.6 | Is data collected from the individual unless an exception applies? | Data sources, third-party imports | Source and basis documented |
| APP 4 | Is unsolicited information assessed and destroyed/de-identified if not collectible? | Ingest pipelines, triage process | Assessment + disposal path exists |
| APP 9 | Are government related identifiers adopted/used/disclosed only as permitted? | ID fields, keys, logs, verification flows | No adoption as own identifier; permitted use |
| APP 10 | Is data accurate, up-to-date, complete and (when used) relevant? | Validation, dedup, staleness, downstream use | Controls exist; corrections propagate |

## Use, disclosure and transfers

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| APP 6 | Is use/disclosure limited to the primary purpose or an exception/consent? | Data lineage, purpose tags, sharing code, API scopes | Secondary uses justified and recorded |
| APP 6.5 | Is a written note made for enforcement-related uses under 6.2(e)? | Notes/logs | Present where applicable |
| APP 7 | Is direct marketing compliant, with a simple opt-out? | Marketing config, suppression list, consent records | Opt-out works; source request honoured |
| APP 8 | Are cross-border disclosures supported by reasonable steps or an exception? | Regions, subprocessor list, SCC/contracts, consent text | s 8.2 basis or steps documented; s 16C accountability |
| APP 11.1 | Is personal information protected with reasonable technical and organisational measures? | TLS/at-rest encryption, IAM, secrets, monitoring, pen tests | Risk-appropriate controls in place |
| APP 11.2 | Is data destroyed or de-identified when no longer needed? | Retention schedule, TTLs, deletion jobs, backups | Deletion enforced; legal holds documented |

## Individual rights and incidents

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| APP 12 | Can individuals access their personal information, with correct timing/charges? | Access/export endpoints, runbooks, SLAs, refusal notices | Works; 30 days (agency)/reasonable (org); no request charge |
| APP 13 | Can individuals correct information, with third-party notification? | Edit flows, correction workflow, refusal notices, associated statements | Works; propagation supported |
| Part IIIC (s 26WH) | Is a suspected breach assessed within 30 days? | Breach runbook, triage process, clock | Process and owner defined |
| Part IIIC (s 26WK/26WL) | Can a statement be prepared and given to the Commissioner, and individuals notified? | Statement template, notification tooling, breach register | Templates and channels exist |
| s 13G | Is serious interference with privacy treated as a penalty risk? | Risk register, governance reporting | Escalation path exists |
| Schedule 2 | Are serious invasions of privacy (seclusion/intrusion, misuse) considered? | Feature reviews, surveillance/recording features, naming/exposure features | Risks identified and controlled |

## Conditional controls

| Ref | Applies if | Control question |
|---|---|---|
| Part IIIA / CR code | Credit reporting body or credit provider | Credit information handled per Part IIIA and the registered CR code |
| Registered APP code | Entity is bound by a code | Additional code obligations are met |
| s 7B(3) employee records | Relying on the exemption | Data truly is an employee record tied to the employment relationship |
| s 7B(2), s 7C | Relying on contractor/political exemptions | Exemption conditions actually met |

## Audit evidence index

Record results using the format in `references/audit.md` (section 7), citing the
specific file, config path or document section for each control.
