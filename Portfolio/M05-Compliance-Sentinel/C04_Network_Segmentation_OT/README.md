# C04 · OT-netwerksegmentatie

Welke uitspraak over de gekozen OT-grens dragen het ontwerp, de testbron en de waarnemingen?

Leg bij elke technische uitslag de bronmissie, datum, testbron, toegestane richting en bewijsgrens vast. Richt een aanvullende technische proef aan de eigenaar van M04.

**Mini-oefeningen**

- [M05-MINI-01 · A.8.22 Risk-to-Control](../README.md#idx-m05-mini-01)
- [M05-MINI-09 · Zones and Conduits](../README.md#idx-m05-mini-09)

**C10-overdracht:** Documenteer bij een uitgevoerde mini herleidbare claim- en bronverwijzingen volgens het [C01–C09 → C10-overdrachtscontract](../C10_CAT_ACE/README.md#overdrachtscontract-c01c09--c10-ontwerpafspraak). De bronmissie behoudt evidence, technische verdicts en eigenaarbesluiten; C10 beoordeelt uitsluitend de methodiekclaims. Een geplande mini levert nog geen overdrachtsrecord op.

**Werkwijze en bronnen**

Elke mini behandelt [de zeven permanente onderzoekshoofdstukken 05.1–05.7](../Methodiek/). Leg per vraag het bewijs, het ontbrekende bewijs of de reden voor N/A vast.

ISO/IEC 27001:2022 Annex A.8.22 voor de eerste casus. IEC 62443-3-2:2020 kan een afgebakende zones-en-conduitsvraag helpen beantwoorden. Kaderbronnen: **NOT VERIFIED voor README-gebruik** tot verificatie van editie en casustoepassing. De casuskeuze, versie en rol staan in het [Framework Register](../README.md#6-framework-register).

[M04-dossier](../../M04-Network-Citadel/README.md) · [M04-bewijsgrenzen](../../M04-Network-Citadel/M04-GAPS.md) · [Gesaneerde M04-testmatrix](../../M04-Network-Citadel/M04-AC04-AC07-TESTMATRIX.csv) · [Netwerkontwerp](../../../architectuur/NETWERKONTWERP.md).

## Technische bronstand van 21 november 2026

M04 rapporteert een geslaagde, afgebakende blokkade aan de geteste netwerkgrens. M04-CORE is **IN PROGRESS**. De integrale acceptatie van AC04/AC07 is **PENDING**. M05 gebruikt de gepubliceerde bewijsgrens als vertrekpunt voor de eerste casus. [M04-bronstand](../../M04-Network-Citadel/M04-GAPS.md).

De technische missie beheert het bewijs en de testuitslagen. M05 documenteert bron, datum, reikwijdte en begrenzing van de interpretatie.

> **Historische bronpassage** · peilcommit `98bd282`, oorspronkelijk pad `Portfolio/M05-Compliance-Sentinel/M04-Network-Citadel/README.md`. [Permalink](https://github.com/SamAsgar/Hybrid-Theory-Public/blob/98bd28252b2adde6a2c129b1d9d3d12641e4fa2d/Portfolio/M05-Compliance-Sentinel/M04-Network-Citadel/README.md). De onderstaande passage bewaart de toenmalige status. De [mini-index](../README.md#mini-exercise-index) bevat de actuele werkstatus.

<!-- BEGIN HISTORISCHE BRON -->

# M04 — Network Citadel | M05-assessmentdossier

**Status:** **IN PROGRESS** — kennistraining afgerond; assessment en eigenaarreview open · [Terug naar M05](../README.md)

Dit dossier bevat uitsluitend M05-assessments over controls, risico's en bewijs van M04 Network Citadel. De methodiek staat één keer in [Methodiek](../Methodiek/) en wordt hier niet herhaald. Bewijs en technische verdicts blijven in de missie zelf ([M04-missiedocumentatie](../../M04-Network-Citadel/README.md)); M05 verwijst daarnaar, kopieert geen bewijs en wijzigt geen verdicts.

| Onderdeel | Methodiek | Assessment voor M04 | Status |
|---|---|---|---|
| 05.1 | [Scope & Applicability](../Methodiek/05.1_Scope_and_Applicability/README.md) | Didactisch behandeld; assessmentreview open | **IN PROGRESS** |
| 05.2 | [Risk-to-Control Traceability](../Methodiek/05.2_Risk_to_Control_Traceability/README.md) | Didactisch behandeld; assessmentreview open | **IN PROGRESS** |
| 05.3 | [Control Effectiveness](../Methodiek/05.3_Control_Effectiveness/README.md) | Didactisch behandeld; assessmentreview open | **IN PROGRESS** |
| 05.4 | [Gaps & Exceptions](../Methodiek/05.4_Gaps_and_Exceptions/README.md) | Didactisch behandeld; assessmentreview open | **IN PROGRESS** |
| 05.5 | [Assurance & Independence](../Methodiek/05.5_Assurance_and_Independence/README.md) | Didactisch behandeld; assessmentreview open | **IN PROGRESS** |
| 05.6 | [Cost & Efficiency](../Methodiek/05.6_Cost_and_Efficiency/README.md) | Onderdeel van M05-MINI-01 (gepland) | **PLANNED** |
| 05.7 | [Systemic Risk](../Methodiek/05.7_Systemic_Risk/README.md) | Onderdeel van M05-MINI-01 (gepland) | **PLANNED** |

Een submap per assessment wordt pas aangemaakt wanneer het assessment daadwerkelijk start. Uitkomsten zijn scoped onderzoeksbeoordelingen (INTERNAL / AI-ondersteund) en geen milestone-acceptatie.

<a id="m05-mini-01"></a>
## M05-MINI-01 — ISO 27001 Risk-to-Control Assessment (EERSTE CASUS IN UITVOERING)

**Status:** **PLANNED / niet gestart.** Een afzonderlijk uitvoeringsdossier wordt pas aangemaakt wanneer de oefening daadwerkelijk start.

| Element | Invulling |
|---|---|
| **Casus** | De bestaande IT/OT-segmentatie uit M04 Network Citadel |
| **Onderzoeksobject** | De firewall (pfSense), de IT/LAB-netwerkgrens, de OT-zone met de PLC en het bestaande, gesaneerde M04-bewijs |
| **Primaire control** | ISO/IEC 27001:2022 Annex A **A.8.22 — Segregation of networks** (A.8.20/8.21 alleen waar werkelijk relevant) |
| **Onderzoeksvragen** | Welke risico's behandelt segmentatie? Wat is het controlontwerp? Wat is geïmplementeerd? Welke werking is aantoonbaar getest? Wat is nog niet bewezen? Wie accepteert restrisico's? Welke afhankelijkheden kunnen tot grotere verstoringen leiden? Wat betekent dit voor kosten, efficiëntie en assurance? |
| **Uitvoeringsgrens** | Steunt uitsluitend op **bestaand** bewijs; gebruikt **geen** veronderstelde nieuwe testresultaten; **geen** live configuratiewijziging. M04 blijft **IN PROGRESS** en de integrale AC04/AC07-acceptatie is **niet** behaald. Ontbrekende tests worden niet in MINI-01 uitgevoerd maar blijven bij M04. |
| **Verdictlabel** | Scoped onderzoeksbeoordeling (PASS / REWORK / EXCEPTION / N/A / NOT VERIFIED), uitgevoerd als **INTERNAL / AI-ONDERSTEUND (SELF-ASSESSMENT)** — niet onafhankelijk |
| **Reviewpunten verwerkt** | Eén regel per hoofdstuk 05.1–05.7 en een scheiding tussen OBSERVED en AI-INTERPRETED bewijs |

### Traceabilitymatrix MINI-01 × zeven hoofdstukken

Eén matrix verbindt de casus met alle zeven hoofdstukken. De kolom "Wat publiek bewijs nu toont" vat **bestaande, scoped** M04-uitkomsten samen; het is **geen** nieuwe beoordeling en geen M05-verdict.

| Hfd. | MINI-01-vraag | Publieke bron | Wat publiek bewijs nu toont | Wat (nog) niet bewezen is | Geplande MINI-01-output |
|---|---|---|---|---|---|
| **05.1** | Welke eisen gelden voor de IT/LAB↔OT-grens en waarom A.8.22? | [Netwerkontwerp](../../../architectuur/NETWERKONTWERP.md), [Wet- en regelgevingskaders](../../../governance/WET_EN_REGELGEVING.md) | Een zonemodel met de OT-zone achter de firewall is ontworpen (**DOCUMENTED**) | Een formeel goedgekeurde allow/deny-policy per zone als ontwerpdocument | Scope-statement, kaderselectie met N/A, mini-SoA (alleen casus) |
| **05.2** | Welk risico behandelt segmentatie, wie is eigenaar, welke behandeling? | [M04-GAPS](../../M04-Network-Citadel/M04-GAPS.md), [Issue #45](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/45) | Open punten en risicoreviews zijn op hoofdlijnen gedocumenteerd | Expliciete (gesimuleerde) risico-eigenaar en behandelbesluit | Eén risicorecord met kans/impact-aannames en behandelvoorstel |
| **05.3** | Ontwerp, implementatie, werking van de segmentatie? | [M04 fase 20](../../M04-Network-Citadel/M04-Bewijsvoering/20_OT_segmentation_and_regression/README.md), [M04-GAPS §19 nov.](../../M04-Network-Citadel/M04-GAPS.md#aanvulling-19-november--gerichte-deeltests) | Gerichte LAB→PLC- en LAB→HMI-flows werden geweigerd, met firewall-BLOCK-events (**scoped**, evidence-review PENDING) | Integrale AC04/AC07-acceptatie (zie de publieke [M04-GAPS](../../M04-Network-Citadel/M04-GAPS.md)) | Apart oordeel ontwerp/implementatie/werking + bewijskwaliteit per bron |
| **05.4** | Welke gaps, uitzonderingen en restrisico's zijn er? | [M04-GAPS](../../M04-Network-Citadel/M04-GAPS.md) | Gaps zijn geregistreerd; een integrale acceptatie ontbreekt | Ownerbesluit per gap: corrigeren, tijdelijk accepteren (EXCEPTION) of verder onderzoeken | Gap-/uitzonderingsregister voor de casus met hertestvoorwaarde |
| **05.5** | Wat mag over deze control worden geclaimd, en door wie? | [AI-werkafspraken](../../../governance/AI_WERKAFSPRAKEN.md), [Statuslegenda §7](../../../governance/STATUSLEGENDA.md#7-bewijsdiscipline) | M04-tests zijn deels met AI-begeleiding ontworpen en geduid | Onafhankelijke review; welk bewijs door Sam zelf is waargenomen | Assurance-statement met onafhankelijkheids- en AI-grenzen |
| **05.6** | Wat kost deze beheersing en de beoordeling ervan? | — (alleen interne planningsramingen) | Er bestaan alleen geschatte planningsuren (**ESTIMATED**) | Gemeten beoordelingsinspanning (MEASURED) | Tijdregistratie MINI-01 + ACE-kosten/efficiëntieregel |
| **05.7** | Welke afhankelijkheden maken dat één fout meerdere controls raakt? | [05.7 Systemic Risk](../Methodiek/05.7_Systemic_Risk/README.md) (methodiek) | Geen publieke dependency-analyse; de methodiek en een fictief voorbeeld zijn beschreven | Elke afhankelijkheid van de casus (de analyse blijft intern) | Interne dependencyregel(s) met bewijsniveau; publiek alleen een gesaneerde samenvatting na review |

<!-- EINDE HISTORISCHE BRON -->


## Leerresultaat 24 november 2026

[MINI-01 · dossier en educatieve PDF](M05-MINI-01_ISO27001_Control_Assessment/README.md). Vijf leerfasen afgerond; 05.6/05.7 en formele beoordeling blijven PENDING. Historische traceabilitymatrix hierboven blijft een gedateerde bron; technische verdicts blijven bij M04.
