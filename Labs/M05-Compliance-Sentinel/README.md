# M05 — Compliance Sentinel | Regulatory Assessment & Security Assurance

**Repository:** Hybrid-Theory-Public · **Publicatievorm:** gesaneerde onderzoeks- en methodiekdocumentatie  
**Missietype:** **Permanente Main Mission** (geen definitieve afsluitstatus)  
**Peildatum:** 21 november 2026 · **Eerder besluit:** missionmodel en M05-structuur goedgekeurd door Sam op 20-11-2026 (besluit [PUB-DEC-001](../../Governance/BESLUITENLOG.md#pub-dec-001--20-11-2026--permanent-missionmodel-en-m05-structuur))

| Statusdimensie | Stand 21-11-2026 |
|---|---|
| Chapterstructuur C01–C10 en mini-index | **OWNER APPROVED** ([PUB-DEC-002](../../Governance/BESLUITENLOG.md#pub-dec-002)) |
| Structuur van deze documentatie | **APPROVED** (structuur en frameworkbenadering) |
| Hoofdstukken 05.1–05.7 | Ingericht; inhoud is methodiek en planning |
| M05-technische uitvoering | **PENDING** — geen afgerond formeel M05-assessment; educatieve casus gestart |
| M05-MS01 — Foundational Security Assurance | **NOT ACHIEVED**; exitcriteria zijn een voorstel (**DRAFT**) |
| M05-MINI-01 — ISO 27001 Risk-to-Control Assessment | **IN PROGRESS**; vijfdelige kennistraining afgerond (5/5); controlassessment IN PROGRESS, eigenaarreview PENDING |
| Compliance-, audit- of assuranceverklaring | **NOT ESTABLISHED** — en binnen dit lab ook niet het doel |

> **Documentatie is geen assessment.** Niets op deze pagina of in de hoofdstukken is een audit-, compliance- of certificeringsuitspraak. Voorbeelden zijn illustraties, geen uitgevoerde tests. Hybrid-Theory is **niet** ISO/IEC 27001-gecertificeerd en claimt geen conformiteit met welk kader dan ook.

---

## 1. Mission overview

M05 Compliance Sentinel onderzoekt **hoe technische beveiligingsbevindingen, risico's, organisatorische verantwoordelijkheden, toepasselijke frameworks en controleerbaar bewijs worden vertaald naar betrouwbare assurance-uitspraken** — en waar die vertaling faalt.

M05 verzorgt risicogestuurd assurance-onderzoek naar geselecteerde beveiligingsmaatregelen, afhankelijkheden en bewijsvoering uit M01–M04. De verantwoordelijkheid voor technische implementatie en testuitvoering blijft bij de betreffende Main Mission en bij Sam als Project Owner. M05 bouwt geen eigen infrastructuur en staat niet hiërarchisch boven de andere permanente Main Missions; het is een aanvullend onderzoeksdomein met een expliciete assurancefunctie.

De missie onderzoekt nadrukkelijk ook de **beperkingen** van compliance, auditmethoden, governance en technische controls. M05 is **niet beperkt tot ISO/IEC 27001**; ISO 27001 Annex A is alleen het primaire startkader voor de eerste mini-oefening.

## 2. Onderzoeksmotief

Techniek kan correct werken terwijl een organisatie niet kan uitleggen welke risico's zijn afgedekt, wie verantwoordelijk is en welk bewijs de conclusie draagt. Het omgekeerde komt ook voor: een volledig ingevulde checklist, met daarachter een control die in werkelijkheid niets tegenhoudt.

Tussen "er staat een firewallregel" en "het risico is aantoonbaar beheerst en de eigenaar heeft het restrisico geaccepteerd" liggen meerdere stappen: ontwerp, implementatie, werking, bewijskwaliteit, eigenaarschap, uitzonderingen en afhankelijkheden. M05 maakt die stappen expliciet.

**Centrale onderzoeksvraag:**

> Hoe maken we de stap van een technische observatie naar een controleerbare uitspraak over risico, verantwoordelijkheid, werking en eventuele resterende afwijkingen, zonder compliance te verwarren met bewezen veiligheid?

Controlgerichte assessments beoordelen maatregelen vaak één voor één. M05 onderzoekt daarnaast wat er gebeurt als meerdere controls van dezelfde component afhangen ([05.7 Systemic Risk](Methodiek/05.7_Systemic_Risk/README.md)). De [academische achtergrond](../../Onderzoek/Academische-Referenties/README.md) over systemisch risico en spillover is daarbij een **inspiratiebron, geen gevalideerde methode**.

## 3. Permanente mission lifecycle

Hybrid-Theory heeft vijf **permanente Main Missions**: M01 Hypervisor Fortress, M02 Phoenix Recovery, M03 Identity Dominion, M04 Network Citadel en M05 Compliance Sentinel.

- Een Main Mission krijgt **geen** definitieve afsluitstatus (geen `MISSION COMPLETE`, geen missie-PASS). Ontwikkeling, revalidatie en verbetering zijn continu.
- Voortgang wordt gemeten via **opeenvolgende milestones**. Een milestone heeft een expliciete scope, vooraf vastgestelde acceptatiecriteria, bewijs, een beoordeling en **expliciete acceptatie door Sam**.
- **Geen van de vijf Main Missions heeft Milestone 01 bereikt** (stand 20-11-2026).
- Een geslaagde technische deeltest is een **scoped technische bevinding**, geen milestone-acceptatie.

De statusbegrippen staan in de [Statuslegenda §3a](../../Governance/STATUSLEGENDA.md#3a-missie--milestone--en-mini-oefeningstatus-20-11-2026).

## 4. Main Mission, milestone en mini-oefening

| Niveau | Voorbeeld | Kenmerk | Kan "af" zijn? |
|---|---|---|---|
| **Main Mission** | M05 Compliance Sentinel | Permanent onderzoeks- en verbeterdomein | **Nee** |
| **Milestone** | M05-MS01 Foundational Security Assurance | Afgebakend doel, vooraf vastgestelde exitcriteria, owneracceptatie | Ja: **ACHIEVED** alleen na acceptatie door Sam |
| **Mini-oefening** | M05-MINI-01 ISO 27001 Risk-to-Control Assessment | Klein werkpakket binnen een missie; levert bewijs en ervaring voor een milestone | Ja, met een **scoped verdict**; sluit geen milestone of missie af |
| **Afgebakende zelfstandige missie** | (nog niet gedefinieerd) | Latere, aparte categorie ná de vijf Main Missions, met eigen begin- en eindcriteria | Ja — identificatieschema nog een ownerbesluit |

**Een MINI-PASS is geen milestone-PASS.** Een milestone-acceptatie is geen missie-afsluiting.

<a name="5-de-zeven-officiële-onderzoekshoofdstukken"></a>
<a name="methodiek-m05"></a>

## 5. De zeven permanente onderzoekshoofdstukken (methodiek)

De naam chapter is voorbehouden aan C01–C10. Onderzoekshoofdstukken 05.1–05.7 vormen de permanente methodiek volgens het besluit van 20 november. Elke mini gebruikt alle zeven vragen uit de canonieke methodiek. Een gemotiveerde N/A of ontbrekende waarneming blijft bij de betreffende vraag zichtbaar.

| # | Methodiek | Kernvraag |
|---|---|---|
| 05.1 | [Scope & Applicability](Methodiek/05.1_Scope_and_Applicability/README.md) | Welke eisen en kaders zijn voor deze casus van toepassing, voor wie, en waarom? |
| 05.2 | [Risk-to-Control Traceability](Methodiek/05.2_Risk_to_Control_Traceability/README.md) | Is de keten asset → dreiging → risico → eigenaar → control → bewijs → besluit herleidbaar? |
| 05.3 | [Control Effectiveness](Methodiek/05.3_Control_Effectiveness/README.md) | Is de control goed ontworpen, aantoonbaar geïmplementeerd én werkend? |
| 05.4 | [Gaps & Exceptions](Methodiek/05.4_Gaps_and_Exceptions/README.md) | Welke afwijkingen, uitzonderingen en restrisico's bestaan er, en wie draagt ze? |
| 05.5 | [Assurance & Independence](Methodiek/05.5_Assurance_and_Independence/README.md) | Wat mag een interne, externe, hybride of AI-ondersteunde review wél en níét claimen? |
| 05.6 | [Cost & Efficiency](Methodiek/05.6_Cost_and_Efficiency/README.md) | Wat kost beheersing en beoordeling, en bestaat er een even veilig, goedkoper alternatief? |
| 05.7 | [Systemic Risk](Methodiek/05.7_Systemic_Risk/README.md) | Welke gedeelde afhankelijkheden laten één falende component meerdere controls tegelijk raken? |

**Navigatie:** [05.1](Methodiek/05.1_Scope_and_Applicability/README.md) · [05.2](Methodiek/05.2_Risk_to_Control_Traceability/README.md) · [05.3](Methodiek/05.3_Control_Effectiveness/README.md) · [05.4](Methodiek/05.4_Gaps_and_Exceptions/README.md) · [05.5](Methodiek/05.5_Assurance_and_Independence/README.md) · [05.6](Methodiek/05.6_Cost_and_Efficiency/README.md) · [05.7](Methodiek/05.7_Systemic_Risk/README.md) · [CAT/ACE v0.4](../../Governance/CAT_ACE_v0.4.md) · [Wet- en regelgevingskaders](../../Governance/WET_EN_REGELGEVING.md) · [Statuslegenda](../../Governance/STATUSLEGENDA.md) · [M04-dossier (eerste casus)](../M04-Network-Citadel/README.md) · [Roadmap](../../Projectlogboeken/ROADMAP.md)

### Mapstructuur

```text
M05-Compliance-Sentinel/
├── Methodiek/
├── C01_Governance_Scope_ISMS/
├── C02_Risk_Management/
├── C03_Identity_and_Access/
├── C04_Network_Segmentation_OT/
├── C05_Logging_Detection_Incident/
├── C06_Backup_Recovery_Continuity/
├── C07_Hardening_Config_Change/
├── C08_Suppliers_Cloud_Third_Parties/
├── C09_Privacy_Publication/
└── C10_CAT_ACE/
```

### Inhoudelijke chapters

| Chapter | Onderzoeksvraag |
|---|---|
| [C01 · Governance, scope en ISMS](C01_Governance_Scope_ISMS/README.md) | Voor welke organisatie, activiteit en periode geldt een eis, wie beslist over uitzonderingen en hoe hangen de ISMS-eisen samen? |
| [C02 · Risicomanagement](C02_Risk_Management/README.md) | Is één geregistreerd risico te volgen tot eigenaar, behandeling, besluit en herbeoordeling? |
| [C03 · Identiteit en toegang](C03_Identity_and_Access/README.md) | Welke toegang is toegekend, welke toegang is nodig en wie heeft het verschil beoordeeld? |
| [C04 · OT-netwerksegmentatie](C04_Network_Segmentation_OT/README.md) | Welke uitspraak over de gekozen OT-grens dragen het ontwerp, de testbron en de waarnemingen? |
| [C05 · Logging, detectie en incidenten](C05_Logging_Detection_Incident/README.md) | Zijn een detectie en het daaropvolgende meldbesluit met betrouwbare tijdstippen te reconstrueren? |
| [C06 · Back-up, herstel en continuïteit](C06_Backup_Recovery_Continuity/README.md) | Welke herstelclaim draagt een gedocumenteerde herstelproef? |
| [C07 · Hardening en configuratiewijzigingen](C07_Hardening_Config_Change/README.md) | Hoe verhoudt de waargenomen configuratie zich tot de gekozen baseline? |
| [C08 · Leveranciers, cloud en ICT-derden](C08_Suppliers_Cloud_Third_Parties/README.md) | Welke externe ICT-diensten en contractuele relaties vallen binnen de afgebakende inventaris? |
| [C09 · Privacy en publicatie](C09_Privacy_Publication/README.md) | Wat is vrijgegeven, door wie, en wat kunnen afzonderlijke openbare passages samen onthullen? |
| [C10 · CAT/ACE](C10_CAT_ACE/README.md) | Welke claims, afhankelijkheden en kosten van de eigen methode zijn aantoonbaar? |


<a name="mini-exercise-index"></a>

### M05 Mini Exercise Index

| Mini-ID | Chapter | Onderwerp | Status | Owner | Primary Source | Last Review |
|---|---|---|---|---|---|---|
| <a id="idx-m05-mini-11"></a>M05-MINI-11 | [C01](C01_Governance_Scope_ISMS/README.md) | Applicability Matrix | PLANNED | Sam | [Labkader](../../Governance/LAB_KADER.md) | — |
| <a id="idx-m05-mini-03"></a>M05-MINI-03 | [C01](C01_Governance_Scope_ISMS/README.md) | Decisions and Exceptions | PLANNED | Sam | [Besluitenlog](../../Governance/BESLUITENLOG.md) | — |
| <a id="idx-m05-mini-10"></a>M05-MINI-10 | [C01](C01_Governance_Scope_ISMS/README.md) | ISMS Clauses 4–10 (oefencasus) | PLANNED | Sam | [Governance](../../Governance/README.md) | — |
| <a id="idx-m05-mini-12"></a>M05-MINI-12 | [C02](C02_Risk_Management/README.md) | Risk Register Review | PLANNED | Sam | privé risicoregister (niet publiek) | — |
| <a id="idx-m05-mini-14"></a>M05-MINI-14 | [C03](C03_Identity_and_Access/README.md) | AD Access Review | PLANNED | Sam | [AD-baselinelog](../../Projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) | — |
| <a id="idx-m05-mini-01"></a>M05-MINI-01 | [C04](C04_Network_Segmentation_OT/README.md) | [A.8.22 Risk-to-Control](C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/README.md) | IN PROGRESS | Sam | [Gesaneerde M04-testmatrix](../M04-Network-Citadel/M04-AC04-AC07-TESTMATRIX.csv) | 24-11-2026 (didactische review) |
| <a id="idx-m05-mini-09"></a>M05-MINI-09 | [C04](C04_Network_Segmentation_OT/README.md) | Zones and Conduits | PLANNED | Sam | [Netwerkontwerp](../../Architectuur/NETWERKONTWERP.md) | — |
| <a id="idx-m05-mini-15"></a>M05-MINI-15 | [C05](C05_Logging_Detection_Incident/README.md) | Log Coverage and Time Sync | PLANNED | Sam | privé daglog (niet publiek) | — |
| <a id="idx-m05-mini-08"></a>M05-MINI-08 | [C05](C05_Logging_Detection_Incident/README.md) | Reporting Timeline Exercise | PLANNED | Sam | [Wet- en regelgevingskaders](../../Governance/WET_EN_REGELGEVING.md) | — |
| <a id="idx-m05-mini-07"></a>M05-MINI-07 | [C06](C06_Backup_Recovery_Continuity/README.md) | Restore Evidence Review | PLANNED | Sam | [M02-herstelontwerp](../../Governance/M02-Phoenix-Recovery/README.md) | — |
| <a id="idx-m05-mini-13"></a>M05-MINI-13 | [C07](C07_Hardening_Config_Change/README.md) | Baseline vs Reality | PLANNED | Sam | [Hardwarebaseline](../../Governance/HARDWARE_BASELINE.md) | — |
| <a id="idx-m05-mini-16"></a>M05-MINI-16 | [C07](C07_Hardening_Config_Change/README.md) | Hypervisor Hardening Review | PLANNED | Sam | [M01-dossier](../M01-Hypervisor-Fortress/README.md) | — |
| <a id="idx-m05-mini-06"></a>M05-MINI-06 | [C08](C08_Suppliers_Cloud_Third_Parties/README.md) | ICT Third-Party Register | PLANNED | Sam | [Hardwarebaseline](../../Governance/HARDWARE_BASELINE.md) | — |
| <a id="idx-m05-mini-04"></a>M05-MINI-04 | [C09](C09_Privacy_Publication/README.md) | Publication Gates | PLANNED | Sam | [Publicatiebeleid](../../Governance/PUBLICATIEBELEID.md) | — |
| <a id="idx-m05-mini-02"></a>M05-MINI-02 | [C10](C10_CAT_ACE/README.md) | Claims Audit | PLANNED | Sam | [CAT/ACE v0.4](../../Governance/CAT_ACE_v0.4.md) | — |
| <a id="idx-m05-mini-05"></a>M05-MINI-05 | [C10](C10_CAT_ACE/README.md) | Dependency Atlas | PLANNED | Sam | [CAT/ACE §8](../../Governance/CAT_ACE_v0.4.md#8-dependency-analyse-relaties-kwetsbaarheid-en-causale-voorzichtigheid) | — |
| <a id="idx-m05-mini-17"></a>M05-MINI-17 | [C10](C10_CAT_ACE/README.md) | Measured Cost Baseline | PLANNED | Sam | [Methodiek 05.6](Methodiek/05.6_Cost_and_Efficiency/README.md) | — |


Primary Source is het vertrekdossier. De technische missie beheert het bewijs. Het Framework Register onderbouwt de kaderkeuze. Last Review betreft alleen een inhoudelijke review. MINI-01 is IN PROGRESS (kennistraining afgerond); de overige oefeningen blijven volgens hun afzonderlijke indexstatus. Bij start krijgt de oefening een eigen map in het betreffende chapter.

## 6. Framework Register

Dit is het **enige** M05-overzicht van referentiekaders. Het legt per kader vast **of en hoe M05 het toepast**. De inhoudelijke beschrijving staat in de canonieke documenten: [CAT/ACE v0.4 §4–§6](../../Governance/CAT_ACE_v0.4.md#4-taxonomie-van-referentiekaders-niet-alles-is-een-regulatory-framework) voor de frameworktaxonomie en [Wet- en regelgevingskaders](../../Governance/WET_EN_REGELGEVING.md) voor wetgeving en assurancestandaarden. Er komt **geen map per framework** en geen automatische volledige frameworkimplementatie.

**Toepassingsstatus in dit register** (beschrijft het gebruik binnen M05, geen engineeringverdict en geen nalevingsniveau):

| Label | Betekenis |
|---|---|
| **SELECTED** | Gekozen als primair kader voor een benoemde casus |
| **PLANNED** | Voorgenomen ondersteunend gebruik in een benoemde casus; nog niet toegepast |
| **REFERENCE** | Beschikbaar als referentie; per casus selecteerbaar; nu niet in gebruik |
| **NOT APPLICABLE** | Voor de benoemde casus bewust niet van toepassing, met reden |
| **NOT VALIDATED** | Eigen of experimenteel model zonder onafhankelijke validatie |

| Framework | Type kader | Primaire relevantie voor M05 | Wanneer toepasselijk | Beperkingen | Toepassingsstatus | Casus, rol en criterium |
|---|---|---|---|---|---| --- |
| **ISO/IEC 27001:2022** | Managementsysteemnorm (certificeerbaar) | ISMS-eisen, risicogestuurd management, Annex A als control-sleutel (05.1–05.4) | Primair startkader; Annex A **A.8.22** in MINI-01 | Hoofdstukken 4–10 zijn de **ISMS-eisen**; Annex A is een referentielijst van controls. Een Annex A-controlassessment bewijst op zichzelf **geen ISO 27001-conformiteit**. Het lab heeft geen operationeel ISMS. | **SELECTED** voor MINI-01 (casusgebonden, geen volledige SoA); uitvoering **IN PROGRESS** | 01 · A.8.22 voor de M04-casus. [Editie](https://www.iso.org/standard/27001) gecontroleerd, precieze normtekst NOT VERIFIED. Kandidaten: 11 · scope, 10 · clausules 4–10, 14 · afgebakende toegangsreview, 15 · logging en tijd. Bepaling en bewijs per nieuwe casus bij start verifiëren. |
| **ISO/IEC 27002:2022** | Guidance bij controls | Interpretatie en implementatierichtlijn per control (05.3) | Bij het beoordelen van controlontwerp, o.a. 8.22 | Guidance, geen eis; geen testprocedure | **PLANNED** — ondersteunend bij MINI-01 | — |
| **ISO/IEC 27005:2022** | Risicomanagementguidance | Risico-identificatie, -analyse, -evaluatie en -behandeling (05.2, 05.4) | Bij elk risicorecord | Geen voorgeschreven kans/impact-schaal; methodiekkeuze moet expliciet zijn | **PLANNED** — ondersteunend bij MINI-01 | 12 · kandidaat voor de beoordeling van één risicorecord. Bij 01 uitsluitend ondersteunend. |
| **NIST CSF 2.0** | Uitkomstgericht cybersecuritykader | Outcome-taal, Current/Target Profile, governance (05.1) | Wanneer een casus een outcome- of profielvergelijking vraagt | Schrijft geen concrete configuratie voor; Tiers zijn geen hostscore | **REFERENCE** — niet geselecteerd voor MINI-01; de actieve controlmapping is PARKED | — |
| **CIS Controls v8.1** | Geprioriteerde controlcatalogus + Assessment Specification | Concrete Safeguards en meetcriteria (05.3) | Bij technische controltoetsing waar een Safeguard beter meetbaar is dan Annex A | Een catalogus is geen bewijs van werking; CIS Benchmarks zijn een ander product | **REFERENCE** — niet geselecteerd voor MINI-01 | — |
| **NIST SP 800-53 Rev. 5 / 800-53A Rev. 5** | Controlcatalogus / assessmentprocedures | Examine–Interview–Test-methode en assessmentdiepgang (05.3, 05.5) | Wanneer een gestructureerde assessmentprocedure als vergelijkingsbasis dient | Gericht op federale systemen; tailoring nodig; extra stappen zijn niet automatisch beter | **REFERENCE** — methodisch bruikbaar; niet geselecteerd voor MINI-01 | — |
| **COBIT 2019** | Enterprise IT-governancekader | Scheiding Governance/management, eigenaarschap, besluitlijnen (05.1, 05.2, 05.4) | Bij vragen over verantwoordelijkheid, escalatie en risicoacceptatie | Geen technische test; de governance-managementscheiding bestond al vóór CAT/ACE | **REFERENCE**; **NOT APPLICABLE** voor MINI-01 | — |
| **ISO 19011:2026** | Auditguidance voor managementsystemen | Auditprogramma, bewijsbetrouwbaarheid, onafhankelijkheid, auditorcompetentie (05.5) | Alleen bij passende auditvragen | Geen cybersecuritycontrolcatalogus. 4e editie, gepubliceerd mei 2026; vervangt de ingetrokken 2018-editie (geverifieerd via de iso.org-catalogus, 20-11-2026) | **REFERENCE**; **NOT APPLICABLE** voor MINI-01 | — |
| **ISA/IEC 62443** | Industriële IT/OT-beveiligingsreeks | Zones & conduits, OT-risicoanalyse, systeemeisen (05.1, 05.7) | Alleen bij relevante OT-verdieping | Geen Security Level-claim zonder volledig 62443-assessment; de lab-OT is een simulatie | **REFERENCE** — in MINI-01 hooguit terminologisch (zones/conduits) | 09 · kandidaat [IEC 62443-3-2:2020](https://webstore.iec.ch/en/publication/30727) voor één zones-en-conduitsvraag. Bij 01 alleen aanvullend als een specifieke interpretatievraag open is. |
| **CAT/ACE v0.4** | Eigen experimenteel onderzoeksmodel | Koppeling governance–management–techniek met Audit, Cost & Efficiency en dependency-analyse (alle hoofdstukken) | Als onderzoekslens per casus | **CONCEPT / NOT VALIDATED**; geen auditnorm, geen certificering, geen bewezen meerwaarde | **NOT VALIDATED** — actuele experimentele methodiekbaseline | 05 · §8 als intern onderzoeksmodel. Benoem bij iedere gedeelde afhankelijkheid of die is waargenomen of verondersteld. |
| NIS2 | Richtlijn | Meldtijdlijn | Gesimuleerd meldscenario | Normadressaat, peildatum en nationale uitwerking bij start afbakenen | Onderzoeksreferentie | 08 · kandidaat [Richtlijn (EU) 2022/2555, art. 23](https://eur-lex.europa.eu/eli/dir/2022/2555/oj). |
| DORA | Verordening | ICT-derdenregister | Gesimuleerde financiële entiteit | Afbakening van de fictieve entiteit en haar contracten vereist | Onderzoeksreferentie | 06 · kandidaat [Verordening (EU) 2022/2554, art. 28 lid 3](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). |
| Interne criteria | Projectbeleid of meetcriterium | Een toetsbaar intern criterium per vraag | Versie en relevante passage bij start vastleggen | Een projectbesluit draagt een interne conclusie | Kandidaten | 03 · herleidbaar besluit. 07 · M02-herstelcriterium. 16 · hypervisorbeleid. 04 · publicatieprocedure. 02 · toegestane claim volgens statuslegenda. 17 · gemeten tijd volgens 05.6. |
| Leveranciersbaseline | Productguidance | Vergelijking met waarneming | Exact asset, product en versie kiezen | Afwijking vraagt context en bewijs | Kandidaat | 13 · één toepasselijke leveranciersbaseline voor het gekozen asset. |

**Selectieregel.** Kies per mini maximaal één primair kader of één intern toetscriterium. Leg in deze tabel de vraag, rol, editie, precieze vindplaats, toepasselijkheid en bronbeperking vast. Een secundaire bron vraagt een concrete onbeantwoorde vraag. Voor 01 is A.8.22 de primaire keuze en zijn ISO/IEC 27002 en 27005 ondersteunend. De overige casuskoppelingen zijn **CANDIDATE**. MINI-08 is een gesimuleerde NIS2-referentie. Nationale omzetting (Cbw) bepaalt de verplichtingen. Toepasselijkheid is open. Bij wetgeving vraagt de casus een normadressaat, jurisdictie en peildatum. Gedetailleerde ISO-/SOC-mappings en de Nederlandse uitwerking zijn **NOT VERIFIED** waar de toepasselijke brontekst ontbreekt. [Wet- en regelgevingskaders](../../Governance/WET_EN_REGELGEVING.md).

## 7. CAT/ACE v0.4 als experimentele methode

[CAT/ACE v0.4](../../Governance/CAT_ACE_v0.4.md) blijft de **actuele experimentele methodiekbaseline** (`CONCEPT / NOT VALIDATED`). In M05 wordt het gebruikt als onderzoekslens, niet als auditnorm:

- **CAT-C / CAT-A / CAT-T** ordenen eisen, eigenaarschap en techniek → vooral [05.1](Methodiek/05.1_Scope_and_Applicability/README.md) en [05.2](Methodiek/05.2_Risk_to_Control_Traceability/README.md).
- **ACE-Audit** → [05.3](Methodiek/05.3_Control_Effectiveness/README.md), [05.4](Methodiek/05.4_Gaps_and_Exceptions/README.md) en [05.5](Methodiek/05.5_Assurance_and_Independence/README.md); **ACE-Cost / ACE-Efficiency** → [05.6](Methodiek/05.6_Cost_and_Efficiency/README.md); de dependency-analyse (§8 van CAT/ACE) → [05.7](Methodiek/05.7_Systemic_Risk/README.md).
- M05 kan CAT/ACE **bevestigen, nuanceren of weerleggen**. Negatieve uitkomsten worden bewaard.

## 8. Praktische onderzoekscyclus

Per casus, proportioneel en zonder verplichte volledige audit:

1. **Afbakenen** (05.1) — één casus, één grens, gekozen kaders en N/A-redenen.
2. **Herleiden** (05.2) — asset, dreiging, risico, eigenaar, control, behandeling.
3. **Toetsen** (05.3) — ontwerp, implementatie en werking apart; bestaand bewijs hergebruiken.
4. **Afwijkingen vastleggen** (05.4) — gaps, uitzonderingen, restrisico, corrigerende actie, hertestvoorwaarde.
5. **Assurance begrenzen** (05.5) — wie heeft beoordeeld, hoe onafhankelijk, wat mag wel en niet worden geclaimd.
6. **Kosten en efficiëntie** (05.6) — gemeten versus geschat, alternatieven onder gelijke beveiligingsgrenzen.
7. **Systemisch kijken** (05.7) — gedeelde afhankelijkheden en mogelijke cascades als expliciete hypothesen.
8. **Ownerbesluit en revalidatie** — Sam beslist over behandeling en acceptatie; na een wijziging volgt een gerichte hertest.

## 9. Evidence- en traceabilitymethodiek

- **Linken, niet kopiëren.** M05 verwijst naar bestaand bewijs in M01–M04 en dupliceert geen evidence.
- **Herkomst per bewijsstuk.** M05 gebruikt beschrijvende herkomstlabels, geen verdicts:
  - `OBSERVED` — door Sam zelf uitgevoerd of waargenomen, met datum.
  - `DOCUMENTED` — vastgelegd in configuratie- of architectuurdocumentatie; zegt niets over gedrag.
  - `AI-INTERPRETED` — duiding door een AI-assistent, niet zelfstandig geverifieerd.
  - `SIMULATED` — fictieve organisatiecontext (bijv. een gesimuleerde risico-eigenaar).
  - `HYPOTHESIS` — onbevestigde relatie of onbevestigd gevolg.
  - `NOT VERIFIED` — onvoldoende bewijs voor de betreffende uitspraak ([Statuslegenda §5](../../Governance/STATUSLEGENDA.md#5-uitsluitend-onderzoeksbeoordeling)).
- **Ontwerp ≠ implementatie ≠ werking.** Een regelscreenshot is geen werkingsbewijs; voor werking zijn positieve én relevante negatieve tests met log- en tijdcorrelatie nodig ([Statuslegenda §7](../../Governance/STATUSLEGENDA.md#7-bewijsdiscipline)).
- **Bidirectionele traceability** volgens [CAT/ACE §9](../../Governance/CAT_ACE_v0.4.md#9-traceability--en-assuranceketen): van eis naar bewijs én van technische afwijking terug naar eigenaar en eis. Ontbrekende schakels worden als gat gemarkeerd, niet ingevuld.
- **Historie blijft staan.** Bestaande testuitslagen, FAILs en hashes worden niet herschreven.

## 10. Status en bekende beperkingen

- Er is nog **geen** M05-casus uitgevoerd. Deze map bevat structuur, methodiek en planning, geen M05-bevindingen.
- De organisatielaag (directie, risico-eigenaar, CISO) is grotendeels **SIMULATED**; een gesimuleerd acceptatiebesluit is geen werkelijke bevoegdheid.
- Eén persoon ontwerpt, bouwt en beoordeelt, met AI-ondersteuning: **geen formele onafhankelijkheid** ([05.5](Methodiek/05.5_Assurance_and_Independence/README.md)).
- Normteksten van ISO/IEC zijn auteursrechtelijk beschermd; M05 noemt controltitels en ID's, niet de volledige normtekst.
- Kleine steekproef, één lab, risico op overfitting aan een bekende omgeving ([CAT/ACE §13](../../Governance/CAT_ACE_v0.4.md#13-evidence-veiligheid-validiteit-en-beperkingen)).
- Het M04-bronbewijs is zelf nog in review (AC04/AC07 integraal **PENDING**); M05 erft die beperking.

## 11. Relatie met M01–M04

| Missie | Wat M05 ervan gebruikt | Grens |
|---|---|---|
| [M01 Hypervisor Fortress](../M01-Hypervisor-Fortress/README.md) | VM-isolatie, de vastgelegde EXCEPTION, de hypervisor als gedeelde afhankelijkheid | M05 verandert geen HV-verdicts |
| [M02 Phoenix Recovery](../../Governance/M02-Phoenix-Recovery/README.md) | Herstelbaarheid als voorwaarde voor betrouwbare controls | M05 claimt geen herstel; status volgt het M02-dossier |
| [M03 Identity Dominion](../../Projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) | Identiteit en DNS als gedeelde afhankelijkheid, eigenaarschap van accounts | AD-basis alleen binnen de geteste scope PASS |
| [M04 Network Citadel](../M04-Network-Citadel/README.md) | IT/OT-segmentatie als **eerste casus** (MINI-01) | M04 blijft **IN PROGRESS**; M05 accepteert geen M04-acceptatiecriteria |

M05-bevindingen gaan als voorstel terug naar de betrokken missie (bijvoorbeeld als REWORK of open gap) en wijzigen daar niets zonder besluit van Sam.

## 12. M05-MS01 — Foundational Security Assurance (VOORSTEL)

**Status:** **NOT ACHIEVED**. De formele exitcriteria zijn **niet vastgesteld**; onderstaande lijst is een voorstel (**DRAFT**) en vraagt een afzonderlijk ownerbesluit.

| # | Voorgesteld exitcriterium | Hoofdstuk |
|---|---|---|
| P1 | Minimaal één afgeronde mini-oefening (MINI-01) met scoped verdict en één ingevulde regel per hoofdstuk 05.1–05.7 | alle |
| P2 | Casusgebonden toepasselijkheid en kaderselectie, inclusief N/A-motivatie en een mini-SoA (alleen casusscope) | 05.1 |
| P3 | Risicorecord met eigenaar, kans/impact-aannames en behandelvoorstel, herleidbaar naar control en bewijs | 05.2 |
| P4 | Ontwerp-, implementatie- en werkingsoordeel apart vastgelegd, met bewijsherkomst (OBSERVED vs AI-INTERPRETED) | 05.3 |
| P5 | Gaps en uitzonderingen met corrigerende actie, hertestvoorwaarde en restrisico-eigenaar | 05.4 |
| P6 | Assurance-uitspraak met expliciete onafhankelijkheids- en AI-grenzen | 05.5 |
| P7 | Beoordelingsinspanning en controlkosten vastgelegd als gemeten (MEASURED) of geschat (ESTIMATED) | 05.6 |
| P8 | Ten minste één gedeelde afhankelijkheid geanalyseerd met bewijsniveau (bevestigd / aannemelijk / niet onderzocht / weerlegd) | 05.7 |
| P9 | Expliciete acceptatie van MS01 door Sam, gedateerd vastgelegd | — |

Latere milestones (MS02+) zijn niet gedefinieerd. De mini-index bevat de zestien aanvullend geplande mini’s per chapter.

## 13. M05-MINI-01 — ISO 27001 Risk-to-Control Assessment (EERSTE CASUS IN UITVOERING)

De [indexrij](#idx-m05-mini-01) geeft de planning. In [C04 · casus en historische traceabilitymatrix](C04_Network_Segmentation_OT/README.md#m05-mini-01) staan de oorspronkelijke zeven vragen en de gedateerde verwijzing naar M04.

## 14. Beperkingen van het publieke bewijs

- Deze publieke versie is een **gesaneerde tegenhanger** van de interne M05-documentatie. Deze documentatie beschrijft de onderwerpen, methodiekvragen en status aan de hand van publieke bronnen. De uiteindelijke vergelijking van inhoud en governance hoort bij de publicatiereview.
- Waar het onderliggende bewijs niet publiek is, staat dat erbij; zulke uitspraken zijn voor een externe lezer **niet onafhankelijk verifieerbaar**.
- De gesaneerde M04-beelden ondersteunen alleen de daarbij beschreven observaties ([saneringsrapport](../M04-Network-Citadel/M04-SANITIZATION-REPORT.md)).
- Publicatie volgt het [publicatiebeleid](../../Governance/PUBLICATIEBELEID.md); de daarin genoemde publicatiegates staan nog **OPEN**. Publieke zichtbaarheid is geen publicatie- of security-PASS.

## 15. Principes voor continue verbetering

- **Permanent, niet eindig:** M05 wordt niet afgesloten. Elke milestone, mini-oefening en review voedt de volgende iteratie.
- **Revalidatie na wijziging:** een eerdere PASS vervalt bij een relevante wijziging tot een gerichte hertest bevestigt dat hij nog geldt.
- **Negatieve resultaten tellen mee:** een weerlegde hypothese of "geen veilige optimalisatie gevonden" is een geldige uitkomst.
- **Methodiek is toetsbaar:** CAT/ACE en deze structuur kunnen op basis van bewijs worden aangepast; eerdere uitkomsten worden niet achteraf herschreven.
- **Proportioneel:** zo weinig administratie als mogelijk, zoveel bewijs als nodig.

*Build with purpose. Secure by design. Validate through evidence. Improve continuously.*

De publieke chapterstructuur is opgenomen in [PR #69](https://github.com/SamAsgar/Hybrid-Theory-Public/pull/69).

### Overdracht van inhoudelijke chapters naar C10

De formele afspraak voor C01–C09 → C10 staat in [C10 · Overdrachtscontract](C10_CAT_ACE/README.md#overdrachtscontract-c01c09--c10-ontwerpafspraak). C10 gebruikt bronverwijzingen naar claims en bevindingen voor methodiekonderzoek; technische verdicts, bewijs en eigenaarbesluiten blijven bij de bronmissies. Dit is een procesafspraak, geen gestart assessment of centraal duplicaatregister.


## Educatieve afsluiting · 24 november 2026

[MINI-01 dossier](C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/README.md) · [Herbruikbare afsluitstructuur (voorstel)](EDUCATIEVE-AFSLUITSTRUCTUUR.md). Kennistraining 5/5; formele beoordeling, 05.6/05.7 en owneracceptatie PENDING. Geen M05-MS01- of M04-acceptatie.
