# Architectuurbaseline | Hybrid-Theory

**Status:** technische architectuur als labreferentie; implementatie en geverifieerde werking worden afzonderlijk gedocumenteerd.  
**Onderzoekscontext:** [CAT/ACE v0.4](../governance/CAT_ACE_v0.4.md), **CONCEPT / NOT VALIDATED**.

## 1. Beoordelingslagen CAT/ACE

| Laag | Betekenis | Toepassing |
|---|---|---|
| **C / 03** | Corporate Governance & Compliance | Fictieve bedrijfsdoelen, toepasselijke eisen, beleid en risicobereidheid |
| **A / 02** | Accountability & Management | Gesimuleerde eigenaren, beslissingsmandaten, processen en risicoacceptatie |
| **T / 01** | Technology & Operations | VMware, pfSense, Windows, Ubuntu, GNS3 en geplande cloud-/OT-componenten |

ACE (**Audit, Cost & Efficiency**) toetst als **interne, externe of hybride beoordelingsfunctie** de controlwerking en het bewijs (**Audit**), de directe en indirecte beheerkosten (**Cost**) en verantwoorde optimalisatie onder dezelfde beveiligingseisen (**Efficiency**). Na wijzigingen volgt gerichte **Revalidation**. CAT-C bepaalt toepasselijke eisen; ACE-Audit beoordeelt die één keer binnen afgebakende scope. Automatisering kan reproduceerbaarheid ondersteunen. Afhankelijkheden worden zowel van eis naar techniek als van technisch defect terug naar eigenaar en beleid onderzocht.

**Interpretatie:** een fictieve governancebeslissing is geen bewijs van echte organisatorische effectiviteit. Benchmarkvergelijkingen zijn onderzoeksinstrumenten, geen bewijs dat CAT/ACE een erkende norm is.

## Actuele netwerktopologie (20 november 2026)

De [gesaneerde Architecture](README.md) toont twee figuren: diagram A met de bestaande netwerken WAN-SIM, MGMT, LAB en OT (**IMPLEMENTED**) en diagram B met de HT-C-010-doelarchitectuur. Van de doelzones bestaat alleen OT als eigen segment; IT-, Security-, private-services- en GNS3-zones en Azure zijn **PLANNED**. Echte host-/beheer-/routeradressen zijn niet gepubliceerd en vervangen door officiële aliassen; open punten dragen **TWIJFEL / NOT VERIFIED**.

FUXA01 en PLC01 staan in de OT-zone; de Modbus TCP/502-verbinding tussen beide is op 15 november getest en op 19 november is de START→STOP-reeks met PLC-readback **TESTED / scoped PASS**. Formele evidence-review van AC01–AC03 en de OT-isolatie (AC04/AC07) zijn **PENDING**. Diagram A (stand 20 november) toont de gescopeerde CORE C2-resultaten per verkeersstroom. Wazuh heeft een beperkte UI-/service-PASS en geen aangetoonde end-to-end SIEM-detectie (0 agents). M02 en Azure blijven **PLANNED**. CAT/ACE v0.4 blijft een onderzoeksconcept, geen behaalde certificering.

## 2. Technische basis

De host draait VMware Workstation met meerdere lab-VM's. pfSense vervult netwerk- en firewallfuncties. Ubuntu Server levert een Linuxbeheeromgeving met Cockpit; GNS3 ondersteunt gesimuleerde netwerkproeven met Wireshark. Windows Server 2025 fungeert in de geteste configuratie als AD-domain controller en DNS-server voor een Windows 11-domainclient.

De testomgeving is **geen productieomgeving** en heeft geen certificering.

## 3. Trust boundaries en afhankelijkheden

- **LAB-segment:** gecontroleerde VM-naar-VM-communicatie via de ingestelde firewall.
- **Managementzone:** afzonderlijke beheertoegang; toegang en actuele adaptertoestand worden per test gespecificeerd.
- **Tijdelijke updates en extern verkeer:** afzonderlijke route-/toestemmingsgrenzen; NAT garandeert niet vanzelf thuisnetwerkisolatie.
- **OT-zone:** eigen segment achter een aparte pfSense-interface (**IMPLEMENTED**); verkeer binnen de zone loopt niet via de firewall. De grens naar andere zones is pas bewezen na de volledige AC04/AC07-tests.
- **Toekomstige GNS3-subnetten, IT- en Security-zones, Azure/Arc:** **PLANNED**; niet in de actuele testresultaten opnemen als reeds bewezen.

Technische bewijsvoering volgt de keten: `securitydoel → control → configuratie → test → observatie → risico → gerichte remediatie`. Hypothesen blijven **onbevestigd** totdat gerichte tests ze onderbouwen; de onderzoeksschaal staat in de [statuslegenda](../governance/STATUSLEGENDA.md).

## 4. Historie, status en herstel

**AD-basis:** forest/DC, relevante DNS- en SRV-records, domain join, testlogin en één GPO zijn binnen de aangetoonde scope PASS. Dit bewijst geen domeinredundantie of onafhankelijke restore.

**Lab 01 (M01):** gerichte controles PASS met één EXCEPTION; werkstatus **IN PROGRESS**, geen integrale labacceptatie.

**Lab 02 (M02) en Azure:** onafhankelijk off-host herstel en clouddeployment zijn nog niet aangetoond (**PENDING/PLANNED** naar onderwerp).

**Operationele werkwijze:** pragmatische, risicogestuurde controles vóór de benodigde werkzaamheden; uitgebreide hardening binnen de relevante lab. [CAT/ACE v0.4](../governance/CAT_ACE_v0.4.md) is een afzonderlijk experimenteel audit-, kosten-, efficiency- en dependency-onderzoeksconcept, **geen** gevalideerde vervanger van bestaande beoordelingsprocedures.

## 5. M04-statusharmonisatie — 20 november 2026

De technische architectuurbaseline blijft een VMware/pfSense-omgeving met WAN-SIM, MGMT, LAB en een afzonderlijke OT-zone. Diagram A is op 20 november geactualiseerd; diagram B kreeg alleen gedateerde statusnotities. Dit is een **statusdelta, geen herontwerp**. Op 19 november zijn de OpenPLC-autostartcorrectie en HMI START→STOP-readback binnen scope getest. Gerichte LAB→OT- en OT→andere-zone/extern-blokkeringen zijn met pfSense-logs gecorreleerd; de volledige AC04/AC07-matrix en formele eigenaaracceptatie blijven **PENDING**. De gerichte uitvoering van 20 november verandert deze acceptatiegrenzen niet.

[Actuele afgebakende testobservaties](NETWERKONTWERP.md#5-m04-harmonisatie-1920-november-2026) · [Gesaneerde fase-20-evidence](../Portfolio/M04-Network-Citadel/M04-Bewijsvoering/20_OT_segmentation_and_regression/README.md).
