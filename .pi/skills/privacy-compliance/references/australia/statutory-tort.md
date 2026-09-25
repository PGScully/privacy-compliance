# Statutory tort for serious invasions of privacy (Schedule 2)

A direct cause of action in tort, introduced by Act No. 75, 2025. It operates
**separately from the APPs** (Sch 2 cl 2, cl 6(2)–(3)) and is not limited to APP
entities — any person can be a defendant. Read it when reviewing products that
intrude on people's private space or misuse information about them: recording or
surveillance, photo/name features, data brokerage, doxxing and similar.

## Cause of action (Sch 2 cl 7)

An individual (the plaintiff) has a cause of action against another person (the
defendant) if **all** of the following are satisfied (cl 7(1)):

1. the defendant **invaded the plaintiff's privacy** by one or both of:
   - **intruding upon the plaintiff's seclusion** — including physically
     intruding into private space, and watching, listening to or recording
     private activities or affairs (cl 6); or
   - **misusing information that relates to the plaintiff** — including
     collecting, using or disclosing information (cl 6);
2. a person in the plaintiff's position would have had a **reasonable expectation
   of privacy** in all the circumstances;
3. the invasion was **intentional or reckless**;
4. the invasion was **serious**; and
5. the **public interest in the plaintiff's privacy outweighed** any
   countervailing public interest.

The invasion is actionable **without proof of damage** (cl 7(2)), and it is
**immaterial whether the information was true** (cl 7(7)).

**Reasonable expectation of privacy** — the court may consider the means
(devices/technology) used, the purpose, the plaintiff's age/occupation/cultural
background, the plaintiff's conduct (including inviting publicity), the place of
any intrusion, and, for misuse of information, the nature of the information
(especially intimate, family, health, medical or financial matters), how it was
held or communicated, and whether it was already public (cl 7(5)).

**Seriousness** — degree of offence, distress or harm to dignity likely for a
person of ordinary sensibilities; whether the defendant knew or ought to have
known; and whether an intentional invasion was motivated by malice (cl 7(6)).

**Countervailing public interests** may include freedom of expression (including
political communication and artistic expression), freedom of the media, the proper
administration of government, open justice, public health and safety, national
security, and the prevention and detection of crime and fraud (cl 7(3)).

## Defences (cl 8)

- The invasion was required or authorised by or under an Australian law or a
  court/tribunal order.
- The plaintiff (or a person with lawful authority) expressly or impliedly
  consented.
- The defendant reasonably believed the invasion was necessary to prevent or
  lessen a serious threat to the life, health or safety of a person.
- The invasion was incidental to a lawful right of defence of persons or property
  and was proportionate, necessary and reasonable.
- **Defamation-related defences** apply where the invasion was by publication of
  information relating to the plaintiff and the defendant could establish an
  equivalent defence (e.g. absolute privilege, publication of public documents,
  fair report of proceedings of public concern) (cl 8(2)–(3)).

An **apology** is not an admission of fault or liability and is not relevant to
liability (cl 13), but may be considered in assessing damages (cl 11(6)(a)).

## Exemptions (Part 3)

The Schedule does not apply to:
- **Journalists etc.** acting in relation to journalistic material (news, current
  affairs, documentaries, commentary or editorial content) — cl 15. Applicable
  even if the conduct breaches a professional code (cl 15(4)).
- **Agencies and State/Territory authorities** other than intelligence and law
  enforcement bodies, acting in good faith in the performance of functions or
  exercise of powers (cl 16); and their staff (cl 16A).
- **Law enforcement bodies** and their staff, and disclosures to them or of
  information they disclosed (cl 16B).
- **Intelligence agencies**, their staff and ASIO affiliates, and disclosures to
  them or of information they disclosed (cl 17).
- **Persons under 18** (cl 18).

Uncertainty about an exemption can be resolved by the court at any stage of the
proceedings (cl 8A).

## Remedies and procedure

- **Injunctions** may be granted at any stage, with particular regard to the
  public interest in publication where publication is involved (cl 9).
- **Summary judgment** for the defendant if the plaintiff has no reasonable
  prospect of success (cl 10).
- **Damages** (cl 11): including for emotional distress; **no aggravated
  damages**; exemplary or punitive damages only in exceptional circumstances. The
  combined non-economic and exemplary/punitive damages cap is the greater of
  **$478,550** and the maximum non-economic damages in defamation proceedings
  under an Australian law (cl 11(5)).
- **Other remedies** (cl 12): account of profits, injunction, order to apologise,
  correction order, destruction/delivery up of material, and a declaration.
- **Time limits** (cl 14): generally the earlier of 1 year after the plaintiff
  became aware and 3 years after the invasion; for a plaintiff under 18, before
  their 21st birthday. The court may extend, up to 6 years after the invasion.
- **Single publication rule** (cl 19) and **deceased persons** (cl 20):
  proceedings cannot be brought for a deceased person or against a deceased
  defendant.
- **Information Commissioner** may intervene or act as amicus (cl 22).
- **Jurisdiction**: Federal Circuit and Family Court (Div 2), the Federal Court,
  State courts and Territory courts (cl 23).

## What to check in a codebase or design

- Does the product record, watch, listen to, or locate people in private spaces,
  or collect information in ways they would not expect?
- Is invasive collection **intentional** and based on a policy or feature
  decision (raising the cl 7(1)(c) "intentional or reckless" element)?
- Are features that publish, index or expose information about individuals
  (naming, tagging, search, "people finder", scraped data) proportionate to a
  countervailing public interest?
- Are consent, corrections and takedown processes robust enough to support the
  cl 8 consent defence and cl 12 correction remedies?
- Could a feature enable doxxing, intimate-image exposure, covert recording or
  surveillance? Treat these as Critical.
