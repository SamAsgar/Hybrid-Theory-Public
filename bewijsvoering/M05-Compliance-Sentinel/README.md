# M05 — Compliance Sentinel | Regulatory Assessment & Security Assurance

**Repository:** Hybrid-Theory-Public · **Publicatievorm:** gesaneerde onderzoeks- en methodiekdocumentatie  
**Missietype:** **Permanente Main Mission** (geen definitieve afsluitstatus)  
**Peildatum:** 20 november 2026 · **Besluit:** missionmodel en M05-structuur goedgekeurd door Sam op 20-11-2026 (besluit [PUB-DEC-001](../../governance/BESLUITENLOG.md#pub-dec-001--20-11-2026--permanent-missionmodel-en-m05-structuur))

| Statusdimensie | Stand 20-11-2026 |
|---|---|
| Structuur van deze documentatie | **APPROVED** (structuur en frameworkbenadering) |
| Hoofdstukken 05.1–05.7 | Ingericht; inhoud is methodiek en planning |
| M05-technische uitvoering | **PENDING** — er is nog geen M05-assessment uitgevoerd |
| M05-MS01 — Foundational Security Assurance | **NOT ACHIEVED**; exitcriteria zijn een voorstel (**DRAFT**) |
| M05-MINI-01 — ISO 27001 Risk-to-Control Assessment | **PLANNED**; niet gestart |
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

Controlgerichte assessments beoordelen maatregelen vaak één voor één. M05 onderzoekt daarnaast wat er gebeurt als meerdere controls van dezelfde component afhangen ([05.7 Systemic Risk](05.7_Systemic_Risk/README.md)). De [academische achtergrond](../../onderzoek/academische-referenties/README.md) over systemisch risico en spillover is daarbij een **inspiratiebron, geen gevalideerde methode**.

## 3. Permanente mission lifecycle

Hybrid-Theory heeft vijf **permanente Main Missions**: M01 Hypervisor Fortress, M02 Phoenix Recovery, M03 Identity Dominion, M04 Network Citadel en M05 Compliance Sentinel.

- Een Main Mission krijgt **geen** definitieve afsluitstatus (geen `MISSION COMPLETE`, geen missie-PASS). Ontwikkeling, revalidatie en verbetering zijn continu.
- Voortgang wordt gemeten via **opeenvolgende milestones**. Een milestone heeft een expliciete scope, vooraf vastgestelde acceptatiecriteria, bewijs, een beoordeling en **expliciete acceptatie door Sam**.
- **Geen van de vijf Main Missions heeft Milestone 01 bereikt** (stand 20-11-2026).
- Een geslaagde technische deeltest is een **scoped technische bevinding**, geen milestone-acceptatie.

De statusbegrippen staan in de [Statuslegenda §3a](../../governance/STATUSLEGENDA.md#3a-missie--milestone--en-mini-oefeningstatus-20-11-2026).

## 4. Main Mission, milestone en mini-oefening

| Niveau | Voorbeeld | Kenmerk | Kan "af" zijn? |
|---|---|---|---|
| **Main Mission** | M05 Compliance Sentinel | Permanent onderzoeks- en verbeterdomein | **Nee** |
| **Milestone** | M05-MS01 Foundational Security Assurance | Afgebakend doel, vooraf vastgestelde exitcriteria, owneracceptatie | Ja: **ACHIEVED** alleen na acceptatie door Sam |
| **Mini-oefening** | M05-MINI-01 ISO 27001 Risk-to-Control Assessment | Klein werkpakket binnen een missie; levert bewijs en ervaring voor een milestone | Ja, met een **scoped verdict**; sluit geen milestone of missie af |
| **Afgebakende zelfstandige missie** | (nog niet gedefinieerd) | Latere, aparte categorie ná de vijf Main Missions, met eigen begin- en eindcriteria | Ja — identificatieschema nog een ownerbesluit |

**Een MINI-PASS is geen milestone-PASS.** Een milestone-acceptatie is geen missie-afsluiting.

## 5. De zeven officiële onderzoekshoofdstukken

De zeven hoofdstukken zijn de **permanente onderzoekscategorieën** van M05 en volgen de zeven onderzoeksdoelen uit [Issue #46](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/46). Ze zijn **geen verplichte lineaire stappen** en **geen checklistlaag**: een casus raakt meestal meerdere hoofdstukken tegelijk.

| # | Hoofdstuk | Kernvraag |
|---|---|---|
| 05.1 | [Scope & Applicability](05.1_Scope_and_Applicability/README.md) | Welke eisen en kaders zijn voor deze casus van toepassing, voor wie, en waarom? |
| 05.2 | [Risk-to-Control Traceability](05.2_Risk_to_Control_Traceability/README.md) | Is de keten asset → dreiging → risico → eigenaar → control → bewijs → besluit herleidbaar? |
| 05.3 | [Control Effectiveness](05.3_Control_Effectiveness/README.md) | Is de control goed ontworpen, aantoonbaar geïmplementeerd én werkend? |
| 05.4 | [Gaps & Exceptions](05.4_Gaps_and_Exceptions/README.md) | Welke afwijkingen, uitzonderingen en restrisico's bestaan er, en wie draagt ze? |
| 05.5 | [Assurance & Independence](05.5_Assurance_and_Independence/README.md) | Wat mag een interne, externe, hybride of AI-ondersteunde review wél en níét claimen? |
| 05.6 | [Cost & Efficiency](05.6_Cost_and_Efficiency/README.md) | Wat kost beheersing en beoordeling, en bestaat er een even veilig, goedkoper alternatief? |
| 05.7 | [Systemic Risk](05.7_Systemic_Risk/README.md) | Welke gedeelde afhankelijkheden laten één falende component meerdere controls tegelijk raken? |

**Navigatie:** [05.1](05.1_Scope_and_Applicability/README.md) · [05.2](05.2_Risk_to_Control_Traceability/README.md) · [05.3](05.3_Control_Effectiveness/README.md) · [05.4](05.4_Gaps_and_Exceptions/README.md) · [05.5](05.5_Assurance_and_Independence/README.md) · [05.6](05.6_Cost_and_Efficiency/README.md) · [05.7](05.7_Systemic_Risk/README.md) · [CAT/ACE v0.4](../../governance/CAT_ACE_v0.4.md) · [Wet- en regelgevingskaders](../../governance/WET_EN_REGELGEVING.md) · [Statuslegenda](../../governance/STATUSLEGENDA.md) · [M04-dossier (eerste casus)](../M04-Network-Citadel/README.md) · [Roadmap](../../projectlogboeken/ROADMAP.md)

## 6. Framework Register

Dit is het **enige** M05-overzicht van referentiekaders. Het legt per kader vast **of en hoe M05 het toepast**. De inhoudelijke beschrijving staat in de canonieke documenten: [CAT/ACE v0.4 §4–§6](../../governance/CAT_ACE_v0.4.md#4-taxonomie-van-referentiekaders-niet-alles-is-een-regulatory-framework) voor de frameworktaxonomie en [Wet- en regelgevingskaders](../../governance/WET_EN_REGELGEVING.md) voor wetgeving en assurancestandaarden. Er komt **geen map per framework** en geen automatische volledige frameworkimplementatie.

**Toepassingsstatus in dit register** (beschrijft het gebruik binnen M05, geen engineeringverdict en geen nalevingsniveau):

| Label | Betekenis |
|---|---|
| **SELECTED** | Gekozen als primair kader voor een benoemde casus |
| **PLANNED** | Voorgenomen ondersteunend gebruik in een benoemde casus; nog niet toegepast |
| **REFERENCE** | Beschikbaar als referentie; per casus selecteerbaar; nu niet in gebruik |
| **NOT APPLICABLE** | Voor de benoemde casus bewust niet van toepassing, met reden |
| **NOT VALIDATED** | Eigen of experimenteel model zonder onafhankelijke validatie |

| Framework | Type kader | Primaire relevantie voor M05 | Wanneer toepasselijk | Beperkingen | Toepassingsstatus |
|---|---|---|---|---|---|
| **ISO/IEC 27001:2022** | Managementsysteemnorm (certificeerbaar) | ISMS-eisen, risicogestuurd management, Annex A als control-sleutel (05.1–05.4) | Primair startkader; Annex A **A.8.22** in MINI-01 | Hoofdstukken 4–10 zijn de **ISMS-eisen**; Annex A is een referentielijst van controls. Een Annex A-controlassessment bewijst op zichzelf **geen ISO 27001-conformiteit**. Het lab heeft geen operationeel ISMS. | **SELECTED** voor MINI-01 (casusgebonden, geen volledige SoA); uitvoering **PLANNED** |
| **ISO/IEC 27002:2022** | Guidance bij controls | Interpretatie en implementatierichtlijn per control (05.3) | Bij het beoordelen van controlontwerp, o.a. 8.22 | Guidance, geen eis; geen testprocedure | **PLANNED** — ondersteunend bij MINI-01 |
| **ISO/IEC 27005:2022** | Risicomanagementguidance | Risico-identificatie, -analyse, -evaluatie en -behandeling (05.2, 05.4) | Bij elk risicorecord | Geen voorgeschreven kans/impact-schaal; methodiekkeuze moet expliciet zijn | **PLANNED** — ondersteunend bij MINI-01 |
| **NIST CSF 2.0** | Uitkomstgericht cybersecuritykader | Outcome-taal, Current/Target Profile, governance (05.1) | Wanneer een casus een outcome- of profielvergelijking vraagt | Schrijft geen concrete configuratie voor; Tiers zijn geen hostscore | **REFERENCE** — niet geselecteerd voor MINI-01; de actieve controlmapping is PARKED |
| **CIS Controls v8.1** | Geprioriteerde controlcatalogus + Assessment Specification | Concrete Safeguards en meetcriteria (05.3) | Bij technische controltoetsing waar een Safeguard beter meetbaar is dan Annex A | Een catalogus is geen bewijs van werking; CIS Benchmarks zijn een ander product | **REFERENCE** — niet geselecteerd voor MINI-01 |
| **NIST SP 800-53 Rev. 5 / 800-53A Rev. 5** | Controlcatalogus / assessmentprocedures | Examine–Interview–Test-methode en assessmentdiepgang (05.3, 05.5) | Wanneer een gestructureerde assessmentprocedure als vergelijkingsbasis dient | Gericht op federale systemen; tailoring nodig; extra stappen zijn niet automatisch beter | **REFERENCE** — methodisch bruikbaar; niet geselecteerd voor MINI-01 |
| **COBIT 2019** | Enterprise IT-governancekader | Scheiding governance/management, eigenaarschap, besluitlijnen (05.1, 05.2, 05.4) | Bij vragen over verantwoordelijkheid, escalatie en risicoacceptatie | Geen technische test; de governance-managementscheiding bestond al vóór CAT/ACE | **REFERENCE**; **NOT APPLICABLE** voor MINI-01 |
| **ISO 19011:2026** | Auditguidance voor managementsystemen | Auditprogramma, bewijsbetrouwbaarheid, onafhankelijkheid, auditorcompetentie (05.5) | Alleen bij passende auditvragen | Geen cybersecuritycontrolcatalogus. 4e editie, gepubliceerd mei 2026; vervangt de ingetrokken 2018-editie (geverifieerd via de iso.org-catalogus, 20-11-2026) | **REFERENCE**; **NOT APPLICABLE** voor MINI-01 |
| **ISA/IEC 62443** | Industriële IT/OT-beveiligingsreeks | Zones & conduits, OT-risicoanalyse, systeemeisen (05.1, 05.7) | Alleen bij relevante OT-verdieping | Geen Security Level-claim zonder volledig 62443-assessment; de lab-OT is een simulatie | **REFERENCE** — in MINI-01 hooguit terminologisch (zones/conduits) |
| **CAT/ACE v0.4** | Eigen experimenteel onderzoeksmodel | Koppeling governance–management–techniek met Audit, Cost & Efficiency en dependency-analyse (alle hoofdstukken) | Als onderzoekslens per casus | **CONCEPT / NOT VALIDATED**; geen auditnorm, geen certificering, geen bewezen meerwaarde | **NOT VALIDATED** — actuele experimentele methodiekbaseline |

**Selectieregel:** andere kaders (bijv. NIS2, DORA, AVG, ISAE 3000/3402, SOC 2, NIST SP 800-82) worden pas toegevoegd wanneer een concrete onderzoekscasus daar aanleiding toe geeft. Registreer dan versie, control- of artikel-ID, toepasselijkheidsreden en N/A-motivatie volgens [CAT/ACE §4](../../governance/CAT_ACE_v0.4.md#4-taxonomie-van-referentiekaders-niet-alles-is-een-regulatory-framework). Voor wetgeving zoals NIS2, DORA en AVG geldt: toepasselijkheid is binnen de huidige onderzoeksscope niet vastgesteld; dit vereist een afzonderlijke beoordeling afhankelijk van activiteiten, rechtspositie en gegevensverwerking. Vrijwillige normen zijn niet bindend tenzij een organisatie zich eraan verbindt ([Wet- en regelgevingskaders](../../governance/WET_EN_REGELGEVING.md#doel-en-afbakening)). Een kader in dit register vermelden betekent **niet** dat het is geïmplementeerd of dat eraan wordt voldaan.

## 7. CAT/ACE v0.4 als experimentele methode

[CAT/ACE v0.4](../../governance/CAT_ACE_v0.4.md) blijft de **actuele experimentele methodiekbaseline** (`CONCEPT / NOT VALIDATED`). In M05 wordt het gebruikt als onderzoekslens, niet als auditnorm:

- **CAT-C / CAT-A / CAT-T** ordenen eisen, eigenaarschap en techniek → vooral [05.1](05.1_Scope_and_Applicability/README.md) en [05.2](05.2_Risk_to_Control_Traceability/README.md).
- **ACE-Audit** → [05.3](05.3_Control_Effectiveness/README.md), [05.4](05.4_Gaps_and_Exceptions/README.md) en [05.5](05.5_Assurance_and_Independence/README.md); **ACE-Cost / ACE-Efficiency** → [05.6](05.6_Cost_and_Efficiency/README.md); de dependency-analyse (§8 van CAT/ACE) → [05.7](05.7_Systemic_Risk/README.md).
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
  - `NOT VERIFIED` — onvoldoende bewijs voor de betreffende uitspraak ([Statuslegenda §5](../../governance/STATUSLEGENDA.md#5-uitsluitend-onderzoeksbeoordeling)).
- **Ontwerp ≠ implementatie ≠ werking.** Een regelscreenshot is geen werkingsbewijs; voor werking zijn positieve én relevante negatieve tests met log- en tijdcorrelatie nodig ([Statuslegenda §7](../../governance/STATUSLEGENDA.md#7-bewijsdiscipline)).
- **Bidirectionele traceability** volgens [CAT/ACE §9](../../governance/CAT_ACE_v0.4.md#9-traceability--en-assuranceketen): van eis naar bewijs én van technische afwijking terug naar eigenaar en eis. Ontbrekende schakels worden als gat gemarkeerd, niet ingevuld.
- **Historie blijft staan.** Bestaande testuitslagen, FAILs en hashes worden niet herschreven.

## 10. Status en bekende beperkingen

- Er is nog **geen** M05-casus uitgevoerd. Deze map bevat structuur, methodiek en planning, geen M05-bevindingen.
- De organisatielaag (directie, risico-eigenaar, CISO) is grotendeels **SIMULATED**; een gesimuleerd acceptatiebesluit is geen werkelijke bevoegdheid.
- Eén persoon ontwerpt, bouwt en beoordeelt, met AI-ondersteuning: **geen formele onafhankelijkheid** ([05.5](05.5_Assurance_and_Independence/README.md)).
- Normteksten van ISO/IEC zijn auteursrechtelijk beschermd; M05 noemt controltitels en ID's, niet de volledige normtekst.
- Kleine steekproef, één lab, risico op overfitting aan een bekende omgeving ([CAT/ACE §13](../../governance/CAT_ACE_v0.4.md#13-evidence-veiligheid-validiteit-en-beperkingen)).
- Het M04-bronbewijs is zelf nog in review (AC04/AC07 integraal **PENDING**); M05 erft die beperking.

## 11. Relatie met M01–M04

| Missie | Wat M05 ervan gebruikt | Grens |
|---|---|---|
| [M01 Hypervisor Fortress](../M01-Hypervisor-Fortress/README.md) | VM-isolatie, de vastgelegde EXCEPTION, de hypervisor als gedeelde afhankelijkheid | M05 verandert geen HV-verdicts |
| [M02 Phoenix Recovery](../../governance/M02-Phoenix-Recovery/README.md) | Herstelbaarheid als voorwaarde voor betrouwbare controls | M05 claimt geen herstel; status volgt het M02-dossier |
| [M03 Identity Dominion](../../projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) | Identiteit en DNS als gedeelde afhankelijkheid, eigenaarschap van accounts | AD-basis alleen binnen de geteste scope PASS |
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

Latere milestones (MS02+) zijn niet gedefinieerd. Mogelijke casussen (identity, herstel, cloudgovernance) zijn **ideeën**, geen planning.

## 13. M05-MINI-01 — ISO 27001 Risk-to-Control Assessment (EERSTE GEPLANDE CASUS)

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
| **05.1** | Welke eisen gelden voor de IT/LAB↔OT-grens en waarom A.8.22? | [Netwerkontwerp](../../architectuur/NETWERKONTWERP.md), [Wet- en regelgevingskaders](../../governance/WET_EN_REGELGEVING.md) | Een zonemodel met de OT-zone achter de firewall is ontworpen (**DOCUMENTED**) | Een formeel goedgekeurde allow/deny-policy per zone als ontwerpdocument | Scope-statement, kaderselectie met N/A, mini-SoA (alleen casus) |
| **05.2** | Welk risico behandelt segmentatie, wie is eigenaar, welke behandeling? | [M04-GAPS](../M04-Network-Citadel/M04-GAPS.md), [Issue #45](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/45) | Open punten en risicoreviews zijn op hoofdlijnen gedocumenteerd | Expliciete (gesimuleerde) risico-eigenaar en behandelbesluit | Eén risicorecord met kans/impact-aannames en behandelvoorstel |
| **05.3** | Ontwerp, implementatie, werking van de segmentatie? | [M04 fase 20](../M04-Network-Citadel/20_OT_segmentation_and_regression/README.md), [M04-GAPS §19 nov.](../M04-Network-Citadel/M04-GAPS.md#aanvulling-19-november--gerichte-deeltests) | Gerichte LAB→PLC- en LAB→HMI-flows werden geweigerd, met firewall-BLOCK-events (**scoped**, evidence-review PENDING) | Integrale AC04/AC07-acceptatie (zie de publieke [M04-GAPS](../M04-Network-Citadel/M04-GAPS.md)) | Apart oordeel ontwerp/implementatie/werking + bewijskwaliteit per bron |
| **05.4** | Welke gaps, uitzonderingen en restrisico's zijn er? | [M04-GAPS](../M04-Network-Citadel/M04-GAPS.md) | Gaps zijn geregistreerd; een integrale acceptatie ontbreekt | Ownerbesluit per gap: corrigeren, tijdelijk accepteren (EXCEPTION) of verder onderzoeken | Gap-/uitzonderingsregister voor de casus met hertestvoorwaarde |
| **05.5** | Wat mag over deze control worden geclaimd, en door wie? | [AI-werkafspraken](../../governance/AI_WERKAFSPRAKEN.md), [Statuslegenda §7](../../governance/STATUSLEGENDA.md#7-bewijsdiscipline) | M04-tests zijn deels met AI-begeleiding ontworpen en geduid | Onafhankelijke review; welk bewijs door Sam zelf is waargenomen | Assurance-statement met onafhankelijkheids- en AI-grenzen |
| **05.6** | Wat kost deze beheersing en de beoordeling ervan? | — (alleen interne planningsramingen) | Er bestaan alleen geschatte planningsuren (**ESTIMATED**) | Gemeten beoordelingsinspanning (MEASURED) | Tijdregistratie MINI-01 + ACE-kosten/efficiëntieregel |
| **05.7** | Welke afhankelijkheden maken dat één fout meerdere controls raakt? | [05.7 Systemic Risk](05.7_Systemic_Risk/README.md) (methodiek) | Geen publieke dependency-analyse; de methodiek en een fictief voorbeeld zijn beschreven | Elke afhankelijkheid van de casus (de analyse blijft intern) | Interne dependencyregel(s) met bewijsniveau; publiek alleen een gesaneerde samenvatting na review |

## 14. Beperkingen van het publieke bewijs

- Deze publieke versie is een **gesaneerde tegenhanger** van de interne M05-documentatie. Structuur, methodiek, kaderselectie en statussen zijn gelijk; concrete interne risicoregisters, bewijs-ID's van ongesaneerde originelen, beheerpaden, adressen en open technische zwaktes zijn **bewust weggelaten**.
- Waar het onderliggende bewijs niet publiek is, staat dat erbij; zulke uitspraken zijn voor een externe lezer **niet onafhankelijk verifieerbaar**.
- De gesaneerde M04-beelden ondersteunen alleen de daarbij beschreven observaties ([saneringsrapport](../M04-Network-Citadel/M04-SANITIZATION-REPORT.md)).
- Publicatie volgt het [publicatiebeleid](../../governance/PUBLICATIEBELEID.md); de daarin genoemde publicatiegates staan nog **OPEN**. Publieke zichtbaarheid is geen publicatie- of security-PASS.

## 15. Principes voor continue verbetering

- **Permanent, niet eindig:** M05 wordt niet afgesloten. Elke milestone, mini-oefening en review voedt de volgende iteratie.
- **Revalidatie na wijziging:** een eerdere PASS vervalt bij een relevante wijziging tot een gerichte hertest bevestigt dat hij nog geldt.
- **Negatieve resultaten tellen mee:** een weerlegde hypothese of "geen veilige optimalisatie gevonden" is een geldige uitkomst.
- **Methodiek is toetsbaar:** CAT/ACE en deze structuur kunnen op basis van bewijs worden aangepast; eerdere uitkomsten worden niet achteraf herschreven.
- **Proportioneel:** zo weinig administratie als mogelijk, zoveel bewijs als nodig.

*Build with purpose. Secure by design. Validate through evidence. Improve continuously.*

**Redactie:** opgesteld met Claude Code op basis van de goedgekeurde M05-structuur en besluiten van Sam; review en publicatievrijgave door Sam.
