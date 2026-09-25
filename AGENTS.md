# AGENTS.md

Agent instructions for the Privacy Compliance skill repo. Human-facing overview,
install/use, capabilities and the legislation status table live in
[`README.md`](README.md) — edit those there, not here.

## Layout

- `skills/privacy-compliance/` — the only uploadable package: `SKILL.md` (Agent Skills
  entry point: routing, workflow, output), `README.md`, `LICENSE`; `assets/` (policy
  and audit templates); `references/` (`audit.md`, `legislation-status.md`, and
  per-jurisdiction `australia/`, `eu/`, `usa/`).
- `legislation/` — full source texts, not shipped: `sources.json` (provenance and
  fingerprints); `Australia/Privacy Act 1988.txt`; `Europe/{GDPR,AI Act,Data Act}/`;
  `USA/California/`.
- `scripts/check-legislation.py` — maintainer legislation drift checker, not shipped.
- `.pi/settings.json` — registers `skills/` for pi discovery.

## Rules

- **Cite by instrument, always.** Australian `Privacy Act 1988 (Cth) s <section>` /
  `Privacy Act 1988 (Cth) Sch 1 cl N.N (APP N.N)`; EU `GDPR Art N`, `AI Act Art N`,
  `Data Act Art N`; California `CCPA § N` / `CCPA Regs § N`. Never a bare
  `Art 13(1)(a)`, `s 26WE` or `§ 7013`.
- **Keep packages portable.** Paths inside a package are relative to the package root
  and must not reference anything outside it; `skills/privacy-compliance/` must work
  when copied out of this repo on its own.
- **Never bundle full statute text** in a package (it dominates install size). Ship
  summaries and citations under `references/<jurisdiction>/` and link the official
  online text.
- **Put content in the right place.** `SKILL.md` is the Agent Skills entry point and
  must work across agents (Claude, Codex, Deepseek, pi); keep drafting/validation
  instructions there, required jurisdiction content in the references, and reusable
  fill-in documents in `assets/`. Naming: `legislation/<Region or Country>/...` and
  `references/<jurisdiction>/...`.
- **Generated files are off-limits.** Never hand-edit between the `legislation-status`
  markers (in `README.md` and `references/legislation-status.md`); use the script.
- No build system, package manifest or tests — the repo is documentation/legislation
  content plus skill files.

## Adding legislation

1. Put the source text in `legislation/<Jurisdiction>/`; extract PDFs to text
   alongside the source with `pdftotext -layout "in.pdf" "out.txt"`.
2. Add a matching reference under `skills/privacy-compliance/references/<jurisdiction>/`,
   link it from `SKILL.md`, and add the official online link to the README
   jurisdiction table.
3. Add the instrument to `legislation/sources.json` and run
   `python scripts/check-legislation.py --write` to record the baseline.

Do not copy the statute text into the package; keep `legislation/` authoritative for
text extraction and quotation.

## Keeping legislation current

`legislation/sources.json` records, per instrument, the official URL, local text path,
SHA-256 of the normalised official text, and the `last_checked` / `last_updated` dates
and status. `scripts/check-legislation.py` fetches each source, compares the
fingerprint and refreshes the manifest and generated status table.

```sh
python scripts/check-legislation.py           # report; exit code 2 if anything changed
python scripts/check-legislation.py --write   # refresh timestamps and status tables
python scripts/check-legislation.py --accept  # accept fetched text as the new baseline
python scripts/check-legislation.py --offline # no network; rebuild tables only
```

On **update available**: review the changed official text, update
`legislation/<Jurisdiction>/` (re-extract PDFs with `pdftotext -layout`), update the
affected references/checklists, then run `--accept`. Detection fingerprints normalised
visible text, so markup/asset churn is ignored, but a reported change still needs
human confirmation. First run against a new source records the baseline automatically.
