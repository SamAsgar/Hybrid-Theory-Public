# M04 Network Citadel — Publieke evidence-index

**Bronperiode:** 31-10-2026 t/m 15-11-2026. **270 records:** 268 PNG, 1 GIF, 1 ontbrekende MP4. 269/269 aanwezige originelen in private werkomgeving op SHA-256 gecontroleerd. Dit is geen beeldsanitatie.

**Status:** M04-CORE IN PROGRESS; AC04/AC07 PENDING. De beelden zijn niet publiek vrijgegeven. Beschrijvingen zijn voornamelijk afkomstig uit een historische OCR-index; waar de bron dat vermeldt, is een screenshot afzonderlijk visueel bekeken. De tijdstempels komen uit bestandsnamen, niet uit onafhankelijke logging.

**ID-reeks:** `M04-ZIP-001` t/m `M04-ZIP-270` is **niet** hetzelfde als de oudere private `M04-EV-001` t/m `M04-EV-210`. Geen nieuwe SSOT.

[README](README.md) · [GAP-analyse](M04-GAPS.md) · [Evidence CSV](M04-EVIDENCE.csv) · [Status per beeld](M04-PUBLICATIESTATUS.md)

## M04 themamappen

- [01 Pre migration baseline](01_Pre_migration_baseline/README.md) (14 records)
- [02 VM Network setup](02_VM_Network_setup/README.md) (29 records)
- [03 FUXA OpenPLC baseline](03_FUXA_OpenPLC_baseline/README.md) (28 records)
- [04 Architecture design](04_Architecture_design/README.md) (6 records)
- [05 PLC01 provisioning](05_PLC01_provisioning/README.md) (10 records)
- [06 PLC program runtime](06_PLC_program_runtime/README.md) (25 records)
- [07 FUXA Modbus AC01 03](07_FUXA_Modbus_AC01_03/README.md) (20 records)
- [08 Pre migration safety](08_Pre_migration_safety/README.md) (12 records)
- [09 OT interface rules](09_OT_interface_rules/README.md) (12 records)
- [10 Snapshots migration](10_Snapshots_migration/README.md) (0 records)
- [11 Client routes tests](11_Client_routes_tests/README.md) (7 records)
- [12 LAN OT firewall](12_LAN_OT_firewall/README.md) (19 records)
- [13 LAN port forward](13_LAN_port_forward/README.md) (9 records)
- [14 pfSense logs](14_pfSense_logs/README.md) (19 records)
- [15 VMnet adapters](15_VMnet_adapters/README.md) (20 records)
- [16 OT AC04 AC07](16_OT_AC04_AC07/README.md) (11 records)
- [17 Network diagnostics](17_Network_diagnostics/README.md) (11 records)
- [18 Forward and regression](18_Forward_and_regression/README.md) (8 records)
- [19 FUXA followup](19_FUXA_followup/README.md) (10 records)

## Bronrecords op datum

### 31-10-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-001` | 31-10-2026 21:52:44 | **CONFIG** | AC04 (voorgeschiedenis LAB) | Client01-VM: netwerkadapter op NAT (voor de verplaatsing naar het LAB-segment). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-002` | 31-10-2026 22:00:04 | **CONFIG** | AC04 beginsituatie | pfSense-VM: 3 adapters - Host-only, NAT, LAN Segment (beginsituatie vóór OT). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-003` | 31-10-2026 22:01:55 | **CONFIG** | AC04 beginsituatie | pfSense-VM: adapter 3 op LAN segment S-HT-LAN01-ISOLATED. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-004` | 31-10-2026 22:08:17 | **CONFIG** | Beginsituatie | pfSense Status / Dashboard (volledig scherm; details in OCR beperkt leesbaar). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-005` | 31-10-2026 22:11:32 | **CONFIG** | Beginsituatie | pfSense Interfaces / LAB (em2). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-006` | 31-10-2026 22:12:52 | **CONFIG** | Beginsituatie | pfSense Interfaces / Interface Assignments. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-007` | 31-10-2026 22:13:34 | **CONFIG** | Beginsituatie | pfSense Services / DHCP Server / LAN. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-008` | 31-10-2026 22:14:16 | **CONFIG** | AC07 regelset LAB | Firewall / Rules / LAB beginsituatie: o.a. 'Block lab naar prive-netwerken' en 'Pass LAB naar internet'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-009` | 31-10-2026 22:17:43 | **CONFIG** | DHCP LAB | pfSense Services / DHCP Server / LAB. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-010` | 31-10-2026 22:22:37 | **TROUBLESHOOT** | DHCP LAB | Waarschuwing: 'ISC DHCP has reached end-of-life' - verwijzing naar wisselen van DHCP-backend. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-011` | 31-10-2026 23:22:14 | **CONFIG** | Rollback | pfSense Diagnostics / Backup & Restore vóór de wijziging. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-012` | 31-10-2026 23:23:39 | **CONFIG** | Rollback | Downloadmelding config-PFSENSE_HOSTNAME-...xml (configuratieback-up gedownload). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-013` | 31-10-2026 23:28:00 | **FIX** | DHCP LAB | pfSense System / Advanced / Networking (wissel DHCP-backend naar Kea). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-014` | 31-10-2026 23:34:07 | **CONFIG** | DHCP LAB | DHCP Server / LAB na de backendwissel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-015` | 31-10-2026 23:43:30 | **TEST** | DHCP LAB | Status / Services: kea-dhcp4, unbound, ntpd e.a. als actief weergegeven. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-016` | 31-10-2026 23:50:31 | **TEST** | Connectiviteit LAB | Client01 ipconfig: adres in [LAB_SUBNET] met gateway PFSENSE_LAB_GW_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-017` | 31-10-2026 23:55:28 | **FAIL** | Connectiviteit LAB | Client01: ping PFSENSE_LAB_GW_IP - 4/4 timed out (100% loss) na ipconfig /renew. | Nog niet gepubliceerd (review vereist) |

