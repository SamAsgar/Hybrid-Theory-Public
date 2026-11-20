# 05.4 — Gaps & Exceptions | M05 Compliance Sentinel

**Hoofdstukstatus:** structuur **APPROVED**; inhoudelijk werk **PENDING** · [Terug naar M05](../../README.md)

## Doel

Afwijkingen **transparant en beslisbaar** maken. Welk verschil bestaat er tussen eis en werkelijkheid, hoe ernstig is het, wie beslist erover, wat is de corrigerende actie en wanneer wordt opnieuw getest? Een uitzondering is een bewust besluit met eigenaar en looptijd, geen stilzwijgende PASS.

## Begrippen

| Begrip | Betekenis in M05 |
|---|---|
| **Gap identification** | Een aantoonbaar verschil vaststellen tussen een gekozen eis en de aangetoonde situatie, met type ([CAT/ACE §7](../../../../governance/CAT_ACE_v0.4.md#7-typen-gap-analyses-welke-vraag-wordt-onderzocht)) en ernst |
| **Nonconformity** | De eis is aantoonbaar **niet** gehaald |
| **Evidence gap** | Er is onvoldoende bewijs om te beoordelen of de eis is gehaald (**NOT VERIFIED**); geen aanname van een defect |
| **Exception** | Een bewust, door Sam vastgelegd besluit om een afwijking tijdelijk toe te staan, met reden, voorwaarden en vervaldatum (**EXCEPTION**, geen PASS) |
| **Residual risk** | Het risico dat na behandeling overblijft |
| **Risk acceptance** | Het expliciete besluit van de bevoegde eigenaar om het restrisico te dragen |
| **Corrective action** | De maatregel die de oorzaak van een nonconformity wegneemt, met eigenaar en termijn |
| **Retesting** | Een gerichte hertest die aantoont dat de corrigerende actie werkt, zonder eerdere uitkomsten te herschrijven |

## Onderzoeksvragen

1. Welke gaps bestaan er tussen de gekozen eis of control en de aangetoonde situatie, en welk type gap is het?
2. Is een afwijking een nonconformity of alleen een evidence gap?
3. Welke uitzonderingen zijn bewust toegestaan, door wie, onder welke voorwaarden en tot wanneer?
4. Welk restrisico blijft over, en wie heeft het geaccepteerd?
5. Welke corrigerende actie is gepland, en welke hertest bewijst dat ze werkt?
6. Welke afwijkingen staan al te lang open?

## Beoordelingsmethodiek

- Een **GAP assessment** per casus, met type en ernst.
- Nonconformities expliciet onderscheiden van evidence gaps.
- Uitzonderingen vastleggen met eigenaar, reden, voorwaarden en vervaldatum.
- Risicoacceptatie alleen via een expliciet, gedateerd besluit van Sam.
- Corrigerende acties koppelen aan de missie die de control bezit; hertests lopen via de planning van die missie.

## Toepasselijke frameworks

ISO/IEC 27001:2022 hoofdstuk 10.2 (nonconformity and corrective action) en 6.1.3 (risk treatment plan; acceptatie van restrisico door risico-eigenaren), ISO/IEC 27005:2022 (risk acceptance), COBIT 2019 APO12/MEA02, en ISO 19011:2026 (classificatie van auditbevindingen; alleen bij auditvragen).

## Praktische context binnen Hybrid-Theory

Voorbeelden die het onderscheid illustreren, uitsluitend op basis van publiek gedocumenteerde situaties:

- **Vastgelegde EXCEPTION:** in M01 is één host-guest-integratie op geselecteerde Windows-VM's bewust als EXCEPTION geaccepteerd ([M01-dossier](../../../M01-Hypervisor-Fortress/README.md)). Dit is een voorbeeld van een uitzondering met eigenaar en scope, en uitdrukkelijk geen PASS.
- **Evidence gap versus nonconformity:** de integrale AC04/AC07-matrix van M04 is **PENDING** ([M04-GAPS](../../../M04-Network-Citadel/M04-GAPS.md)). Zolang tests ontbreken, is dat een evidence gap (NOT VERIFIED), geen bewezen tekortkoming.
- **Open risicoreview:** waar publieke M04-documentatie een regel of configuratie als "open risk review" markeert, is dat een kandidaat voor een expliciet ownerbesluit: corrigeren, tijdelijk accepteren of verder onderzoeken.

Actuele, nog niet opgeloste technische zwaktes en de interne risicoregistratie worden niet gepubliceerd.

## Verwachte evidence en deliverables

- Een casusgebonden gap- en uitzonderingsregister, als onderdeel van de ene casusmatrix en niet als los register per hoofdstuk.
- Per item: type, ernst, eigenaar, besluit (corrigeren / accepteren / onderzoeken), hertestvoorwaarde en vervaldatum.
- Een verwijzing naar de bestaande registratie van het item, zonder hernummering.

## Kwaliteitscriteria

- Zonder besluit van Sam bestaat er geen uitzondering.
- Elk item heeft een eigenaar en een hertestvoorwaarde.
- Een gesloten item verwijst naar de hertest die het sluit.

## Beperkingen

- **EXCEPTION is geen PASS** ([Statuslegenda §2](../../../../governance/STATUSLEGENDA.md#2-engineeringverdict-altijd-met-scope)).
- M05 sluit geen M01–M04-risico's; het doet voorstellen aan de eigenaar.
- Restrisico-acceptatie in het lab is een labbesluit, geen juridische acceptatie namens een organisatie.
- De publieke versie toont alleen gesaneerde voorbeelden; de volledige interne registratie is niet publiek.

## Relaties met andere hoofdstukken

Ontvangt tekortkomingen uit [05.3](../05.3_Control_Effectiveness/README.md) en onbehandelde risico's uit [05.2](../05.2_Risk_to_Control_Traceability/README.md). De betrouwbaarheid van het gapoordeel valt onder [05.5](../05.5_Assurance_and_Independence/README.md); de kosten van herstel tegenover acceptatie onder [05.6](../05.6_Cost_and_Efficiency/README.md). Gaps in gedeelde componenten wegen zwaarder via [05.7](../05.7_Systemic_Risk/README.md).

## Huidige onderzoeksstatus

**PENDING.** Er is nog geen M05-gapbeoordeling uitgevoerd.
