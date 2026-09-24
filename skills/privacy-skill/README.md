# privacy-skill

A portable [Agent Skills](https://agentskills.io/specification) package that helps
coding assistants review software, designs, data flows and policies for privacy and
data-protection compliance, and flag issues with precise citations to the relevant
provision.

## Coverage

| Jurisdiction | Instrument |
|---|---|
| Australia | Privacy Act 1988 (Cth) and the 13 Australian Privacy Principles (APPs) |
| European Union | GDPR — Regulation (EU) 2016/679 |
| European Union | AI Act — Regulation (EU) 2024/1689 |
| European Union | Data Act — Regulation (EU) 2023/2854 |

## Package contents

```
SKILL.md                         Entry point: jurisdiction routing, workflow, output format
LICENSE
references/
  australia/
    README.md                    Orientation and citation summary
    scope.md                     Coverage, definitions, exemptions, permitted situations
    apps.md                      APP 1-13 clause-by-clause checklist
    breach-notification.md       Part IIIC notifiable data breaches
    statutory-tort.md            Schedule 2 serious invasions of privacy
  eu/
    gdpr.md                      Principles, lawful bases, rights, obligations, transfers, fines
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

Ask the agent to review a change, design, data flow or policy for privacy issues.
The skill will:

1. establish which jurisdiction(s) apply;
2. classify the data (personal, sensitive/special-category, identifiers);
3. map the data lifecycle to the relevant obligations;
4. check breach, impact-assessment and AI/GPAI duties where relevant; and
5. report findings, each citing the exact provision (for example `APP 11.1`,
   `Privacy Act 1988 (Cth) s 26WE`, `GDPR Art 6(1)(a)`, `AI Act Art 5(1)(f)`,
   `Data Act Art 4(12)`).

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
