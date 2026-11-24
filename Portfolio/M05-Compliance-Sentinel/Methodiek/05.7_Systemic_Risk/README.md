# 05.7 — Systemic Risk | M05 Compliance Sentinel

**Hoofdstukstatus:** structuur **APPROVED**; inhoudelijk werk **PENDING** · [Terug naar M05](../../README.md)

> Dit hoofdstuk is de kern van het Hybrid-Theory-onderzoeksmotief. Het beschrijft methodiek en een **fictief** voorbeeld; het bevat geen overzicht van de werkelijke infrastructuur. Er is in M05 nog **geen** dependency- of fault-injectiontest uitgevoerd; **geen enkel cascade-effect is bewezen**.

## Doel

Onderzoeken hoe **gedeelde afhankelijkheden, single points of failure en keteneffecten** de impact van één falende component of control kunnen vergroten: over technische lagen, over IT/OT/cloud-grenzen en over governance heen. En onderzoeken waar **traditionele controlgerichte beoordelingen** zulke effecten structureel missen.

## Waarom dit een apart hoofdstuk is

Control-assessments (een SoA, een controlcatalogus, een steekproefaudit) beoordelen maatregelen meestal **één voor één**: segmentatie (A.8.22), logging (A.8.15), monitoring (A.8.16), back-up (A.8.13). Elk kan afzonderlijk een PASS krijgen. Als die controls echter **dezelfde component, dezelfde beheerder of dezelfde aanname** delen, kunnen ze tegelijk falen. Dat patroon, *common-mode failure*, is zichtbaar in een afhankelijkheidsgraaf, maar niet in een lijst van losse controls.

## Begrippen

