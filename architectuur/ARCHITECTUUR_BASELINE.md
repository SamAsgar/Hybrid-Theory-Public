# Architectuurbaseline | Hybrid-Theory

**Status:** technische architectuur als labreferentie; implementatie en geverifieerde werking worden afzonderlijk gedocumenteerd.  
**Onderzoekscontext:** CAT/ACE v0.2, **CONCEPT / NOT VALIDATED**.

## 1. Beoordelingslagen CAT/ACE

| Laag | Betekenis | Toepassing |
|---|---|---|
| **C / 03** | Corporate Governance & Compliance | Fictieve bedrijfsdoelen, toepasselijke eisen, beleid en risicobereidheid |
| **A / 02** | Accountability & Management | Gesimuleerde eigenaren, beslissingsmandaten, processen en risicoacceptatie |
| **T / 01** | Technology & Operations | VMware, pfSense, Windows, Ubuntu, GNS3 en geplande cloud-/OT-componenten |

ACE (**Automation, Compliance & Efficiency**) is een evaluatiedimensie over alle lagen. Afhankelijkheden worden waar relevant zowel van eis naar control als van technisch defect terug naar besluit en proces gevolgd.

**Interpretatie:** een fictieve governancebeslissing is geen bewijs van echte organisatorische effectiviteit. Benchmarkvergelijkingen zijn onderzoeksinstrumenten, geen bewijs dat CAT/ACE een erkende norm is.

## 2. Technische basis

De host draait VMware Workstation met meerdere lab-VM's. pfSense vervult netwerk- en firewallfuncties. Ubuntu Server levert een Linuxbeheeromgeving met Cockpit; GNS3 ondersteunt gesimuleerde netwerkproeven met Wireshark. Windows Server 2025 fungeert in de geteste configuratie als AD-domain controller en DNS-server voor een Windows 11-domainclient.

De testomgeving is **geen productieomgeving** en heeft geen certificering.

## 3. Trust boundaries en afhankelijkheden

- **LAB-segment:** gecontroleerde VM-naar-VM-communicatie via de ingestelde firewall.
- **Managementzone:** afzonderlijke beheertoegang; toegang en actuele adaptertoestand worden per test gespecificeerd.
- **Tijdelijke updates en extern verkeer:** afzonderlijke route-/toestemmingsgrenzen; NAT garandeert niet vanzelf thuisnetwerkisolatie.
- **Toekomstige GNS3-subnetten, IT/OT, Azure/Arc:** **PLANNED**; niet in de actuele testresultaten opnemen als reeds bewezen.

Technische bewijsvoering volgt de keten: `securitydoel → control → configuratie → test → observatie → risico → gerichte remediatie`. Hypothesen blijven **onbevestigd** totdat gerichte tests ze onderbouwen; de onderzoeksschaal staat in de [statuslegenda](../governance/STATUSLEGENDA.md).

## 4. Historie, status en herstel

**AD-basis:** forest/DC, relevante DNS- en SRV-records, domain join, testlogin en één GPO zijn binnen de aangetoonde scope PASS. Dit bewijst geen domeinredundantie of onafhankelijke restore.

**Lab 01 (M01):** gerichte controles PASS met één EXCEPTION; werkstatus **IN PROGRESS**, geen integrale labacceptatie.

**Lab 02 (M02) en Azure:** onafhankelijk off-host herstel en clouddeployment zijn nog niet aangetoond (**PENDING/PLANNED** naar onderwerp).

**Operationele werkwijze:** pragmatische, risicogestuurde controles vóór de benodigde werkzaamheden; uitgebreide hardening binnen de relevante lab. [CAT/ACE v0.2](../governance/CAT_ACE_v0.2.md) is een afzonderlijk experimenteel assurance- en dependency-onderzoeksconcept, **geen** gevalideerde vervanger van bestaande beoordelingsprocedures.
