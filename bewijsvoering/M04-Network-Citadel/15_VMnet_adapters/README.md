# 15 VMnet adapters

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 20 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
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
| `M04-ZIP-209` | 09-11-2026 17:09:37 | **TEST** | AC04 FUXA01 | FUXA01 vóór migratie: ens36 FUXA_TEMP_NAT_IP (VMnet8). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-210` | 09-11-2026 17:35:36 | **TEST** | AC04 FUXA01 | FUXA01 na herstart op OT-segment: netplan nog 'dhcp4: true'; docker fuxa Up. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-211` | 09-11-2026 18:04:02 | **ERROR** | FUXA01 netwerk | 'systemctl is-system-running: degraded'; back-up van de YAML; heredoc afgebroken na invoer 'df'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-212` | 09-11-2026 18:12:02 | **CONFIG** | FUXA01 netwerk | nano /etc/netplan/01-fuxa.yaml: ens36 FUXA01_OT_IP, default via PFSENSE_OT_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-213` | 09-11-2026 18:15:10 | **TEST** | FUXA01 netwerk | netplan generate / get: adres FUXA01_OT_IP, dhcp4 false. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-214` | 09-11-2026 18:24:02 | **TEST** | FUXA01 netwerk | netplan apply; docker ps: fuxa Up 56 minutes, 1881 gepubliceerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-257` | 15-11-2026 17:17:38 | **TROUBLESHOOT** | AC04 PLC01 | PLC01-VM adapterinstellingen gecontroleerd (device status / segment). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-258` | 15-11-2026 17:18:01 | **FIX** | AC04 PLC01 | PLC01-VM adapter: LAN segment S-HT-OT60-ISOLATED (her)bevestigd. | Nog niet gepubliceerd (review vereist) |
