# Australian Privacy Principles (Schedule 1)

Clause-by-clause checklist. For each principle: the obligation, the engineering
signals to inspect, and the common failures. All cites are to Schedule 1 unless
another section is named.

---

## APP 1 — Open and transparent management of personal information

**Obligation.** Take reasonable steps to implement practices, procedures and
systems that ensure compliance and enable handling of inquiries and complaints
(cl 1.2). Have a clearly expressed, up-to-date **APP privacy policy** (cl 1.3)
containing the matters in cl 1.4, make it available free of charge in an
appropriate form (cl 1.5), and give a copy in a requested form (cl 1.6).

**cl 1.4 required contents:** kinds of personal information collected and held;
how it is collected and held; purposes of collection, holding, use and disclosure;
how to access and seek correction; how to complain and how complaints are handled;
whether personal information is likely to be disclosed overseas; and, if so, the
countries where practicable.

**Engineering signals.**
- Is there a reachable privacy policy linked from every data-collection point?
- Does the policy match what the code actually does (fields, vendors, offshore
  regions, retention)?
- Is there a documented complaints/inquiries path and an owner?

**Common failures.** Policy missing, stale, or contradicted by the data flow;
overseas disclosure omitted; no process to keep the policy current.

---

## APP 2 — Anonymity and pseudonymity

**Obligation.** Individuals must have the option of not identifying themselves,
or of using a pseudonym, when dealing with the entity (cl 2.1), unless the entity
is required/authorised by Australian law or a court/tribunal order to deal only
with identified individuals, or it is impracticable to deal with unidentified
individuals (cl 2.2).

**Engineering signals.** Is identity actually required for this transaction
(quoting, browsing, low-risk feedback)? Is there a design reason identification is
"impracticable"?

**Common failures.** Mandatory account creation where anonymous use is
practicable; no pseudonymous option; conflating account identity with a legal
identity requirement that does not exist.

---

## APP 3 — Collection of solicited personal information

**Obligation.**
- **Non-sensitive** (cl 3.1–3.2): an agency must not collect unless reasonably
  necessary for, or directly related to, its functions; an organisation must not
  collect unless reasonably necessary.
- **Sensitive** (cl 3.3): must not collect unless the individual consents **and**
  the necessity test is met, or a cl 3.4 exception applies (required/authorised by
  law; permitted general situation; permitted health situation; enforcement body;
  non-profit membership).
- **Means** (cl 3.5): collect only by lawful and fair means.
- **Source** (cl 3.6): collect from the individual unless they consent, it is
  required/authorised by law, or it is unreasonable or impracticable to collect
  from them.
- Applies to **solicited** collection (cl 3.7).

**Engineering signals.** Every form field, SDK event, import and enrichment step.
Ask "is this field necessary for a stated purpose?" Sensitive-data flags
(health, ethnicity, biometrics, criminal record). Third-party data brokers.

**Common failures.** Over-collection ("just in case"); collecting sensitive data
without valid consent; covert collection via trackers; buying or enriching data
without checking the source and notice.

---

## APP 4 — Dealing with unsolicited personal information

**Obligation.** If the entity receives personal information it did not solicit, it
must within a reasonable period determine whether it could have collected it under
APP 3 (cl 4.1). It may use or disclose it to make that determination (cl 4.2). If
it could not have collected it and it is not in a Commonwealth record, it must
destroy or de-identify it as soon as practicable, if lawful and reasonable
(cl 4.3). Otherwise APPs 5–13 apply as if it had been collected under APP 3
(cl 4.4).

**Engineering signals.** Free-text fields, email ingestion, résumés, support
attachments, webhooks. Is there a process to assess and purge unsolicited data?

**Common failures.** Unsolicited sensitive data (e.g. health details in a support
ticket) retained indefinitely with no assessment.

---

## APP 5 — Notification of the collection of personal information

**Obligation.** At or before collection, or as soon as practicable after, take
reasonable steps to notify the individual, or make them aware, of the cl 5.2
matters.

**cl 5.2 matters:** identity and contact details; that collection was from a third
party or the individual may not be aware (and the circumstances); any legal
requirement/authorisation; the purposes; the main consequences of not providing
it; usual disclosure recipients; that the policy covers access and correction;
that the policy covers complaints; whether overseas disclosure is likely; and the
likely countries where practicable.

