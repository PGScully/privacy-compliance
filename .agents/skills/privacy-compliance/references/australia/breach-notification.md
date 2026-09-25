# Notifiable data breaches (Part IIIC)

A scheme for notifying **eligible data breaches**. Read it whenever you find
unauthorised access, unauthorised disclosure or loss of personal information, or
when reviewing incident-response runbooks and alerting.

## What an eligible data breach is (s 26WE)

An eligible data breach occurs if the entity holds personal information (or
credit reporting / credit eligibility / tax file number information) that it is
required to protect under s 15 (APP 11.1) and either:

- there is **unauthorised access to, or unauthorised disclosure of, the
  information**, and a reasonable person would conclude the access or disclosure
  would be likely to result in **serious harm** to any individual to whom the
  information relates (s 26WE(2)(a)); or
- the information is **lost** in circumstances where unauthorised access or
  disclosure is likely to occur and, if it did, a reasonable person would
  conclude it would be likely to result in serious harm (s 26WE(2)(b)).

An individual who may be harmed is **at risk** from the breach (s 26WE(2)(d)).

## Relevant matters for "serious harm" (s 26WG)

The kinds of information; the sensitivity of the information; whether it is
protected by security measures and how likely those are to be overcome; who has
or could obtain it; whether security technology (e.g. encryption) was used and
whether the actor could circumvent it; the nature of the harm; and any other
relevant matters.

## Remedial action exception (s 26WF)

If the entity takes action before the access or disclosure results in serious
harm, and as a result a reasonable person would conclude serious harm is no
longer likely, the access or disclosure is **not** (and is taken never to have
been) an eligible data breach. Similar exceptions apply to loss before or after
unauthorised access/disclosure (s 26WF(3)–(5)). Remedies must be genuine and
effective — the exception is not a way to avoid reporting.

## Other exceptions

- **My Health Records Act 2012** — if the access, disclosure or loss has been or
  must be notified under s 75 of that Act, Part IIIC does not apply (s 26WD).
- **Overseas recipients** — information disclosed under APP 8.1 and held by an
  overseas recipient is treated as held by the disclosing APP entity
  (s 26WC(1)); the entity is treated as required not to breach APP 11.1.

## Obligations and timeframes

### Suspected breach — assessment (s 26WH)

If the entity is aware of **reasonable grounds to suspect** an eligible data
breach but not reasonable grounds to believe one has occurred, it must carry out
a **reasonable and expeditious assessment** and take all reasonable steps to
complete it **within 30 days** of becoming aware (s 26WH(2)).

### Statement to the Commissioner (s 26WK)

If the entity is aware of **reasonable grounds to believe** there has been an
eligible data breach, it must, as soon as practicable, prepare a statement and
give a copy to the Commissioner. The statement must set out (s 26WK(3)):
- the identity and contact details of the entity;
- a description of the eligible data breach;
- the kind or kinds of information concerned;
- recommendations about steps individuals should take.

It may also identify other affected entities (s 26WK(4)).

### Notification to individuals (s 26WL)

The entity must take reasonable steps to notify the contents of the statement:
- to **each individual** to whom the information relates, if practicable
  (s 26WL(2)(a)); or
- to **each individual at risk** from the breach, if that is what is practicable
  (s 26WL(2)(b)); or
- if neither is practicable, **publish** the statement on the entity's website and
  take reasonable steps to publicise it (s 26WL(2)(c)).

Notification must occur as soon as practicable after the statement is prepared
(s 26WL(3)) and may use the method normally used to communicate with the
individual (s 26WL(4)).

### Other entities

An entity that complies with s 26WH, or ss 26WK and 26WL, need not duplicate the
same notification for the same access, disclosure or loss that is also a breach
of other entities (ss 26WJ, 26WM).

## Consequences and review signals

- Contravening s 26WH(2), 26WK(2), 26WL(3) or s 26WR(10) is **taken to be an
  interference with privacy** (s 13(4A)).
- The Commissioner may obtain information or documents about actual or suspected
  eligible data breaches (Part IIIC Div 4) and may direct notification.

## What to check in a codebase or design

- Are unauthorised access, disclosure and loss detected and alerted on?
- Is there a documented assessment path with a **30-day** clock and an owner?
- Can the system produce the s 26WK(3) statement contents quickly (what data,
  whose data, contact details, recommendations)?
- Is there a mechanism to identify and contact **at-risk individuals**, and a
  fallback to website publication?
- Does the runbook distinguish **suspected** (assess) from **believed**
  (notify)?
- Are security measures (encryption, key management) adequate, given s 26WG
  treats weak or circumventable protections as increasing serious-harm risk?
