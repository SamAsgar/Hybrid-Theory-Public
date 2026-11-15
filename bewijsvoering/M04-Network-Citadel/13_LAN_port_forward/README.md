# 13 LAN port forward

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 9 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-164` | 08-11-2026 21:11:16 | **CONFIG** | NAT PLC01 | Port forward aanmaken (Edit Redirect Entry) voor PLC01. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-165` | 08-11-2026 21:28:19 | **CONFIG** | NAT PLC01 | Bron van de port forward: Network MGMT_CLIENT_IP / 32. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-166` | 08-11-2026 21:37:23 | **CONFIG** | NAT PLC01 | Filter rule association: 'Add unassociated filter rule'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-167` | 08-11-2026 21:40:21 | **CONFIG** | NAT PLC01 | Port Forward-lijst: 'M04 MGMT -> PLC01 web' LAN 8080 -> PLC01_OT_IP:8080 naast de Wazuh-regel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-179` | 08-11-2026 22:57:14 | **CONFIG** | NAT FUXA01 | Port forward voor FUXA01 aanmaken, association None. LET OP: op 11-11 blijkt de bron hier foutief ([MALFORMED_SOURCE_ADDRESS]). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-245` | 11-11-2026 18:39:19 | **TROUBLESHOOT** | NAT FUXA01 | pfctl -sn (visueel bevestigd): rdr voor poort 1881 heeft bron '[MALFORMED_SOURCE_ADDRESS]' (eerste cijfer ontbreekt); de regels voor 8080 en 8443 hebben 'MGMT_CLIENT_IP'. Root cause van de mislukte FUXA-beheertests. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-246` | 11-11-2026 18:45:06 | **FIX** | NAT FUXA01 | Port Forward / Edit FUXA01 (aangemaakt 11/8/26 23:00:17): bron gecorrigeerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-247` | 11-11-2026 18:52:24 | **PASS** | Beheerpad FUXA01 | Host: PFSENSE_MGMT_IP:1881 = True en 8080 = True na de NAT-correctie. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-248` | 11-11-2026 18:52:34 | **PASS** | NAT | pfctl -sn na correctie (visueel bevestigd): alle drie rdr-regels (1881 -> FUXA01_OT_IP, 8080 -> PLC01_OT_IP, 8443 -> [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN]:443) met bron MGMT_CLIENT_IP. | Nog niet gepubliceerd (review vereist) |
