# 05.1 — Scope & Applicability | M05 Compliance Sentinel

**Hoofdstukstatus:** structuur **APPROVED**; inhoudelijk werk **PENDING** · [Terug naar M05](../../README.md)

## Doel

Vaststellen **wat** er in een casus wordt beoordeeld, **waartegen** en **waarom**, vóórdat er iets wordt getoetst. Een assessment zonder expliciete scope en toepasselijkheidsmotivatie leidt tot checklistinflatie, of tot schijnzekerheid ("we voldoen aan ISO 27001") die het bewijs niet draagt.

## Onderzoeksvragen

1. Welke systemen, netwerkgrenzen, processen en periode vallen binnen de casus, en wat valt er bewust buiten?
2. Welke stakeholders hebben belang bij de uitkomst (fictieve directie, proceseigenaar OT, CISO, beheerder, auditor), en welke belangen kunnen botsen, zoals beschikbaarheid tegenover isolatie?
3. Welke eisen zijn **wettelijk**, welke **contractueel**, welke **vrijwillig** en welke zijn alleen **onderzoeksreferentie**? Welke zijn voor een persoonlijk lab feitelijk niet van toepassing?
4. Welk framework of welke control is voor déze casus het meest passend, en welke kaders vallen af (N/A met reden)?
5. Waar ligt de **compliancegrens**: wat kan een technische test aantonen, en wat vereist een organisatorisch of juridisch oordeel dat het lab niet kan leveren?
6. Wie is verantwoordelijk voor scope, eisen en acceptatie (CAT-C en CAT-A)?

## Beoordelingsmethodiek

- **Scope-statement** opstellen: object, trust boundary, periode, uitsluitingen.
- **Stakeholder- en belangenoverzicht**, in het lab grotendeels **SIMULATED**.
- **Kaderselectie** uit het [Framework Register](../../README.md#6-framework-register), met versie, control-ID en N/A-motivatie volgens [CAT/ACE §4](../../../../Governance/CAT_ACE_v0.4.md#4-taxonomie-van-referentiekaders-niet-alles-is-een-regulatory-framework).
- **Soort eis classificeren** volgens onderstaande tabel; de juridische uitwerking blijft in [Wet- en regelgevingskaders](../../../../Governance/WET_EN_REGELGEVING.md).
- **Casusgebonden mini-SoA**: alleen de geselecteerde controls voor deze casus, met reden voor opname of uitsluiting. Geen volledige Statement of Applicability.

| Soort eis | Voorbeeld | Bindend voor Hybrid-Theory? |
|---|---|---|
| **Wettelijk** | NIS2/Cyberbeveiligingswet, DORA, AVG | **Niet vastgesteld.** Toepasselijkheid is binnen de huidige onderzoeksscope niet vastgesteld; dit vereist een afzonderlijke beoordeling afhankelijk van activiteiten, rechtspositie en gegevensverwerking. In M05-casussen alleen bruikbaar als fictieve sectorcontext, expliciet als SIMULATED gemarkeerd |
| **Contractueel** | Leveranciers- of klantafspraken, licentievoorwaarden | Alleen voor werkelijk aangegane voorwaarden (bijv. evaluatielicenties); geen fictieve contracten als bewijs |
| **Vrijwillige norm** | ISO/IEC 27001:2022, IEC 62443 | **Nee**, tenzij een organisatie zich eraan verbindt; in het lab een ontwerp- en toetslens |
| **Onderzoeksreferentie** | NIST CSF 2.0, CIS Controls, NIST SP 800-53A, COBIT, CAT/ACE | Nooit bindend; per casus geselecteerd voor een concrete onderzoeksfunctie |

## Toepasselijke frameworks

ISO/IEC 27001:2022 (hoofdstuk 4 context en scope; 6.1.3 toepasselijkheid), NIST CSF 2.0 (Organizational Profiles), COBIT 2019 (governance- versus managementdoelen), ISA/IEC 62443 (zones en conduits, alleen bij OT-verdieping), en NIS2/Cbw, DORA en AVG uitsluitend bij een expliciete fictieve sectorcontext. Geen enkel kader is automatisch verplicht voor het lab.

## Praktische context binnen Hybrid-Theory

**Voorbeeld (gepland, niet uitgevoerd) — M05-MINI-01:** de scope is de grens tussen IT/LAB en de OT-zone, met de PLC als beschermd asset en de firewall als handhavingspunt. De primaire control is ISO/IEC 27001:2022 A.8.22.

Buiten scope vallen:
- verkeer dat de zonegrens niet passeert (bijvoorbeeld procesverkeer binnen één zone), omdat het methodisch geen bewijs voor A.8.22 kan leveren;
- detectie en monitoring (M04-uitbreiding);
- herstel (M02).

NIST CSF en CIS Controls worden voor deze casus niet geselecteerd (**REFERENCE**); de actieve controlmapping is **PARKED**.

## Verwachte evidence en deliverables

- Scope-statement met trust boundary en uitsluitingen.
- Kaderselectie en N/A-register (versie, ID, reden).
- Mini-SoA uitsluitend voor de casusscope.
- Stakeholder- en rollenoverzicht, met markering SIMULATED waar van toepassing.

## Kwaliteitscriteria

- De scope is zo smal dat het beschikbare bewijs haar kan dragen.
- Iedere uitsluiting heeft een reden; "niet gekeken" is geen N/A.
- Iedere geselecteerde eis is als wettelijk, contractueel, vrijwillig of onderzoeksreferentie geclassificeerd.

## Beperkingen

- Een conclusie mag nooit breder zijn dan de scope.
- Een mini-SoA is een **onderzoeksartefact**, geen bewijs van een werkend ISMS of van ISO 27001-conformiteit.
- Toepasselijkheid van wetgeving voor een echte organisatie is een juridisch oordeel buiten dit lab.

## Relaties met andere hoofdstukken

Bepaalt de grenzen voor [05.2](../05.2_Risk_to_Control_Traceability/README.md) (welke risico's) en [05.3](../05.3_Control_Effectiveness/README.md) (welke controls). Een te brede scope ondermijnt [05.5](../05.5_Assurance_and_Independence/README.md); scopekeuzes bepalen de beoordelingskosten in [05.6](../05.6_Cost_and_Efficiency/README.md). Afhankelijkheden buiten de scope worden in [05.7](../05.7_Systemic_Risk/README.md) expliciet benoemd in plaats van genegeerd.

## Huidige onderzoeksstatus

**PENDING.** Er is nog geen scope-statement of mini-SoA opgesteld; MINI-01 is **PLANNED**.
