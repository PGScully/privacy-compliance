# AGENTS.md

## Project

**Privacy Skill** — a skill for coding assistants that surfaces privacy concerns derived
from privacy legislation. The skill is meant to apply across the whole development
lifecycle: requirements gathering, implementation, and post-deployment operation.

## Repository layout

```
README.md                              Project overview and requirements
legislation/                           Source legislation, one sub-folder per jurisdiction
  Australia/Privacy Act 1988.txt       Australian Privacy Act (copied statute text)
```

## Key requirements (from README)

1. The skill must be applicable at every stage of development, not just code review.
2. Every issue flagged by the skill must cite the relevant section(s) of the relevant
   privacy legislation.

## Adding legislation

Place the text of the relevant legislation in a sub-folder of `legislation/` named
after the jurisdiction (e.g. `legislation/Australia/`).

## Notes

- No build system, package manifest, or tests currently exist — the repo is
  documentation/legislation content plus whatever skill files are added later.
- When adding skill content, cite legislation as `Act name YYYY s <section>` so
  references stay checkable against the text in `legislation/`.
