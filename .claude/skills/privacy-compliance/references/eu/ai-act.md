# EU AI Act — Regulation (EU) 2024/1689

The AI Act is a product-safety/fundamental-rights regulation for AI, not a privacy
law — but it is a core part of a privacy review because several obligations turn on
personal data, biometrics and fundamental rights. Full text:
[EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj). Cite as **AI Act Art N**.
Last checked/updated: see [`legislation-status.md`](../legislation-status.md).

## 1. Scope and relationship to privacy law

- **Subject matter (Art 1):** harmonised rules for placing on the market, putting
  into service and use of AI systems; prohibitions; high-risk requirements;
  transparency rules; general-purpose AI (GPAI) model rules; market surveillance.
- **Scope (Art 2):** providers, deployers, importers, distributors and affected
  persons in the Union, including non-EU providers whose output is used in the
  Union. Excludes military/defence/national-security uses, purely personal
  non-professional use by natural-person deployers, and R&D before market
  placement.
- **Privacy carve-out (Art 2(7)):** the AI Act does **not** affect the GDPR,
  Directive 2002/58/EC or Directive 2016/680 (subject to Art 10(5) and Art 59).
  Always assess GDPR alongside the AI Act.
- **Definitions (Art 3):** AI system; risk; **provider**; **deployer**; GPAI model;
  GPAI model with systemic risk; and others.

## 2. Prohibited practices (Art 5) — highest priority

Banned outright (fines up to EUR 35m/7%):
- (a) subliminal, manipulative or deceptive techniques that materially distort
  behaviour and cause significant harm;
- (b) exploiting vulnerabilities based on age, disability or social/economic
  situation;
- (c) **social scoring** by public authorities leading to detrimental treatment;
- (d) **predictive policing** based solely on profiling or personality traits
  (narrow support tool exception);
- (e) creating/expanding **facial recognition databases by untargeted scraping**
  of the internet or CCTV;
- (f) **emotion inference in workplace and education** (except medical/safety);
- (g) **biometric categorisation** inferring race, political opinions, trade union
  membership, religious/philosophical beliefs, sex life or sexual orientation;
- (h) **real-time remote biometric identification in publicly accessible spaces
  for law enforcement**, subject to narrow, strictly necessary exceptions and
  authorisation safeguards (Art 5(2)–(7)).

If a feature matches any of these, flag it **Critical** and recommend removal or
redesign, regardless of consent.

## 3. High-risk classification (Art 6, Annex III)

- **Art 6(1):** AI as a safety component of, or a product covered by, Annex I
  Union harmonisation legislation requiring third-party conformity assessment.
- **Art 6(2):** AI systems listed in **Annex III**. The Annex III areas:
  1. Biometrics (remote identification, categorisation, emotion recognition);
  2. Critical infrastructure safety components;
  3. Education and vocational training (admission, assessment, monitoring);
  4. Employment and workers' management (recruitment, selection, task allocation,
     performance monitoring);
  5. Essential private/public services (benefits eligibility, **creditworthiness/
     credit scoring** except fraud detection, life/health insurance pricing,
     emergency-call triage);
  6. Law enforcement (victim/offender risk, polygraphs, evidence reliability,
     profiling);
  7. Migration, asylum and border control;
  8. Administration of justice and democratic processes (assisting judicial
     research/application of law, influencing elections/referenda).
- **Art 6(3):** narrow procedural tasks, improving prior human work, detecting
  deviations, or preparatory tasks may escape high-risk status — **but profiling
  always remains high-risk** (Art 6(3), second subparagraph). The provider must
  document a non-high-risk assessment (Art 6(4)).

## 4. Requirements for high-risk AI (Art 8–15)

- **Art 9 risk management system** — continuous, lifecycle-wide; identify/analyse
  risks to health, safety and **fundamental rights**; testing against defined
  metrics; consider impacts on minors and vulnerable groups.
- **Art 10 data and data governance** — training/validation/testing data must be
  relevant, representative, error-free and complete as far as possible; examine and
  mitigate biases; **Art 10(5)** permits processing special-category data solely
  for bias detection/correction, subject to strict conditions (no less intrusive
  alternative, pseudonymisation, security, no onward sharing, deletion once bias
  corrected, documented justification).
