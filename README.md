# Hybrid-Theory
### Secure Hybrid Enterprise Network

**Experimental Research on Cybersecurity, Systemic Risk and Cross-Layer Dependencies**  
**Research status:** Exploratory | Methodology under development

> **English summary:** Hybrid-Theory is a hands-on hybrid enterprise cybersecurity lab exploring systemic risk, cross-layer dependencies and security assurance. It combines VMware, pfSense, Windows, Linux and GNS3; Azure and full IT/OT integration remain planned; FUXA HMI and Wazuh SIEM have now been deployed with limited functional checks. The research approach is experimental and not yet validated.

### Wat ik heb gebouwd en getest

**Stand van zaken: 4 november 2026.** Hieronder staat wat daadwerkelijk is ingericht en op beperkte punten getest. **PASS geldt uitsluitend binnen de genoemde scope**. De [statuslegenda](governance/STATUSLEGENDA.md) maakt onderscheid tussen implementatie, verificatie en openstaand werk.

| Component | Gebouwd en getest | Nog open |
|---|---|---|
| **VMware Workstation** | Meerdere VM's ingericht. Hypervisor- en guest-isolation-deelcontroles **PASS**, met één bewuste **EXCEPTION** voor Windows-host/guest-integratie. [Review](projectlogboeken/2026-11-01-hypervisor-fortress-deelreview.md) | Integrale hardening, tijdsynchronisatie, restore |
| **pfSense + Kea DHCP** | Virtueel LAB-segment, DHCP-leases, gateway en gerichte firewall-/connectiviteitsproeven **PASS**. Wazuh kreeg via pfSense een lease. [Sessielog](projectlogboeken/2026-11-01-windows-client-pfsense-windows-server-ad-ds.md) | Uitgebreide positieve/negatieve isolatietests |
| **Windows Server 2025 / AD DS / DNS / Windows 11** | Forest/DC-promotie, DNS/SRV, domain join, testlogin en één GPO **PASS**. [AD-rapport](projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) | Hardening, redundantie, onafhankelijk herstel |
| **Ubuntu Server + Cockpit** | Linuxserver en beheerinterface ingericht; basisbeheer bereikt. [Linux-bewijs](bewijsvoering/Linux/README.md) | Aanvullende services en hardening |
| **GNS3 + Wireshark** | VPCS–switch–VPCS, bidirectionele ICMP, ARP en packetcapture **PASS** in LAB01. [Bewijs](bewijsvoering/GNS3/README.md) | Grotere netwerken en gedetailleerde isolatie |
| **FUXA (SCADA/HMI)** | Eigen Ubuntu-VM, Docker en FUXA-container geïnstalleerd; webinterface en HMI-editor bereikbaar vanuit de host (**beperkte functie-PASS**, 2–3 nov.). | **Geen** gekoppelde OpenPLC, Modbus-verkeer, OT-segmentatie of gevalideerde authenticatie/TLS. Publiek bewijs van de VM-hardware: [FUXA VMware-inventaris (gesanitized)](bewijsvoering/VMware/08-FUXA-VMware-Inventory-Sanitized.png); een volledige FUXA/PLC-functionele test blijft open. |
| **Wazuh 4.14.9 (SIEM)** | OVA geïmporteerd, CPU/VMware-opstartprobleem verholpen, DHCP/gateway gecontroleerd, manager/indexer/dashboard-services actief en dashboardlogin bereikbaar (**beperkte functie-PASS**, 3–4 nov.). GPT-header gerepareerd en rootpartitie uitgebreid. [Publieke hardware-inventaris](bewijsvoering/VMware/README.md). | **0 agents**: geen bewezen end-to-end detectie; definitieve XFS-groei, indexer write-health, negatieve toegangsproef en restore nog open. Functioneel bewijs is nog niet publiek gepubliceerd. |

**PLANNED / niet aangetoond:** OpenPLC, FUXA↔PLC/Modbus-koppeling, Suricata, Wazuh-agentdetectie, volledige IT/OT-isolatie, Azure/Entra/Arc en onafhankelijke off-host restore. De VM's worden binnen het RAM-budget niet noodzakelijk tegelijk gedraaid.

## 1. Introduction and research motive

