---
name: privacy-skill
description: Review code, designs, data flows and policies for privacy and data-protection compliance across jurisdictions - the Australian Privacy Act 1988 and its 13 Australian Privacy Principles, the EU GDPR, the EU AI Act and the EU Data Act - and draft or update privacy policies and privacy notices. Use when handling personal or sensitive data, designing collection, storage, sharing, retention or deletion; creating privacy policies, notices or consent flows; assessing cross-border transfers; planning for or responding to data breaches; or reviewing AI, connected-product and cloud features. Produces findings or policy drafts that cite the relevant section, article or APP clause.
license: MIT
---

# Privacy review and policy drafting

Work against the privacy legislation bundled in `legislation/` to do one of two
things:

- **Review** software, designs, data flows and written policies, and flag issues
  with precise citations (sections 1–5).
- **Draft or update a privacy policy / privacy notice**, with every required
  element traced to its provision (section 6).

Both modes start by choosing the jurisdiction(s) below.

> This skill supports engineering, design and documentation work, not legal
> advice. Flag uncertainty and recommend qualified legal advice for novel,
> high-risk or disputed questions.

## 1. Choose the jurisdiction(s)

Determine which regimes apply before reviewing anything. If more than one applies,
review under each and report overlapping findings once, citing both.

| Regime | Applies when | Reference | Statute text |
|---|---|---|---|
| **Australia — Privacy Act 1988 (Cth)** | An APP entity (agency or organisation) with an Australian link, or a file number recipient / credit reporting body. | `references/australia/` | `legislation/Australia/Privacy Act 1988.txt` |
| **EU — GDPR (2016/679)** | Processing in the context of EU/EEA establishment, or offering goods/services to or monitoring people in the EU. | `references/eu/gdpr.md` | `legislation/Europe/GDPR/GDPR.txt` |
| **EU — AI Act (2024/1689)** | Placing on the market, putting into service or using AI systems with EU effect, including non-EU providers. | `references/eu/ai-act.md` | `legislation/Europe/AI Act/EU AI Act.txt` |
| **EU — Data Act (2023/2854)** | Connected products, related services, data sharing, cloud switching or unlawful governmental access with EU effect. | `references/eu/data-act.md` | `legislation/Europe/Data Act/EU Data Act.txt` |

Use the statute text to verify a citation when the point is contested or
high-stakes. When in doubt about which regime applies, state the assumption.

## 2. Task A — review workflow

Work through these steps in order. Do not skip step 1 — most false positives come
from applying an obligation that does not apply.

1. **Establish scope.** For each candidate regime, confirm the entity/role, the
   territorial or Australian link, and any exemption or exclusion (e.g. Australian
   small-business and employee-record exemptions; GDPR household and criminal-law
   exclusions; AI Act military/defence, personal-use and R&D exclusions; Data Act
   micro/small-enterprise and non-production exclusions).
2. **Classify the data.** Identify personal data, sensitive/special-category data,
   and any regulated identifiers. Classification drives which clauses apply.
3. **Map the data lifecycle.** For each stage — collect, notify, store, use,
   disclose/share, transfer, retain, destroy — check the corresponding obligation.
4. **Check the special regimes** where relevant: breaches, impact assessments, AI
   risk classification, and government-access safeguards.
5. **Report findings** in the format below, each with a citation and severity.

## 3. Severity

- **Critical** — likely serious interference/breach, a prohibited practice, an
  unreported notifiable breach, or sensitive/special-category processing without a
  lawful basis; exposes the entity to penalties.
- **High** — clear breach of a specific provision with real harm potential.
- **Medium** — a gap likely to breach an obligation in some circumstances, or a
  missing required control.
- **Low** — documentation, policy or transparency improvements; no direct breach.

## 4. Output format

```
### [Severity] Short title
- **Issue:** what is wrong or risky.
- **Location:** file:line, component, design section or policy paragraph.
- **Obligation:** exact provision(s), e.g. APP 11.1 (Privacy Act 1988 (Cth) Sch 1 cl 11.1); GDPR Art 6(1)(a); AI Act Art 5(1)(f); Data Act Art 4(12).
- **Why it applies:** tie the facts to the provision, including the regime, data class and any exemption/exclusion considered.
- **Recommendation:** a concrete, testable change.
```

End with a **Summary** (counts by severity, per regime) and a **Scope &
assumptions** note (what was reviewed, assumed scope, and any legal questions for
counsel).

## 5. Quick mapping: common patterns

