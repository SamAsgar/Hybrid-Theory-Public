# 17 Network diagnostics

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 11 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-219` | 09-11-2026 18:57:53 | **CONFIG** | Beheerpad FUXA01 | Diagnostics / Packet Capture op LAN (em0) ingesteld. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-220` | 09-11-2026 19:02:39 | **FAIL** | Beheerpad FUXA01 | Host: Test-NetConnection PFSENSE_MGMT_IP:1881 = False (ping True), met capture-venster. Oorzaak pas op 11-11 gevonden. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-221` | 11-11-2026 17:02:34 | **CONFIG** | AC07 testclient | Client01-VM adapterinstellingen (LAN segment-keuze; TPM aanwezig). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-222` | 11-11-2026 17:10:15 | **CONFIG** | AC07 testclient | VM adapter op LAN segment S-HT-LAN01-ISOLATED. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-223` | 11-11-2026 17:16:01 | **CONFIG** | DHCP LAB | DHCP Server LAB: Kea, 'Enable DHCP server on LAB'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-224` | 11-11-2026 17:17:25 | **CONFIG** | DHCP LAN | DHCP Server LAN-tabblad (LAN-DHCP; uitgeschakeld laten). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-225` | 11-11-2026 17:21:33 | **TEST** | AC07 testclient | Client01: gateway en routetabel (bron [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN]). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-226` | 11-11-2026 17:23:01 | **PASS** | AC07 testclient | Client01: Test-Connection PFSENSE_LAB_GW_IP geeft antwoorden. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-241` | 11-11-2026 18:11:16 | **TEST** | AC07 | Firewalllog met filter: '0 Matched Firewall Log Entries'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-249` | 15-11-2026 16:14:05 | **TEST** | Connectiviteit LAB | hybrid-theory-linux: hostname -I = LAB_NET_IP, alleen lokale route (geen default route). Zelfde adres als DC01 op 1 november. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-250` | 15-11-2026 16:31:52 | **ERROR** | Connectiviteit LAB | hybrid-theory-linux: 'Temporary failure resolving nl.archive.ubuntu.com'; geen default route. | Nog niet gepubliceerd (review vereist) |
