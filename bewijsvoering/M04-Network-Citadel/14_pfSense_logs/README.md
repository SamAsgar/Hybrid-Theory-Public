# 14 pfSense logs

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 19 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-195` | 08-11-2026 23:54:18 | **FAIL** | AC07 OT (verwacht) | plc01: ping PFSENSE_OT_IP 0/4 (100% loss). Verwacht gedrag zonder OT-regels; zie firewalllog 000517. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-197` | 09-11-2026 00:03:23 | **TEST** | AC07 OT | Firewalllog OT: 'Default deny rule IPv4 ([RULE_ID_REDACTED])' op DHCP-broadcasts (8 nov 23:42-23:44). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-198` | 09-11-2026 00:05:17 | **PASS** | AC07 OT | Firewalllog OT: Default deny blokkeert ICMP PLC01_OT_IP -> PFSENSE_OT_IP (8 nov 23:53). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-199` | 09-11-2026 00:09:24 | **CONFIG** | AC07 OT | OT-regel toegevoegd en toegepast: 'M04 TEMP PLC01 to OT gateway ICMP' (echoreq). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-200` | 09-11-2026 00:10:50 | **PASS** | AC07 OT | plc01: ping PFSENSE_OT_IP 4/4 met de tijdelijke regel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-201` | 09-11-2026 00:12:32 | **TEST** | AC07 OT | plc01: eerst 4/4, daarna 0/4 (na uitschakelen tijdelijke regel). Bijbehorende firewalllog ontbreekt. | Nog niet gepubliceerd (review vereist) |
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
