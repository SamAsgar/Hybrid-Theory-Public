# 02 VM Network setup

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 29 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-015` | 31-10-2026 23:43:30 | **TEST** | DHCP LAB | Status / Services: kea-dhcp4, unbound, ntpd e.a. als actief weergegeven. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-016` | 31-10-2026 23:50:31 | **TEST** | Connectiviteit LAB | Client01 ipconfig: adres in [LAB_SUBNET] met gateway PFSENSE_LAB_GW_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-017` | 31-10-2026 23:55:28 | **FAIL** | Connectiviteit LAB | Client01: ping PFSENSE_LAB_GW_IP - 4/4 timed out (100% loss) na ipconfig /renew. | Nog niet gepubliceerd (review vereist) |
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