De failure modes komen uit [CAT/ACE v0.4 §8](../../../../Governance/CAT_ACE_v0.4.md#8-dependency-analyse-relaties-kwetsbaarheid-en-causale-voorzichtigheid) en worden hier toegepast:

| Begrip | Kernvraag in M05 |
|---|---|
| **Cross-layer dependency** | Hangt een technische control af van een managementbesluit, of een governanceclaim van één technische component? (in beide richtingen) |
| **Single point of failure (SPOF)** | Welke component heeft geen aangetoonde alternatieve route? |
| **Shared dependency** | Welke DNS, identiteit, gateway, host, tijdbron of beheerlaag wordt door meerdere diensten of controls gedeeld? |
| **Common-cause failure** | Welke ene foutbron kan meerdere controls tegelijk ongeldig maken? |
| **Cascading failure** | Hoe werkt uitval over meerdere afhankelijkheidsranden door? |
| **Risicoconcentratie** | Hoeveel controls, claims of diensten steunen op dezelfde node of persoon? |
| **Spillover** | Waar raakt een fout in één domein (IT) een ander domein (OT, governance, assurance)? |
| **Recovery coupling** | Vereist herstel juist de dienst die is uitgevallen? |

## Onderzoeksvragen

1. Welke nodes dragen **meerdere controls of claims tegelijk**, en wat gebeurt er met die claims als de node faalt?
2. Welke nodes zijn vooral **doorgevers** (veel uitgaande afhankelijkheden) en welke vooral **ontvangers** (afhankelijk van veel andere)?
3. Welke afhankelijkheden worden pas na een storing zichtbaar (hidden dependencies)?
4. Waar loopt een afhankelijkheid door de **IT/OT/cloud-governancegrens**?
5. Welke systemische effecten mist een gangbare controlgerichte beoordeling, en kan een dependency-analyse dat **aantoonbaar** aanvullen, of juist niet?
6. Onder welke omstandigheden levert dependency-analyse **geen** meerwaarde of vals-positieve afhankelijkheden op?

## Beoordelingsmethodiek

### Dependency graph

Een dependency-register per casus (geen aparte graafdatabase) met:
- **Nodes:** component, dienst, control, rol of besluit.
- **Edges:** relatietypen uit CAT/ACE, zoals `requires`, `routes`, `resolves`, `authenticates`, `monitors`, `protects`, `recovers`, `owns` en `accepts-risk`.
- **Per edge:** bron, richting, bewijsniveau (bevestigd / aannemelijk / niet onderzocht / weerlegd) en de controls die eraan hangen.

De **afhankelijkheid** en het **mogelijke gevolg** krijgen elk een eigen label. Een aangetoonde afhankelijkheid maakt een veronderstelde cascade niet aangetoond.

### Herkomstlabels in dit hoofdstuk

| Label | Betekenis en scope |
|---|---|
| **OBSERVED** | Feitelijk opgetreden in een gedateerde, herleidbare test of gebeurtenis, alleen binnen die scope. |
| **DOCUMENTED** | Vastgelegd in configuratie- of architectuurdocumentatie. Zegt niets over gedrag bij falen. |
| **HYPOTHESIS** | Plausibele relatie of plausibel gevolg, nooit gericht getest. |
| **SIMULATED** | Fictieve organisatie- of bedrijfscontext, bijvoorbeeld een gesimuleerde proceseigenaar of bedrijfsimpact. |
| **NOT VERIFIED** | Er is onvoldoende bewijs om de uitspraak te beoordelen; geen aanname van een defect. |

### Predict-then-break

1. Leg de werkende baseline vast.
2. Formuleer **vooraf** welk effect een gecontroleerde, omkeerbare verstoring volgens de graaf zou moeten hebben, plus een tegenhypothese.
3. Voer de verstoring uitsluitend uit na expliciet besluit van Sam, met rollback en binnen eigen systemen ([Labkader](../../../../Governance/LAB_KADER.md)).
4. Vergelijk de waarneming (ground truth) met de voorspelling en met wat een reguliere controlbeoordeling had gevonden.
5. Herstel en valideer. De uitkomst is bevestigd, gedeeltelijk bevestigd, weerlegd of onvoldoende bewijs.

[CAT/ACE §12](../../../../Governance/CAT_ACE_v0.4.md#12-illustratief-scenario-addns-als-gedeelde-afhankelijkheid) beschrijft zo'n scenario voor AD/DNS. Dat scenario is uitdrukkelijk **niet uitgevoerd**.

### Concentratiebeschouwing

Per node tellen hoeveel controls of claims ervan afhangen. Dit is een onderzoeksidee, **geen gevalideerde metriek**.

## Methodologisch voorbeeld (abstract, fictief)

Het voorbeeld hieronder beschrijft een **fictieve organisatie** ("Organisatie X"). Het illustreert alleen de redenering en is **geen** beschrijving van de Hybrid-Theory-infrastructuur, van de actuele toestand ervan of van uitgevoerde tests. Alle elementen zijn **SIMULATED**. De labels geven aan welke bewijsklasse een vergelijkbare uitspraak in een echte casus zou vragen.

**Casus Organisatie X (SIMULATED):** een productieafdeling met een OT-zone die door een zonegrens van het kantoornetwerk is gescheiden. Drie controls worden afzonderlijk beoordeeld en krijgen elk een scoped PASS: netwerksegmentatie, logging van grensverkeer en een back-upprocedure.

| Stap | Redenering in het voorbeeld | Label dat een echte casus zou vragen |
|---|---|---|
| 1. Controls apart | Segmentatie, logging en back-up zijn elk getoetst en scoped PASS | **OBSERVED** — alleen als de tests gedateerd en herleidbaar zijn uitgevoerd |
| 2. Gedeelde node zoeken | Het ontwerp toont dat alle drie controls op hetzelfde grensapparaat steunen: het handhaaft de zonegrens, schrijft de grenslogs en is het pad naar de back-updoelen | **DOCUMENTED** — een ontwerp of configuratie zegt nog niets over gedrag bij falen |
| 3. Gevolg voorspellen | Valt het grensapparaat uit of wordt het verkeerd geconfigureerd, dan kunnen drie controls tegelijk ongeldig worden (common-cause failure) | **HYPOTHESIS** — tot een goedgekeurde, omkeerbare test het bevestigt of weerlegt |
| 4. Faalrichting | Faalt het apparaat open (verkeer toegestaan) of dicht (alles geblokkeerd)? | **NOT VERIFIED** — zonder test onbekend; niet invullen op basis van aannames |
| 5. Spillover naar governance | Een fictieve proceseigenaar moet over productieverlies beslissen, terwijl de bewijsbron (logs) zelf geraakt is | **SIMULATED** — een gesimuleerd besluit is geen werkelijke bevoegdheid |
| 6. Vergelijking | Een control-voor-controlbeoordeling gaf drie losse PASS-oordelen; de graaf toont één concentratiepunt | Onderzoeksuitkomst: alleen als meerwaarde vastgesteld wanneer de voorspelling ook getest is |

**Cascadehypothese in graafvorm (SIMULATED / HYPOTHESIS):**

```text
Grensapparaat ──protects──▶ Control A: segmentatie
Grensapparaat ──logs──────▶ Control B: logging (bewijsbron voor A)
Grensapparaat ──routes────▶ Control C: back-uppad
Control C ──recovers──────▶ Grensapparaat   → recovery coupling
```

De les uit het voorbeeld is methodisch: drie losse PASS-oordelen kunnen samen een concentratierisico verbergen. Of dat in een echte omgeving zo is, blijkt alleen uit een eigen, gelabelde en waar nodig geteste analyse. De interne M05-analyse van Hybrid-Theory zelf wordt **niet** gepubliceerd.

## Relatie met de academische onderzoeksachtergrond

De [masterscriptie (2021)](../../../../Onderzoek/Academische-Referenties/scriptie-2021.md) onderzocht volatiliteitsspreiding tussen Europese sectoren en landen met DCC-GARCH en connectedness-analyse, met onderscheid tussen **transmitters** en **receivers** van schokken. M05 gebruikt dat als **conceptuele analogie**:

| Scriptie | M05 / Hybrid-Theory |
|---|---|
| Sector of land als transmitter of receiver | Node met veel uitgaande respectievelijk inkomende afhankelijkheden |
| Toenemende connectedness in een crisis | Toename van gedeelde afhankelijkheden bij een storing of wijziging |
| Spillover tussen sectoren | Spillover tussen IT, OT, governance en assurance |

**Grens:** DCC-GARCH is toegepast op financiële tijdreeksen en is **niet gevalideerd voor cyberrisico's**. In het lab bestaan geen vergelijkbare tijdreeksen. De analogie levert onderzoeksvragen op, geen methode, model of bewijs. Er wordt geen academische of methodologische meerwaarde geclaimd ([academische referenties](../../../../Onderzoek/Academische-Referenties/README.md#relevantie-voor-hybrid-theory)).

## Grenzen van traditionele controlgerichte beoordelingen (onderzoekshypothesen)

1. **Controlisolatie:** een SoA toont welke controls gekozen zijn, niet welke controls dezelfde component delen.
2. **Point-in-time:** een audit beoordeelt een moment; drift tussen beoordelingen valt buiten beeld ([CAT/ACE §7, gap 15](../../../../Governance/CAT_ACE_v0.4.md#7-typen-gap-analyses-welke-vraag-wordt-onderzocht)).
3. **Steekproef:** zeldzame cascades komen in een steekproef zelden voor.
4. **Grensverlies:** IT-, OT- en cloudcontrols worden vaak door verschillende teams en kaders beoordeeld; afhankelijkheden over die grens heen hebben geen eigenaar.
5. **Assurance op assurance:** beoordelingen die op dezelfde beoordelaar of hetzelfde hulpmiddel steunen, delen dezelfde blinde vlek.

Dit zijn **hypothesen**. Bestaande kaders adresseren delen ervan al (bijv. ISO/IEC 27005 voor risico-afhankelijkheden, IEC 62443 voor zones en conduits, NIST SP 800-160 Vol. 2 voor cyber resiliency). M05 moet aantonen óf en wanneer een dependency-analyse in dit lab iets toevoegt, en mag concluderen dat dat niet zo is.

## Toepasselijke frameworks

CAT/ACE v0.4 §8–§12 (dependency-analyse; experimenteel), ISO/IEC 27005:2022, ISA/IEC 62443-3-2 (zones en conduits; alleen bij OT-verdieping), NIST SP 800-160 Vol. 2 (cyber resiliency), NIST SP 800-34 / ISO 22301 (continuïteit en herstel) en MITRE ATT&CK for ICS.

## Verwachte evidence en deliverables

- Dependency-regels per casus in de casusmatrix: node, edge-type, bron, labels voor afhankelijkheid en gevolg, en de getroffen controls.
- Een concentratieoverzicht: welke controls en claims delen dezelfde node.
- Een expliciete lijst van hypothesen tegenover waarnemingen.
- Bij een goedgekeurde test: de voorspelling vooraf, ground truth, rollbackbewijs en de conclusie.

## Kwaliteitscriteria

- Elke afhankelijkheid en elk gevolg heeft een eigen herkomstlabel.
- Een afhankelijkheid heet pas "bevestigd" na een directe waarneming of een gecontroleerde test; een architectuurdiagram is geen bewijs.
- Negatieve uitkomsten ("geen extra inzicht") worden bewaard.

## Beperkingen

- Correlatie en plausibiliteit zijn **geen** causaliteit.
- Geen fault-injection zonder ownerbesluit, rollback en veiligheidsgrenzen; geen OT-safetyrisico.
- Onbekende edges worden niet als ontbrekend gerekend (geen vals-negatieven construeren).
- De publieke versie bevat alleen methodiek en een fictief voorbeeld. Een eventuele dependency-analyse van de werkelijke omgeving blijft intern en wordt niet gepubliceerd.

## Relaties met andere hoofdstukken

Verbreedt [05.2](../05.2_Risk_to_Control_Traceability/README.md) van lineaire ketens naar netwerken. Verklaart waarom losse PASS-oordelen in [05.3](../05.3_Control_Effectiveness/README.md) samen kunnen falen. Geeft gaps in gedeelde nodes extra gewicht in [05.4](../05.4_Gaps_and_Exceptions/README.md). Maakt afhankelijkheid van één beoordelaar zichtbaar voor [05.5](../05.5_Assurance_and_Independence/README.md). Redundantie tegenover concentratie is een kostenvraag in [05.6](../05.6_Cost_and_Efficiency/README.md).

## Huidige onderzoeksstatus

**PENDING.** Methodiek beschreven; het voorbeeld is fictief (SIMULATED). In M05 is geen dependency-analyse of -test uitgevoerd.
