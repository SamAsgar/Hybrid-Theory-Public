# CAT/ACE v0.4 — Audit, Cost & Efficiency | Evidence-Driven Assurance & Dependency Research

**Auteur en conceptontwikkeling:** Project Owner / @SamAsgar  
**Versie:** v0.4 | 3 november 2026  
**Onderzoeksstatus:** **CONCEPT / NOT VALIDATED**  
**Onderzoeksomgeving:** Hybrid-Theory  
**Type document:** onderzoeksvoorstel, referentiekader en voorlopig experimenteel protocol  
**Afbakening:** geen erkende auditnorm, formele certificering, complianceverklaring of aangetoonde superioriteit boven bestaande methoden

> **CAT/ACE v0.4 is een experimenteel, modulair onderzoeksmodel dat de CAT-lagen (Corporate Governance & Compliance, Accountability & Management en Technology & Operations) koppelt aan ACE: Audit, Cost & Efficiency. ACE kan als interne, externe of hybride beoordelingsfunctie worden uitgevoerd.**
>
> Dit is een **eigen onderzoeksconcept van de Project Owner**. Bestaande frameworks zoals **COBIT, ISO/IEC 27001 en NIST CSF** behandelen governance en management al. **De drie lagen zijn op zichzelf geen nieuwe uitvinding.** De te onderzoeken meerwaarde ligt in een **reproduceerbare koppeling** van verantwoordelijkheden, technische controls, systeemafhankelijkheden, gecontroleerde foutinjectie, bewijsvoering en restrisicobesluiten.
>
> De ontwikkeling is **evidence-driven**: resultaten kunnen de aannames ondersteunen, nuanceren **of weerleggen**. CAT/ACE is **niet bewezen beter** dan bestaande beoordelingsprocedures. De daadwerkelijke meerwaarde moet worden onderzocht met vooraf bepaalde criteria en onafhankelijke vergelijking.

## 1. Onderzoeksmotief en onderzoeksvraag

Veel bestaande kaders bieden al volwassen manieren om beveiligingsdoelen, risico's, processen en technische controls te beoordelen. De onderzoeksvraag is daarom **niet** of governance en techniek voor het eerst bij elkaar kunnen worden gebracht. De vraag is of een reproduceerbaar onderzoeksproces in een gesimuleerde hybride omgeving, met **interne, externe of hybride Audit / Cost / Efficiency-beoordeling**, aantoonbaar betere inzichten in controlwerking, afhankelijkheden, totale kosten en veilige optimalisatie kan leveren **zonder** verlies van auditkwaliteit of beveiliging.

**Centrale onderzoeksvraag**

> In hoeverre kan een geïntegreerde **interne, externe of hybride Audit / Cost / Efficiency-beoordeling**, verbonden met governance, management, technische controls en dependency-analyse, aantoonbare meerwaarde bieden bij het herkennen en beheersen van cybersecurityrisico's én het onderbouwen van doelmatige beveiligingsbesluiten ten opzichte van passende bestaande procedures?

**Deelvragen**

1. Welke technische en organisatorische afhankelijkheden worden met reguliere control- en gap-assessments al herkend, en welke blijven onder de gekozen scope onzichtbaar?
2. Kunnen gerichte *predict-then-break*-experimenten plausibele single points of failure, common causes, cascading failures en root causes betrouwbaar bevestigen of weerleggen?
3. Kunnen bevindingen van technische configuratie en testbewijs in beide richtingen worden gekoppeld aan eigenaarschap, beleid, bedrijfsimpact en restrisicobesluiten?
4. Hoe verhouden de totale kosten van technische beheersing, assessment, onderhoud en herstel zich tot die van passende alternatieven bij vergelijkbare beveiligingsuitkomsten?
5. Onder welke omstandigheden levert de aanpak **geen** voordeel op, creëert zij belangenconflicten, of produceert zij vals-positieve afhankelijkheden, schijnbesparingen en onnodige beoordelingslast?

**Herkomst van de onderzoeksvraag:** [masterscriptie over systemisch risico en financiële spillover-effecten](../onderzoek/academische-referenties/scriptie-2021.md) biedt academische inspiratie voor het herkennen van transmitters, receivers en keteneffecten. Een economische connectedness-analyse of DCC-GARCH-model is daarmee **niet automatisch gevalideerd voor cybersecurity**.

## 2. Conceptueel model: CAT-structuur en ACE-beoordelingsfunctie

De drie lagen worden gebruikt om onderzoeksvragen en bewijs *te ordenen*, niet als claim dat een nieuwe governancearchitectuur is uitgevonden.

| Laag | Volledige naam | Onderzoeksvragen | Voorbeelden van bewijs |
| --- | --- | --- | --- |
| **C / Layer 03** | **Corporate Governance & Compliance** | Welke bedrijfsdoelen, wettelijke eisen, risicotolerantie, policies en formele verplichtingen zijn relevant? | Toepasselijkheidsmatrix, fictief beleid, risico-/controlmapping, besluitenregister |
| **A / Layer 02** | **Accountability & Management** | Wie is eigenaar, wie implementeert, wie autoriseert, wie monitort en wie mag restrisico accepteren? | RACI, wijzigingsbesluit, fictieve proceseigenaar, reviewlog, risicobehandeling |
| **T / Layer 01** | **Technology & Operations** | Welke services, identiteiten, configuraties, protocollen en afhankelijkheden realiseren of bedreigen de beoogde uitkomst? | VM-configuratie, pfSense-regels, DNS/SRV-tests, GPO-resultaten, packet captures, restore-test |

**ACE = Audit, Cost & Efficiency**: één beoordelingsfunctie **over** de CAT-lagen, geen vierde organisatorische laag en **geen verplichte derde partij**.

- **A / Audit:** toets de toepasbare eisen én de geselecteerde controls op opzet, implementatie, feitelijke werking, bewijs en restrisico. Beoordeel onafhankelijkheid en competente reviewer; een technische PASS bewijst geen volledige wettelijke naleving.
- **C / Cost:** bepaal directe en indirecte kosten van huidige beheersing en alternatieven: licenties, hardware, cloud, energie, mensen, onderhoud, incidenten en herstel. Maak **MEASURED** versus **ESTIMATED** transparant.
- **E / Efficiency:** vergelijk **gelijke of betere beveiligingsuitkomsten** met de benodigde middelen, doorlooptijd, foutkans en complexiteit. Minder kosten ten koste van vereiste beveiliging is géén efficiëntieverbetering.

**Anti-dubbeling:** **CAT-C definieert vereisten en toepasselijkheid; ACE-Audit beoordeelt deze één keer per gescopeerd controlrecord.** CAT-A legt eigenaarschap en risicobesluiten vast, CAT-T de daadwerkelijke techniek. ACE-Cost en ACE-Efficiency gebruiken hetzelfde evidence- en risico-object en rapporteren geen afzonderlijke 'compliance-PASS'.

**Uitvoeringsvorm:** Internal ACE (interne audit-/risk-/securityfunctie), External ACE (externe auditor/specialist) of Hybrid ACE (interne controles met een onafhankelijke interne of externe second review). *Intern* kan objectief zijn, maar is niet per definitie onafhankelijk; *extern* is evenmin automatisch onafhankelijk. Leg maker, beoordelaar, adviesrol en mogelijke belangenconflicten vast. Een AI-review of zelftest is geen formele onafhankelijke certificeringsaudit.

