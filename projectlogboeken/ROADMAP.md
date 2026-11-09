# Engineeringroadmap | Hybrid-Theory

**Werkstatus per 02-11-2026, M04 bijgewerkt op 09-11-2026.** Fasen 0–7 zijn technische werkpakketten; **Lab 01 t/m Lab 05** zijn de beoordelings- en uitvoeringsdomeinen. Zij zijn niet één-op-één gelijk en hoeven niet numeriek te worden uitgevoerd. Zie [statuslegenda](../governance/STATUSLEGENDA.md).

| Fase | Technisch werkpakket | Aangetoonde status | Nog uit te voeren |
|---|---|---|---|
| **0** | Documentatie en portfolio-export | GitHub-zichtbaarheid **PUBLIC** (gecontroleerd 05-11-2026), publicatiegates **OPEN** | Secrets/history-scan, pixelredactie, ontbrekende bestanden, eigenaar-PASS voor gates |
| **1** | Ubuntu en Cockpit | **IMPLEMENTED**, gerichte beheerproeven **PASS** | Verder service- en herstelontwerp |
| **2** | pfSense en LAB-beveiliging | **IMPLEMENTED**; gerichte DHCP-/ICMP-/firewallproeven **PASS**. Aparte OT-interface met default deny **IMPLEMENTED** (8 nov.) | Volledige isolatie en bredere protocollen niet aangetoond; OT-zone nog zonder systemen en zonder tests; tijdelijke egressregel beoordelen |
| **3** | Windows Server 2025, AD/DNS, Windows 11 en GPO | **VERIFIED** voor gerichte AD/client-basistests op 1 november | Hardening, tijdbron, herstel, aanvullende negatieve tests |
| **4** | GNS3 en Wireshark | Kleine VPCS-/ARP-/ICMP-topologie **PASS** | Uitbreiding, tijdsynchronisatie, GNS3-dataplane-isolatie |
| **5** | Tweede fysieke Linux-host | **PLANNED** | Hardwareinstallatie, beheer, backup-/herstelontwerp |
| **6** | Azure / Azure Arc / Entra | **PLANNED** | Kosten, geschiktheid, toestemming en eventuele deployment |
| **7** | Backup en disaster recovery | **PLANNED** | Onafhankelijke off-host kopie en aantoonbare restore |

## Vijf canonieke labs

| ID | Labnaam | Werkstatus en begrenzing | Relevante rapportage |
|---|---|---|---|
| **M01** | **Lab 01 — Hypervisor Security & Virtualization Hardening** | **IN PROGRESS**; gerichte controlerondes PASS met één EXCEPTION; geen integrale acceptatie | [M01-deelreview](2026-11-01-hypervisor-fortress-deelreview.md) |
| **M02** | **Lab 02 — Backup, Recovery & Disaster Resilience** | **PENDING**; geen onafhankelijke off-host restore | [AD-herstelgrens](2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) |
| **M03** | **Lab 03 — Hybrid Identity & Access Management** | **IN PROGRESS**; AD-basis gescopeerd PASS; Entra/IAM-uitbreiding niet aangetoond | [AD/DNS/domain join/GPO](2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) |
| **M04** | **Lab 04 — Network Segmentation & Security Architecture** | **IN PROGRESS**; beperkte pfSense- en GNS3-tests PASS; functionele OT-baseline AC01–AC03 PASS binnen scope (6 nov.); OT-interface op de firewall IMPLEMENTED (8 nov.); migratie van de PLC naar het OT-segment gemeld (9 nov., bewijs niet onafhankelijk geverifieerd); regressie AC01–AC03 na de migratie, HMI-migratie, AC04 en AC07 **PENDING**; **M04-CORE IN PROGRESS** | [pfSense](2026-10-26-projectstatus.md), [GNS3](2026-10-28-gns3-kvm-diagnose-parkeerregister.md), [OT-baseline](2026-11-06-m04-network-citadel-ot-baseline.md), [OT-interface](2026-11-08-m04-ot-firewallinterface.md), [PLC-migratie](2026-11-09-m04-plc-migratie-governance-publiek.md) |
| **M05** | **Lab 05 — Regulatory Assessment & Security Assurance** | **PENDING**; geen afgeronde assurance-acceptatie | [CAT/ACE v0.4: Audit, Cost & Efficiency](../governance/CAT_ACE_v0.4.md) (intern/extern/hybride; concept, geen lab-PASS) |

## Koppeltabel Fase ↔ Lab

Dit zijn **inhoudelijke raakvlakken**, geen afrondingscriteria en geen bewijs dat een lab door voltooiing van een fase automatisch PASS krijgt.

| Fase | Ondersteunt |
|---|---|
| **0** | Lab 01–05: governance, publicatie en evidence |
| **1** | Lab 01 (VM-/hostbasis), Lab 04 (beheergrenzen) |
| **2** | Lab 04 (firewall, segmentatie) |
| **3** | Lab 03 (AD, DNS en domeinclient) |
| **4** | Lab 04 (GNS3-netwerksimulaties) |
| **5** | Lab 02 (beoogde onafhankelijke herstelhost) |
| **6** | Lab 03 (beoogde Entra-integratie), Lab 04 (beoogde cloudnetwerkgrenzen) |
| **7** | Lab 02 (back-up en herstel) |

**Overkoepelend:** Lab 05 gebruikt geschikte controls en bewijs uit de andere labs; geen afzonderlijke technische fase impliceert daarmee een formele audit-PASS.

## Bewijs- en publicatiegrenzen

**Laatst gedocumenteerde pfSense-configuratie (1 november):** een tijdelijke IPv4 ALLOW Any-egressregel voor de Windows 11-testclient, onder de bestaande RFC1918-blockregel, was gebruikt voor gerichte internet-/activatietests. **Op 8 november stond deze regel nog in de regelset** (gelezen tijdens de M04-sessie, niet gewijzigd). De actuele toestand van deze regel is sindsdien niet opnieuw vastgesteld. Zie [sessielog](2026-11-01-windows-client-pfsense-windows-server-ad-ds.md) en [M04 OT-interface](2026-11-08-m04-ot-firewallinterface.md).

**GitHub-zichtbaarheid: PUBLIC** (gecontroleerd 05-11-2026); **publieke zichtbaarheid is geen publicatievrijgave.** Beeldredactie, volledige secretscan en Git-geschiedenis zijn niet volledig geverifieerd. Zie het [goedgekeurde publicatiebeleid](../governance/PUBLICATIEBELEID.md).

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam; M04-regels op 08-11-2026 en 09-11-2026 bijgewerkt door Claude.
