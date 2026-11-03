# AI-werkafspraken | Publieke samenvatting

**Status:** operationele, risicogestuurde engineeringafspraken. De Project Owner beslist over scope, rechten, kosten, risicovolle wijzigingen en acceptatie. Deze samenvatting bevat geen private overlegverwijzingen.

## 1. Doelgericht, proportioneel en veilig

HT-011 Flexible Security / Mission-Based Hardening: tijdens preflight uitsluitend noodzakelijke controls voor veilige werking, oplossing van een concrete blokkade of voorkoming van een onaanvaardbaar risico. Uitgebreide hardening en aanvullende controlematrices horen bij het relevante lab.

Deze aanpak schrapt **nooit** toestemmingseisen, bescherming van secrets, lab-vs-overige-netwerken-grenzen, financiële autorisatie of een passende herstelroute bij ingrijpende wijzigingen.

## 2. Geen overbodige dubbele controles

Bestaande, valide PASS-tests worden hergebruikt zolang configuratie en scope ongewijzigd zijn. Bij nieuwe foutindicatie, gewijzigde trust boundary of nieuwe vereiste herhalen we een gerichte test.

## 3. Werkwijze in het lab

- Maximaal drie concrete uitvoerstappen per begeleidingsronde.
- Eén wijziging tegelijk wanneer dit de diagnose beter toetsbaar maakt.
- Symptoom, hypothese, onderscheidende test, bewijs, herstel en verdict vastleggen.
- **PASS** = acceptatiecriteria gehaald binnen specifieke scope.
- **REWORK** = concrete fout, ontbrekend essentieel bewijs of risico.
- **EXCEPTION** = bewuste en vastgelegde risicoacceptatie door Project Owner.

## 4. AI Collaboration

Sam: **Project Owner & Lead Architect (mens)**. ChatGPT: **Engineering Orchestrator (AI)**. Claude: **Critical Security Auditor & Chaos Engineer (AI)**. Microsoft Copilot: **Microsoft Specialist & Automation Engineer (AI)**. GitHub Copilot: **Coding & Automation Assistant (AI)**. De rollen zijn ondersteunend; Sam beslist over scope en risicoacceptatie. Een gerichte tweede AI-beoordeling is geen formele onafhankelijke audit.

## 5. Technische scope en publicatie

- Geen ongeautoriseerde toegang tot andermans systemen of het privé-thuisnetwerk.
- Geen secrets, werkelijke infrastructuuridentificatoren, privébestandspaden of ruwe interne chatgeschiedenis in publieke voorbeelden.
- Geen ongeteste claim over domeinredundantie, netwerkisolatie, backup/restore, Azure-resources of wettelijke compliance.
- Archivering van historische observaties verandert hun oorspronkelijke testverdict niet.

**Onderzoek:** [CAT/ACE v0.4](CAT_ACE_v0.4.md) is een experimentele **interne, externe of hybride Audit / Cost / Efficiency-beoordeling**, met toetsbaar bewijs, risicogebonden kostenafweging en **Revalidation** na wijzigingen. Dit vervangt **Risk-Based Validation** voor operationele engineering niet automatisch. Een AI-review is geen formele onafhankelijke audit. Zie [statuslegenda](STATUSLEGENDA.md).

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