### 01-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-018` | 01-11-2026 00:00:35 | **TROUBLESHOOT** | AC07 regelset LAB | Firewalllog: regel 'Block lab naar prive-netwerken ([RULE_ID_REDACTED])' blokkeert [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN] -> PFSENSE_LAB_GW_IP:53. Oorzaak: RFC1918-blok vangt ook de eigen gateway. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-019` | 01-11-2026 00:03:45 | **CONFIG** | AC07 regelset LAB | Firewall / Rules / Edit (nieuwe regel; velden in OCR niet leesbaar). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-020` | 01-11-2026 00:10:57 | **FIX** | AC07 regelset LAB | Nieuwe LAB-regel opgeslagen, [RULE_ID_REDACTED], aangemaakt 11/1/26 00:10:13 (ICMP Client01 -> pfSense). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-021` | 01-11-2026 00:14:34 | **PASS** | Connectiviteit LAB | Client01: eerst 100% loss, daarna ping PFSENSE_LAB_GW_IP 4/4 replies - fix aantoonbaar in één venster. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-022` | 01-11-2026 00:17:10 | **CONFIG** | AC07 regelset LAB | LAB-regels: ALLOW ICMP Client01->pfSense, Block RFC1918, Pass LAB naar internet. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-023` | 01-11-2026 00:23:28 | **TEST** | Connectiviteit LAB | Client01 ipconfig /all: DHCP-server en DNS PFSENSE_LAB_GW_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-024` | 01-11-2026 00:29:43 | **CONFIG** | AC04 (voorgeschiedenis LAB) | Client01-VM: netwerkadapter nu op LAN Segment. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-025` | 01-11-2026 00:51:17 | **CONFIG** | NAT | Firewall / NAT / Outbound: automatische regels voor [MGMT_SUBNET] en [LAB_SUBNET]. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-026` | 01-11-2026 00:52:49 | **CONFIG** | AC07 regelset LAB | LAB-regels met tellers (Block RFC1918 heeft treffers). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-027` | 01-11-2026 01:00:52 | **CONFIG** | AC07 regelset LAB | Bewerken regel 1793054444 (was 'Pass LAB naar internet', aangemaakt 26-10). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-028` | 01-11-2026 01:02:27 | **FIX** | AC07 regelset LAB | Toegepast: brede 'Pass LAB naar internet' vervangen door 'TEMP Client01 outbound internet' (bron [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN]). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-029` | 01-11-2026 01:06:27 | **CONFIG** | AC07 regelset LAB | Nieuwe regel 'ALLOW Client01 DNS to pfSense'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-030` | 01-11-2026 01:08:50 | **CONFIG** | AC07 regelset LAB | Toegepaste LAB-regelset (4 regels): DNS, ICMP, Block RFC1918, TEMP Client01 outbound. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-031` | 01-11-2026 01:12:05 | **TEST** | Connectiviteit LAB | Client01: PowerShell en browser met geladen externe webpagina - uitgaand verkeer werkt na de regelwijziging. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-032` | 01-11-2026 01:20:47 | **CONFIG** | AC04 (voorgeschiedenis LAB) | WindowsServer-VM: adapter op LAN segment S-HT-LAN01-ISOLATED. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-033` | 01-11-2026 01:23:16 | **TEST** | Connectiviteit LAB | DC ipconfig /all: DHCP-adres in [LAB_SUBNET], DHCP/DNS PFSENSE_LAB_GW_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-034` | 01-11-2026 01:27:51 | **TEST** | Connectiviteit LAB | DC arp -a: PFSENSE_LAB_GW_IP -> PFSENSE_LAB_GW_MAC (pfSense LAB). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-035` | 01-11-2026 01:29:57 | **TROUBLESHOOT** | Connectiviteit LAB | DC: statisch adres DC01_LAB_IP met AddressState 'Invalid'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-036` | 01-11-2026 01:30:24 | **CONFIG** | Connectiviteit LAB | DC: Set-DnsClientServerAddress naar PFSENSE_LAB_GW_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-037` | 01-11-2026 01:31:16 | **TROUBLESHOOT** | Connectiviteit LAB | DC: AddressState 'Tentative'; ipconfig met gateway PFSENSE_LAB_GW_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-038` | 01-11-2026 01:38:36 | **PASS** | Connectiviteit LAB | DC (PS-HT-DC01): DC01_LAB_IP AddressState 'Preferred'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-039` | 01-11-2026 13:56:42 | **CONFIG** | Beginsituatie | pfSense-console: WAN em1 DHCP, LAN em0, LAB em2 (interface-overzicht). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-040` | 01-11-2026 13:59:49 | **TROUBLESHOOT** | AC07 regelset LAB | Firewalllog 1 nov: RFC1918-blok treft DC01_LAB_IP -> PFSENSE_LAB_GW_IP:53 UDP (DNS van de DC wordt geblokkeerd). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-041` | 01-11-2026 14:03:01 | **PASS** | Connectiviteit LAB | Client: ping PFSENSE_LAB_GW_IP 4/4. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-042` | 01-11-2026 14:03:16 | **FAIL** | Connectiviteit LAB | WindowsServer: ping PFSENSE_LAB_GW_IP 100% loss (ICMP-regel geldt alleen voor Client01). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-043` | 01-11-2026 14:03:21 | **TEST** | Connectiviteit LAB | Beide vensters naast elkaar: client ping slaagt, server niet - bevestigt bronspecifieke regel. | Nog niet gepubliceerd (review vereist) |

### 02-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-044` | 02-11-2026 23:10:49 | **ERROR** | FUXA netwerk | FUXA01 eerste login: ens36 DOWN, 'Network is unreachable', DNS-resolutie mislukt. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-045` | 02-11-2026 23:13:04 | **TROUBLESHOOT** | FUXA netwerk | FUXA01: ens36 UP zonder IPv4; /etc/netplan/ is leeg. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-046` | 02-11-2026 23:19:15 | **ERROR** | FUXA netwerk | netplan: '01-fuxa.yaml:4:12: Error in network definition: expected mapping (check indentation)'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-047` | 02-11-2026 23:22:02 | **CONFIG** | AC04 | FUXA01-VM: adapter Custom (VMnet8, NAT) - FUXA staat buiten pfSense. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-048` | 02-11-2026 23:40:51 | **PASS** | FUXA netwerk | FUXA01: ping github.com 3/3 na correctie van de netplan-YAML. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-049` | 02-11-2026 23:44:44 | **CONFIG** | FUXA installatie | apt-installatie docker.io op FUXA01. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-050` | 02-11-2026 23:56:00 | **ERROR** | FUXA installatie | docker run verkeerd afgebroken ('--name: command not found'); daarna het volledige run-commando (poort 1881, volumes, frangoteam/fuxa:latest). | Nog niet gepubliceerd (review vereist) |