**Automation** blijft een waardevolle **werkwijze voor herhaalbaarheid** en bewijskwaliteit, maar is in v0.4 géén aparte ACE-letter. Volledige compliance is **geen voorwaarde** om kosten en alternatieven te onderzoeken; bij besluiten blijven de toepasselijke eisen en vastgestelde risicogrenzen leidend.

Een afbeelding met drie lagen is **geen** bewijs dat de relaties, beheersing of organisatieprocessen functioneren. Binnen het persoonlijke lab is de managementlaag grotendeels **gesimuleerd**.

## 3. CAT/ACE v0.4 in de praktijk — uitvoerbaar protocol en vier casussen

> **Leidraad, geen uitgevoerd auditrapport.** De onderstaande voorbeelden beschrijven **voorgestelde assessments**. Reeds behaalde technische lab-PASS-verdicts behouden hun eigen beperkte scope. Organisatorische rollen in de onderzoeksomgeving zijn **SIMULATED**, bedragen zijn uitsluitend werkelijk gemeten wanneer dat expliciet staat, en een ACE-beoordeling is geen certificeringsaudit.

### 3.1 Van CAT-inventarisatie tot ACE-besluit

| Fase | Uitvoering in een echte of gesimuleerde organisatie | Minimale output |
| --- | --- | --- |
| **CAT-C: define** | Bepaal scope, kritieke bedrijfsdoelen, eisen, norm-/controlversie, verplicht of vrijwillig, en onderbouw N/A | Requirement-ID, eigenaar van beleid, toepasselijkheidsbesluit |
| **CAT-A: assign** | Benoem control owner, service owner, risk owner, besluitbevoegde en reviewrollen | RACI, change-/exception-ID, beslislog |
| **CAT-T: map** | Leg services, firewallregels, accounts, DNS, VM's, netwerkzones en afhankelijkheden vast | Configbaseline, diagram, control-to-systemmapping |
| **ACE-A: Audit** | Onderzoek control design, implementatie, operationele effectiviteit, positieve/negatieve tests, logs, evidence en afwijkingen | Eén controlrecord met scopegebonden PASS/REWORK/EXCEPTION/N/A/NOT VERIFIED |
| **ACE-C: Cost** | Meet of schat aanschaf, cloud/licentie, energie, opslag, arbeid, onderhoud, downtime en herstel; vergelijk gelijkwaardige periode | Kostenbaseline en aannameregister (MEASURED/ESTIMATED) |
| **ACE-E: Efficiency** | Vergelijk status quo met minimaal één alternatief onder dezelfde beveiligings-, beschikbaarheids- en risicogrenzen | Trade-offmatrix met kosten, veiligheidsimpact, complexiteit en effort |
| **Decision** | Laat bevoegde eigenaar maatregel, geen wijziging of tijdelijke exception autoriseren | Verantwoord besluit + restrisico |
| **Revalidation** | Herhaal relevante checks na wijziging; analyseer drift en onverwachte interacties | Nieuw testbewijs met datum, reviewer, scope en verdict |

Deze volgorde is **logisch, niet strikt sequentieel**: Cost/Efficiency mogen parallel aan audit en remediation worden onderzocht. Een tekortkoming kan juist extra analyse vergen om de goedkoopste **verantwoorde** hersteloptie te vinden. Besparen is nooit het automatische einddoel: **'geen verantwoorde besparing' is een legitieme uitkomst**.

### 3.2 Wie voert ACE uit? Internal, External en Hybrid

| Vorm | Reële werkverdeling | Belangenconflict/waarborg | Voorbeeld in Hybrid-Theory |
| --- | --- | --- | --- |
| **Internal ACE** | Interne audit, security, risk of compliance toetst eigen omgeving | Maker van de control en reviewer onderscheiden; self-check niet als onafhankelijke review verkopen | Eigen validatietest met expliciete aanduiding **SELF-ASSESSMENT** |
| **External ACE** | Externe specialist/auditor met afgesproken testscope en bewijstoegang | Externe consultant mag eigen ontwerp niet zonder scheiding onafhankelijk goedkeuren | Externe review van gesaneerde evidence, **alleen als daadwerkelijk uitgevoerd** |
| **Hybrid ACE** | Interne voorbereiding en tests, gevolgd door risicogerichte tweede review | Scope, reviewer, beoordelingscriteria en eventuele onafhankelijke hertest vastleggen | Interne configuratiecheck + afzonderlijke reviewer van kritieke uitkomsten |

**Opdrachtgeverschap:** CAT-A bepaalt wie externe opdracht verleent, wie adviezen mag overnemen en wie restrisico kan accepteren. ACE adviseert; de auditor **neemt geen managementbesluit**. Bij certificering/attestatie gelden aanvullende beroeps- en onafhankelijkheidsregels buiten deze experimentele methode.

### 3.3 Praktijkvoorbeeld 1: pfSense — segmentatie, tijdelijke internetregel en rule review

**Startpunt.** Een labclient krijgt tijdelijk internet via pfSense. Een te brede firewallregel kan ongewenste bereikbaarheid creëren. De huidige pfSense/Kea-gateway- en clienttests zijn beperkt gerapporteerd; **een volledige ACE-segmentatieaudit is nog niet aangetoond**.

| CAT/ACE-stap | Voorgestelde concrete actie | Bewijs en besliscriterium |
| --- | --- | --- |
| **CAT-C** | Schrijf een fictieve security requirement: 'alleen expliciet geautoriseerde LAB-clientstromen; MGMT/trust boundary blijft gesloten' | Policy-ID; gekozen CIS/NIST/vendorreferentie; **SIMULATED** beleidscontext |
| **CAT-A** | Wijs change- en risico-eigenaar toe; autoriseer bron, doel, protocol, looptijd en eventuele uitzondering | Fictief wijzigingsbesluit, tijdslimiet, verantwoordelijke; uitzondering is **geen PASS** |
| **CAT-T** | Leg LAB-interface, DHCP-pool, NAT, firewallvolgorde, routes en logconfig vast | Gesaneerde rule-export, configuratieversie en topologie |
| **ACE-Audit / Examine** | Controleer first-match-rulevolgorde, scope, onbedoelde brede allow-regels en tijdelijke uitzonderingen | Reviewchecklist en config evidence, maar nog **geen** bewezen netwerkisolatie |
| **ACE-Audit / Test** | Test **positief** toegestane clientverbindingen; test **negatief** bewust ongeautoriseerde doel-/zone-/poortstromen; correleer logs | Alleen positief + negatief onderbouwde teststromen kunnen een scopegebonden PASS opleveren |
| **ACE-Cost** | Registreer benodigde beheer- en reviewminuten, logging-/VM-ruimte en eventuele herstelinspanning | Tijdsregistratie, kosten per uur en frequentie; geen gefingeerde besparingen |
| **ACE-Efficiency** | Vergelijk (1) handmatige review van bestaande regel en (2) smallere least-privilege-regel met herhaalbare testset | Verbetering alleen als dezelfde noodzakelijke businessflow blijft werken én niet-toegestane flows geblokkeerd blijven |
| **Revalidation** | Na wijziging: herhaal verbindingstests, inspecteer logs en controleer rollback | Nieuw verdict per test en datum, geen automatische overerving van eerdere PASS |

**Rekenvoorbeeld, uitsluitend HYPOTHETICAL:** 40 minuten handmatige review versus 15 minuten met een gevalideerd script bespaart per gelijkwaardige wijziging 25 minuten. Bij 12 wijzigingen per jaar is dat 300 minuten (5 uur), **maar alleen** vóór onderhoud en scriptontwikkeling, én slechts als false positives/negatives en veiligheid gelijkwaardig zijn. Meet dit in echte experimenten voordat 'bespaard' wordt gerapporteerd.

