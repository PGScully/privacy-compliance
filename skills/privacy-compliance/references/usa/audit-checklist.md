# USA / California — audit checklist (CCPA and CCPA Regulations)

Control-by-control audit procedures for a California privacy audit. Use with
`references/audit.md` (methodology, ratings, reporting), `references/usa/ccpa.md`
(obligations) and `references/usa/privacy-policy.md` (notice content).

Cite statute controls as **§ 1798.xxx** and regulations as **§ 70xx**.

## Applying this checklist at each stage

Identical to the other jurisdictions: the controls apply at every stage, but the
evidence changes (see `references/audit.md`).

- **Requirements:** confirm the entity meets a business threshold (§ 1798.140(d));
  map planned personal information against the statutory categories and identify
  sensitive PI; decide whether any processing is a "sale"/"share"; require the
  Notice at Collection, retention rule and, where relevant, ADMT and risk
  assessment processes.
- **Design:** design the opt-out/limit/delete/correct/know flows, opt-out
  preference signal handling, vendor contract terms and the ADMT opt-out/appeal.
- **Build / operation:** inspect code and config, re-perform rights requests, and
  test operating effectiveness from records and published notices.

## Scope and governance

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| § 1798.140(d) | Does the entity meet a business threshold (or voluntarily certify)? | Revenue, data volumes, revenue sources | Correctly in/out of scope; documented |
| Regs § 7100 | Are staff handling inquiries trained? | Training records | Training delivered and current |
| Regs § 7101 | Are request-handling records kept? | Request logs, workpapers | Records kept per § 7101 |
| § 1798.130(a)(5) | Is the privacy policy reviewed at least every 12 months? | Policy version/date | Updated within 12 months |

## Collection, purpose and retention

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| § 1798.100(a) | Is notice given at/before collection for every category, purpose, sale/share status, sensitive PI and retention? | Notice at Collection, forms, app flows | All elements present at each collection point |
| § 1798.100(c); Regs § 7002 | Is collection/use/retention/sharing reasonably necessary and proportionate, and within disclosed/compatible purposes? | Data inventory, purpose records, consent for other purposes | Justified per purpose; no undeclared categories |
| Regs § 7004 | Do request/consent methods avoid dark patterns? | UI, request flows | No manipulative design |
| § 1798.100(e) | Are reasonable security procedures in place? | Security controls, § 1798.81.5 mapping | Appropriate to the information |

## Disclosures and notices

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| Regs § 7011 | Does the privacy policy contain all required content? | Policy vs § 7011(e) checklist | All elements present |
| Regs § 7012 | Is the Notice at Collection complete and well placed? | Notice, placement | § 7012(e) items; readily available |
| Regs § 7013 | Is the opt-out notice/link present where selling/sharing? | Homepage links, notice | Conspicuous; interactive form |
| Regs § 7014 | Is the limit notice/link present where required? | Homepage links, notice | Conspicuous; interactive form |
| Regs § 7015 | If used, is the Alternative Opt-out Link correct? | Link title, icon, page | "Your Privacy Choices" + icon |
| Regs § 7016 | Is a financial incentive notice provided? | Notice, opt-in flow | Material terms, value, withdrawal |
| Regs § 7220 | Is a Pre-use Notice given for ADMT significant decisions? | Notice, placement | § 7220(c) content; from 1 Jan 2027 |

## Consumer requests

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| § 1798.130(a)(1) | Are there two or more request methods (toll-free minimum unless online-only)? | Methods, portal, phone | Methods present and working |
| § 1798.130(a)(2) | Are know/delete/correct requests answered within 45 days (extendable once by 45 with notice)? | Request logs, SLAs | Timelines met; extensions notified |
| Regs § 7022 | Are deletions propagated (service providers/contractors; third parties sold/shared to)? | Deletion workflow, downstream confirmations | Propagation implemented |
| Regs § 7023 | Are corrections made with commercially reasonable efforts? | Correction workflow | Corrections applied and recorded |
| Regs § 7024 | Do know/access responses cover the 12-month period and portable format? | Response templates | Correct scope and format |
| Regs § 7025 | Are opt-out preference signals honoured? | Signal handling, GPC | Processed; frictionless where elected |
| Regs § 7026 | Are sale/share opt-outs honoured within 15 business days? | Opt-out workflow | Timeline met across systems |
| Regs § 7027 | Are limit requests honoured within 15 business days? | Limit workflow | Timeline met |
| Regs § 7028 | Is re-opt-in handled with the 12-month wait? | Consent records | 12-month rule applied |
| § 1798.125 | Is non-retaliation enforced (including employees/applicants/contractors)? | Policies, pricing logic | No discriminatory treatment |

## Verification and minors

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| Regs §§ 7060–7062 | Is verification reasonable and proportionate? | Verification procedure | Documented; matches request type |
| Regs § 7063 | Are authorized agents handled correctly? | Agent procedure | Per § 7063 |
| § 1798.130(a)(7) | Is verification data used only for verification? | Data handling | Not reused or over-retained |
| § 1798.120(c); Regs §§ 7070–7072 | Is under-16 sale/share controlled with affirmative authorisation? | Age controls, opt-in flows | Opt-in before sale/share; willful disregard avoided |

## Third parties and contracts

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| § 1798.100(d); Regs § 7051 | Do service-provider/contractor contracts contain all required terms? | Contracts | Specific purposes; prohibitions; audit/stop rights |
| Regs § 7051(b) | Are subcontractors bound by equivalent terms? | Subcontracts | Flow-down present |
| Regs § 7052–7053 | Are third-party agreements complete and enforced? | Contracts, due diligence | § 7053 terms; diligence performed |

## Tall obligations (audits, risk assessments, ADMT)

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| Regs §§ 7120–7124 | Is a cybersecurity audit performed where the threshold is met? | Audit report, auditor independence, retention | Completed per schedule; independent; retained 5 years |
| Regs §§ 7150–7157 | Are risk assessments performed **before** high-risk processing? | Risk assessment reports | Triggered activities assessed; documented |
| Regs § 7157 | Can risk assessments be submitted to the CPPA on request? | Availability, format | Retrievable |
| Regs §§ 7200, 7220–7222 | Is the ADMT regime met (notice, opt-out/appeal, access)? | ADMT inventory, notices, flows | In place before 1 Jan 2027 use |

## Enforcement readiness

| Ref | Control question | Evidence | Conforms if |
|---|---|---|---|
| § 1798.150 | Is reasonable security maintained to reduce breach liability? | Security programme | § 1798.81.5 controls |
| § 1798.155 | Are fines and remediation tracked? | Risk register, governance | Escalation and remediation path |

## Audit evidence index

Record results using the format in `references/audit.md` (section 7), citing the
specific file, config path or document section for each control.
