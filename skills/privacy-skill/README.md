# privacy-skill

A portable [Agent Skills](https://agentskills.io/specification) package that helps
coding assistants **review** software, designs, data flows and policies for privacy
and data-protection compliance, **audit** code and documentation against a defined
scope, and **draft or update privacy policies and privacy notices** — tracing every
finding or required element to its provision.

## Coverage

| Jurisdiction | Instrument |
|---|---|
| Australia | Privacy Act 1988 (Cth) and the 13 Australian Privacy Principles (APPs) |
| European Union | GDPR — Regulation (EU) 2016/679 |
| European Union | AI Act — Regulation (EU) 2024/1689 |
| European Union | Data Act — Regulation (EU) 2023/2854 |

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
legislation/                     Copies of the statute text cited by this package
  Australia/Privacy Act 1988.txt
  Europe/GDPR/GDPR.txt
  Europe/AI Act/EU AI Act.txt
  Europe/Data Act/EU Data Act.txt
```

The `legislation/` files are copies included so the package is self-contained and
its citations are verifiable offline. The canonical source (including the original
PDFs) lives in the repository's top-level `legislation/`; copy files from there into
this package when legislation is added or updated.

## Install

Copy this directory (or the repository's `skills/` directory) into a location your
agent scans for skills:

- Agent Skills standard: `.agents/skills/` (project) or `~/.agents/skills/` (user).
- pi: add the directory to the `skills` setting, or use `--skill <path>`.
- Other agents: point their skills location at this directory.

Once discovered, the skill is selectable automatically and/or invokable as
`/skill:privacy-skill`.

## Use

### Review

Ask the agent to review a change, design, data flow or policy for privacy issues.
The skill will:

1. establish which jurisdiction(s) apply;
2. classify the data (personal, sensitive/special-category, identifiers);
3. map the data lifecycle to the relevant obligations;
4. check breach, impact-assessment and AI/GPAI duties where relevant; and
5. report findings, each citing the exact provision (for example `APP 11.1`,
   `Privacy Act 1988 (Cth) s 26WE`, `GDPR Art 6(1)(a)`, `AI Act Art 5(1)(f)`,
   `Data Act Art 4(12)`).

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

## Keeping legislation in sync

This package carries copies of the statute text it cites. When the source
legislation changes:

1. update the file in the repository's top-level `legislation/`;
2. copy the relevant text into `legislation/` here; and
3. update the affected references.

## Scope and caveats

This package supports engineering and design review; it is not legal advice.
Statutes change — verify currency against the official register before relying on a
citation in a high-stakes context. Each regime sits alongside others (credit
reporting and APP codes, ePrivacy, DMA, DSA, NIS2, national Member State law) that
this package does not fully cover.

## License

MIT — see [LICENSE](LICENSE).