**Voorbeeldbesluit:** *REWORK* voor ongeteste deny-stromen; *NOT VERIFIED* voor volledige isolatie; *PASS* kan blijven staan voor eerder specifiek bewezen gateway/internetgedrag. Zo ontstaat geen nep-compliance uit één succesvolle ping.

### 3.4 Praktijkvoorbeeld 2: AD DS / DNS / GPO — gedeelde afhankelijkheid en redundantie

**Startpunt.** Een enkele domain controller levert in het lab AD DS en DNS. Clients gebruiken DNS/SRV-records, authenticatie en GPO. Basisinstallatie, domeinjoin, login en één GPO zijn beperkt **PASS**. Een cascade na DNS-uitval is **HYPOTHESIZED / NOT VERIFIED**.

| CAT/ACE-stap | Voorgestelde concrete actie | Bewijs en grens |
| --- | --- | --- |
| **CAT-C** | Definieer fictieve identity-/beschikbaarheidsdoelen en aanvaardbare onderbreking | Beschikbaarheidseis, gekozen control, RTO/RPO-doel (**SIMULATED**) |
| **CAT-A** | Wijs identity/service owner en risicoacceptant toe; documenteer single-DC-afweging | Fictieve RACI en expliciet restrisicobesluit |
| **CAT-T** | Breng Windows Server AD/DNS, Windows-client, GPO, netwerkpad en eventuele tijdafhankelijkheden in kaart | DNS/SRV- en loginbaseline, eventlogs, dependency graph |
| **ACE-Audit** | Meet werkende resolutie, authenticatie en GPO; voorspel het effect van een kleine, omkeerbare DNS-onderbreking; test alleen met vooraf gevalideerde rollback | Vergelijk ground truth met voorspelling; foutinjectie **niet als reeds uitgevoerd claimen** |
| **ACE-Cost** | Vergelijk single-DC met herstelvoorziening versus mogelijk tweede DC + back-ups: extra compute, storage, tijd, beheer | Gemeten/geschatte TCO over dezelfde periode, zonder gratis hardware aan te nemen |
| **ACE-Efficiency** | Beoordeel de verhouding tussen beschikbaarheid, beheerscomplexiteit, herstelbaarheid, licentie-/resourcekosten en downtime-impact | Een extra DC is niet automatisch doelmatig; enkel goedkope single-DC evenmin |
| **Revalidation** | Herstel DNS en controleer naamresolutie, domeinlogin, bedoelde GPO en eventuele afhankelijkheidsimpact | Nieuwe evidence, incidenttijdlijn en correcte status per control |

**Concrete beslisvariant:** wanneer een tweede DC meer beheerkosten veroorzaakt maar de fictieve bedrijfs-RTO wezenlijk verbetert, kan hogere uitgave rationeler zijn. ACE documenteert die *trade-off*, niet enkel de laagste factuur. **Een VM-snapshot is geen onafhankelijke off-host restore.**

### 3.5 Praktijkvoorbeeld 3: VMware Workstation — guest isolation en Phoenix Recovery

**Startpunt.** In M01 wordt VM-guest isolation onderzocht; sommige functies kunnen voor beheer expliciet als **EXCEPTION** worden toegestaan. M02 vereist een **onafhankelijke back-up én werkende restore**; die is nog niet aangetoond.

| CAT/ACE-stap | Voorgestelde concrete actie | Bewijs en grens |
| --- | --- | --- |
| **CAT-C** | Leg VM-isolatiedoel, minimale recovery-eis, RPO/RTO en autorisatiebeleid vast | Fictieve security- en continuïteitseisen |
| **CAT-A** | Wijs beheerder, control owner, herstelverantwoordelijke en uitzonderingseigenaar aan | Beslislog voor clipboard/shared folders/drag-and-drop, rollen **SIMULATED** |
| **CAT-T** | Inventariseer host/guest-instellingen, VMware Tools, VM-disks, snapshotafhankelijkheid en off-host medium | Gesaneerde instellingen en backup-/restorearchitectuur |
| **ACE-Audit** | Controleer isolatie per VM, uitzonderingen, en test echte herstelbaarheid vanaf een onafhankelijke kopie met integriteits- en functietest | Een instellingenscreenshot bewijst niet de veilige werking; een snapshot is geen restore-PASS |
| **ACE-Cost** | Leg capaciteit van externe opslag, energie/ruimte, encryptie, onderhoud, back-upfrequentie, restore-uren vast | Kosten en aannames, inclusief hersteltesttijd |
| **ACE-Efficiency** | Vergelijk handmatige settingcontrole met herhaalbaar script; vergelijk back-upopties onder hetzelfde RPO/RTO-doel | Minder opslag is niet efficiënt als herstel faalt; extra hardening kan gebruiksgemak kosten |
| **Revalidation** | Hercontroleer relevante isolatie en voer na wijziging een onafhankelijke restore uit | Gescopeerde nieuwe controle; M02 blijft PENDING tot bewezen herstel |

**Praktische prioritering:** de grootste winst kan eerst komen uit een **gevalideerd, herstelbaar back-upproces**, niet uit het optimaliseren van enkele minuten VM-review. ACE kan dus bewust **extra kosten aanbevelen** als de risicoreductie dat rechtvaardigt.

### 3.6 Praktijkvoorbeeld 4: IT/OT — FUXA HMI, OpenPLC en (toekomstige) Wazuh/Suricata-monitoring

**Startpunt.** Een geïsoleerd OT-simulatieontwerp koppelt een HMI (FUXA) aan een PLC-simulator (OpenPLC) en eventueel netwerk-/hostmonitoring. **Aanwezigheid van software betekent niet dat OT-zones, detectie en weerbaarheid al end-to-end zijn getest.** Geen interferentie met echte fysieke processen.

| CAT/ACE-stap | Voorgestelde concrete actie | Bewijs en grens |
| --- | --- | --- |
| **CAT-C** | Kies een fictieve OT-scope met beschikbaarheids-/safetydoelen; selecteer passende IEC 62443-/NIST OT-referenties | Toepasselijkheid per ICS-simulatie, geen wettelijke OT-claim |
| **CAT-A** | Wijs fictieve operations owner, safety reviewer, change approver en risico-eigenaar toe | Testtoestemming, abort-criteria en rollback, **SIMULATED** |
| **CAT-T** | Documenteer HMI, PLC-simulator, protocollen, VMware-netwerkzones, pfSense-regels en logging | Topologie, protocolflows, inventaris; alles uitsluitend op eigen systemen |
| **ACE-Audit** | Controleer geautoriseerde HMI/PLC-communicatie, ongewenste cross-zone verbindingen, toegestane serviceaccounts en bewijs van log-/detectiecoverage | Positieve én negatieve tests; geen risicovolle fysieke fault-injection |
| **ACE-Cost** | Inventariseer extra CPU/RAM, disk, ingest, beheeruren en eventuele toolingkosten van monitoring | Hardwaremeting, storage rate en operationele onderhoudslast |
| **ACE-Efficiency** | Vergelijk volledige logging met risicogerichte logging onder dezelfde detectie- en safety-eisen | Lagere resourcebelasting telt alleen als essentiële events en operationele werking behouden blijven |
| **Revalidation** | Verifieer na tuning opnieuw HMI/PLC-functionele communicatie, zoneblokkades, logdetectie en herstel | Alleen uitgevoerde tests als VERIFIED; overige **PLANNED / NOT VERIFIED** |