Hybrid-Theory is een technisch onderzoeksproject waarin een hybride bedrijfsnetwerk wordt opgebouwd met VMware, pfSense, Windows Server, Windows 11, Ubuntu en GNS3, aangevuld met FUXA en Wazuh. Azure en volledige IT/OT-integratie blijven gepland. Naast het bouwen en beveiligen van deze infrastructuur wil ik onderzoeken hoe risico's ontstaan en zich via onderlinge afhankelijkheden kunnen verspreiden.

Dit sluit conceptueel aan bij [mijn Northumbria-masterscriptie (2021) over systemic risk en spillover-effecten](onderzoek/academische-referenties/scriptie-2021.md). Daarin onderzocht ik welke Europese landen en economische sectoren financiële schokken verspreiden (*transmitters*) en welke erdoor worden geraakt (*receivers*). In hybride infrastructuren kunnen verstoringen eveneens via afhankelijkheden doorwerken, maar de mechanismen verschillen en de cybersecuritytoepassing moet onafhankelijk worden getoetst.

De motivatie bestaat uit drie doelstellingen. Ten eerste wil ik cruciale afhankelijkheden tussen IT, OT, cloud, bedrijfsbeheer en governance herkennen. Ten tweede wil ik onderzoeken hoe veranderingen binnen deze onderdelen vroegtijdig kunnen worden vastgesteld en welke gevolgen ze hebben voor de rest van de organisatie. Ten derde wil ik verder kijken dan uitsluitend wet- en regelgeving. Compliance is belangrijk, maar naleving alleen voorkomt niet automatisch complexe cyberdreigingen, verborgen zwakheden of keteneffecten.

Daarom richt het onderzoek zich ook op single points of failure, verborgen afhankelijkheden, cascading failures en onderliggende oorzaken. De [academische referenties, MSc-bewijsstukken en onderzoeksachtergrond](onderzoek/academische-referenties/README.md) zijn apart gedocumenteerd.

## 2. Research objectives

De centrale onderzoeksvraag is:

**In hoeverre kan een geïntegreerde beoordeling van governance, management en technische infrastructuur bijdragen aan het herkennen van beveiligingszwakheden, kritieke afhankelijkheden en systeemrisico's?**

### 2.1 Eigen onderzoeksconcept en wetenschappelijk uitgangspunt

**CAT/ACE v0.4 is een experimenteel model dat governance, management en techniek koppelt aan interne, externe of hybride Audit, Cost & Efficiency-beoordelingen.** Dit onderzoeksconcept is door mijzelf bedacht en wordt binnen Hybrid-Theory verder ontwikkeld en getoetst.

Bestaande frameworks zoals **COBIT, ISO/IEC 27001 en NIST CSF** behandelen al governance en management. **De drie lagen zijn op zichzelf geen nieuwe uitvinding.** De te onderzoeken meerwaarde ligt in een reproduceerbare koppeling van verantwoordelijkheden, technische controls, afhankelijkheden, gecontroleerde foutinjectie, bewijsvoering en restrisicobesluiten.

De ontwikkeling is *evidence-driven*: de resultaten kunnen de aannames ondersteunen, nuanceren of weerleggen. **CAT/ACE is niet bewezen beter** dan bestaande beoordelingsprocedures.

De drie samenhangende lagen zijn **Corporate Governance & Compliance**, **Accountability & Management** en **Technology & Operations**. ACE toetst controls en compliancebewijs, vergelijkt kosten en veilige optimalisatie, en valideert wijzigingen opnieuw. Zie de [uitgebreide onderzoeksdocumentatie over frameworks en gap-analyses](governance/CAT_ACE_v0.4.md) en de [architectuurbaseline](architectuur/ARCHITECTUUR_BASELINE.md) voor de uitwerking.

### 2.2 Cross-layer dependencies

Het onderzoeksmodel bekijkt relaties tussen governance, management en technologie **in beide richtingen**. Een technische storing kan gevolgen hebben voor bedrijfsprocessen, terwijl een beleids- of managementwijziging invloed kan hebben op technische maatregelen. Deze afhankelijkheden, eventuele cascading failures en veronderstelde oorzaken moeten aan de hand van tests en bewijs worden getoetst.

### 2.3 Virtual enterprise

Binnen de gesimuleerde organisatie worden verantwoordelijkheden van directie, business process owner, CISO, IT-manager en system administrator onderzocht. Dit helpt om technische bevindingen te koppelen aan eigenaarschap en risicoacceptatie. Fictieve besluiten vormen geen bewijs van werkelijke managementeffectiviteit. De **organisatorische rollen** in deze simulatie zijn iets anders dan de **AI-samenwerkingsrollen** in sectie 8.