### 03-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-051` | 03-11-2026 00:06:07 | **CONFIG** | FUXA installatie | Image 'frangoteam/fuxa:latest' binnengehaald (digest zichtbaar) en container-ID teruggegeven. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-052` | 03-11-2026 01:38:44 | **TEST** | FUXA web | Browser: [REDACTED_URL] bereikbaar; security-setupwizard toont 'Authentication with Token: Disabled'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-053` | 03-11-2026 22:49:31 | **CONFIG** | AC05 context | WAZUH01-VM: adapter op LAN segment S-HT-LAN01-ISOLATED (LAB-zone achter pfSense). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-054` | 03-11-2026 22:58:58 | **ERROR** | AC05 context | Wazuh-VM: 'ip -4 addr' toont alleen loopback - geen IPv4-adres. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-055` | 03-11-2026 23:01:58 | **TROUBLESHOOT** | AC05 context | Wazuh-VM: nmcli niet aanwezig (command not found). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-056` | 03-11-2026 23:05:49 | **TROUBLESHOOT** | AC05 context | Wazuh-VM: networkctl status eth0 (link up, geen IPv4). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-057` | 03-11-2026 23:08:23 | **TROUBLESHOOT** | AC05 context | Wazuh-VM: systemd-networkd-log met 'lease lost' / service gestopt. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-058` | 03-11-2026 23:12:53 | **CONFIG** | DHCP LAB | pfSense DHCP Server (Kea) instellingenpagina. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-059` | 03-11-2026 23:21:08 | **CONFIG** | DHCP LAB | pfSense Services / DHCP Server / LAB. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-060` | 03-11-2026 23:23:36 | **PASS** | DHCP LAB | Status / DHCP Leases: [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN] uitgegeven aan 'wazuh-server' (03-11 23:11). Let op: [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN] is in de firewallregels 'Client01'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-061` | 03-11-2026 23:24:07 | **TEST** | AC05 context | Wazuh-VM: eth0 heeft dynamisch IPv4-adres. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-062` | 03-11-2026 23:28:17 | **PASS** | AC05 context | Wazuh-VM: wazuh-manager, wazuh-indexer en wazuh-dashboard 'active'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-063` | 03-11-2026 23:35:55 | **CONFIG** | Beheer | pfSense System / Advanced / Admin Access. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-064` | 03-11-2026 23:38:31 | **CONFIG** | NAT | Firewall / NAT / Port Forward: lijst nog leeg. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-065` | 03-11-2026 23:45:34 | **CONFIG** | NAT | Port forward 'Edit Redirect Entry' voor het Wazuh-dashboard; 'Add associated filter rule'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-066` | 03-11-2026 23:47:43 | **TEST** | NAT | Host: VMware Network Adapter VMnet1 = MGMT_CLIENT_IP (bron voor de port forward). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-067` | 03-11-2026 23:59:53 | **ERROR** | AC05 context | Wazuh-dashboard via port forward bereikbaar, maar 'Invalid username or password'. | Nog niet gepubliceerd (review vereist) |

### 04-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-068` | 04-11-2026 00:00:52 | **ERROR** | AC05 context | Wazuh-healthcheck: index geblokkeerd, 'disk usage exceeded flood-stage watermark'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-069` | 04-11-2026 00:17:41 | **TROUBLESHOOT** | AC05 context | Wazuh-VM: partitietabel/GPT-melding en df -hT / (root-FS kleiner dan de schijf). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-070` | 04-11-2026 00:35:52 | **FIX** | AC05 context | Wazuh-VM na herstel: lsblk toont sda1 op 50G. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-071` | 04-11-2026 00:38:50 | **PENDING** | AC05 | Wazuh-dashboard overzicht: 'This instance has no agents registered'. AC05 niet aangetoond. | Nog niet gepubliceerd (review vereist) |

### 05-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-072` | 05-11-2026 17:39:13 | **CONFIG** | PLC01 installatie | Ubuntu-installer netwerk: ens33 via DHCP ([HISTORIC_NAT_DHCP], VMnet8). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-073` | 05-11-2026 18:19:06 | **CONFIG** | PLC01 installatie | Eerste consolelogin plc01 (Ubuntu 24.04.5 LTS). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-074` | 05-11-2026 18:21:07 | **CONFIG** | PLC01 beheer | Eerste SSH-verbinding vanaf de host: ED25519-hostkey-fingerprint ter bevestiging. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-075` | 05-11-2026 18:25:57 | **CONFIG** | OpenPLC installatie | OpenPLC install.sh: Python-afhankelijkheden geïnstalleerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-076` | 05-11-2026 18:28:55 | **PASS** | OpenPLC installatie | 'Compilation finished successfully!' (alleen build van de runtime). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-077` | 05-11-2026 18:34:25 | **TEST** | OpenPLC web | Web-UI op PLC01_TEMP_NAT_IP:8080: Users-pagina, 'Status: Stopped'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-078` | 05-11-2026 18:44:45 | **CONFIG** | OpenPLC | Dashboard: Blank Program, Stopped. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-079` | 05-11-2026 18:45:37 | **CONFIG** | OpenPLC protocollen | Settings: protocolservers en poorten (Modbus, DNP3, EtherNet/IP 44818), 'Start OpenPLC in RUN mode'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-080` | 05-11-2026 19:55:36 | **CONFIG** | PLC01 | plc01: geheugen en schijfgebruik (57% van 9,8G). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-081` | 05-11-2026 19:58:12 | **CONFIG** | OpenPLC protocollen | Settings (tweede opname): EtherNet/IP en persistent storage zichtbaar. Opgeslagen eindtoestand niet aantoonbaar. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-082` | 05-11-2026 22:23:49 | **CONFIG** | AC01 programma | nano: opslaan als [REDACTED_LOCAL_PATH]/M04_Motor_Simulation.st. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-083` | 05-11-2026 22:26:13 | **TEST** | AC01 programma | iec2c op het ST-bestand levert POUS.c, LOCATED_VARIABLES.h, VARIABLES.csv e.d. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-084` | 05-11-2026 22:32:59 | **CONFIG** | AC01 programma | ST-bron v1: Motor_Start gemapt op %IX (ingang). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-085` | 05-11-2026 22:41:21 | **ERROR** | AC01 programma | iec2c: 'unexpected token after VAR in located variable(s) declaration' - 3 error(s), Bailing out. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-086` | 05-11-2026 22:44:18 | **FIX** | AC01 programma | ST-bron aangepast: Motor_Start AT %QX0.0 (coil i.p.v. ingang). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-087` | 05-11-2026 22:48:29 | **TROUBLESHOOT** | AC01 programma | Venster met zowel '3 error(s) found' als latere VARIABLES-uitvoer (tussenstap). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-088` | 05-11-2026 23:01:22 | **CONFIG** | AC01 programma | Web-UI Programs: M04_Motor_Simulation.st geselecteerd voor upload. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-089` | 05-11-2026 23:05:18 | **ERROR** | AC01 programma | Melding 'Program Name cannot be blank'; daarna Program Info 'M04 Motor Simulation v1.0', file 504923.st. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-090` | 05-11-2026 23:07:30 | **CONFIG** | AC01 programma | Web-UI: 'Compiling program / Generating C files'. Eindmelding van deze build niet in de selectie. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-091` | 05-11-2026 23:11:22 | **TEST** | AC01 / Modbus | plc01: ss -tlnp toont openplc luisterend op [WILDCARD_BIND]:502. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-092` | 05-11-2026 23:15:30 | **TEST** | AC01 | OpenPLC Monitoring UIT: Motor_Start/Running/Alarm FALSE, Temperature 25 (visueel bevestigd). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-093` | 05-11-2026 23:16:49 | **TEST** | AC01 | OpenPLC Monitoring tijdens schakelen (waarden in OCR niet eenduidig). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-094` | 05-11-2026 23:16:58 | **TEST** | AC01 | OpenPLC Monitoring terug UIT: alles FALSE, 25 (visueel bevestigd). | Nog niet gepubliceerd (review vereist) |