**Beslismoment:** ACE kan adviseren om bepaalde niet-kritieke logs minder frequent te bewaren, maar alleen wanneer de gekozen detectiedoelen, audittrail en wettelijke vereisten behouden blijven. Eventueel kan het adviseren **meer capaciteit** toe te voegen. Efficiëntie is *veilig resultaat per ingezette middelen*, geen wedstrijd wie het kleinste VM'tje kan draaien.

### 3.7 Eén gedeeld audit-/kosten-/efficiëntierecord

| Veld | Wat er concreet in moet |
| --- | --- |
| **Assessment-ID / datum / scope** | Unieke controle, periode, netwerkgrens, gecontroleerd systeem |
| **ACE-positie en onafhankelijkheid** | INTERNAL, EXTERNAL of HYBRID; reviewer, onafhankelijkheid, eigen werk, belangenconflict |
| **CAT-C** | Requirement/control-ID, bron/versie, toepasselijkheid, N/A-motivatie |
| **CAT-A** | Owner, besluitbevoegde, eventuele gesimuleerde rol, akkoord/exception |
| **CAT-T** | Configbaseline, dependency edges, wijzigings- en logreferenties |
| **ACE-Audit** | Opzet, implementatie, daadwerkelijke werking, positieve/negatieve tests, bewijs/provenance, verdict |
| **ACE-Cost** | Periode, eenheid, meetbron, kostenbaseline, MEASURED/ESTIMATED en TCO-aannames |
| **ACE-Efficiency** | Status quo versus alternatief, identieke doelen/constraints, effort en complexiteit |
| **Decision & risk** | Gekozen optie, afgewezen alternatieven, restrisico, autorisatie |
| **Revalidation** | Hertest na wijziging, reviewer, evidence, nieuwe status, regressie |

**Geen dubbele compliance-PASS:** CAT-C beschrijft de eis; ACE-Audit levert een controleoordeel over **diezelfde eis** binnen een scope. Cost en Efficiency leveren aanvullende beslisinformatie, geen concurrerende nalevingsscore.

### 3.8 Wanneer optimalisatie wordt afgewezen

ACE moet ook expliciet kunnen concluderen **NO SAFE OPTIMIZATION IDENTIFIED**: wanneer een goedkopere back-up geen herstelgarantie geeft, een smallere loggingconfiguratie essentiële alarmsignalen mist of een automatiseringsscript meer onderhoud en foutkansen introduceert. Kostenonderzoek kan lopen terwijl een control nog REWORK is, maar de uiteindelijke wijziging blijft binnen vastgestelde beveiligings- en risicogrenzen.

## 4. Taxonomie van referentiekaders: niet alles is een regulatory framework

Het benchmarkprogramma gebruikt **alle relevante** kaders voor het concrete experiment, maar past ze niet blind allemaal tegelijk toe. Het is belangrijk juridische verplichtingen, normen, handreikingen en testprocedures **niet als uitwisselbare scores** te presenteren.

| Type | Voorbeelden | Wat de bron kan leveren | Wat de bron niet automatisch levert |
| --- | --- | --- | --- |
| **Wet- en regelgeving** | AVG/GDPR, NIS2 en toepasselijke nationale uitwerking, DORA | Juridische verplichtingen **indien van toepassing**, verantwoording, toezicht en meld-/beheervereisten | Een complete technische testprocedure of een automatische verplichting voor ieder lab |
| **Management- en governancekaders** | COBIT 2019, ISO/IEC 27001, ISO 19011 | Governance-/managementdoelen, ISMS-eisen, auditprincipes en verantwoordingslijnen | Bewijs dat een technische service werkelijk bestand is tegen verstoring |
| **Risico- en assuranceguidance** | ISO/IEC 27005, NIST SP 800-30, NIST RMF / SP 800-37 | Risico-identificatie, risicoanalyse, behandeling, selectie en monitoring | Een kant-en-klare controle voor ieder protocol of platform |
| **Uitkomstgerichte cybersecuritykaders** | NIST CSF 2.0 | Organisational Profiles, gewenste outcomes, governance/risk management | Voorgeschreven concrete firewall- of GPO-commando's |
| **Controlcatalogi** | CIS Controls v8.1, ISO/IEC 27002, NIST SP 800-53 Rev. 5 | Securitymaatregelen om te selecteren en te mappen op risico's | Zonder assessment geen bewijs van correcte implementatie |
| **Assessmentprocedures** | NIST SP 800-53A Rev. 5, CIS Controls Assessment Specification, ISO/IEC 27008 | Evidencevragen, control-assessment en meet-/beoordelingscriteria | Een nieuwe wet of universele vergelijking met alle overige procedures |
| **Technische configuratiebenchmarks** | CIS Benchmarks, vendor baselines, Microsoft Security Baselines | Platformspecifieke instellingen en afwijkingen | Organisatorische effectiviteit of end-to-end herstelbewijs |
| **Dreigings- en detectiemodellen** | MITRE ATT&CK, OWASP ASVS bij applicatietests | Realistische dreigings-/verificatiescenario's, coverage en technische eisen | Op zichzelf compliancecertificering of causaal bewijs |
| **OT-/ICS-specifieke referenties** | ISA/IEC 62443, NIST SP 800-82 Rev. 3 | Zones/conduits, OT-beveiligingsprocessen, veiligheid/beschikbaarheid | Automatische toepasselijkheid op een gewone IT- of providerrouter |
| **Veerkracht en continuïteit** | ISO 22301, CIS Control 11, NIST SP 800-34 | Business continuity en recovery-controls | Bewijs van een werkelijk uitgevoerde off-host restore |

**Selectieregel:** registreer per referentie: naam, versie/uitgave, type, toepasselijkheidsreden, control-/artikel-ID, bron-URL, gekozen toets, aannames, eventuele rechten/licentiebeperkingen en reden voor **N/A**. Een referentie die ongeschikt blijkt kan gedocumenteerd afvallen.

## 5. Kernframeworks: werking, bijdrage en relevante beperkingen

### 5.1 NIST Cybersecurity Framework 2.0

**Govern, Identify, Protect, Detect, Respond en Recover** bieden een taal voor cybersecurity-uitkomsten. De **Current Profile** en **Target Profile** maken een onderbouwde gap mogelijk; **Tiers** karakteriseren de inrichting van risicogovernance en management, niet één enkele hostconfiguratie.

**Toepassing:** bepalen welke bedrijfs- en security-outcomes een test ondersteunt; verschillen tussen huidig en beoogd profiel vastleggen; ontbrekende eigenaarschap- en herstelrelaties identificeren.

**Beperking:** het CSF schrijft niet voor welke CLI-regel in pfSense correct is. Gebruik daarvoor technische referenties en werkelijke tests.