**Engineering signals.** Just-in-time notices at each collection point, not only a
buried policy. Consent/notice screens for sign-up, payment, telemetry.

**Common failures.** No notice for data collected via third parties or trackers;
missing legal-authority statement; no mention of offshore disclosure.

---

## APP 6 — Use or disclosure of personal information

**Obligation.** Personal information collected for a **primary purpose** must not
be used or disclosed for a **secondary purpose** unless the individual consents
(cl 6.1(a)) or cl 6.2/6.3 applies.
- **cl 6.2:** reasonable expectation + (sensitive: directly related; else:
  related) to the primary purpose; or required/authorised by law; or a permitted
  general situation; or a permitted health situation (organisations); or
  reasonably necessary for enforcement-related activities.
- **cl 6.4:** where health info was collected under s 16B(2), de-identify before
  disclosure.
- **cl 6.5:** a written note is required for enforcement-body uses/disclosures
  under cl 6.2(e).
- **cl 6.6:** for related bodies corporate, the receiving entity inherits the
  primary purpose.
- **cl 6.7:** APP 6 does not apply to direct marketing (APP 7) or government
  related identifiers (APP 9).

**Engineering signals.** Data warehouses, analytics, model training, sharing with
partners, internal secondary uses. Purpose tags on data assets and lineage.

**Common failures.** Purpose creep — reusing sign-up data for analytics, ML or
marketing without consent or expectation; sharing with "partners" not disclosed.

---

## APP 7 — Direct marketing

**Obligation.** An organisation must not use or disclose personal information for
direct marketing (cl 7.1) unless an exception applies:
- **cl 7.2** (non-sensitive, collected from the individual): the individual would
  reasonably expect it, a simple opt-out is provided, and they have not opted out.
- **cl 7.3** (non-sensitive, not expected or collected from a third party): consent
  or impracticable to obtain consent, plus a simple opt-out, a prominent statement
  in each communication, and no prior opt-out.
- **cl 7.4** (sensitive): the individual consented.
- **cl 7.5**: contracted service provider for a Commonwealth contract.
- **cl 7.6–7.7**: individuals may request not to receive marketing, request no
  third-party use, and request the source; no charge and prompt compliance.
- **cl 7.8**: APP 7 does not apply to the extent the Spam Act 2003, Do Not Call
  Register Act 2006, Interactive Gambling Act 2001 Div 5 Part 7B or prescribed
  laws apply.

**Engineering signals.** Opt-out links, suppression lists, consent records,
lead-generation sources, ad-tech integrations.

**Common failures.** No opt-out; opt-out buried or ineffective; marketing to
purchased lists; sensitive data used for marketing without consent; ignoring
"source of the data" requests.

---

## APP 8 — Cross-border disclosure of personal information

**Obligation.** Before disclosing personal information to an overseas recipient,
take reasonable steps to ensure the recipient does not breach the APPs (other
than APP 1) (cl 8.1). This does not apply if cl 8.2 applies: the recipient is
subject to a law or binding scheme that is, overall, substantially similar and
the individual can enforce it (cl 8.2(a)); the recipient is covered by a
prescribed country or binding scheme (cl 8.3); the entity expressly informs the
individual and they consent (cl 8.2(b)); the disclosure is required/authorised by
law (cl 8.2(c)); a permitted general situation other than items 4 or 5 applies
(cl 8.2(d)); an agency discloses under an international agreement (cl 8.2(e)); or
an enforcement-related disclosure (cl 8.2(f)).

**Accountability.** Under s 16C, if the overseas recipient breaches the APPs, that
act is taken to be the disclosing entity's breach.

**Engineering signals.** Cloud regions, subprocessors, offshore support, CDNs,
analytics vendors, backups and disaster recovery. Check the AAPPs/subprocessors
list against the privacy policy and consent.

**Common failures.** Undisclosed offshore processing; assuming a vendor's
certification is a s 8.2 defence; no contractual controls; consent screens that
do not actually inform the individual that cl 8.1 will not apply.

---

## APP 9 — Adoption, use or disclosure of government related identifiers

**Obligation.** An organisation must not adopt a government related identifier as
its own identifier (cl 9.1) or use/disclose it (cl 9.2) unless a specified
exception applies: required/authorised by law; reasonably necessary to verify
identity for the entity's functions; reasonably necessary to fulfil obligations to
an agency or State/Territory authority; a permitted general situation (other than
items 4 or 5); reasonably necessary for enforcement-related activities; or the
cl 9.3 regulations apply.

