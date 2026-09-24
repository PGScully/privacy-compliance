---
name: privacy-skill
description: Review code, designs, data flows and policies for privacy and data-protection compliance across jurisdictions - the Australian Privacy Act 1988 and its 13 Australian Privacy Principles, the EU GDPR, the EU AI Act and the EU Data Act. Use when handling personal or sensitive data, designing collection, storage, sharing, retention or deletion; building privacy notices, consent, access or correction flows; assessing cross-border transfers; planning for or responding to data breaches; or reviewing AI, connected-product and cloud features. Produces findings that each cite the relevant section, article or APP clause.
license: MIT
---

# Privacy review

Review software, designs, data flows and written policies against the privacy
legislation bundled in `legislation/`, and flag issues with precise citations to
the provision relied on.

> This skill supports engineering and design review, not legal advice. Flag
> uncertainty and recommend qualified legal advice for novel, high-risk or
> disputed questions.

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

## 2. Workflow

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

## 6. Bundled references

**Australia** — see `references/australia/README.md` for orientation.
- `scope.md` — coverage, definitions, exemptions and permitted situations.
- `apps.md` — APP 1 to APP 13 clause-by-clause checklist.
- `breach-notification.md` — Part IIIC eligible data breaches.
- `statutory-tort.md` — Schedule 2 serious invasions of privacy.

**European Union**
- `references/eu/gdpr.md` — principles, lawful bases, rights, obligations, transfers, fines.
- `references/eu/ai-act.md` — prohibitions, high-risk classification, requirements, transparency, GPAI.
- `references/eu/data-act.md` — data access/sharing, cloud switching, government access.

## 7. Caveats

- The bundled statutes are official texts: Australian Privacy Act 1988 compilation
  No. 104 (4 June 2026); GDPR; AI Act; Data Act. Verify currency against the
  official register before relying on a citation in a high-stakes context.
- Each regime sits alongside others (e.g. Australian credit reporting and APP codes;
  the ePrivacy Directive, DMA, DSA, NIS2; national Member State law). Note overlaps;
  this skill is not exhaustive.
- This skill is portable across agents that support the Agent Skills `SKILL.md`
  format (Claude, Codex, and others).
