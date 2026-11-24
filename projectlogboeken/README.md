# Projectlogboeken | Hybrid-Theory

De oorspronkelijke logs vormen **historische momentopnamen of later afgeleide rapporten**. Nieuwere, afzonderlijk gedateerde onderzoeksnotities overschrijven de oorspronkelijke testuitslagen niet. Voor actuele interpretatie: [roadmap](ROADMAP.md) en [statuslegenda](../governance/STATUSLEGENDA.md).

| Datum | Verslag | Reikwijdte |
|---|---|---|
| 25 oktober | [Ubuntu/Cockpit en eerste engineeringstatus](2026-10-25-projectstatus.md) | Gesaneerde historische momentopname |
| 26 oktober | [pfSense gerichte netwerkproeven](2026-10-26-projectstatus.md) | Historische afgeleide testnotitie; beperkte ICMP-blokkade |
| 27 oktober | [Hostcapaciteit en geheugendiagnose](2026-10-27-hostcapaciteit-geheugendiagnose.md) | Metingen en destijds voorgesteld RAM-budget |
| 28 oktober | [GNS3/KVM, VPCS en parkeerregister](2026-10-28-gns3-kvm-diagnose-parkeerregister.md) | Gesaneerde historische diagnose |
| 31 oktober | [Windows 11-installatie](2026-10-31-windows11-client-installatie.md) | Installatie-PASS; later configuratiewerk afzonderlijk |
| 1 november, eerdere sessie | [Windows 11/pfSense/Windows Server](2026-11-01-windows-client-pfsense-windows-server-ad-ds.md) | Installatie en netwerkbaseline; AD-promotie op dit sessiemoment nog PENDING |
| 1 november, later | [AD DS, DNS, domain join en GPO](2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) | Afgebakende technische PASS na de eerdere sessie |
| 1 november | [M01 — Lab 01: Hypervisor Security & Virtualization Hardening](2026-11-01-hypervisor-fortress-deelreview.md) | Gerichte controlerondes, PASS met één EXCEPTION; lab IN PROGRESS |
| 4 november | [Phoenix Recovery en private-cloudonderzoek](2026-11-04-onderzoeksdag-phoenix-recovery-private-cloud.md) | Alleen architectuur-, risico- en vergelijkingsonderzoek; **geen technische labuitvoering** |
| 6 november | [M04 functionele OT-baseline](2026-11-06-m04-network-citadel-ot-baseline.md) | Gescopeerde AC01–AC03 PASS; OT-segmentatie nog PENDING |
| 7 november | [M04-CORE pre-migratiecheckpoint](2026-11-07-m04-core-pre-migratie-checkpoint.md) | Snapshotvoorbereiding gemeld; geen nieuwe technische tests of security-PASS |
| 7–8 november | [M04: OT-interface op de firewall](2026-11-08-m04-ot-firewallinterface.md) | OT-interface IMPLEMENTED met default deny; HMI/PLC nog niet verplaatst, isolatietests PENDING |
| 8–9 november | [M04: PLC-migratie, troubleshooting en governance](2026-11-09-m04-plc-migratie-governance-publiek.md) | Gesanitiseerde voortgang: PLC-netwerkmigratie en gerichte tests, governance- en publicatieproces; HMI-migratie, AC04/AC07 PENDING |
| 11 november | [M04: segmentatie en beheer gevalideerd](2026-11-11-m04-segmentatie-en-beheer-validatie.md) | Nieuwe tussenstand: HMI op OT, beheerverbindingen en gerichte LAB→OT-blokkade TESTED PASS; troubleshooting en vervolgcriteria; AC04/AC07 volledig PENDING |
| 19 november | [M04: OpenPLC-autostart en OT-regressie](2026-11-19-m04-openplc-autostart-en-ot-regressie.md) | Gesaneerde labupdate over PLC-herstart en functionele regressie. AC04/AC07 integraal PENDING. |
| 20 november | [M04: CORE C2-netwerkvalidatie](2026-11-20-m04-core-c2-netwerkvalidatie.md) | Gerichte LAB- en OT-blokkades, routecontrole en open acceptatiegates |
| 21 november | [M04 · LAN- en WAN-blokkades naar OT](2026-11-21-m04-core-management-segmentatie.md) | F13–F15 scoped PASS voor de beheer-VM. F24 scoped PASS voor TCP/502 en TCP/8080. Beide testroutes verwijderd. |
| 24 november | [M05-MINI-01 · IT/OT-controlassessment en rapportage](2026-11-24-m05-mini-01-controlassessment.md) | Kennistraining afgerond; casusassessment, 05.6/05.7 en eigenaarreview PENDING; geen nieuwe technische tests |

**Actueel overzicht:** [Fase 0–7 en Lab 01–05](ROADMAP.md). De volledige oorspronkelijke engineeringdiscussie is niet overgenomen; dit overzicht bevat uitsluitend bestaande bestanden.

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam; op 08-11-2026 aangevuld door Claude.
