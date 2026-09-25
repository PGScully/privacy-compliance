# Privacy Compliance

A privacy-compliance skill for coding assistants, derived from privacy legislation. The
skill reviews software, designs, data flows and policies for privacy and
data-protection compliance, flags issues with citations to the relevant provision,
audits code and documentation against a defined scope, and drafts or updates privacy
policies and privacy notices.

## Skill Requirements

1. The skill should be applicable across all stages of development, from requirements gathering, through implementation, to post deployment operation.
2. Any issues flagged by this skill should reference the relevant privacy
   legislation by name/abbreviation as well as the relevant section(s).

## Layout

This repository is a skills collection. Each package lives in its own directory
under `skills/` and carries the skill entry point and references, so it can be
uploaded to a skills repository as-is. The full statute texts are kept at the top
level for reference and text extraction, but are **not** bundled in the package.

```
legislation/                     Original source legislation (incl. source PDFs)
  Australia/Privacy Act 1988.txt
  Europe/GDPR/                   GDPR text + source PDF
  Europe/AI Act/                 AI Act text + source PDF
  Europe/Data Act/               Data Act text + source PDF
  USA/California/                CCPA statute and regulations text + source PDFs
skills/
  privacy-compliance/             Uploadable skill package
    SKILL.md                     Agent Skills entry point
    README.md                    Package documentation
    LICENSE
    assets/
      privacy-policy-template.md  Fill-in template (APP 1.4 / GDPR Art 13-14)
      audit-report-template.md    Fill-in audit report template
    references/
      audit.md                    Audit methodology, ratings and reporting
      australia/                 Australian Privacy Act 1988
        README.md
        scope.md
        apps.md
        privacy-policy.md        APP privacy policy requirements
        audit-checklist.md       APP audit procedures and evidence map
        breach-notification.md
        statutory-tort.md
      eu/
        gdpr.md                  GDPR (2016/679)
        privacy-notice.md        GDPR Art 12-14 notice content
        audit-checklist.md       GDPR/AI Act/Data Act audit procedures
        ai-act.md                AI Act (2024/1689)
        data-act.md              Data Act (2023/2854)
      usa/                       California CCPA
        README.md                Orientation, scope and definitions
        ccpa.md                  CCPA obligations
        privacy-policy.md        Required CCPA disclosures
        audit-checklist.md       CCPA audit procedures
```

The top-level `legislation/` directory holds the full source texts (including source
PDFs). It is **not** part of the uploaded package: to keep the installed skill small
(~200 KB), the package ships summaries and citations and links to the official texts
below rather than bundling the full statutes.

The package covers:

- Australia — [Privacy Act 1988](https://www.legislation.gov.au/C2004A03712/latest/text)
- European Union — [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- European Union — [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- European Union — [Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)
- USA / California — [CCPA](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=1.81.5.&part=4.) and the [CCPA Regulations](https://cppa.ca.gov/regulations/) (both effective 1 January 2026)

## Capabilities

- **Review** — flag privacy issues in code, designs, data flows and policies, each
  naming the legislation and citing the specific provision (for example
  `Privacy Act 1988 (Cth) Sch 1 cl 11.1 (APP 11.1)`,
  `Privacy Act 1988 (Cth) s 26WE`, `GDPR Art 6(1)(a)`, `AI Act Art 5(1)(f)`,
  `Data Act Art 4(12)`, `CCPA § 1798.120`, `CCPA Regs § 7013(c)(1)`).
- **Audit** — assess requirements, designs, code and documentation against a defined
  scope and criteria at any lifecycle stage (requirements, design, build, operation,
  change), rating every control and producing a report with a control matrix,
  evidence index and an overall opinion.
- **Draft a privacy policy** — create or update a policy/notice, with every required
  element traced to its provision (AU **APP 1.4**; EU **GDPR Art 13/14**).

## Using the skill

See [`skills/privacy-compliance/README.md`](skills/privacy-compliance/README.md) for full
install and usage instructions. In short, place
`skills/privacy-compliance/` where your agent discovers skills:

- Agent Skills standard: `.agents/skills/` (project) or `~/.agents/skills/` (user).
- pi: running pi from this repository discovers it automatically — the project
  settings file [`.pi/settings.json`](.pi/settings.json) registers `skills/`.
  It is available as `/skill:privacy-compliance`.

## Adding legislation

To extend an existing jurisdiction or add a new one:

1. Place the source text in the top-level `legislation/<Jurisdiction>/`. For PDFs,
   extract to text alongside the source file so you can quote and verify
   provisions:

   ```sh
   pdftotext -layout "legislation/Europe/GDPR/CELEX_32016R0679_EN_TXT.pdf" \
     "legislation/Europe/GDPR/GDPR.txt"
   ```

2. Add a matching reference under `skills/privacy-compliance/references/<jurisdiction>/`,
   link it from `SKILL.md`, and add the official online link to the jurisdiction
   table. Do **not** copy the full statute text into the package.
3. Add the instrument to `legislation/sources.json` and run
   `python scripts/check-legislation.py --write` (see below).

## Legislation status

The table records when each instrument was last checked and last updated (UTC). It
is generated by [`scripts/check-legislation.py`](scripts/check-legislation.py); do
not edit it by hand.

<!-- legislation-status:start -->
_Status is maintained by `scripts/check-legislation.py`; run it to refresh._

| Instrument | Jurisdiction | Official text | Last checked (UTC) | Last updated (UTC) | Status |
|---|---|---|---|---|---|
| Privacy Act 1988 (Cth) | Australia | [legislation.gov.au](https://www.legislation.gov.au/C2004A03712/latest/text) | 2026-09-24 | 2026-09-24 | current |
| GDPR (Regulation (EU) 2016/679) | European Union | [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | 2026-09-24 | 2026-09-24 | current |
| AI Act (Regulation (EU) 2024/1689) | European Union | [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | 2026-09-24 | 2026-09-24 | current |
| Data Act (Regulation (EU) 2023/2854) | European Union | [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2023/2854/oj) | 2026-09-24 | 2026-09-24 | current |
| CCPA statute (Civil Code 1798.100 et seq.) | USA / California | [leginfo.legislature.ca.gov](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=1.81.5.&part=4.) | 2026-09-24 | 2026-09-24 | current |
| CCPA Regulations (11 CCR 7000 et seq.) | USA / California | [cppa.ca.gov](https://cppa.ca.gov/regulations/) | 2026-09-24 | 2026-09-24 | current |
<!-- legislation-status:end -->

## Detecting and applying legislation updates

Official texts change without notice. Run the checker to detect drift:

```sh
python scripts/check-legislation.py          # report status; exit code 2 if anything changed
python scripts/check-legislation.py --write  # also refresh the timestamps and table above
python scripts/check-legislation.py --offline # rebuild the table without network access
```

The checker fetches each `official_url`, fingerprints the normalised visible text,
and compares it with the baseline in `legislation/sources.json`. When a source
reports **update available**:

1. Review the change in the official text (follow the link in the table).
2. Update the top-level `legislation/<Jurisdiction>/` text — for the EU and US PDFs
   re-extract with `pdftotext -layout`.
3. Update the affected reference(s) under `skills/privacy-compliance/references/` and, if
   a provision changed, the corresponding audit/notice checklists.
4. Re-run `python scripts/check-legislation.py --accept` to record the new baseline
   and advance the `last updated` date.

Notes:

- Fingerprinting uses the normalised visible text, so page furniture and asset churn
  do not trigger a false positive; a reported change still needs human confirmation
  against the official register.
- First run against a newly added source records the baseline automatically.
- In CI, treat exit code 2 as a prompt to review, not necessarily a failure.
