# privacy-compliance

A portable [Agent Skills](https://agentskills.io/specification) package that helps
coding assistants **review** software, designs, data flows and policies for privacy
and data-protection compliance, **audit** code and documentation against a defined
scope, and **draft or update privacy policies and privacy notices** — tracing every
finding or required element to the legislation and provision it comes from.

## Coverage

| Jurisdiction | Instrument |
|---|---|
| Australia | Privacy Act 1988 (Cth) and the 13 Australian Privacy Principles (APPs) |
| European Union | GDPR — Regulation (EU) 2016/679 |
| European Union | AI Act — Regulation (EU) 2024/1689 |
| European Union | Data Act — Regulation (EU) 2023/2854 |
| USA / California | CCPA (Civil Code §§ 1798.100–1798.199.100) and the CCPA Regulations (11 CCR §§ 7000–7304), both effective 1 January 2026 |

## Package contents

```
SKILL.md                         Entry point: jurisdiction routing, workflows, output format
LICENSE
assets/
  privacy-policy-template.md     Fill-in policy template mapped to APP 1.4 / GDPR Art 13-14
  audit-report-template.md       Fill-in audit report (scope, findings, control matrix, opinion)
references/
  audit.md                       Audit methodology: planning, evidence, ratings, reporting
  australia/
    README.md                    Orientation and citation summary
    scope.md                     Coverage, definitions, exemptions, permitted situations
    apps.md                      APP 1-13 clause-by-clause checklist
    privacy-policy.md            APP privacy policy requirements and drafting checklist
    audit-checklist.md           APP audit procedures and evidence map
    breach-notification.md       Part IIIC notifiable data breaches
    statutory-tort.md            Schedule 2 serious invasions of privacy
  eu/
    gdpr.md                      Principles, lawful bases, rights, obligations, transfers, fines
    privacy-notice.md            GDPR Art 12-14 notice content and checklist
    audit-checklist.md           GDPR/AI Act/Data Act audit procedures
    ai-act.md                    Prohibitions, high-risk classification, requirements, GPAI
    data-act.md                  Data access/sharing, cloud switching, government access
  usa/
    README.md                    CCPA orientation, scope and key definitions
    ccpa.md                      CCPA obligations (rights, notices, contracts, ADMT, audits)
    privacy-policy.md            Required CCPA disclosures and policy content
    audit-checklist.md           CCPA audit procedures
```

The package ships summaries and citations, not the full statutes, to keep the
installed size small (~200 KB). Use the official texts below to quote or verify a
provision.

## Install

Install with the [Agent Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add PGScully/privacy-compliance
```

Add `-g` to install for your user rather than the current project, or `-a '*'` to
target every detected agent.

### Manual installation

Alternatively, copy this directory (or the repository's `skills/` directory) into a
location your agent scans for skills:

- Agent Skills standard: `.agents/skills/` (project) or `~/.agents/skills/` (user).
- pi: add the directory to the `skills` setting, or use `--skill <path>`.
- Other agents: point their skills location at this directory.

Once discovered, the skill is selectable automatically and/or invokable as
`/skill:privacy-compliance`.

## Use

### Review

Ask the agent to review a change, design, data flow or policy for privacy issues.
The skill will:

1. establish which jurisdiction(s) apply;
2. classify the data (personal, sensitive/special-category, identifiers);
3. map the data lifecycle to the relevant obligations;
4. check breach, impact-assessment and AI/GPAI duties where relevant; and
5. report findings, each naming the legislation and citing the exact provision
   (for example `Privacy Act 1988 (Cth) Sch 1 cl 11.1 (APP 11.1)`,
   `Privacy Act 1988 (Cth) s 26WE`, `GDPR Art 6(1)(a)`, `AI Act Art 5(1)(f)`,
   `Data Act Art 4(12)`, `CCPA § 1798.120`, `CCPA Regs § 7013(c)(1)`).

### Draft a privacy policy

Ask the agent to create or update a privacy policy or privacy notice. The skill
will gather the required inputs, draft from `assets/privacy-policy-template.md`,
and return the document plus a coverage check and a list of open questions. It
targets the Australian **APP 1.4** contents and the **GDPR Art 13/14** information
requirements (and merges them where both apply).

### Audit at any lifecycle stage

Ask the agent to audit for privacy compliance — at requirements gathering before any
code exists, during design and build, at release, in operation, or for a change. The
skill plans the audit (stage(s), scope, criteria, exclusions), collects the evidence
available at that stage, tests every control in the jurisdiction checklist and rates
it (Conforms / Partially conforms / Does not conform / Not applicable / Not tested),
then produces a report with a control matrix, evidence index and an overall opinion.
Pre-code audits return requirements and design gaps; later audits can test operating
effectiveness. Start from `assets/audit-report-template.md`; the method is in
`references/audit.md` and the procedures in
`references/australia/audit-checklist.md` and `references/eu/audit-checklist.md`.

## Citations

Every citation names the legislation as well as the provision — never a bare
`Art 6(1)(a)`, `s 26WE` or `§ 7013`. Name the instrument with its official
identifier on first use, then use the accepted abbreviation:

| Instrument | Cite as |
|---|---|
| Australia | `Privacy Act 1988 (Cth) s 16C`; `Privacy Act 1988 (Cth) Sch 1 cl 11.1 (APP 11.1)` |
| EU | `GDPR Art 6(1)(a)`; `AI Act Art 5(1)(f)`; `Data Act Art 4(12)` |
| USA / California | `CCPA § 1798.120`; `CCPA Regs § 7013(c)(1)` (11 CCR § 7013) |

Give the provision at the finest useful granularity, and cite each applicable
instrument separately (e.g. `GDPR Art 6(1)(a); Privacy Act 1988 (Cth) APP 3.3`).

## Official texts

- Australia — [Privacy Act 1988](https://www.legislation.gov.au/C2004A03712/latest/text)
- European Union — [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- European Union — [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- European Union — [Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)
- USA / California — [CCPA statute](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=1.81.5.&part=4.)
- USA / California — [CCPA Regulations](https://cppa.ca.gov/regulations/)

## Legislation status

When each instrument was last checked and last updated is recorded in
[`references/legislation-status.md`](references/legislation-status.md). In the source
repository this table is generated by `scripts/check-legislation.py`; the package
ships the latest table as a snapshot.

## Scope and caveats

This package supports engineering and design review; it is not legal advice.
Statutes change — verify currency against the official register before relying on a
citation in a high-stakes context. Each regime sits alongside others (credit
reporting and APP codes, ePrivacy, DMA, DSA, NIS2, national Member State law) that
this package does not fully cover.

## License

MIT — see [LICENSE](LICENSE).
