# 05.2 — Risk-to-Control Traceability | M05 Compliance Sentinel

**Hoofdstukstatus:** structuur **APPROVED**; inhoudelijk werk **PENDING** · [Terug naar M05](../../README.md)

## Doel

Een **herleidbare keten** maken van technische observatie naar managementbesluit, en terug:

```text
Asset → Threat → Risk → Owner → Control → Evidence → Verdict → Decision
```

Zonder die keten is een control een losse maatregel en een risicoacceptatie een losse uitspraak. De keten is **bidirectioneel**: van eis naar bewijs, en van een technische afwijking terug naar het getroffen proces, de eigenaar en de eis ([CAT/ACE §9](../../../../governance/CAT_ACE_v0.4.md#9-traceability--en-assuranceketen)).

## Onderzoeksvragen

1. Welke assets en kritieke afhankelijkheden zijn in de casus relevant, en welke (fictieve) bedrijfsfunctie leunt erop?
2. Welke dreigingen en kwetsbaarheden zijn plausibel, en op welk bewijs of welke aanname rust dat?
3. Hoe worden kans en impact beoordeeld, en zijn de schaal en aannames expliciet en herhaalbaar?
4. Wie is risico-eigenaar, wie is control-eigenaar, en wie mag restrisico accepteren?
5. Welke behandeloptie is gekozen (mitigeren, accepteren, overdragen, vermijden) en waarom?
6. Kan een technische afwijking terug worden gevolgd naar proces, eigenaar en eis, en waar breekt de keten?

## Beoordelingsmethodiek

- **Asset- en afhankelijkheidsinventaris** voor de casus, met verwijzing naar bestaande documentatie in plaats van duplicatie.
- **Dreigingsscenario's** formuleren, waar passend met MITRE ATT&CK for ICS als referentie.
- **Kans/impact-beoordeling** met een vooraf vastgelegde ordinale schaal en een aannameregister.
- **Risk treatment en risk-to-control mapping** in **één** matrix per casus.
- **Ketentoets in beide richtingen:** elke schakel krijgt een bron, en elke ontbrekende schakel wordt zichtbaar gemarkeerd.

## Toepasselijke frameworks

ISO/IEC 27005:2022 (risicoproces), ISO/IEC 27001:2022 hoofdstuk 6.1.2–6.1.3 en 8.2–8.3, COBIT 2019 APO12 (Managed Risk), NIST SP 800-30 (risk assessment), en ISA/IEC 62443-3-2 (OT-risicoanalyse per zone, alleen bij OT-verdieping).

## Praktische context binnen Hybrid-Theory

**Illustratief, gesaneerd scenario (SIMULATED context; geen uitgevoerde beoordeling):**

| Schakel | Invulling in het voorbeeld | Herkomst |
|---|---|---|
| **Asset** | Een gesimuleerde PLC die een motorproces aanstuurt, in een afgescheiden OT-zone | DOCUMENTED (architectuur) |
| **Threat** | Ongeautoriseerde netwerktoegang vanuit de IT/LAB-zone tot de PLC | HYPOTHESIS |
| **Risk** | Ongewenste procesbesturing of verstoring; kans en impact met expliciete aannames | SIMULATED (fictieve bedrijfsimpact) |
| **Owner** | Fictieve OT-proceseigenaar als risico-eigenaar; firewallbeheerder als control-eigenaar | SIMULATED |
| **Control** | ISO/IEC 27001:2022 A.8.22 — segmentatie met default deny tussen zones | DOCUMENTED (ontwerp) |
| **Evidence** | Gerichte negatieve tests met firewalllogs ([M04 fase 20](../../../M04-Network-Citadel/M04-Bewijsvoering/20_OT_segmentation_and_regression/README.md)) | OBSERVED (scoped; review PENDING) |
| **Verdict** | Scoped onderzoeksbeoordeling; in dit voorbeeld zou de integrale werking **NOT VERIFIED** blijven | — |
| **Decision** | Besluit van Sam: verder testen, corrigeren of tijdelijk accepteren | Nog niet genomen |

Werkelijke assetinventarissen en interne risicoregisters worden niet gepubliceerd; publiek staan alleen de [M04-GAPS](../../../M04-Network-Citadel/M04-GAPS.md) op hoofdlijnen.

## Verwachte evidence en deliverables

- Risicorecord(s) met asset, dreiging, kans/impact en aannames.
- Eigenaarstoewijzing (RACI), gemarkeerd als SIMULATED waar van toepassing.
- Risk-to-control-regel(s) in de casusmatrix, met link naar bewijs en besluit.
- Gemarkeerde ketenbreuken, zoals een control zonder eigenaar of een risico zonder besluit.

## Kwaliteitscriteria

- Elke schakel heeft een bron; een ontbrekende schakel wordt als gat gemarkeerd, niet aangevuld met aannames.
- Kans/impact-scores zijn ordinaal en transparant; geen schijnprecisie of samengestelde score zonder onderbouwing.
- Bestaande risico-identificatoren worden hergebruikt, niet hernummerd.

## Beperkingen

- Correlatie is geen causaliteit: een plausibel dreigingspad is geen aangetoond aanvalspad.
- Eigenaarschap en bedrijfsimpact zijn in het lab gesimuleerd; een gesimuleerd besluit is geen werkelijke bevoegdheid.
- De publieke versie toont een gesaneerd voorbeeld; de onderliggende interne mapping is niet onafhankelijk verifieerbaar.

## Relaties met andere hoofdstukken

Bouwt op de scope uit [05.1](../05.1_Scope_and_Applicability/README.md) en levert de controls die [05.3](../05.3_Control_Effectiveness/README.md) toetst. Onbehandelde of geaccepteerde risico's gaan naar [05.4](../05.4_Gaps_and_Exceptions/README.md). Afhankelijkheden in de keten zijn input voor [05.7](../05.7_Systemic_Risk/README.md).

## Huidige onderzoeksstatus

**PENDING.** Er is nog geen M05-risk-to-control-matrix opgesteld.