**Bronnen:** [NIST CSF 2.0](https://www.nist.gov/cyberframework) · [CSF Tiers guidance](https://csrc.nist.gov/pubs/sp/1302/final).

### 5.2 ISO/IEC 27001:2022, ISO/IEC 27002:2022 en ISO/IEC 27005:2022

- **ISO/IEC 27001:** eisen voor opzetten, onderhouden en verbeteren van een ISMS, inclusief risicobehandeling, eigenaarschap, scope en managementverantwoordelijkheid.
- **ISO/IEC 27002:** guidance bij informatiebeveiligingscontrols; helpt geschikte maatregelen te selecteren en contextueel te interpreteren.
- **ISO/IEC 27005:** handreiking voor het herkennen, analyseren, evalueren, behandelen en monitoren van informatiebeveiligingsrisico's.

**Toepassing:** koppelen van een technisch controleprobleem aan de beoogde ISMS-control, verantwoordelijke, keuze tot risicoacceptatie en benodigde vervolgactie.

**Beperking:** een lab met een gesimuleerde directie en enkele tests is **geen gecertificeerd of volledig operationeel ISMS**. Een Statement of Applicability kan als **fictief onderzoeksartefact** dienen, nooit als bewijs van certificering.

**Bronnen:** [ISO/IEC 27001](https://www.iso.org/standard/27001) · [ISO/IEC 27005](https://www.iso.org/standard/80585.html).

### 5.3 COBIT 2019

COBIT onderscheidt **governance** van **management** en biedt doelen en modellen voor waardecreatie, besluitvorming, verantwoordelijkheden, processen en performance.

**Toepassing:** beoordelen of de technische eigenaar, controleverantwoordelijke, escalatie en risicoacceptatie logisch en aantoonbaar met de bedrijfsdoelen verbonden zijn.

**Beperking:** dit onderscheid en de governance-managementkoppeling **bestonden al vóór CAT/ACE**. De potentiële bijdrage van dit onderzoeksconcept moet dus in toetsbare cross-layer-evidence liggen, niet in het opnieuw benoemen van organisatiestructuren.

**Bron:** [ISACA COBIT](https://www.isaca.org/resources/cobit).

### 5.4 CIS Critical Security Controls v8.1 + Assessment Specification + CIS Benchmarks

De **18 CIS Controls** bieden een geprioriteerde set Safeguards. **Implementation Groups** ondersteunen selectie op basis van context. De **Assessment Specification** beschrijft inputs, operations, measures en metrics voor geselecteerde Safeguards; **CIS Benchmarks** geven veel concretere productspecifieke configuratieaanbevelingen.

**Toepassing:** van risico naar controle-eis en meetbaar configuratiebewijs, bijvoorbeeld secure configuration, account management, network infrastructure management en data recovery.

**Beperking:** de Assessment Specification en productbenchmarks vervullen **verschillende functies**. Een toegepaste setting bewijst geen effectief herstel na een storing.

**Bronnen:** [CIS Controls v8.1](https://www.cisecurity.org/controls/v8-1) · [Assessment Specification](https://www.cisecurity.org/controls/cis-controls-assessment-specification) · [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks).

### 5.5 NIST SP 800-53 en SP 800-53A Rev. 5

**SP 800-53** is een catalogus van security- en privacycontrols; **SP 800-53A** biedt procedures om geselecteerde controls te **assessen**. Relevante methoden zijn **Examine, Interview en Test**. Selecteer controlobjective, scope en passende diepgang, en leg bewijs/uitzonderingen vast.

**Toepassing:** een gecontroleerde vergelijking tussen een bestaande assessmentprocedure en een voorgestelde aanvullende dependency- of fault-injectiontest.

**Beperking:** NIST 800-53A bevat zelf al uitgebreide risicogestuurde en aanpasbare assessmentprocedures. Nieuwe onderzoekstests worden niet automatisch beter omdat ze een extra dependency graph toevoegen.

**Bronnen:** [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/final) · [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

### 5.6 ISO 19011 en auditpraktijk

**ISO 19011:2026** biedt richtlijnen voor het auditen van managementsystemen, zoals auditprogrammering, bewijs, onafhankelijkheid en auditcompetentie. Het is **auditguidance**, geen cybersecuritycontrolcatalogus.

**Toepassing:** beoordelaarsconsistentie, steekproefstrategie, bewijsbetrouwbaarheid, rapportage en omgaan met tegenstrijdig bewijs.

**Bron:** [ISO 19011](https://www.iso.org/standard/19011).

## 6. Contextspecifieke kaders en juridische toepasselijkheid

**Geen van deze kaders is per definitie verplicht voor een persoonlijk oefenlab.** Bij ieder scenario wordt eerst de **sector, entiteit, regio, data, diensten en juridische toepasselijkheid** beschreven.

| Referentie | Relevante scenario's | Voorbehoud |
| --- | --- | --- |
| **AVG/GDPR** | Verwerking van persoonsgegevens, privacy-by-design, toegangsbeveiliging, bewaartermijnen | Voor een fictief lab zonder persoonsgegevens geen automatische volledige juridische audit; gebruik waar relevant fictieve dataset en artikelmapping |
| **NIS2** | Organisaties/sectoren die onder toepasselijke EU- en nationale implementatie vallen; managementverantwoordelijkheid, risicobeheer en incidenten | EU-richtlijn en nationale implementatie niet verwarren; actuele Nederlandse toepasselijkheid afzonderlijk vaststellen |
| **DORA** | Bepaalde financiële entiteiten en ICT-derdenrisico's in financiële dienstverlening; resilience, testen en incidentmanagement | Niet automatisch van toepassing op de onderzoeksomgeving; wettelijke drempels/uitzonderingen toetsen |
| **ISA/IEC 62443** | Geautoriseerd, geïsoleerd OT-/ICS-lab met zones/conduits en gecontroleerde industriële protocollen | Veiligheid, beschikbaarheid en eigen systeemtoestemming gaan vóór foutinjectie |
| **NIST SP 800-82 Rev. 3** | OT-architectuur en bedreigings-/controlafweging met operationele en safety-eisen | Een gewone ISP-/thuisrouter is niet automatisch OT |
| **MITRE ATT&CK** | Detection engineering, logging en adversary-emulation in een eigen lab | Coverage is geen directe complianceclaim; geen aanvallen op externe systemen |
| **OWASP ASVS 5.0** | Wanneer een applicatie/API in scope komt | Niet geschikt als maatstaf voor een uitsluitend pfSense-firewalllab |
| **ISO 22301 / herstelreferenties** | Business continuity, afhankelijkheid van herstelservices en recoverydoelen | Een VMware-snapshot telt niet als bewijs van onafhankelijke off-host recovery |

**Officiële bronnen:** [AVG/GDPR (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2 (EUR-Lex)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [ISA/IEC 62443 (ISA)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) · [NIST OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [MITRE ATT&CK](https://attack.mitre.org/) · [OWASP ASVS](https://asvs.owasp.org/).

## 7. Typen gap-analyses: welke vraag wordt onderzocht?

Een *gap* is een **aantoonbaar verschil** tussen huidige toestand en expliciet gekozen eis, doel, benchmark of gewenste beheersing. Een vermoeden zonder geschikte evidence blijft **UNVERIFIED**. De onderstaande analysetypen overlappen deels; in een experiment mogen meerdere typen worden gecombineerd, mits er geen fictieve onafhankelijkheid of dubbele dekking wordt gerapporteerd.

| Type gap-analyse | Vergelijkingsbasis | Voorbeeld in Hybrid-Theory | Passend bewijs / beperking |
| --- | --- | --- | --- |
| **1. Regulatory & compliance gap** | Toepasselijke bepaling versus feitelijk proces/control | Fictieve verwerkingsactiviteit versus gekozen AVG-control | Juridische toepasselijkheid vooraf toetsen; geen fictieve compliance-PASS |
| **2. Governance/ownership gap** | Verwacht besluit-/risico-eigenaarschap versus vastgelegde rol | Wie autoriseert tijdelijke internettoegang of restrisico? | RACI en besluitlog; in lab **SIMULATED** |
| **3. Maturity/capability gap** | Current versus Target Profile of geschikt capabilitymodel | Van ad-hoc firewallwijzigingen naar reviewbaar wijzigingsproces | Heldere criteria; CSF Tiers niet omzetten naar willekeurige hostscore |
| **4. Control-design gap** | Beveiligingsdoel versus ontworpen werking | Firewallregel te breed voor de gewenste trust boundary | Architectuur + regelscope; design alleen bewijst geen effectiviteit |
| **5. Control-implementation gap** | Beoogde control versus feitelijke configuratie | Is de beoogde pfSense-regel of Windows-GPO geïnstalleerd? | Configuratie, beheerexport en gerichte verificatie |
| **6. Operating-effectiveness gap** | Geïmplementeerde control versus werkelijke testuitkomst | Blokkeert de firewall ook een ongeautoriseerde stroom? | Gerichte positieve én negatieve tests; protocol/scope vastleggen |
| **7. Technical configuration/hardening gap** | Vendor/CIS securitybaseline versus VM-/OS-instellingen | Guest Isolation, shared folders, accountrechten | Productspecifieke benchmark en versie; exception apart vastleggen |
| **8. Identity & access gap** | Least privilege en auth-flow versus feitelijke rechten | AD/GPO/login, gesimuleerde IAM-taken | Testaccount, resultaat, rechtenscope, geen productie-ID's |
| **9. Architecture/segmentation gap** | Trust boundary/zoneontwerp versus bereikbaarheid | LAB, MGMT, pfSense en toekomstige subnetten | Route-/regelpad + deny-tests; geen algemene isolatieclaim op één ping |
| **10. Dependency/systemic-risk gap** | Gevalideerde afhankelijkheidsgraaf versus gewenste veerkracht | Single DC/DNS, gedeelde gateway, cascaderende impact | *Predict-then-break*, meerdere observaties, alternatieve oorzaken |
| **11. Detection/monitoring gap** | Verwachte observatie- of detectiecoverage versus testincident | Logt pfSense het relevante blokkeer-event? | Log, tijdcorrelatie, ATT&CK-mapping waar passend |
| **12. Recovery/resilience gap** | Hersteldoelen en back-upbeleid versus echte recovery | Off-host backup en daadwerkelijke VM-/AD-restore | RPO/RTO-doel, restore-log, integriteits- en functionele checks |
| **13. Third-party/supply-chain gap** | Geselecteerde supplier-controls versus gedeelde afhankelijkheid | Cloud-IDP of providerconnectiviteit als externe afhankelijkheid | Contract/scope fictief; daadwerkelijke providerrechten respecteren |
| **14. Evidence/auditability gap** | Vereiste controleclaim versus bewijsvolledigheid | Screenshot bestaat, maar testtimestamp of negatieve test ontbreekt | Provenance, reproduceerbaarheid, scope en reviewer |
| **15. Continuous-assurance gap** | Geldige vorige PASS versus gewijzigde configuratie | Policywijziging na een geslaagde isolatietest | Change-detectie, beperkte regressietest, drift-tracking |
| **16. Automation/repeatability gap** | Handmatige beoordeling versus veilige herhaalbare toets | Script voor adapter-/regelcontrole | Automatisering is een middel binnen ACE, geen aparte letter; meet tijd en fout-positieven |
| **17. Cost / total-cost gap** | Huidige kostenbasis versus alternatief onder dezelfde beveiligingsvoorwaarden | Off-host back-up, reviewtijd, monitoring-capaciteit | TCO, periode en MEASURED/ESTIMATED scheiden |
| **18. Efficiency / outcome gap** | Beveiligingsresultaat per inspanning, tijd of totale kosten | Smalle pfSense-regel met geautomatiseerde regressietest | Veiligheidsniveau, onderhoud en risico moeten vergelijkbaar zijn |
| **19. Reviewer-independence gap** | Onafhankelijkheidsclaim versus werkelijke rol- en adviesconflicten | Eigen hardening zelf beoordelen | Markeer SELF-ASSESSMENT, interne/externe reviewer en beperkingen |

**Beoordelingscategorieën per geselecteerde eis**

- **PASS**: vereiste aantoonbaar gehaald binnen aangegeven scope.
- **REWORK**: eis niet gehaald of essentieel bewijs ontbreekt.
- **EXCEPTION**: aantoonbaar en expliciet geautoriseerd afwijkend risico; geen automatische PASS.
- **N/A**: eis buiten scope / aantoonbaar niet van toepassing, met reden.
- **NOT VERIFIED**: onvoldoende bewijs om een conclusie te trekken.

Een **maturity gap** is niet hetzelfde als een **technische misconfiguratie**. Een **control-design PASS** is niet hetzelfde als **operationele effectiviteit**. Het doel is juist deze verschillen zichtbaar te houden.

## 8. Dependency-analyse: relaties, kwetsbaarheid en causale voorzichtigheid

Een dependency graph bestaat uit **nodes** (services, technische componenten, processen, personen/rollen en controls) en **edges** (gerelateerde afhankelijkheden). Iedere edge krijgt een eigenaar/bron, bewijskwaliteit, status en, waar relevant, een richting en mogelijke impact.

**Voorgestelde relatiecategorieën:** `requires`, `authenticates`, `resolves`, `routes`, `trusts`, `monitors`, `stores`, `protects`, `recovers`, `authorizes`, `owns` en `accepts-risk`.

**Te onderzoeken failure modes:**

1. **Single point of failure (SPOF):** één noodzakelijke component zonder aangetoonde alternatieve route.
2. **Shared dependency:** meerdere diensten gebruiken dezelfde DNS, identiteit, opslag, netwerkroute, certificaat of beheerlaag.
3. **Common-cause failure:** een gedeelde foutbron beïnvloedt meerdere controls of systemen tegelijk.
4. **Cascading failure / spillover:** uitval of fout werkt door over meerdere afhankelijkheidsranden.
5. **Hidden dependency:** de relatie blijkt pas na een gerichte test of storing.
6. **Root cause versus symptoom:** uitval van een clientlogin kan een downstream-gevolg van DNS of tijdsafwijking zijn, in plaats van een direct accountprobleem.
7. **Recovery coupling:** herstel van de ene dienst vraagt juist de dienst die momenteel niet beschikbaar is.
8. **Control interaction:** een beveiligingsmaatregel verbetert een doel maar schaadt een ander doel, zoals beheerbaarheid of herstelbaarheid.

**Beoordeling van relaties (geen extra formele verdictstatus):** onderscheid tussen rechtstreeks bevestigde relatie, voorlopig aannemelijke relatie, onvoldoende onderzocht en een door de waarnemingen weerlegde hypothese. In het onderzoeksregister geldt bij ontbrekend bewijs de onderzoeksschaal **NOT VERIFIED**. **Correlatie en plausibiliteit zijn geen sluitend bewijs van causaliteit.** Waar foutinjectie niet verantwoord is, blijft de conclusie beperkt.

## 9. Traceability- en assuranceketen

Gebruik waar relevant de volgende bidirectionele keten:

```text
Business / Governance requirement
    → Security objective
    → Risk owner / control owner
    → Technical control & component
    → Baseline configuration
    → Validation test / fault-injection scenario
    → Observation & evidence (timestamp, scope, provenance)
    → Dependency / impact assessment
    → Risk decision: mitigate | accept | transfer | avoid
    → Remediation / exception / retest
```

In omgekeerde richting moet een technische afwijking terug te volgen zijn naar het **getroffen proces, verantwoordelijke actor en eventueel relevante eis**. Als geen actor of eis is vastgesteld, wordt het gat expliciet gemarkeerd in plaats van ingevuld op basis van aannames.

**Voorstel voor minimaal evidencerecord**

| Veld | Betekenis |
| --- | --- |
| Experiment-ID / versie | Unieke referentie en onderzoeksversie |
| Scope / trust boundary | Eigen VM's, segmenten en geautoriseerde systemen |
| Hypothese en tegenhypothese | Te bevestigen én te weerleggen verklaring |
| Toepasselijke benchmark | Versie, control-ID, normtype en N/A-onderbouwing |
| Baseline | Vastgelegde configuratie en reeds geldige PASS-tests |
| Voorspelling | Wat verwacht de onderzoeker vooraf te zien? |
| Gecontroleerde wijziging | Exacte toegestane foutinjectie, rollback en randvoorwaarden |
| Ground truth | Directe, onafhankelijke feitelijke observatie waar mogelijk |
| Resultaten baseline-assessments | Wat bestaande methoden hebben gevonden |
| Resultaten voorgesteld model | Extra of afwijkende bevindingen, zonder achteraf maatstaf te veranderen |
| Relatiebeoordeling | Bevestigd / aannemelijk / nog niet onderzocht / hypothese weerlegd; onderzoeksuitkomst afzonderlijk volgens de onderzoeksschaal |
| Evidencelinks | Gesaneerd, tijdgestempeld, toegangsveilig en reproduceerbaar |
| Risico en eigenaar | Impact, onzekerheid, te ondernemen actie en risicoacceptatie |
| Verdict | PASS / REWORK / EXCEPTION / N/A / NOT VERIFIED met scope |
| ACE-uitvoeringsvorm en onafhankelijkheid | INTERNAL / EXTERNAL / HYBRID; reviewer, maker, adviesbelang, eventuele conflicten |
| Cost & Efficiency | Gemeten/geraamde kosten, TCO-periode, status quo en alternatieven, beveiligingsgrenzen |
| Revalidation en beslisstatus | Autorisatie, restrisico, hertest en eventuele nieuwe beperkte PASS |

## 10. Experimenteel protocol: van hypothese naar toetsbare conclusie

Een **voorlopig protocol**, geen verplichte zware audit vóór elk technisch lab:

1. **Scope & hypothesis:** bepaal testobject, trust boundaries, toepasselijke eisen, hypothese, tegenhypothese, acceptatie- en stopcriteria.
2. **Baseline:** verzamel reeds bestaande geldige evidence, versie, topologie, tijdbron, instellingen en herstelroute.
3. **Controlled experiment:** voer binnen eigen geautoriseerde en herstelbare labgrenzen de beoogde verandering, beperkte storing of negatieve netwerkcheck uit.
4. **Ground truth:** leg vast wat werkelijk gebeurde; scheid directe observaties van interpretaties.
5. **Benchmark selection:** kies **alle relevante** normen, procedures en controls die een inhoudelijke bijdrage leveren, zonder ongeschikte bronnen kunstmatig mee te tellen.
6. **CAT/ACE v0.4 assessment:** pas CAT-C/A/T, **ACE-Audit, ACE-Cost en ACE-Efficiency** toe op dezelfde scope; leg INTERNAL/EXTERNAL/HYBRID, onafhankelijkheid, evidence, kostenbaseline, alternatieven en trade-offs vast. Het kostenonderzoek kan parallel aan remediation lopen.
7. **Comparison:** vergelijk met geselecteerde bestaande procedures op vooraf gedefinieerde criteria; registreer overlap, extra signalen, gemiste issues en onderzoeksinspanning.
8. **Remediation/rollback:** herstel de testomgeving veilig, documenteer beheersmaatregelen en eventuele eigenaar-exceptions.
9. **Conclusion & iteration:** rapporteer welke hypothese standhoudt, faalt of onzeker blijft; pas het *volgende* protocol aan zonder de uitslag van de huidige proef te herschrijven.

**Labprioriteit:** implementatie en veilige werking gaan vóór zware analyses. Bestaande geldige PASS-tests mogen worden hergebruikt. Het volledige protocol kan pas tijdens de onderzoeksvergelijking worden afgerond; het mag het bouwen van de basisinfrastructuur niet blokkeren.

**Onderzoeksambitie:** meer dan 100 labs/experimenten; dit is een **voornemen**, geen afgeronde dataset. Een mogelijke fasering is kalibratie → iteratieve ontwikkeling → bevroren onafhankelijke validatie → stress-/overdrachtstests. Na bevriezing mogen meetcriteria niet stilzwijgend worden aangepast om de uitkomst gunstiger te laten lijken.

## 11. Vergelijking met bestaande methoden: fair benchmarkdesign

**Basisprincipe:** een framework is niet altijd een assessmentprocedure. Vergelijk niet simpelweg een NIST CSF-outcome-taxonomie met een technisch foutinjectieprotocol alsof zij hetzelfde doel hebben.

**Vergelijkingsgroepen naar toepasbaarheid:**

- **Governance/managementbaseline:** een afgebakende ISO 27001- of COBIT-beoordeling.
- **Controlbaseline:** een geselecteerde CIS Safeguard, technische benchmark of NIST 800-53-control.
- **Assessmentbaseline:** passende NIST 800-53A-procedures (of een andere expliciet bestaande procedure) met dezelfde informatie en scope.
- **Onderzoeksuitbreiding:** de voorgestelde dependency-, cross-layer- en fault-injectionstappen.

Er mogen meerdere relevante bronnen per lab zijn. **Drie kaders is geen magisch minimum dat technische vergelijkbaarheid garandeert.** Selecteer representatieve procedures, documenteer waarom, en vermeld expliciet als een valide vergelijking onmogelijk is.

| Meetcriterium | Mogelijke meting | Noodzakelijke nuance |
| --- | --- | --- |
| **True positives / false positives** | Correct herkende versus onterecht gemelde problemen | Alleen wanneer ground truth bekend en labels onafhankelijk gecontroleerd zijn |
| **Dependency precision / recall** | Herkende, correcte edges versus alle relevante geverifieerde edges | Onbekende edges niet als foutieve negatieven presenteren |
| **Root-cause accuracy** | Juiste oorzaak herkend bij gecontroleerde fout | Uitkomst kan meerduidig blijven |
| **Evidence completeness** | Aandeel vereiste artefacten met provenance en relevante test | Veel screenshots ≠ sterk bewijs |
| **Traceability coverage** | Aandeel bevindingen gekoppeld aan control, eigenaar en risicobesluit | Gefingeerde governance-actor expliciet markeren |
| **Time-to-detect / time-to-assess** | Tijd tot probleemherkenning en beoordeling, in minuten | Zelfde startpunt en soort scenario gebruiken |
| **Automation / repeatability** | Reproduceerbaarheid en aantal handmatige stappen | Ondersteunende techniek binnen ACE; extra scripts kunnen onderhoud vergen |
| **Cost / total cost** | Kosten van beheer, licentie, cloud, opslag, tijd, incident en herstel | Gelijke meetperiode, bron, expliciete aannames en TCO |
| **Efficiency at fixed security outcome** | Effort en kosten per gelijkwaardige beveiligings-/beschikbaarheidsuitkomst | Alleen vergelijkbaar als controlwerking en risicogrenzen behouden blijven |
| **Reviewer independence** | Scheiding ontwerp/test/audit en vastgelegde rolconflicten | Extern is niet automatisch onafhankelijk; AI-review is geen formele audit |
| **Risk utility** | Relevantie van gevonden risico voor impact/prioritering | Ordinale beoordeling transparant, niet willekeurig samengestelde score |
| **Recovery validity** | Werkelijk herstel en controle van functies en integriteit | Snapshot-aanwezigheid telt niet als bewezen restore |
| **Inter-reviewer agreement** | Overeenstemming tussen reviewers bij dezelfde dataset | Reviewerbias en AI-overlap documenteren |

**Falsifieerbaarheid:** het concept faalt op een geselecteerde hypothese als bestaande procedures dezelfde relevante afhankelijkheden met vergelijkbare of betere nauwkeurigheid, bewijskwaliteit en inspanning herkennen, of als CAT/ACE aantoonbaar onbetrouwbare extra bevindingen produceert. **Negatieve resultaten blijven behouden.**

## 12. Illustratief scenario: AD/DNS als gedeelde afhankelijkheid

**Status: ONDERZOEKSCASUS / NIET UITGEVOERDE FAULT-INJECTIONTEST.**

**Hypothese:** in een beperkt lab kan een enkele AD/DNS-component een gedeelde afhankelijkheid vormen voor meerdere clients en processen. Controleverlies van DNS-resolutie kan dan op authenticatie lijken, zonder dat het primaire probleem bij het gebruikersaccount ligt.

**Voorgestelde observaties** (alleen na goedgekeurde rollback en binnen eigen VM's):

1. Observeer in de werkende baseline DNS-resolutie, SRV-records, domeinlogin, GPO en eventlogs.
2. Formuleer vooraf welk effect een **gecontroleerde** DNS- of netwerkonderbreking volgens de dependencygraph zou moeten veroorzaken.
3. Vergelijk geobserveerde foutmeldingen met de voorspelling en met reguliere config-, control- en operating-effectiveness-assessments.
4. Herstel de verbinding en valideer herstel van DNS, authenticatie en bedoelde GPO-toepassing.

**Bestaand labbewijs:** AD DS, DNS/SRV, domain join, testlogin en één GPO zijn in de beperkte basisopstelling eerder **PASS** gerapporteerd. **De hier beschreven foutinjectie en afgeleide cascading effects zijn nog NIET VERIFIED.** Ook is geen off-host restore-PASS behaald.

**Mogelijke resultaatcategorieën:** hypothese bevestigd binnen scope / gedeeltelijk bevestigd / weerlegd / onvoldoende bewijs. **Geen** causale conclusie trekken zonder betrouwbare testobservaties.

## 13. Evidence, veiligheid, validiteit en beperkingen

- **Technisch geobserveerd:** configuratie of gebeurtenis met relevante originele logs, context en gerichte test; een component krijgt alleen **VERIFIED** binnen de geteste scope.
- **Organisatorisch gesimuleerd:** fictief proces, managementactor of compliancecontext; nooit als echt organisatiebewijs gebruiken.
- **Hypothese of onderzoeksbeoordeling:** onbevestigde voorspellingen zijn niet als technisch bewijs te gebruiken; in het onderzoek geldt bij ontbrekend bewijs **NOT VERIFIED**.

**Veiligheidsgrenzen:** alleen eigen en expliciet geautoriseerde systemen, vooraf bepaalde rollback, geen secrets in screenshots/commits, geen onverwachte cloudkosten, geen ingreep aan provider-/thuissystemen buiten bevoegdheid. OT-tests mogen geen fysieke safety-risico's veroorzaken.

**Methodologische beperkingen:** steekproefbias bij eigen labs, afwezigheid van echte besluitvorming, beperkte aantallen storingen, scenario-afhankelijke resultaten, AI-reviewerbias, onvolledige ground truth, verschillen tussen frameworkdoeleinden en risico op overfitting aan een bekend lab.

**Belangrijke onderscheidingen:** een configuratie-PASS bewijst geen operating effectiveness; een test-PASS bewijst geen organisatiebrede naleving; een gesimuleerd risicoacceptatiebesluit is geen werkelijke juridische bevoegdheid; een conceptuele afhankelijkheid is geen bewezen oorzaak; een geanonimiseerd document is niet automatisch veilig voor publieke distributie.

## 14. Roadmap en open onderzoekspunten

| Onderdeel | Status |
| --- | --- |
| Concept en eerste lagen/ACE-definities | **DEFINED — EXPERIMENTAL** |
| Eerste technische basisomgeving (VMware/pfSense/Windows/Linux/GNS3) | **GEDEELTELIJK IMPLEMENTED/VERIFIED** binnen eerdere afzonderlijke tests |
| Systematische benchmarkselectie per scenario | **PLANNED** |
| Consistente dependencygraph en onafhankelijke ground truth | **PLANNED** |
| Repliceerbare vergelijking over meerdere labs | **PLANNED** |
| Onafhankelijke bevroren validatiefase | **PLANNED** |
| Bewezen hogere nauwkeurigheid of efficiëntie | **NOT ESTABLISHED** |
| Erkende auditmethodiek of certificering | **NOT CLAIMED** |

Bij de verdere ontwikkeling moeten onder meer **effectieve scoring zonder willekeur**, **N/A-regels**, onafhankelijke beoordelaars, traceerbaarheid, herbruikbare artefactformaten, multidimensionale efficiëntie, juridisch toepasselijkheidsbeheer en modellen voor onvolledige afhankelijkheidskennis worden onderzocht.

## 15. Bronnen, versiebeheer en gerelateerde documentatie

**Primaire officiële bronnen**

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework).
- [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).
- [CIS Critical Security Controls v8.1](https://www.cisecurity.org/controls/v8-1) en [CIS Controls Assessment Specification](https://www.cisecurity.org/controls/cis-controls-assessment-specification).
- [ISO/IEC 27001](https://www.iso.org/standard/27001), [ISO/IEC 27005](https://www.iso.org/standard/80585.html) en [ISO 19011](https://www.iso.org/standard/19011).
- [ISACA COBIT](https://www.isaca.org/resources/cobit).
- [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj), [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) en [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
- [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards), [NIST OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final), [MITRE ATT&CK](https://attack.mitre.org/) en [OWASP ASVS](https://asvs.owasp.org/).

**Intern gerelateerde publieke projectbestanden**

- [Governance-index](README.md).
- [Labkader en autorisatie](LAB_KADER.md).
- [Wet- en regelgeving](WET_EN_REGELGEVING.md).
- [Architectuurbaseline](../architectuur/ARCHITECTUUR_BASELINE.md).
- [Projectroadmap](../projectlogboeken/ROADMAP.md).
- [Technische evidence](../bewijsvoering/README.md).
- [Academische inspiratie: masterscriptie systeemrisico](../onderzoek/academische-referenties/scriptie-2021.md).

**Versiebeheer:** v0.4 is een **onderzoeksversie**, geen afgerond empirisch resultaat. De eerdere [v0.2](CAT_ACE_v0.2.md) blijft apart behouden. v0.3 werd als concept onderzocht; v0.4 gebruikt **Audit / Cost / Efficiency** intern, extern of hybride, zonder bewezen superioriteit. Wijzigingen in methodologie, evidenceclassificatie en benchmarkcriteria horen later expliciet gedateerd en verantwoord te worden. Gepubliceerde onderzoeksresultaten mogen niet achteraf worden aangepast aan een gewijzigde hypothese zonder vermelding.

---

**Onderzoeksprincipe:** *Frameworks bepalen niet vooraf welke conclusie uit een experiment moet volgen. De feiten kunnen het concept verbeteren, beperken of weerleggen.*

**Statusdefinities:** [STATUSLEGENDA](STATUSLEGENDA.md). De vijf labnamen en M01–M05 volgen de [roadmap](../projectlogboeken/ROADMAP.md); onderzoeksassessments zijn geen technische labverdicts.

**Conceptregistratie:** [HT-C-007 / CAT/ACE v0.4 in RTBL-HT-Concepts](https://github.com/SamAsgar/Hybrid-Theory/issues/2#issuecomment-6602136641). 

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