## 3. Research methodology

Het onderzoek wordt uitgevoerd binnen Hybrid-Theory. Per geselecteerd scenario worden een baseline, verwachtingen en testprocedures vastgelegd. Vervolgens worden gecontroleerde verstoringen uitgevoerd om afhankelijkheden, netwerkgedrag en herstel te onderzoeken.

Configuraties, logs en testresultaten vormen de technische bewijsvoering. Organisatorische simulaties en onbevestigde aannames worden afzonderlijk benoemd, zodat duidelijk blijft welke bevindingen daadwerkelijk zijn aangetoond.

## 4. Hybrid network architecture

De [architectuurbaseline](architectuur/ARCHITECTUUR_BASELINE.md) en het [netwerkontwerp](architectuur/NETWERKONTWERP.md) beschrijven de bestaande en beoogde samenhang tussen VMware, pfSense, Windows, Ubuntu en GNS3. FUXA (HMI) en Wazuh (SIEM) zijn later toegevoegd; de architectuurdocumentatie moet hiervoor nog worden bijgewerkt. Azure en de volledige IT/OT-koppeling blijven onderdeel van het doelmodel. De beoogde segmentatie en cloudverbindingen vormen een **doelmodel**: niet alle VLAN's, verbindingen en diensten zijn geïmplementeerd of getest.

De [architectuurdocumentatie](architectuur/README.md) beschrijft de conceptuele doelarchitectuur en technische grenzen. De tweede fysieke Linux-host, Azure, OpenPLC en Suricata zijn nog **PLANNED**. FUXA en Wazuh zijn inmiddels ingericht; hun verdere integratie en veiligheidstests staan open.

**GNS3: basisomgeving IMPLEMENTED en beperkte VPCS/ARP/ICMP-tests PASS.** De uitbreiding met drie groepen van 25 virtuele clients, aanvullende subnetten en uitgebreidere isolatietests is nog gepland. Zie [GNS3-bewijsvoering](bewijsvoering/GNS3/README.md).

**Windows/AD: basis VERIFIED binnen de geteste scope.** Forest/DC, DNS, domain join, testlogin en één GPO zijn aangetoond; uitgebreide identity-hardening, domeinredundantie en een onafhankelijke restore niet. Zie het [AD-baselinerapport](projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md).

**FUXA en Wazuh: basisomgevingen IMPLEMENTED, beperkte functietests PASS.** De FUXA-webeditor is bereikbaar, zonder PLC-integratie. Wazuh is toegankelijk als SIEM-dashboard, zonder gevalideerde agentdetectie. Voor beide staan netwerk-/securityacceptatie en publieke end-to-end bewijsvoering nog open.

## 5. Foundational labs

De vijf canonieke labs. **M01–M05 zijn IDs**, geen automatische completion-verdicts. Zie [statuslegenda](governance/STATUSLEGENDA.md) en [roadmap](projectlogboeken/ROADMAP.md).

| ID en labnaam | Werkstatus en bewijs |
|---|---|
| **M01 · Lab 01 — Hypervisor Security & Virtualization Hardening** | **IN PROGRESS**; gerichte HV-01–HV-04-controles **PASS met één EXCEPTION**. [M01-review](projectlogboeken/2026-11-01-hypervisor-fortress-deelreview.md) |
| **M02 · Lab 02 — Backup, Recovery & Disaster Resilience** | **PENDING**; geen off-host restore aangetoond. [AD-/herstelrapport](projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) |
| **M03 · Lab 03 — Hybrid Identity & Access Management** | **IN PROGRESS**; AD/DNS/domain join/GPO **PASS binnen scope**; Entra **PLANNED**. [AD-rapport](projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) |
| **M04 · Lab 04 — Network Segmentation & Security Architecture** | **IN PROGRESS**; gerichte pfSense- en GNS3-tests **PASS binnen hun afzonderlijke scopes**; volledige isolatie niet aangetoond. FUXA- en Wazuh-netwerkgrenzen vragen nog aanvullende tests. [pfSense](architectuur/PFSENSE_PLAN.md) · [GNS3](bewijsvoering/GNS3/README.md) |
| **M05 · Lab 05 — Regulatory Assessment & Security Assurance** | **PENDING**; geen afgeronde assurance-acceptatie. [Regulatory frameworks](governance/WET_EN_REGELGEVING.md) |