- **Art 11 technical documentation** (Annex IV).
- **Art 12 record-keeping** — automatic logging over the system's lifetime;
  specific biometric-identification logging minimums.
- **Art 13 transparency to deployers** — instructions for use with characteristics,
  limitations, accuracy metrics, human oversight measures, log interpretation.
- **Art 14 human oversight** — effective oversight, automation-bias awareness,
  ability to override/stop; **two-person verification** for biometric
  identification decisions (Art 14(5)).
- **Art 15 accuracy, robustness and cybersecurity** — resilience to errors and
  attacks (data poisoning, adversarial examples, model evasion).

## 5. Operator obligations

- **Providers (Art 16, 17, 18, 19, 43, 47–49):** comply with Section 2; quality
  management system; keep documentation (10 years, Art 18); keep logs; conformity
  assessment; EU declaration of conformity; CE marking; registration.
- **Deployers of high-risk AI (Art 26):** use per instructions; assign competent
  human oversight; ensure input data relevance; monitor and report risks/serious
  incidents; keep logs at least 6 months; **inform workers' representatives and
  affected workers before workplace use** (Art 26(7)); use provider information for
  DPIAs (Art 26(9)); authorisation rules for post-remote biometric identification
  (Art 26(10)); **inform natural persons subject to the system** where it makes or
  assists decisions about them (Art 26(11)).
- **Fundamental rights impact assessment (Art 27):** required for certain public
  bodies, private entities providing public services, and deployers of Annex III
  points 5(b) and 5(c) systems (creditworthiness, life/health insurance). Must
  describe processes, affected groups, risks, human oversight and mitigation; may
  complement a GDPR Art 35 DPIA.

## 6. Transparency obligations (Art 50)

- Inform people they are **interacting with an AI system** (unless obvious).
- **Mark synthetic audio/image/video/text as machine-readable and detectable**.
- Inform people exposed to **emotion recognition or biometric categorisation**.
- **Disclose deep fakes** and AI-generated public-interest text (with a limited
  artistic/fictional carve-out and editorial-responsibility exemption).

## 7. General-purpose AI models (Chapter V)

- **Art 51:** a GPAI model has **systemic risk** if it has high-impact capabilities
  (presumed above 10^25 FLOP training compute) or is designated by the Commission.
- **Art 52:** providers must notify the Commission without delay, within two weeks.
- **Art 53:** GPAI providers must keep technical documentation (Annex XI), provide
  information to downstream providers (Annex XII), have a copyright policy, and
  publish a **sufficiently detailed summary of training content**. Open-source
  models are exempt from some duties unless they present systemic risk.
- **Art 54–56:** authorised representatives, systemic-risk obligations and codes of
  practice.

## 8. Penalties (Art 99)

- Prohibited practices (Art 5): up to **EUR 35,000,000 or 7%** of worldwide annual
  turnover, whichever is higher.
- Other operator/notified-body breaches (including provider Art 16, deployer
  Art 26, transparency Art 50): up to **EUR 15,000,000 or 3%**.
- Incorrect/incomplete/misleading information: up to **EUR 7,500,000 or 1%**.
- SMEs/start-ups: capped at the lower amount.

## 9. Engineering signals and common failures

| Signal | Check |
|---|---|
| Biometric identification/categorisation, emotion detection | Art 5 prohibitions first; then Annex III high-risk and Art 14(5) |
| Recruitment, credit scoring, insurance pricing, education assessment | Annex III points 3/4/5; Art 6(3) profiling rule |
| Chatbots / generative features | Art 50 interaction notice and synthetic-content marking |
| Workplace monitoring / productivity analytics | Art 5(1)(f) emotion ban; Art 26(7) worker information |
| Model training pipelines | Art 10 data governance; Art 10(5) special-category conditions |
| Overrides / review tooling | Art 14 human oversight and stop controls |

**Common failures:** assuming GDPR consent cures an Art 5 prohibition (it does
not); missing Annex III classification; treating bias-mitigation processing of
special-category data as ordinary processing; no logging or human override;
claiming the Art 6(3) exemption while profiling.