| Pattern | Check |
|---|---|
| New field, form or telemetry event | AU APP 3 + APP 5; GDPR Art 5(1)(c), 6, 13 |
| Consent / cookie banner / preference centre | AU APP 3.3, APP 5; GDPR Art 7, 9 |
| Analytics, ad tech, trackers, lead gen | AU APP 6, APP 7; GDPR Art 5(1)(b), 21, 22 |
| Cloud, offshore hosting, offshore support | AU APP 8, s 16C; GDPR Art 44–49; Data Act Art 32 |
| Logs, backups, warehouse, ML training data | AU APP 11, APP 10; GDPR Art 5(1)(e), 25, 32; AI Act Art 10, 12 |
| Deletion / access / correction / portability | AU APP 11.2, 12, 13; GDPR Art 15–20; Data Act Art 4, 30 |
| Identity verification, IDs, biometrics | AU APP 3, APP 9; GDPR Art 9; AI Act Art 5, Annex III |
| AI features (chat, scoring, detection) | AI Act Art 5 prohibitions, Art 6/Annex III, Art 14, 26, 50; GDPR Art 22, 35 |
| Workplace monitoring / HR platforms | AU s 7B(3) employee records; AI Act Art 5(1)(f), Art 26(7) |
| Incident response / breach runbooks | AU Part IIIC (s 26WE, 26WH, 26WK, 26WL); GDPR Art 33–34 |
| Connected products / IoT / cloud | Data Act Art 3–6, 30–32; GDPR Art 6, 20 |
| Public-body data requests | Data Act Art 14–18; GDPR Art 6(1)(e) |
| Writing or updating a privacy policy | `references/australia/privacy-policy.md`, `references/eu/privacy-notice.md`, `assets/privacy-policy-template.md` |

## 6. Task B — draft or update a privacy policy

Use this when asked to create or update a privacy policy or privacy notice. The
output is a drafted document plus a coverage check.

### 6.1 Gather the inputs

Ask for, or infer from the repository and mark as assumed, the following. Do not
invent facts — record unknowns as open questions.

- Entity: legal name, contact details, DPO (if any), EU representative or joint
  controllers (if any); entity type and jurisdictions in scope.
- Data: categories of personal information, and separately sensitive/
  special-category data.
- Collection: sources (direct, third parties, automatic) and means.
- Purposes and the **legal basis** for each (EU Art 6; and whether reliance is on
  consent or legitimate interests).
- Recipients and categories of recipients.
- Overseas disclosures/transfers: countries and safeguards.
- Retention periods or the criteria used to determine them.
- Marketing, profiling and automated decisions.
- Access, correction, complaint and opt-out mechanisms.

### 6.2 Draft

Start from `assets/privacy-policy-template.md` and fill it in. Keep it concise,
plain-language and up to date (AU APP 1.3; EU Art 12). Delete inapplicable
sections and remove the annotations before returning the final text.

Consult the jurisdiction requirement checklists while drafting:

- Australia — `references/australia/privacy-policy.md` (required contents in
  **APP 1.4**, collection-notice matters in **APP 5.2**, cross-border in **APP 8**).
- EU — `references/eu/privacy-notice.md` (transparency in **Art 12**, content for
  data collected from the subject in **Art 13**, from other sources in **Art 14**,
  plus Art 8, 21, 22, 26, 27, 37 and AI Act Art 50).

Where both apply, produce a combined or layered notice that satisfies both, with
clearly separated jurisdiction sections where the wording differs.

### 6.3 Validate and report

Return, after the draft:

1. **Coverage check** — a table mapping each required element (APP 1.4(a)–(g);
   GDPR Art 13(1)–(2) / Art 14) to the section of the draft that satisfies it.
2. **Gaps and open questions** — every placeholder or assumed fact that must be
   confirmed before publishing.
3. **Publication checklist** — dated and versioned, available free of charge and in
   an appropriate form (AU APP 1.5–1.6), reachable from every collection point, and
   consistent with what the system actually does.

## 7. Bundled references

**Australia** — see `references/australia/README.md` for orientation.
- `scope.md` — coverage, definitions, exemptions and permitted situations.
- `apps.md` — APP 1 to APP 13 clause-by-clause checklist.
- `privacy-policy.md` — APP privacy policy requirements and drafting checklist.
- `breach-notification.md` — Part IIIC eligible data breaches.
- `statutory-tort.md` — Schedule 2 serious invasions of privacy.

**European Union**
- `references/eu/gdpr.md` — principles, lawful bases, rights, obligations, transfers, fines.
- `references/eu/privacy-notice.md` — GDPR Art 12–14 notice content and checklist.
- `references/eu/ai-act.md` — prohibitions, high-risk classification, requirements, transparency, GPAI.
- `references/eu/data-act.md` — data access/sharing, cloud switching, government access.

**Assets**
- `assets/privacy-policy-template.md` — fill-in template mapped to APP 1.4 and
  GDPR Art 13/14.

## 8. Caveats

- The bundled statutes are official texts: Australian Privacy Act 1988 compilation
  No. 104 (4 June 2026); GDPR; AI Act; Data Act. Verify currency against the
  official register before relying on a citation in a high-stakes context.
- Each regime sits alongside others (e.g. Australian credit reporting and APP codes;
  the ePrivacy Directive, DMA, DSA, NIS2; national Member State law). Note overlaps;
  this skill is not exhaustive.
- This skill is portable across agents that support the Agent Skills `SKILL.md`
  format (Claude, Codex, and others).