## 6. Comparative evaluation

**Benchmarkreferentiekader: alle relevante regulatory frameworks, wettelijke vereisten, normen, controlframeworks en bestaande beoordelingsprocedures**, voor zover deze van toepassing zijn op de onderzochte organisatie, technische scope en scenario's. Dit is dus **niet beperkt tot drie frameworks**. Mogelijke referenties zijn onder meer **ISO/IEC 27001, COBIT 2019, NIST CSF 2.0, CIS Controls v8.1 en NIST SP 800-53A**, aangevuld met bijvoorbeeld **AVG/GDPR, NIS2 of DORA** wanneer de fictieve organisatie en het scenario binnen hun toepassingsgebied vallen.

De vergelijkingen beoordelen onder meer kwetsbaarheden, afhankelijkheden, oorzaken, reproduceerbaarheid, bewijskwaliteit, kosten, efficiëntie en beoordelingsinspanning. Niet elk framework is een wettelijke verplichting of een rechtstreeks vergelijkbare auditmethodiek. Daarom worden **toepasselijkheid en type referentiekader per experiment onderbouwd**. Het gebruik van deze kaders impliceert geen certificering of bewezen compliance. De [vergelijkingsmethoden, typen gap-analyses en toepasselijkheidsregels](governance/CAT_ACE_v0.4.md) zijn afzonderlijk uitgewerkt. [Wet- en regelgevingskaders](governance/WET_EN_REGELGEVING.md) bespreken ook **ISAE 3402, ISAE 3000 en SOC 2** als bestaande assurance- en attestatieperspectieven.

## 7. Future research and limitations

Het langetermijndoel is om circa 30 relevante technische labs uit te voeren als basis voor verdere methodiekontwikkeling en mogelijk toekomstig academisch onderzoek. De praktische labuitvoering behoudt daarbij prioriteit.

Openstaande concrete vervolgtests zijn onder meer **OpenPLC installeren en met FUXA via Modbus verbinden, Suricata correct positioneren, Wazuh-agents en gecontroleerde detectie toevoegen, extra firewall-isolatietests en een onafhankelijk herstel aantonen**. De volgorde hangt mede af van het beschikbare RAM- en opslagbudget.

Een belangrijke beperking is dat het onderzoek plaatsvindt binnen een gecontroleerde en deels gesimuleerde bedrijfsomgeving. Technische resultaten kunnen worden getest, maar echte organisatorische besluitvorming wordt daarmee niet bewezen. De onderzoeksaanpak wordt daarom aan de hand van zowel positieve als negatieve resultaten verder beoordeeld.

## 8. AI collaboration

**Sam is Project Owner & Lead Architect (mens)** en beslist over ontwerp, scope en risicoacceptatie. De ondersteunende rollen zijn **ChatGPT — Engineering Orchestrator (AI)**, **Claude — Critical Security Auditor & Chaos Engineer (AI)**, **Microsoft Copilot — Microsoft Specialist & Automation Engineer (AI)** en **GitHub Copilot — Coding & Automation Assistant (AI)**. Een gerichte AI-review is geen formele onafhankelijke audit. Zie [rollen en overdracht](ai-samenwerking/ROLLEN_EN_OVERDRACHT.md), [AI-werkafspraken](governance/AI_WERKAFSPRAKEN.md) en [besluiten](governance/BESLUITENLOG.md). De technische uitvoering volgt **Risk-Based Validation**, met gescopeerd bewijs en eigenaarbesluiten.

## Projectdocumentatie

[Academische referenties](onderzoek/academische-referenties/README.md) · [AI-samenwerking](ai-samenwerking/README.md) · [Architectuur en ontwerpdocumentatie](architectuur/README.md) · [Netwerkontwerp](architectuur/NETWERKONTWERP.md) · [Projectlogboeken](projectlogboeken/README.md) · [Technische bewijsvoering](bewijsvoering/README.md) · [Governance-documentatie](governance/README.md)

## Publicatiestatus

GitHub-repository: PUBLIC. Deze repository bevat de openbare documentatie, onderzoeksconcepten en technische bewijsvoering van Hybrid-Theory.

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
