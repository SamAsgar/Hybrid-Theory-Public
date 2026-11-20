# 05.7 — Systemic Risk | M05 Compliance Sentinel

**Hoofdstukstatus:** structuur **APPROVED**; inhoudelijk werk **PENDING** · [Terug naar M05](../README.md)

> Dit hoofdstuk is de kern van het Hybrid-Theory-onderzoeksmotief. Elke voorbeeldafhankelijkheid hieronder heeft een herkomstlabel. Er is in M05 nog **geen** dependency- of fault-injectiontest uitgevoerd; **geen enkel cascade-effect is bewezen**.

## Doel

Onderzoeken hoe **gedeelde afhankelijkheden, single points of failure en keteneffecten** de impact van één falende component of control kunnen vergroten: over technische lagen, over IT/OT/cloud-grenzen en over governance heen. En onderzoeken waar **traditionele controlgerichte beoordelingen** zulke effecten structureel missen.

## Waarom dit een apart hoofdstuk is

Control-assessments (een SoA, een controlcatalogus, een steekproefaudit) beoordelen maatregelen meestal **één voor één**: segmentatie (A.8.22), logging (A.8.15), monitoring (A.8.16), back-up (A.8.13). Elk kan afzonderlijk een PASS krijgen. Als die controls echter **dezelfde component, dezelfde beheerder of dezelfde aanname** delen, kunnen ze tegelijk falen. Dat patroon, *common-mode failure*, is zichtbaar in een afhankelijkheidsgraaf, maar niet in een lijst van losse controls.

## Begrippen

