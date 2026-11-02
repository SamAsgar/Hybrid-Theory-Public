# Hardware- en systeemstatus | Publieke baseline

**Bronmoment:** technische stand tot en met 1 november 2026.  
**Classificatie:** gesaneerde inventaris; geen privé-infrastructuuridentificatoren.

| Component | Hardware/rol | Aangetoonde status | Open |
|---|---|---|---|
| Windows-host | 32 GB RAM, VMware Workstation | Host en Workstation **IMPLEMENTED**, gerichte M01-instellingen **PASS + EXCEPTION** | Capaciteits- en isolatievalidatie bij verdere uitbreiding |
| pfSense CE 2.9.0 | Virtuele firewall, LAB DHCP en routering | **IMPLEMENTED**, Kea DHCP/gerichte gatewaytests **PASS** | Full-scope segmentatie, IPv6, bredere ruleset |
| Ubuntu Server 24.04 LTS | Linux VM met Cockpit | **IMPLEMENTED**, eerdere toegang en enkele services **PASS** | Meer uitgebreide services/restore |
| GNS3 VM/Desktop + Wireshark | Eenvoudig VPCS-netwerklab | **IMPLEMENTED**, ARP/ICMP/capture **PASS** | Grotere topologie, tijdbron en uitgebreide dataplane-review |
| Windows Server 2025 | Virtuele AD-domain controller | Forest/DC, DNS en SRV **PASS** binnen scope | Replicatie, hardening, off-host restore |
| Windows 11 Enterprise Evaluation | Domeinclient en beheertest | OS/VMware Tools, LAB-verbinding, domain join en één GPO **PASS** binnen scope | Volledige IAM-/securityvalidatie |
| Tweede fysieke Linux-host | Back-up/recovery | **PLANNED** | Installatie en echte hersteltest |
| Microsoft Azure / Azure Arc | Hybride identiteit en beheer | **PLANNED** | Cloudbudget, toegang en deployment |

## Grenzen van het bewijs

De aanwezigheid van een snapshot bewijst geen onafhankelijke back-up of succesvolle restore. Een specifiek toegestane netwerkstroom bewijst niet dat elke andere stroom geblokkeerd is. Een AI-review is geen vervanging van een reproduceerbaar technisch testresultaat.

**Lab 01 (M01): IN PROGRESS.** Gerichte deelcontrols PASS met één geaccepteerde EXCEPTION; geen volledige labacceptatie.  
**Lab 02 (M02): PENDING.** Onafhankelijke back-up en daadwerkelijke restore niet aangetoond.  
**CAT/ACE v0.2:** onderzoeksconcept, **NOT VALIDATED**.

**Laatst gedocumenteerde pfSense-egress (1 november):** tijdelijke, brede IPv4 **ALLOW Any** voor uitsluitend de betreffende Windows 11-testclient, onder de bestaande RFC1918-blockregel, bedoeld voor internet/activatie. **Geen definitieve egress-hardening; actuele live-regelstatus niet opnieuw gecontroleerd.** Zie [Windows/pfSense-sessielog](../projectlogboeken/2026-11-01-windows-client-pfsense-windows-server-ad-ds.md). 

**Statusgebruik:** [statuslegenda](STATUSLEGENDA.md).

Zie [actuele engineeringroadmap](../projectlogboeken/ROADMAP.md), [AD-basisrapport](../projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) en [M01-deelreview](../projectlogboeken/2026-11-01-hypervisor-fortress-deelreview.md).
