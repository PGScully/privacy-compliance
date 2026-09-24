# USA / California — CCPA orientation

Two instruments apply together, both effective **1 January 2026**:

| Instrument | Citation | Text |
|---|---|---|
| California Consumer Privacy Act of 2018 (as amended, incl. AB 137 and AB 566) | `CCPA § 1798.xxx` (Civil Code) | `legislation/USA/California/CCPA statute.txt` |
| CCPA Regulations (California Privacy Protection Agency) | `CCPA Regs § 70xx` (Title 11, Div 6) | `legislation/USA/California/CCPA regulations.txt` |

The regulations do not stand alone: a violation of the regulations is a violation of
the CCPA (Regs § 7000(b)). Cite both where relevant, e.g. "CCPA § 1798.100; CCPA
Regs § 7002".

## Who is covered ("business")

CCPA § 1798.140(d): a for-profit entity that does business in California, controls
or is controlled by such an entity (common branding), or is a 40/40 joint venture,
and meets one or more thresholds (as adjusted under § 1798.199.95(d)):

- annual gross revenues over **USD 25,000,000** in the preceding calendar year;
- alone or in combination, annually **buys, sells or shares** the personal
  information of **100,000 or more consumers or households**; or
- derives **50% or more** of annual revenues from selling or sharing personal
  information.

Entities that are not covered may voluntarily certify to the CPPA and be bound
(§ 1798.140(d)(4)). The statute also reaches **service providers, contractors and
third parties** that handle personal information for a business.

## Key definitions (§ 1798.140)

- **Personal information** — information that identifies, relates to, describes,
  is reasonably capable of being associated with, or could reasonably be linked to
  a particular consumer or household; excludes deidentified and aggregate consumer
  information and lawfully obtained publicly available information.
- **Sensitive personal information** § 1798.140(ae) — government identifiers
  (SSN, driver's licence, passport), account log-in/credentials, precise
  geolocation, racial/ethnic origin, religious/philosophical beliefs, union
  membership, contents of mail/email/texts, genetic data, biometric information,
  health, sex life or sexual orientation, and **neural data**.
- **Sell** § 1798.140(ad) and **share** § 1798.140(ah) — broad; "share" captures
  cross-context behavioral advertising. Both are subject to the opt-out.
- **Service provider** (ag) and **contractor** (j) — persons processing on the
  business's behalf under a written contract with the required terms.
- **Third party** (ai) — anyone who is not the business, a service provider,
  contractor, or the consumer.
- **Automated decisionmaking technology (ADMT)** — Regs § 7001(e): technology
  (including profiling) that replaces or substantially informs human
  decisionmaking; **significant decisions** are defined at Regs § 7001(ddd).
- **Dark pattern**, **cross-context behavioral advertising**, **consent**,
  **profiling**, **precise geolocation**, **sensitive location**.

## Consumer rights

- Know / access — §§ 1798.110, 1798.115
- Delete — § 1798.105
- Correct — § 1798.106
- Opt out of sale/sharing — § 1798.120
- Limit use/disclosure of sensitive personal information — § 1798.121
- No retaliation — § 1798.125
- Opt out of, and access, ADMT for significant decisions — Regs §§ 7200, 7220–7222

## Read next

- `ccpa.md` — obligations in detail (collection, rights, notices, contracts,
  security, ADMT, audits, risk assessments, enforcement).
- `privacy-policy.md` — required disclosures and policy content.
- `audit-checklist.md` — control-by-control audit procedures.

## Note on overlap

CCPA privacy notices and GDPR notices can be merged, but the CCPA adds
California-specific rights (opt-out of sale/sharing, limit sensitive PI, ADMT) and
prescriptive notice content. See `references/eu/privacy-notice.md` where both apply.
