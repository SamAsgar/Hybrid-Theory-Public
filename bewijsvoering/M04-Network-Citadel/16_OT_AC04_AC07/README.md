# 16 OT AC04 AC07

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 11 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-196` | 08-11-2026 23:57:21 | **TEST** | PLC01 netwerk | plc01: ip neigh PFSENSE_OT_IP lladdr PFSENSE_OT_MAC STALE - L2-bereik naar de OT-gateway. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-202` | 09-11-2026 00:14:58 | **PASS** | Beheerpad PLC01 | Host: Test-NetConnection PFSENSE_MGMT_IP:8080 = True, bron VMnet1 MGMT_CLIENT_IP. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-203` | 09-11-2026 00:16:37 | **PASS** | Beheerpad PLC01 | Host: HTTP-antwoord met 'Location: /login' via de port forward. LET OP: Set-Cookie sessiewaarde zichtbaar. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-204` | 09-11-2026 00:17:14 | **PASS** | Beheerpad PLC01 | Host: curl [REDACTED_URL] -> 'HTTP status: 302'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-205` | 09-11-2026 00:23:17 | **PASS** | PLC01 persistentie | plc01 na nieuwe consolelogin: ens33 PLC01_OT_IP en default route aanwezig. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-206` | 09-11-2026 00:24:10 | **PASS** | PLC01 persistentie | Gecombineerd: plc01-adres/route en TcpTestSucceeded True in één beeld. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-215` | 09-11-2026 18:34:29 | **PASS** | FUXA01 lokaal | FUXA01: lokale HTTP-headers (Content-Length 66382) en ip neigh PFSENSE_OT_IP REACHABLE. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-216` | 09-11-2026 18:41:57 | **CONFIG** | AC07 pfSense->FUXA | GIF (38 frames): Diagnostics / Test Port, bronadres 'OT' wordt geselecteerd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-217` | 09-11-2026 18:44:09 | **PASS** | AC07 pfSense->FUXA | Diagnostics / Test Port: 'Port test to host: FUXA01_OT_IP Port: 1881 successful'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-259` | 15-11-2026 17:20:49 | **PASS** | Intra-OT bereik | plc01 -> FUXA01_OT_IP: ping 3/3. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-260` | 15-11-2026 17:23:54 | **PASS** | Intra-OT bereik | FUXA01 -> PLC01_OT_IP: ping 3/3; neigh REACHABLE (PLC01_OT_MAC). | Nog niet gepubliceerd (review vereist) |