**Engineering signals.** Using driver's licence, Medicare, passport or TFN numbers
as primary keys, in logs, or across systems; storing identifiers beyond
verification.

**Common failures.** Copying a government identifier into a customer database or
using it as a join key; retaining ID scans after verification.

---

## APP 10 — Quality of personal information

**Obligation.** Take reasonable steps to ensure personal information collected is
accurate, up-to-date and complete (cl 10.1); and that information used or
disclosed is, having regard to the purpose, accurate, up-to-date, complete and
relevant (cl 10.2).

**Engineering signals.** Validation, deduplication, staleness of records, data
quality pipelines feeding decisions or disclosures.

**Common failures.** Relying on stale data for consequential decisions; no way for
individuals to keep data current (interacts with APP 13).

---

## APP 11 — Security of personal information

**Obligation.** Take reasonable steps to protect personal information from misuse,
interference and loss, and from unauthorised access, modification or disclosure
(cl 11.1). Where the entity no longer needs the information, and it is not a
Commonwealth record and retention is not required by law, take reasonable steps to
destroy or de-identify it (cl 11.2). Those steps include technical and
organisational measures (cl 11.3).

**Engineering signals.** Encryption at rest and in transit, access control and
least privilege, secrets management, logging and monitoring, backups, secure
disposal, retention schedules, third-party access.

**Common failures.** No encryption for sensitive data; over-broad access; secrets
in code; indefinite retention with no deletion job; de-identification that is
reversible; no retention policy tied to a purpose.

---

## APP 12 — Access to personal information

**Obligation.** On request, give the individual access to personal information
the entity holds (cl 12.1). **Exceptions:** agencies under the FOI Act or similar
laws (cl 12.2); organisations on the grounds in cl 12.3 (serious threat to life,
health or safety or public health/safety; unreasonable impact on others' privacy;
frivolous/vexatious; legal proceedings; prejudicial negotiations; unlawful;
required/authorised by law to deny; suspected unlawful activity or serious
misconduct; enforcement-related prejudice; commercially sensitive
decision-making).

**Timing and manner.** Respond within 30 days (agency) or a reasonable period
(organisation), in the requested manner where reasonable and practicable
(cl 12.4). Give access another way if refused (cl 12.5–12.6). Agencies must not
charge for the request or access (cl 12.7); organisations must not charge for the
request and any charge must not be excessive (cl 12.8). Refusals require a written
notice with reasons, complaint mechanisms and prescribed matters (cl 12.9).

**Engineering signals.** Self-service export, support workflows, SLAs, identity
verification for access requests.

**Common failures.** No export path; fees charged for merely making a request;
silent refusal without written reasons.

---

## APP 13 — Correction of personal information

**Obligation.** Correct personal information the entity is satisfied is
inaccurate, out-of-date, incomplete, irrelevant or misleading, having regard to
the purpose for which it is held, or when the individual requests correction
(cl 13.1). Notify other APP entities to whom the information was previously
disclosed if the individual requests it and it is not impracticable or unlawful
(cl 13.2). Refusals require a written notice with reasons, complaint mechanisms
and prescribed matters (cl 13.3). If correction is refused and the individual
requests it, associate a statement that the information is inaccurate etc. in a
way that is apparent to users (cl 13.4). Respond within 30 days (agency) or a
reasonable period (organisation) and do not charge (cl 13.5).

**Engineering signals.** Editable profiles, correction request workflows,
propagation of corrections to downstream systems and third parties.

**Common failures.** No correction path; corrections not propagated; no support
for associated statements.

---

## Cross-cutting notes

- **Consent** must be current, informed and specific; check how it is recorded
  and withdrawn, and whether withdrawal actually stops processing.
- **Reasonable steps** is the standard throughout — what is reasonable scales
  with sensitivity, volume, harm and available controls.
- **Enforcement**: a breach of an APP is an interference with privacy (s 13), and
  a **serious** interference is a civil penalty provision (s 13G). See Part V
  (investigations) and Part VIB (compliance and enforcement).
- **Credit reporting** has its own rules in Part IIIA and the registered CR code;
  **APP codes** (Part IIIB) may bind an entity in addition to the APPs.