### 06-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-095` | 06-11-2026 00:00:48 | **TEST** | AC02 voorbereiding | plc01- en fuxa-terminals: adressen PLC01_TEMP_NAT_IP/.130, docker en listeners. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-096` | 06-11-2026 00:11:13 | **PASS** | Modbus TCP (NAT-topologie) | FUXA01 -> PLC01: 'Modbus TCP bereikbaar' (poorttest, geen Modbus-transactie). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-097` | 06-11-2026 00:24:00 | **CONFIG** | FUXA Modbus | FUXA Plugins-pagina: modbus-driver geïnstalleerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-098` | 06-11-2026 00:41:03 | **CONFIG** | FUXA Modbus | Connection PLC01-MOTOR: ModbusTCP, polling 1 sec, PLC01_TEMP_NAT_IP:502, Slave ID 1. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-099` | 06-11-2026 00:43:00 | **TEST** | FUXA Modbus | Device-tegel PLC01-MOTOR PLC01_TEMP_NAT_IP:502 Modbus-TCP Slave ID 1. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-100` | 06-11-2026 00:48:34 | **CONFIG** | AC02 tags | Tag Property Motor_Running (register/offset). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-101` | 06-11-2026 00:53:46 | **CONFIG** | AC02 tags | Tag Property: Coil Status (Read/Write 000001-065536), Bool, address offset. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-102` | 06-11-2026 01:03:20 | **CONFIG** | AC02 tags | Taglijst PLC01-MOTOR. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-103` | 06-11-2026 13:45:13 | **CONFIG** | AC01 | OpenPLC Programs: 'M04 Motor Simulation v1.0' geladen, Status Stopped. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-104` | 06-11-2026 14:12:31 | **CONFIG** | AC01 programma | plc01: cat van de definitieve ST-bron. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-105` | 06-11-2026 15:38:20 | **CONFIG** | AC01 | Dashboard: programma M04 Motor Simulation v1.0, Status Stopped. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-106` | 06-11-2026 15:40:12 | **TEST** | AC01 / Modbus | Dashboard Running; runtime-log: Modbus 502, EtherNet/IP 44818 en Snap7 (S7) gestart. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-107` | 06-11-2026 15:45:08 | **PASS** | Modbus TCP (NAT-topologie) | Host: Test-NetConnection PLC01_TEMP_NAT_IP:502 = True, bron VMnet8 [UNMAPPED_IPV4]. Bewijst bereik host->PLC, geen isolatie. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-108` | 06-11-2026 15:45:21 | **TEST** | Modbus | plc01: ss -lnt toont LISTEN [WILDCARD_BIND]:502. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-109` | 06-11-2026 16:10:23 | **ERROR** | Beheer | SSH 'Permission denied' met plcadmin@FUXA_TEMP_NAT_IP (verkeerde gebruiker voor de FUXA-VM). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-110` | 06-11-2026 16:13:01 | **PASS** | Modbus TCP (NAT-topologie) | FUXA01: /dev/tcp/PLC01_TEMP_NAT_IP/502 -> 'TCP PASS'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-111` | 06-11-2026 16:15:25 | **TEST** | FUXA | docker ps: fuxa 'Up 3 hours', 1881/tcp gepubliceerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-112` | 06-11-2026 16:32:13 | **TEST** | AC01 | OpenPLC: 'Running: M04 Motor Simulation v1.0'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-113` | 06-11-2026 16:33:26 | **PASS** | AC01 | Monitoring AAN: Motor_Start TRUE, Motor_Running TRUE, Alarm FALSE, Temperature 45 (visueel bevestigd). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-114` | 06-11-2026 16:36:55 | **PASS** | AC01 | Monitoring UIT: FALSE/FALSE/FALSE, 25, status Running (visueel bevestigd). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-115` | 06-11-2026 16:38:14 | **TEST** | AC02 | FUXA-tags: Motor_Running=0, Motor_Start=0, timestamp 06-11-2026 16:38:12 (visueel bevestigd). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-116` | 06-11-2026 16:39:06 | **TEST** | AC02 | FUXA-tags: beide 1, timestamp 16:39:03 (visueel bevestigd). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-117` | 06-11-2026 16:39:39 | **TEST** | AC02 | OpenPLC Monitoring op hetzelfde moment (tegenhanger van de FUXA-waarden). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-118` | 06-11-2026 16:40:19 | **TEST** | AC02 | OpenPLC Monitoring na terugschakelen. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-119` | 06-11-2026 16:40:27 | **PASS** | AC02 | FUXA-tags: beide terug naar 0, timestamp 16:40:25 - reeks 0->1->0 compleet voor Motor_Start en Motor_Running. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-120` | 06-11-2026 16:48:34 | **CONFIG** | AC03 HMI | FUXA-editor MainView. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-121` | 06-11-2026 16:50:38 | **CONFIG** | AC03 HMI | Tag selection: PLC01-MOTOR -> Motor_Start. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-122` | 06-11-2026 16:54:01 | **CONFIG** | AC03 HMI | Button settings > Events (actie op de tag). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-123` | 06-11-2026 16:56:51 | **CONFIG** | AC03 HMI | Button settings: naam Motor_Control. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-124` | 06-11-2026 16:59:12 | **TEST** | AC03 | OpenPLC Monitoring tijdens de HMI-proef. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-125` | 06-11-2026 16:59:38 | **TEST** | AC03 | FUXA runtime op FUXA_TEMP_NAT_IP met knop Motor_Control. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-126` | 06-11-2026 17:04:59 | **PASS** | AC03 | Schermopname (58,8 s): klik op Motor_Control in FUXA, OpenPLC Monitoring toont TRUE/TRUE/45 en daarna FALSE/FALSE/25. Steekproef van 5 frames bekeken; geen Modbus-pcap. | Video ontbreekt |
| `M04-ZIP-127` | 06-11-2026 23:13:00 | **CONFIG** | AC04 preflight | pfSense-console na boot (2.9.0-RELEASE), menu. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-128` | 06-11-2026 23:24:14 | **TEST** | AC04 preflight | Preflight FUXA01: ens36 FUXA_TEMP_NAT_IP, routes (VMnet8). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-129` | 06-11-2026 23:27:37 | **TEST** | AC04 preflight | Preflight PLC01: ens33 PLC01_TEMP_NAT_IP, routes (VMnet8). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-130` | 06-11-2026 23:30:51 | **CONFIG** | AC04 preflight | VM Settings: adapter op LAN segment S-HT-LAN01-ISOLATED (preflight-inventaris). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-131` | 06-11-2026 23:31:18 | **CONFIG** | AC04 preflight | FUXA01-VM: adapter VMnet8 (NAT). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-132` | 06-11-2026 23:31:51 | **CONFIG** | AC04 preflight | PLC01-VM: adapterinstellingen (VMnet8) boven de plc01-console. | Nog niet gepubliceerd (review vereist) |

### 07-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-133` | 07-11-2026 01:48:30 | **CONFIG** | AC04 rollback | Snapshot Manager pfSense: '26-10-26' en 'M04-CORE-PRE-MIGRATION...' aanwezig. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-134` | 07-11-2026 01:48:53 | **CONFIG** | AC04 rollback | Snapshot Manager FUXA01: 'M04-CORE-PRE-MIGRATION...'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-135` | 07-11-2026 01:49:25 | **CONFIG** | AC04 rollback | Snapshot Manager PLC01: 'M04-CORE-PRE-MIGRATION...'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-136` | 07-11-2026 21:37:12 | **CONFIG** | AC04 | pfSense-VM: Network Adapter 4 toegevoegd (nog NAT); Global LAN Segments: S-HT-LAN01-ISOLATED en S-HT-OT60-ISOLATED. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-137` | 07-11-2026 22:57:13 | **CONFIG** | AC04 | pfSense-VM adapter 4 -> LAN segment S-HT-OT60-ISOLATED. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-138` | 07-11-2026 22:57:48 | **CONFIG** | AC04 | pfSense-VM devices: 4 adapters (Host-only, NAT, LAN Segment, LAN Segment). | Nog niet gepubliceerd (review vereist) |

### 08-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-139` | 08-11-2026 00:26:46 | **CONFIG** | AC04 | pfSense Interfaces / OT (em3) (adresvelden in OCR niet leesbaar). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-140` | 08-11-2026 00:56:56 | **CONFIG** | AC07 | Firewall / Rules / OT: 'No rules are configured for this interface' (default deny volgens configuratie). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-141` | 08-11-2026 00:57:16 | **CONFIG** | AC07 | Firewall / Rules / LAB gelezen: ICMP-allow, Block RFC1918, TEMP Client01 outbound. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-142` | 08-11-2026 01:03:33 | **CONFIG** | AC07 | Alias RFC1918 = 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-143` | 08-11-2026 13:48:38 | **CONFIG** | AC04 rollback | VM-menu pfSense: snapshots 'M04-CORE-PRE-MIGRATION-pfSense' 07/11/2026 01:47:46 en '26-10-26'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-144` | 08-11-2026 13:51:56 | **CONFIG** | AC04 rollback | VM-menu FUXA01: 'M04-CORE-PRE-MIGRATION-FUXA01' 07/11/2026 01:48. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-145` | 08-11-2026 13:52:38 | **CONFIG** | AC04 rollback | VM-menu PLC01: 'M04-CORE-PRE-MIGRATION-PLC01' 07/11/2026 01:49. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-146` | 08-11-2026 14:59:18 | **TROUBLESHOOT** | AC04 beheerpad | Host: VMnet1 = MGMT_CLIENT_IP; Find-NetRoute PFSENSE_OT_IP kiest Wi-Fi via [UNMAPPED_IPV4] - de host bereikt OT niet rechtstreeks via pfSense. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-147` | 08-11-2026 16:40:08 | **CONFIG** | NAT | Port Forward-lijst: alleen HT-WAZUH-DASHBOARD-ACCESS (LAN 8443 -> [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN]:443, bron MGMT_CLIENT_IP). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-148` | 08-11-2026 17:10:29 | **CONFIG** | AC07 | Firewall / Rules / Floating: geen floating rules. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-149` | 08-11-2026 17:46:31 | **CONFIG** | AC07 | Regeldetails 'Block lab naar prive-netwerken': [RULE_ID_REDACTED], aangemaakt 26-10. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-150` | 08-11-2026 17:50:15 | **CONFIG** | AC04 beheerpad | Host: adapterdetails VMware Network Adapter VMnet1 (MAC zichtbaar). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-151` | 08-11-2026 17:53:07 | **CONFIG** | AC04 | pfSense-console (interface-overzicht na toevoegen OT). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-152` | 08-11-2026 18:29:06 | **CONFIG** | Logging | pfSense Status / System Logs / Settings (logrotatie, remote logging uit). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-153` | 08-11-2026 18:31:39 | **CONFIG** | Rollback | Diagnostics / Backup & Restore vóór de regelwijzigingen. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-154` | 08-11-2026 18:43:33 | **FAIL** | Rollback | PowerShell-controle van het back-upbestand: grootte 26402, HeeftEncryptedConfig False, HeeftPfSenseConfig False. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-155` | 08-11-2026 18:46:19 | **FAIL** | Rollback | Tweede controle: XML False, Base64OpenSSL False, BinaryOpenSSL False - bestand is niet als geldige pfSense-config herkend. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-156` | 08-11-2026 18:47:43 | **CONFIG** | Rollback | Diagnostics / Config History (interne configuratieversies). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-157` | 08-11-2026 18:54:23 | **CONFIG** | AC07 LAN | LAN-regels VOOR M04: Default allow LAN to any (IPv4/IPv6) + NAT-regel Wazuh-dashboard. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-158` | 08-11-2026 20:09:51 | **CONFIG** | AC04 | Interface OT (opt2): instellingenpagina incl. block private/bogon-opties. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-159` | 08-11-2026 20:15:19 | **CONFIG** | Rollback | Backup Configuration opnieuw (area All). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-160` | 08-11-2026 20:16:39 | **PENDING** | Rollback | Twee back-upbestanden (18:36 en 20:15), beide 25 KB, type 'Microsoft Edge HTM...'. Inhoud niet gevalideerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-161` | 08-11-2026 20:42:35 | **CONFIG** | AC07 LAN->OT | Nieuwe LAN-regel: Block, beschrijving 'M04 LAN -> OT default deny'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-162` | 08-11-2026 20:45:25 | **CONFIG** | AC07 LAN->OT | LAN-regellijst direct na toevoegen van de blokregel (positie t.o.v. de default allow in deze opname niet gecontroleerd; eindvolgorde zie 2026-11-09 170520). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-163` | 08-11-2026 20:51:32 | **TEST** | AC07 LAN->OT | Status / Filter Reload: regels geladen, 'Done'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-164` | 08-11-2026 21:11:16 | **CONFIG** | NAT PLC01 | Port forward aanmaken (Edit Redirect Entry) voor PLC01. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-165` | 08-11-2026 21:28:19 | **CONFIG** | NAT PLC01 | Bron van de port forward: Network MGMT_CLIENT_IP / 32. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-166` | 08-11-2026 21:37:23 | **CONFIG** | NAT PLC01 | Filter rule association: 'Add unassociated filter rule'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-167` | 08-11-2026 21:40:21 | **CONFIG** | NAT PLC01 | Port Forward-lijst: 'M04 MGMT -> PLC01 web' LAN 8080 -> PLC01_OT_IP:8080 naast de Wazuh-regel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-168` | 08-11-2026 21:46:10 | **CONFIG** | AC07 LAN | LAN-regels: 'NAT M04 MGMT -> PLC01 web' toegevoegd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-169` | 08-11-2026 21:51:19 | **CONFIG** | AC07 LAN | LAN-regels na Apply. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-170` | 08-11-2026 21:59:21 | **TEST** | AC07 (beperkt) | Host: Test-NetConnection PFSENSE_MGMT_IP:22 = False (ping True). Doel is pfSense zelf; geen bewijs van OT-isolatie. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-171` | 08-11-2026 22:08:43 | **CONFIG** | AC07 | pfctl -sr: default deny IPv4 in/out ([RULE_ID_REDACTED]/104). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-172` | 08-11-2026 22:13:02 | **CONFIG** | AC07 | pfctl -sr: anti-lockout en Client01 DNS-regels. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-173` | 08-11-2026 22:13:09 | **CONFIG** | AC07 | pfctl -sr (einde): TEMP Client01 outbound internet ([RULE_ID_REDACTED]) nog actief. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-174` | 08-11-2026 22:16:03 | **CONFIG** | NAT PLC01 | Regeldetails: [RULE_ID_REDACTED], 'Created 11/8/26 21:39:48 by NAT Port Forward'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-175` | 08-11-2026 22:26:52 | **CONFIG** | AC07 LAN | Zelfstandige passregel 'M04 MGMT PLC01 explicit allow'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-176` | 08-11-2026 22:29:15 | **CONFIG** | NAT PLC01 | Filter rule association omgezet naar 'None'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-177` | 08-11-2026 22:29:54 | **CONFIG** | NAT PLC01 | Port Forward / Edit: association None, aangemaakt 11/8/26 21:39:48. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-178` | 08-11-2026 22:45:47 | **TEST** | AC07 LAN->OT | pfctl -sr: 'block drop in log quick on em0 from <LAN__NETWORK> to [OT_SUBNET]' (M04 LAN -> OT default deny, id 1794167081) geladen. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-179` | 08-11-2026 22:57:14 | **CONFIG** | NAT FUXA01 | Port forward voor FUXA01 aanmaken, association None. LET OP: op 11-11 blijkt de bron hier foutief ([MALFORMED_SOURCE_ADDRESS]). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-180` | 08-11-2026 23:02:17 | **CONFIG** | AC07 LAN | Zelfstandige passregel 'M04 MGMT FUXA01 explicit allow' (FUXA01 staat dan nog niet in OT). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-181` | 08-11-2026 23:03:37 | **CONFIG** | AC07 LAN | LAN-regellijst na toevoegen FUXA-regel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-182` | 08-11-2026 23:08:54 | **TEST** | AC07 LAN | pfctl -sr: FUXA01 allow, PLC01 explicit allow ([RULE_ID_REDACTED]), daarna LAN -> OT default deny - volgorde geladen. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-183` | 08-11-2026 23:10:27 | **CONFIG** | AC04 PLC01 | PLC01-VM adapter > Advanced: MAC-adres zichtbaar. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-184` | 08-11-2026 23:11:19 | **CONFIG** | AC04 PLC01 | PLC01-VM adapter VOOR migratie: Custom VMnet8 (NAT). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-185` | 08-11-2026 23:14:22 | **CONFIG** | AC04 PLC01 | PLC01-VM adapter -> LAN segment S-HT-OT60-ISOLATED. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-186` | 08-11-2026 23:22:52 | **CONFIG** | AC04 PLC01 | PLC01-VM: instelling bevestigd, LAN segment S-HT-OT60-ISOLATED. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-187` | 08-11-2026 23:25:49 | **FAIL** | Beheerpad PLC01 | Host: Test-NetConnection PFSENSE_MGMT_IP:8080 = False (PLC01 heeft nog geen OT-adres). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-188` | 08-11-2026 23:29:28 | **ERROR** | PLC01 netwerk | plc01 na segmentwissel: ens33 UP met alleen IPv6 link-local, lege routetabel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-189` | 08-11-2026 23:31:47 | **TROUBLESHOOT** | PLC01 netwerk | plc01: systemd-networkd-log (Link UP, Gained carrier, geen DHCP-lease). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-190` | 08-11-2026 23:37:52 | **TROUBLESHOOT** | PLC01 netwerk | plc01: bestaande netplan (dhcp4 true), cloud-init disabled-by-marker-file. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-191` | 08-11-2026 23:46:28 | **CONFIG** | PLC01 netwerk | Netplan-YAML: ens33 statisch PLC01_OT_IP, default via PFSENSE_OT_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-192` | 08-11-2026 23:48:59 | **TEST** | PLC01 netwerk | sudo netplan get / generate zonder fouten. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-193` | 08-11-2026 23:50:32 | **CONFIG** | PLC01 netwerk | netplan try --timeout 120 (bevestigingsprompt). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-194` | 08-11-2026 23:52:39 | **PASS** | PLC01 netwerk | plc01: ens33 PLC01_OT_IP, default via PFSENSE_OT_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-195` | 08-11-2026 23:54:18 | **FAIL** | AC07 OT (verwacht) | plc01: ping PFSENSE_OT_IP 0/4 (100% loss). Verwacht gedrag zonder OT-regels; zie firewalllog 000517. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-196` | 08-11-2026 23:57:21 | **TEST** | PLC01 netwerk | plc01: ip neigh PFSENSE_OT_IP lladdr PFSENSE_OT_MAC STALE - L2-bereik naar de OT-gateway. | Nog niet gepubliceerd (review vereist) |

### 09-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-197` | 09-11-2026 00:03:23 | **TEST** | AC07 OT | Firewalllog OT: 'Default deny rule IPv4 ([RULE_ID_REDACTED])' op DHCP-broadcasts (8 nov 23:42-23:44). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-198` | 09-11-2026 00:05:17 | **PASS** | AC07 OT | Firewalllog OT: Default deny blokkeert ICMP PLC01_OT_IP -> PFSENSE_OT_IP (8 nov 23:53). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-199` | 09-11-2026 00:09:24 | **CONFIG** | AC07 OT | OT-regel toegevoegd en toegepast: 'M04 TEMP PLC01 to OT gateway ICMP' (echoreq). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-200` | 09-11-2026 00:10:50 | **PASS** | AC07 OT | plc01: ping PFSENSE_OT_IP 4/4 met de tijdelijke regel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-201` | 09-11-2026 00:12:32 | **TEST** | AC07 OT | plc01: eerst 4/4, daarna 0/4 (na uitschakelen tijdelijke regel). Bijbehorende firewalllog ontbreekt. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-202` | 09-11-2026 00:14:58 | **PASS** | Beheerpad PLC01 | Host: Test-NetConnection PFSENSE_MGMT_IP:8080 = True, bron VMnet1 MGMT_CLIENT_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-203` | 09-11-2026 00:16:37 | **PASS** | Beheerpad PLC01 | Host: HTTP-antwoord met 'Location: /login' via de port forward. LET OP: Set-Cookie sessiewaarde zichtbaar. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-204` | 09-11-2026 00:17:14 | **PASS** | Beheerpad PLC01 | Host: curl [REDACTED_URL] -> 'HTTP status: 302'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-205` | 09-11-2026 00:23:17 | **PASS** | PLC01 persistentie | plc01 na nieuwe consolelogin: ens33 PLC01_OT_IP en default route aanwezig. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-206` | 09-11-2026 00:24:10 | **PASS** | PLC01 persistentie | Gecombineerd: plc01-adres/route en TcpTestSucceeded True in één beeld. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-207` | 09-11-2026 17:05:20 | **CONFIG** | AC07 LAN | LAN-regels 9 nov (visueel bevestigd), volgorde: Anti-Lockout; M04 MGMT FUXA01 allow (MGMT_CLIENT_IP -> FUXA01_OT_IP:1881); M04 MGMT PLC01 allow (-> PLC01_OT_IP:8080); M04 LAN -> OT default deny (LAN subnets -> [OT_SUBNET]); Default allow LAN IPv4/IPv6; NAT Wazuh. Alle tellers 0/0 B. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-208` | 09-11-2026 17:05:39 | **CONFIG** | AC07 OT / SSOT-M04-005 | OT-regels 9 nov 17:05: 'M04 TEMP PLC01 to OT gateway ICMP' staat er nog, grijs weergegeven met inschakel-icoon = uitgeschakeld (visueel bevestigd). Toont de configuratiestand, geen hertest. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-209` | 09-11-2026 17:09:37 | **TEST** | AC04 FUXA01 | FUXA01 vóór migratie: ens36 FUXA_TEMP_NAT_IP (VMnet8). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-210` | 09-11-2026 17:35:36 | **TEST** | AC04 FUXA01 | FUXA01 na herstart op OT-segment: netplan nog 'dhcp4: true'; docker fuxa Up. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-211` | 09-11-2026 18:04:02 | **ERROR** | FUXA01 netwerk | 'systemctl is-system-running: degraded'; back-up van de YAML; heredoc afgebroken na invoer 'df'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-212` | 09-11-2026 18:12:02 | **CONFIG** | FUXA01 netwerk | nano /etc/netplan/01-fuxa.yaml: ens36 FUXA01_OT_IP, default via PFSENSE_OT_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-213` | 09-11-2026 18:15:10 | **TEST** | FUXA01 netwerk | netplan generate / get: adres FUXA01_OT_IP, dhcp4 false. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-214` | 09-11-2026 18:24:02 | **TEST** | FUXA01 netwerk | netplan apply; docker ps: fuxa Up 56 minutes, 1881 gepubliceerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-215` | 09-11-2026 18:34:29 | **PASS** | FUXA01 lokaal | FUXA01: lokale HTTP-headers (Content-Length 66382) en ip neigh PFSENSE_OT_IP REACHABLE. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-216` | 09-11-2026 18:41:57 | **CONFIG** | AC07 pfSense->FUXA | GIF (38 frames): Diagnostics / Test Port, bronadres 'OT' wordt geselecteerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-217` | 09-11-2026 18:44:09 | **PASS** | AC07 pfSense->FUXA | Diagnostics / Test Port: 'Port test to host: FUXA01_OT_IP Port: 1881 successful'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-218` | 09-11-2026 18:48:17 | **TROUBLESHOOT** | Beheerpad | Host ipconfig: Wi-Fi-gateway [UNMAPPED_IPV4] (context voor verkeerde bronkeuze). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-219` | 09-11-2026 18:57:53 | **CONFIG** | Beheerpad FUXA01 | Diagnostics / Packet Capture op LAN (em0) ingesteld. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-220` | 09-11-2026 19:02:39 | **FAIL** | Beheerpad FUXA01 | Host: Test-NetConnection PFSENSE_MGMT_IP:1881 = False (ping True), met capture-venster. Oorzaak pas op 11-11 gevonden. | Nog niet gepubliceerd (review vereist) |

### 11-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-221` | 11-11-2026 17:02:34 | **CONFIG** | AC07 testclient | Client01-VM adapterinstellingen (LAN segment-keuze; TPM aanwezig). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-222` | 11-11-2026 17:10:15 | **CONFIG** | AC07 testclient | VM adapter op LAN segment S-HT-LAN01-ISOLATED. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-223` | 11-11-2026 17:16:01 | **CONFIG** | DHCP LAB | DHCP Server LAB: Kea, 'Enable DHCP server on LAB'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-224` | 11-11-2026 17:17:25 | **CONFIG** | DHCP LAN | DHCP Server LAN-tabblad (LAN-DHCP; uitgeschakeld laten). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-225` | 11-11-2026 17:21:33 | **TEST** | AC07 testclient | Client01: gateway en routetabel (bron [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN]). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-226` | 11-11-2026 17:23:01 | **PASS** | AC07 testclient | Client01: Test-Connection PFSENSE_LAB_GW_IP geeft antwoorden. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-227` | 11-11-2026 17:29:14 | **TEST** | AC07 LAB->OT | Client01 [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN] -> FUXA01_OT_IP:1881: TcpTestSucceeded False. Op zichzelf geen firewallbewijs. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-228` | 11-11-2026 17:30:11 | **TROUBLESHOOT** | DHCP LAB | pfSense systeemlog (herstart/IP-wijziging WAN, packages herstart). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-229` | 11-11-2026 17:31:05 | **TROUBLESHOOT** | DHCP LAB | Firewalllog: [APIPA]-verkeer (APIPA) geblokkeerd op LAN. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-230` | 11-11-2026 17:36:55 | **CONFIG** | AC07 LAB->OT | Packet Capture op LAB (em2) ingesteld. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-231` | 11-11-2026 17:39:47 | **TEST** | AC07 LAB->OT | Capture LAB em2: herhaalde TCP-pakketten bron .100 -> doel .20 poort 1881 (ingress op LAB zichtbaar; adressen in OCR vervormd). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-232` | 11-11-2026 17:40:23 | **TEST** | AC07 LAB->OT | Client01: opnieuw TcpTestSucceeded False. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-233` | 11-11-2026 17:44:52 | **TROUBLESHOOT** | AC07 LAB->OT | Capturepagina met 'OT (em3)' geselecteerd, maar uitvoerlabel 'packetcapture-em2-20261111173719.pcap'. Labelconflict: niet bruikbaar als OT-egressbewijs. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-234` | 11-11-2026 17:58:44 | **TEST** | AC07 LAB->OT | Client01: derde poging, False. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-235` | 11-11-2026 17:59:30 | **TEST** | AC07 LAB->OT | Nieuwe capture op em3 (tcpdump -ni em3, host FUXA01_OT_IP, tcp 1881), bestand packetcapture-em3-20261111175509.pcap; geen pakketten zichtbaar. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-236` | 11-11-2026 18:02:16 | **CONFIG** | AC07 LAB->OT | LAB-regels met tellers: Block RFC1918 heeft treffers; TEMP Client01 outbound staat eronder. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-237` | 11-11-2026 18:04:10 | **PASS** | AC07 LAB->OT | Firewalllog LAB: BLOCK 'Block lab naar prive-netwerken ([RULE_ID_REDACTED])' [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN] -> FUXA01_OT_IP:1881 TCP:S, 17:57-17:58. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-238` | 11-11-2026 18:06:24 | **TEST** | AC07 LAB->OT | Client01: 'TCP connect to (FUXA01_OT_IP : 1881) failed'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-239` | 11-11-2026 18:07:08 | **PASS** | AC07 LAB->OT | Firewalllog LAB: zelfde BLOCK, laatste regel 18:05:49. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-240` | 11-11-2026 18:11:10 | **TROUBLESHOOT** | Beheerpad | Host -> PLC01_OT_IP:1881 via Wi-Fi [UNMAPPED_IPV4]: False. Verkeerde bron én verkeerde poort; ongeldig als test. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-241` | 11-11-2026 18:11:16 | **TEST** | AC07 | Firewalllog met filter: '0 Matched Firewall Log Entries'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-242` | 11-11-2026 18:17:41 | **FAIL** | Beheerpad | Host: PFSENSE_MGMT_IP:8080 False en 1881 failed (volgens log stonden VM's uit; ongeldig als firewallbewijs). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-243` | 11-11-2026 18:25:14 | **PASS** | Beheerpad PLC01 | Host: PFSENSE_MGMT_IP:8080 = True (bron MGMT_CLIENT_IP). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-244` | 11-11-2026 18:34:11 | **FAIL** | Beheerpad FUXA01 | Host: PFSENSE_MGMT_IP:1881 = False terwijl 8080 True is. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-245` | 11-11-2026 18:39:19 | **TROUBLESHOOT** | NAT FUXA01 | pfctl -sn (visueel bevestigd): rdr voor poort 1881 heeft bron '[MALFORMED_SOURCE_ADDRESS]' (eerste cijfer ontbreekt); de regels voor 8080 en 8443 hebben 'MGMT_CLIENT_IP'. Root cause van de mislukte FUXA-beheertests. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-246` | 11-11-2026 18:45:06 | **FIX** | NAT FUXA01 | Port Forward / Edit FUXA01 (aangemaakt 11/8/26 23:00:17): bron gecorrigeerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-247` | 11-11-2026 18:52:24 | **PASS** | Beheerpad FUXA01 | Host: PFSENSE_MGMT_IP:1881 = True en 8080 = True na de NAT-correctie. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-248` | 11-11-2026 18:52:34 | **PASS** | NAT | pfctl -sn na correctie (visueel bevestigd): alle drie rdr-regels (1881 -> FUXA01_OT_IP, 8080 -> PLC01_OT_IP, 8443 -> [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN]:443) met bron MGMT_CLIENT_IP. | Nog niet gepubliceerd (review vereist) |

### 15-11-2026

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-249` | 15-11-2026 16:14:05 | **TEST** | Connectiviteit LAB | hybrid-theory-linux: hostname -I = LAB_NET_IP, alleen lokale route (geen default route). Zelfde adres als DC01 op 1 november. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-250` | 15-11-2026 16:31:52 | **ERROR** | Connectiviteit LAB | hybrid-theory-linux: 'Temporary failure resolving nl.archive.ubuntu.com'; geen default route. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-251` | 15-11-2026 16:55:12 | **TEST** | FUXA01 persistentie | FUXA01 nieuwe consolelogin 15 nov: docker fuxa 'Up About a minute' (start na boot). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-252` | 15-11-2026 16:58:54 | **PASS** | Beheerpad FUXA01 | Host: PFSENSE_MGMT_IP:1881 = True (bron VMnet1). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-253` | 15-11-2026 17:00:04 | **PASS** | FUXA web via beheerpad | Host: curl -I via port forward geeft HTTP-headers (text/html, 66382 bytes, 15 nov 15:59 GMT). Statusregel zelf staat boven het zichtbare deel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-254` | 15-11-2026 17:08:58 | **FAIL** | AC01-AC03 regressie | FUXA01 -> PLC01_OT_IP:502: 'No route to host' - MODBUS TCP FAIL. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-255` | 15-11-2026 17:13:27 | **TROUBLESHOOT** | AC01-AC03 regressie | FUXA01: route via ens36, ip neigh PLC01_OT_IP = FAILED (geen L2-bereik). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-256` | 15-11-2026 17:15:09 | **TEST** | AC01-AC03 regressie | plc01: adres PLC01_OT_IP en route aanwezig, neighbour-tabel leeg. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-257` | 15-11-2026 17:17:38 | **TROUBLESHOOT** | AC04 PLC01 | PLC01-VM adapterinstellingen gecontroleerd (device status / segment). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-258` | 15-11-2026 17:18:01 | **FIX** | AC04 PLC01 | PLC01-VM adapter: LAN segment S-HT-OT60-ISOLATED (her)bevestigd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-259` | 15-11-2026 17:20:49 | **PASS** | Intra-OT bereik | plc01 -> FUXA01_OT_IP: ping 3/3. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-260` | 15-11-2026 17:23:54 | **PASS** | Intra-OT bereik | FUXA01 -> PLC01_OT_IP: ping 3/3; neigh REACHABLE (PLC01_OT_MAC). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-261` | 15-11-2026 17:26:19 | **FAIL** | AC01-AC03 regressie | FUXA01 -> PLC01_OT_IP:502: 'Connection refused' - MODBUS TCP FAIL (runtime draait niet). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-262` | 15-11-2026 17:33:28 | **TROUBLESHOOT** | AC01-AC03 regressie | plc01: niets op :502, wel python3 op :8080; geen failed units. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-263` | 15-11-2026 17:59:54 | **TEST** | Beheerpad | Browser: PFSENSE_MGMT_IP:8080/login en FUXA op PFSENSE_MGMT_IP:1881 met Motor_Control. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-264` | 15-11-2026 18:15:51 | **TROUBLESHOOT** | AC01-AC03 regressie | plc01: ping naar FUXA 3/3; controle op failed units en OpenPLC-map. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-265` | 15-11-2026 18:57:00 | **TEST** | AC01 regressie | OpenPLC-dashboard via beheerpad: programma M04 Motor Simulation v1.0, 'Status: Stopped'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-266` | 15-11-2026 18:57:59 | **FIX** | AC01 regressie | Start PLC: runtime-log 'start_modbus() ... port 502', EtherNet/IP 44818 gestart. Titelregel in OCR toont nog 'Stopped'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-267` | 15-11-2026 19:06:19 | **TEST** | Modbus OT | plc01: ss toont openplc LISTEN op [WILDCARD_BIND]:502. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-268` | 15-11-2026 19:10:08 | **PASS** | Modbus TCP (OT-topologie) | FUXA01: eerst 'Connection refused', daarna 'MODBUS TCP PASS' naar PLC01_OT_IP:502. Poortbereik, geen Modbus-transactie. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-269` | 15-11-2026 19:32:31 | **PENDING** | AC02/AC03 regressie | FUXA device PLC01-MOTOR staat nog op PLC01_TEMP_NAT_IP:502 (oud NAT-adres). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-270` | 15-11-2026 19:34:16 | **PENDING** | AC02/AC03 regressie | FUXA Connection property: Slave IP and Port nog PLC01_TEMP_NAT_IP:502. Laatste beeld in de ZIP; herconfiguratie en tagtest niet aangetoond. | Nog niet gepubliceerd (review vereist) |