De failure modes komen uit [CAT/ACE v0.4 §8](../../../governance/CAT_ACE_v0.4.md#8-dependency-analyse-relaties-kwetsbaarheid-en-causale-voorzichtigheid) en worden hier toegepast:

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
| **OBSERVED** | Feitelijk opgetreden in een gedateerde test of gebeurtenis, alleen binnen die scope. Staat erbij als de bron niet publiek is. |
| **DOCUMENTED** | Vastgelegd in publieke configuratie- of architectuurdocumentatie. Zegt niets over gedrag bij falen. |
| **HYPOTHESIS** | Plausibele relatie of plausibel gevolg, nooit gericht getest. |
| **SIMULATED** | Fictieve organisatie- of bedrijfscontext, bijvoorbeeld een gesimuleerde proceseigenaar of bedrijfsimpact. |
| **NOT VERIFIED** | Er is onvoldoende bewijs om de uitspraak te beoordelen; geen aanname van een defect. |

### Predict-then-break

1. Leg de werkende baseline vast.
2. Formuleer **vooraf** welk effect een gecontroleerde, omkeerbare verstoring volgens de graaf zou moeten hebben, plus een tegenhypothese.
3. Voer de verstoring uitsluitend uit na expliciet besluit van Sam, met rollback en binnen eigen systemen ([Labkader](../../../governance/LAB_KADER.md)).
4. Vergelijk de waarneming (ground truth) met de voorspelling en met wat een reguliere controlbeoordeling had gevonden.
5. Herstel en valideer. De uitkomst is bevestigd, gedeeltelijk bevestigd, weerlegd of onvoldoende bewijs.

[CAT/ACE §12](../../../governance/CAT_ACE_v0.4.md#12-illustratief-scenario-addns-als-gedeelde-afhankelijkheid) beschrijft zo'n scenario voor AD/DNS. Dat scenario is uitdrukkelijk **niet uitgevoerd**.

### Concentratiebeschouwing

Per node tellen hoeveel controls of claims ervan afhangen. Dit is een onderzoeksidee, **geen gevalideerde metriek**.

## Methodologisch voorbeeld (gesaneerd)

Het voorbeeld laat de redenering zien op basis van **publiek gedocumenteerde** kenmerken van het lab. Het is geen volledige inventaris en noemt geen adressen, beheerroutes of open technische zwaktes.

| # | Node | Afhankelijkheid | Label | Mogelijk gevolg bij falen | Label |
|---|---|---|---|---|---|
| E1 | **Firewall-VM** | Handhaaft de zonegrenzen en levert DHCP aan de LAB-zone ([pfSense-plan](../../../architectuur/PFSENSE_PLAN.md)) | DOCUMENTED | Gelijktijdige impact op LAB-diensten, de segmentatieclaim en de firewalllogs die als bewijs dienen. Of de firewall daarbij open of dicht faalt, is onbekend. | HYPOTHESIS; gedrag bij falen NOT VERIFIED |
| | | Tijdens een eerdere labsessie (4 nov.) kreeg een LAB-VM geen DHCP-lease zolang de firewall-VM uit stond; na het starten wel | OBSERVED (bronlog niet publiek; extern niet onafhankelijk verifieerbaar) | | |
| E2 | **Virtualisatiehost** | Eén Windows-host met VMware Workstation draagt de lab-VM's; een tweede host is gepland ([Hardware Baseline](../../../governance/HARDWARE_BASELINE.md)) | DOCUMENTED | Een hostfout raakt alle zones en controls tegelijk (common cause) | HYPOTHESIS |
| E3 | **Identiteitsdienst** | Eén domain controller levert AD DS en DNS; domain join en login werkten binnen de geteste scope ([AD-baseline](../../../projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md)) | OBSERVED (scoped) | Een DNS-storing die zich voordoet als authenticatie- of GPO-probleem | HYPOTHESIS; NOT VERIFIED |
| E4 | **Tijdbron** | Een afzonderlijke externe tijdbron is nog niet ingericht (open punt in de AD-baseline) | DOCUMENTED | Onbetrouwbare correlatie van client-, firewall- en capturebewijs, waardoor meerdere controls tegelijk slechter aantoonbaar worden (A.8.15–8.17) | HYPOTHESIS |
| E5 | **Herstelvoorziening** | Een snapshot bestaat, maar herstel is niet getest; een onafhankelijke restore is niet aangetoond ([besluitenoverzicht](../../../governance/BESLUITENLOG.md), [M02](../../../governance/M02-Phoenix-Recovery/README.md)) | DOCUMENTED | Recovery coupling: herstel leunt op dezelfde host die kan falen (E2) | HYPOTHESIS |
| E6 | **Monitoringlaag** | Dashboardtoegang is getest; agentdetectie is niet aangetoond ([README](../../../README.md)) | DOCUMENTED | Een falende control wordt niet automatisch gesignaleerd, waardoor de impact van E1–E5 later zichtbaar wordt | HYPOTHESIS |
| E7 | **Bedrijfsfunctie en risico-eigenaar** | Een fictieve OT-proceseigenaar draagt het risico van procesverstoring | SIMULATED | Een technische storing wordt een bedrijfs- en governancevraag (spillover naar besluitvorming) | SIMULATED |
| E8 | **Beoordelaar + AI-ondersteuning** | Eén persoon voert uit en beoordeelt, met AI-begeleiding ([AI-samenwerking](../../../ai-samenwerking/README.md)) | DOCUMENTED | Een gedeelde blinde vlek in meerdere beoordelingen tegelijk ([05.5](../05.5_Assurance_and_Independence/README.md)) | HYPOTHESIS |

**Voorbeeld van een cascadehypothese (HYPOTHESIS, niet getest):**

```text
E2 host faalt ──requires──▶ E1 firewall-VM niet beschikbaar
   E1 ──routes/serves──▶ LAB-diensten (DHCP) en zonegrens
   E1 ──protects──▶ A.8.22-claim (segmentatie)
   E1 ──logs──▶ bewijs voor A.8.22 en A.8.15
   E6 ──monitors──▶ (geen automatische signalering)
   E5 ──recovers──▶ leunt op E2  → recovery coupling
```

Alleen de DHCP-afhankelijkheid in E1 en de scoped identiteitsafhankelijkheid in E3 zijn ooit feitelijk waargenomen. De keten hierboven is een **voorspelling** die pas na een goedgekeurde, omkeerbare test iets mag bewijzen. Er is geen incident van deze aard opgetreden.

## Relatie met de academische onderzoeksachtergrond

De [masterscriptie (2021)](../../../onderzoek/academische-referenties/scriptie-2021.md) onderzocht volatiliteitsspreiding tussen Europese sectoren en landen met DCC-GARCH en connectedness-analyse, met onderscheid tussen **transmitters** en **receivers** van schokken. M05 gebruikt dat als **conceptuele analogie**:

| Scriptie | M05 / Hybrid-Theory |
|---|---|
| Sector of land als transmitter of receiver | Node met veel uitgaande respectievelijk inkomende afhankelijkheden |
| Toenemende connectedness in een crisis | Toename van gedeelde afhankelijkheden bij een storing of wijziging |
| Spillover tussen sectoren | Spillover tussen IT, OT, governance en assurance |

**Grens:** DCC-GARCH is toegepast op financiële tijdreeksen en is **niet gevalideerd voor cyberrisico's**. In het lab bestaan geen vergelijkbare tijdreeksen. De analogie levert onderzoeksvragen op, geen methode, model of bewijs. Er wordt geen academische of methodologische meerwaarde geclaimd ([academische referenties](../../../onderzoek/academische-referenties/README.md#relevantie-voor-hybrid-theory)).

## Grenzen van traditionele controlgerichte beoordelingen (onderzoekshypothesen)

1. **Controlisolatie:** een SoA toont welke controls gekozen zijn, niet welke controls dezelfde component delen.
2. **Point-in-time:** een audit beoordeelt een moment; drift tussen beoordelingen valt buiten beeld ([CAT/ACE §7, gap 15](../../../governance/CAT_ACE_v0.4.md#7-typen-gap-analyses-welke-vraag-wordt-onderzocht)).
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
- De publieke versie toont een gesaneerd voorbeeld. De volledige interne dependency-inventaris is niet publiek, en uitspraken die daarop steunen zijn extern niet onafhankelijk verifieerbaar.

## Relaties met andere hoofdstukken

Verbreedt [05.2](../05.2_Risk_to_Control_Traceability/README.md) van lineaire ketens naar netwerken. Verklaart waarom losse PASS-oordelen in [05.3](../05.3_Control_Effectiveness/README.md) samen kunnen falen. Geeft gaps in gedeelde nodes extra gewicht in [05.4](../05.4_Gaps_and_Exceptions/README.md). Maakt afhankelijkheid van één beoordelaar zichtbaar voor [05.5](../05.5_Assurance_and_Independence/README.md). Redundantie tegenover concentratie is een kostenvraag in [05.6](../05.6_Cost_and_Efficiency/README.md).

## Huidige onderzoeksstatus

**PENDING.** De voorbeeldafhankelijkheden zijn gedocumenteerde kenmerken, twee scoped waarnemingen en verder hypothesen. In M05 is geen dependency-test uitgevoerd.
