# EU Data Act — Regulation (EU) 2023/2854

The Data Act governs access to and sharing of data from connected products and
services, cloud switching, and safeguards against unlawful governmental access. It
covers both personal and non-personal data, and it **complements** the GDPR rather
than replacing it. Full text: `legislation/Europe/Data Act/EU Data Act.txt`. Cite
as **Data Act Art N**.

## 1. Scope and relationship to the GDPR

- **Subject matter (Art 1):** making product/related-service data available to
  users; data sharing between data holders and recipients; access by public sector
  bodies on exceptional need; switching between data processing services;
  safeguards against unlawful third-party access to non-personal data; and
  interoperability.
- **Scope (Art 1(2)–(4)):** connects to connected products, related services and
  virtual assistants; applies to manufacturers, providers, users, data holders,
  recipients, public sector bodies and data processing service providers — largely
  irrespective of establishment — where the product/service is used in the Union.
- **GDPR priority (Art 1(5)):** the Data Act is **without prejudice** to the GDPR,
  the ePrivacy Directive and Directive 2016/680. Where users are data subjects,
  Chapter II rights **complement** GDPR access (Art 15) and portability (Art 20).
  **In a conflict, the EU data-protection law prevails.**
- **Definitions (Art 2):** data; metadata; personal data (as in GDPR Art 4(1));
  non-personal data; connected product; related service; data holder; data
  recipient; user; and others.

## 2. User access to connected-product data (Chapter II)

- **Art 3:** connected products and related services must be designed so that
  product/related-service data are, **by default**, easily, securely, free of
  charge, in a comprehensive, structured, commonly used and machine-readable
  format, and directly accessible to the user where technically feasible. Before
  contract conclusion, the seller/provider must disclose data types, formats,
  volumes, continuity, storage location/retention and how the user can access,
  retrieve or erase data (Art 3(2)–(3)).
- **Art 4:** where direct access is unavailable, data holders must make readily
  available data accessible to the user without undue delay, of the same quality,
  easily, securely, free of charge and in a machine-readable format; no dark
  patterns (Art 4(4)); no over-collection of verification information or
  unnecessary logs (Art 4(5)); trade-secret safeguards (Art 4(6)–(8)).
  **Art 4(12):** where the user is **not** the data subject, personal data may be
  made available only with a valid GDPR Art 6 legal basis and, where relevant,
  Art 9 conditions and ePrivacy Art 5(3).
- **Art 5:** users may direct data holders to share data with third parties.
  **Art 5(7):** the same GDPR legal-basis requirement applies for personal data.
  Gatekeepers under the DMA cannot be eligible third parties (Art 5(3)).
- **Art 6:** third parties may process shared data only for the agreed purpose and
  must respect data-protection law; must erase when no longer necessary; may not
  use it for profiling unless necessary for the requested service (Art 6(2)(b));
  no onward sharing except under contract (Art 6(2)(c)); no competitive use.
- **Art 7:** Chapter II does not apply to micro/small enterprises (with
  conditions).

## 3. Public sector access on exceptional need (Chapter V)

- **Art 14–15:** public sector bodies, the Commission, the ECB and Union bodies may
  request data only where there is an **exceptional need** for a specific task in
  the public interest (e.g. public emergencies, prevention/recovery), subject to
  necessity and proportionality; data minimisation and time limits apply.
- **Art 17:** requests must specify the data, demonstrate the exceptional need,
  explain the purpose and duration, justify the choice of data holder, and — where
  personal data are requested — specify necessary and proportionate technical and
  organisational measures such as **pseudonymisation** and whether anonymisation
  is possible (Art 17(1)(g)); requests should concern non-personal data first and
  only request personal data in pseudonymised form where that is insufficient
  (Art 17(2)(e)); personal-data requests must be notified to the relevant
  supervisory authority (Art 17(2)(i)).
- **Art 18–19:** data holders comply without undue delay unless the request is
  manifestly unfounded or excessive; safeguards for trade secrets and personal
  data apply.

## 4. Cloud switching (Chapter VI)

- **Art 23–31:** providers of data processing services must support customer
  switching: remove obstacles, provide contractual and technical support, make
  export possible, and avoid egress charges for switching (Art 29).
- **Art 30:** facilitate functional equivalence; provide **open interfaces** on
  equal terms (Art 30(2)); on request, export all exportable data in a structured,
  commonly used and machine-readable format (Art 30(5)).
- Privacy relevance: switching and export must be interoperable with GDPR
  portability (Art 20) and must not cause unauthorised disclosure; personal data
  handling during export still requires a lawful basis.

## 5. Unlawful international governmental access (Chapter VII)

- **Art 32:** providers of data processing services must take all adequate
  technical, organisational and legal measures (including contracts) to prevent
  international/third-country governmental access to **non-personal** data held in
  the Union where that would conflict with Union or Member State law (Art 32(1)).
  Third-country judgments/decisions are enforceable only on an international
  agreement basis (Art 32(2)); absent an agreement, transfer/access is permitted
  only if the third country's system meets the conditions in Art 32(3) (reasoned
  and specific decisions, judicial review of objections, ability to weigh Union
  legal interests); respond with the **minimum amount of data** permissible
  (Art 32(4)); **inform the customer** before complying unless law enforcement
  confidentiality requires otherwise (Art 32(5)).

## 6. Penalties (Art 40)

Member States set effective, proportionate and dissuasive penalties. For
infringements of Chapters II, III and V, **GDPR supervisory authorities** may impose
administrative fines under **GDPR Art 83**, up to the Art 83(5) amount (EUR 20m/4%).

## 7. Engineering signals and common failures

| Signal | Check |
|---|---|
| IoT / connected product data flows | Art 3 default access, Art 4 user access and GDPR Art 4(12) basis |
| "Share my data with third party" features | Art 5/6 purpose limits, GDPR legal basis, no gatekeeper recipient |
| Data export / cloud migration | Art 30 open interfaces and machine-readable export; GDPR Art 20 |
| Public-body data requests | Art 14–18 exceptional-need test, pseudonymisation, supervisory notification |
| Vendor/offshore cloud contracts | Art 32 governmental-access safeguards and customer notice |

**Common failures:** exposing other people's personal data to a product "owner"
without a GDPR legal basis (Art 4(12)/5(7)); treating Data Act access rights as
overriding the GDPR; no logging or abuse prevention on access requests; ignoring
the Art 32 safeguards in cloud contracts; charging egress fees that block
switching.
