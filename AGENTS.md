# AGENTS.md

## Project

**Privacy Skill** — a skill for coding assistants that surfaces privacy concerns derived
from privacy legislation. The skill is meant to apply across the whole development
lifecycle: requirements gathering, implementation, and post-deployment operation.

## Repository layout

```
README.md                              Project overview and requirements
AGENTS.md                              Agent instructions for this repo
.pi/settings.json                      Registers skills/ for pi discovery
legislation/                           Original source legislation (not uploaded)
  Australia/Privacy Act 1988.txt       Australian statute text
  Europe/GDPR/                         GDPR text + source PDF
  Europe/AI Act/                       AI Act text + source PDF
  Europe/Data Act/                     Data Act text + source PDF
  USA/California/                      CCPA statute and regulations text + source PDFs
skills/
  privacy-skill/                       Self-contained, uploadable skill package
    SKILL.md                           Agent Skills entry point (routing, workflow, output)
    README.md                          Package documentation and install/use
    LICENSE
    assets/
      privacy-policy-template.md       Fill-in policy template (APP 1.4 / GDPR Art 13-14)
      audit-report-template.md         Fill-in audit report
    references/                        Review, audit and drafting references
      audit.md                         Audit methodology, ratings and reporting
      australia/                       AU Privacy Act 1988
        README.md                      Orientation and citation summary
        scope.md                       Coverage, definitions, exemptions
        apps.md                        APP 1-13 clause-by-clause checklist
        privacy-policy.md              APP privacy policy requirements
        audit-checklist.md             APP audit procedures and evidence map
        breach-notification.md         Part IIIC notifiable data breaches
        statutory-tort.md              Schedule 2 serious invasions of privacy
      eu/
        gdpr.md                        EU GDPR (2016/679)
        privacy-notice.md              GDPR Art 12-14 notice content
        audit-checklist.md             GDPR/AI Act/Data Act audit procedures
        ai-act.md                      EU AI Act (2024/1689)
        data-act.md                    EU Data Act (2023/2854)
      usa/                             California CCPA (statute + regulations)
        README.md                      Orientation, scope and definitions
        ccpa.md                        CCPA obligations
        privacy-policy.md              Required CCPA disclosures
        audit-checklist.md             CCPA audit procedures
```

The top-level `legislation/` directory holds the full source texts and is **not** part
of any uploaded package. Packages ship summaries and citations only, and link to the
official online texts; this keeps the installed skill small (currently ~200 KB).

## Key requirements (from README)

1. The skill must be applicable at every stage of development, not just code review.
2. Every issue flagged by the skill must cite the relevant section(s) of the relevant
   privacy legislation.

## Adding legislation

Place the original text in the top-level `legislation/<Jurisdiction>/`, add a matching
reference under `skills/privacy-skill/references/<jurisdiction>/`, link it from
`SKILL.md`, and add the **official online link** to the jurisdiction table. Do not
copy the full statute text into the package. Keep the top-level `legislation/` as the
authoritative source for text extraction and quotation.

## Outputs

A skill suitable for use by multiple agents, e.g. Claude, Codex, Deepseek, etc, with
sub-folders for each jurisdiction.

- Each skill is packaged in its own directory under `skills/`, ready to upload to a
  skills repository as-is.
- Entry point is `skills/privacy-skill/SKILL.md`, written to the Agent Skills spec so
  it works across agents (Claude, Codex, Deepseek, pi, ...).
- Per-jurisdiction detail lives under `skills/privacy-skill/references/<jurisdiction>/`.
- The skill routes by jurisdiction and cites the exact provision for every finding.
- The skill has three capabilities: **review** (flag issues), **audit** (rate every
  control against a defined scope and produce a report), and **draft a privacy
  policy/notice** (targeting AU APP 1.4 and EU GDPR Art 13/14, merged where needed).
- The **audit** capability applies across the whole lifecycle — at requirements
  gathering before any code exists, through design, build, operation and later
  changes. Each audit states the stage(s) in scope; pre-code audits give design-only
  assurance and return requirements/design gaps.
- Keep all paths inside a package **relative to the package root**, so the package
  stays portable when uploaded on its own.

## Building the EU statute text

The EU PDFs were extracted to plain text with `pdftotext -layout`, e.g.:

```sh
pdftotext -layout "legislation/Europe/GDPR/CELEX_32016R0679_EN_TXT.pdf" \
  "legislation/Europe/GDPR/GDPR.txt"
```

Keep the extracted `.txt` alongside the source PDF in the top-level `legislation/`.
The text stays in the top-level directory — do **not** copy it into the package.

## Notes

- No build system, package manifest, or tests currently exist — the repo is
  documentation/legislation content plus the skill files.
- When adding a capability, keep the drafting/validation instructions in `SKILL.md`
  and the required content in the jurisdiction references; keep reusable fill-in
  documents under `assets/`.
- When adding skill content, cite legislation in the native form: Australian
  `Act name YYYY s <section>` / `APP N.N`; EU `Regulation name Art N`.
- Keep the jurisdiction sub-folder naming consistent: `legislation/<Region or
  Country>/...` and `references/<jurisdiction>/...`.
- Do not add files that reference paths outside the package; a package must work
  when copied out of this repository on its own.
- Do not bundle full statute text in a package (it dominates the installed size).
  Reference the summary under `references/<jurisdiction>/` and link the official
  online text instead.
