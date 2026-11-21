# Engineeringroadmap | Hybrid-Theory

**Werkstatus per 02-11-2026, M04 bijgewerkt op 20-11-2026.** Fasen 0–7 zijn technische werkpakketten; **Lab 01 t/m Lab 05** zijn de beoordelings- en uitvoeringsdomeinen. Zij zijn niet één-op-één gelijk en hoeven niet numeriek te worden uitgevoerd. Zie [statuslegenda](../governance/STATUSLEGENDA.md).

| Fase | Technisch werkpakket | Aangetoonde status | Nog uit te voeren |
|---|---|---|---|
| **0** | Documentatie en portfolio-export | GitHub-zichtbaarheid **PUBLIC** (gecontroleerd 05-11-2026), publicatiegates **OPEN** | Secrets/history-scan, pixelredactie, ontbrekende bestanden, eigenaar-PASS voor gates |
| **1** | Ubuntu en Cockpit | **IMPLEMENTED**, gerichte beheerproeven **PASS** | Verder service- en herstelontwerp |
| **2** | pfSense en LAB-beveiliging | **IMPLEMENTED**; gerichte DHCP-/ICMP-/firewallproeven **PASS**, afzonderlijke OT-interface sinds 8 nov., PLC en HMI in die virtuele OT-zone bevestigd op 15 nov. | Integrale AC04/AC07-zone-/protocol- en egressvalidatie, beoordeling tijdelijke uitzonderingen |
| **3** | Windows Server 2025, AD/DNS, Windows 11 en GPO | **VERIFIED** voor gerichte AD/client-basistests op 1 november | Hardening, tijdbron, herstel, aanvullende negatieve tests |
| **4** | GNS3 en Wireshark | Kleine VPCS-/ARP-/ICMP-topologie **PASS** | Uitbreiding, tijdsynchronisatie, GNS3-dataplane-isolatie |
| **5** | Tweede fysieke Linux-host | **PLANNED** | Hardwareinstallatie, beheer, backup-/herstelontwerp |
| **6** | Azure / Azure Arc / Entra | **PLANNED** | Kosten, geschiktheid, toestemming en eventuele deployment |
| **7** | Backup en disaster recovery | **PLANNED** | Onafhankelijke off-host kopie en aantoonbare restore |

## Vijf canonieke labs

| ID | Labnaam | Werkstatus en begrenzing | Relevante rapportage |
|---|---|---|---|
| **M01** | **Lab 01 — Hypervisor Security & Virtualization Hardening** | **IN PROGRESS**; gerichte controlerondes PASS met één EXCEPTION; Milestone 01 niet behaald | [M01-deelreview](2026-11-01-hypervisor-fortress-deelreview.md) |
| **M02** | **Lab 02 — Backup, Recovery & Disaster Resilience** | **PENDING**; geen onafhankelijke off-host restore | [AD-herstelgrens](2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) |
| **M03** | **Lab 03 — Hybrid Identity & Access Management** | **IN PROGRESS**; AD-basis gescopeerd PASS; Entra/IAM-uitbreiding niet aangetoond | [AD/DNS/domain join/GPO](2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) |
| **M04** | **Lab 04 — Network Segmentation & Security Architecture** | **IN PROGRESS**. AC01–AC03-regressie na PLC-herstart **TESTED / PASS** binnen de geteste scope. AC04/AC07 gerichte netwerkdeeltests **PASS**. De integrale matrix en formele bewijsreview blijven **PENDING**. | [M04-basis](2026-11-06-m04-network-citadel-ot-baseline.md), [M04 11 nov.](2026-11-11-m04-segmentatie-en-beheer-validatie.md), [M04 15 nov.](2026-11-15-m04-ot-modbus-applicatievalidatie.md), [M04 19 nov.](2026-11-19-m04-openplc-autostart-en-ot-regressie.md), [M04 C2 20 nov.](2026-11-20-m04-core-c2-netwerkvalidatie.md) |
| **M05** | **Lab 05 — Regulatory Assessment & Security Assurance** | Structuur en zeven onderzoekshoofdstukken **APPROVED** (20 nov.); technische uitvoering **PENDING**; M05-MS01 **NOT ACHIEVED**; eerste casus M05-MINI-01 **PLANNED** | [M05-documentatie](../Portfolio/M05-Compliance-Sentinel/README.md) · [CAT/ACE v0.4](../governance/CAT_ACE_v0.4.md) (concept, geen lab-PASS) |

## Permanente Main Missions, milestones en mini-oefeningen

Sinds 20 november 2026 (besluit van Sam) zijn **M01–M05 permanente Main Missions**: ze krijgen geen definitieve afsluitstatus. Voortgang wordt gemeten via **milestones** met expliciete scope, vooraf vastgestelde acceptatiecriteria, bewijs, beoordeling en acceptatie door Sam. De bestaande fasen en labnamen behouden hun betekenis.

| Categorie | Identificatie | Levenscyclus | Afsluiting |
|---|---|---|---|
| **Roadmapfase** | 0–7 | Technisch werkpakket | Afgerond bij bewijs voor de faseacceptatie |
| **Foundation Lab** | Lab 01–05 | Naam van het onderzoeksdomein, gekoppeld aan M01–M05 | Volgt de missie |
| **Permanente Main Mission** | M01–M05 | Continu ontwikkelen, revalideren en verbeteren | **Nooit** definitief afgesloten |
| **Milestone** | `Mnn-MSnn` (bijv. M05-MS01) | Afgebakend doel met vooraf vastgestelde exitcriteria | **ACHIEVED** alleen na acceptatie door Sam |
| **Mini-oefening** | `Mnn-MINI-nn` (bijv. M05-MINI-01) | Klein werkpakket binnen een missie | Scoped verdict; sluit geen milestone of missie af |
| **Afgebakende zelfstandige missie** | Nog niet vastgesteld | Latere categorie ná M01–M05, met eigen begin- en eindcriteria | Eigen eindacceptatie |

**Stand 20 november 2026:** geen van M01–M05 heeft **Milestone 01** bereikt. Bestaande technische PASS-resultaten blijven scoped technische bevindingen; ze zijn geen milestone-afronding. Formuleringen als "geen integrale acceptatie" of "geen volledige missie-PASS" in gedateerde logs lezen als "geen milestone-acceptatie" ([Statuslegenda §3a](../governance/STATUSLEGENDA.md#3a-missie--milestone--en-mini-oefeningstatus-20-11-2026)).

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

## M04 CORE C2 — 20 november 2026

[Projectlog](2026-11-20-m04-core-c2-netwerkvalidatie.md): gerichte extra LAB- en OT-denies bevestigd. De directe beheerroute, IPv6-beleidsreview, veilige WAN-test, DNS/NTP-ontwerp, herstelbewijs en formele acceptatie staan open. **AC04/AC07 integraal PENDING**. **AC05 PENDING**, **AC06/AC08 PLANNED**. De eigenaar bepaalt AC06-scope en cliëntaantal.


## M04-CORE update 21 november 2026

**M04-CORE IN PROGRESS · Milestone 01 open · AC04/AC07 integraal PENDING.** F24 is aangetoond voor TCP/502 en TCP/8080. F13–F15 wachten op formele bronacceptatie en review per poort. Beide tijdelijke routes zijn verwijderd. De adaptereindstand, DNS/NTP, IPv6 en alternatieve paden, AC01–AC03-review en herstelvalidatie staan open. EXT en de industriële DMZ volgen later. [Uitvoering en resterende stappen](2026-11-21-m04-core-management-segmentatie.md)
