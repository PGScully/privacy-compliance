# Privacy Skill

A privacy skill for coding assistants, derived from privacy legislation. The
skill reviews software, designs, data flows and policies for privacy and
data-protection compliance, flagging issues with citations to the relevant
provision, and drafts or updates privacy policies and privacy notices.

## Skill Requirements

1. The skill should be applicable across all stages of development, from requirements gathering, through implementation, to post deployment operation.
2. Any issues flagged by this skill should include references to the relevant sections of the relevant privacy legislation.

## Layout

This repository is a skills collection. Each package lives in its own directory
under `skills/` and is self-contained (entry point, references and bundled source
text), so it can be uploaded to a skills repository as-is.

```
legislation/                     Original source legislation (incl. source PDFs)
  Australia/Privacy Act 1988.txt
  Europe/GDPR/                   GDPR text + source PDF
  Europe/AI Act/                 AI Act text + source PDF
  Europe/Data Act/               Data Act text + source PDF
skills/
  privacy-skill/                 Uploadable, self-contained skill package
    SKILL.md                     Agent Skills entry point
    README.md                    Package documentation
    LICENSE
    assets/
      privacy-policy-template.md  Fill-in template (APP 1.4 / GDPR Art 13-14)
    references/
      australia/                 Australian Privacy Act 1988
        README.md
        scope.md
        apps.md
        privacy-policy.md        APP privacy policy requirements
        breach-notification.md
        statutory-tort.md
      eu/
        gdpr.md                  GDPR (2016/679)
        privacy-notice.md        GDPR Art 12-14 notice content
        ai-act.md                AI Act (2024/1689)
        data-act.md              Data Act (2023/2854)
    legislation/                 Copies of the text cited by the package
```

The top-level `legislation/` directory is the original source and is not part of the
uploaded package. The package carries its own copies of the relevant text under
`skills/privacy-skill/legislation/`.

The package covers:

- Australia — [Privacy Act 1988](https://www.legislation.gov.au/C2004A03712/latest/text)
- European Union — [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- European Union — [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- European Union — [Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)

## Capabilities

- **Review** — flag privacy issues in code, designs, data flows and policies, each
  with a citation to the specific provision (for example `APP 11.1`,
  `Privacy Act 1988 (Cth) s 26WE`, `GDPR Art 6(1)(a)`, `AI Act Art 5(1)(f)`,
  `Data Act Art 4(12)`).
- **Draft a privacy policy** — create or update a policy/notice, with every required
  element traced to its provision (AU **APP 1.4**; EU **GDPR Art 13/14**).

## Using the skill

See [`skills/privacy-skill/README.md`](skills/privacy-skill/README.md) for full
install and usage instructions. In short, place
`skills/privacy-skill/` where your agent discovers skills:

- Agent Skills standard: `.agents/skills/` (project) or `~/.agents/skills/` (user).
- pi: running pi from this repository discovers it automatically — the project
  settings file [`.pi/settings.json`](.pi/settings.json) registers `skills/`.
  It is available as `/skill:privacy-skill`.

## Adding legislation

To extend an existing jurisdiction or add a new one:

1. Place the source text in the top-level `legislation/<Jurisdiction>/`. For PDFs,
   extract to text alongside the source file so agents can quote and verify
   provisions:

   ```sh
   pdftotext -layout "legislation/Europe/GDPR/CELEX_32016R0679_EN_TXT.pdf" \
     "legislation/Europe/GDPR/GDPR.txt"
   ```

2. Copy the relevant text file(s) into the package under
   `skills/privacy-skill/legislation/<Jurisdiction>/` so the package stays
   self-contained.
3. Add a matching reference under `skills/privacy-skill/references/<jurisdiction>/`
   and link it from `SKILL.md`.
