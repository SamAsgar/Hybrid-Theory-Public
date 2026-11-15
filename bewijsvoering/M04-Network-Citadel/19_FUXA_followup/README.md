# 19 FUXA followup

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 10 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-251` | 15-11-2026 16:55:12 | **TEST** | FUXA01 persistentie | FUXA01 nieuwe consolelogin 15 nov: docker fuxa 'Up About a minute' (start na boot). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-252` | 15-11-2026 16:58:54 | **PASS** | Beheerpad FUXA01 | Host: PFSENSE_MGMT_IP:1881 = True (bron VMnet1). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-253` | 15-11-2026 17:00:04 | **PASS** | FUXA web via beheerpad | Host: curl -I via port forward geeft HTTP-headers (text/html, 66382 bytes, 15 nov 15:59 GMT). Statusregel zelf staat boven het zichtbare deel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-254` | 15-11-2026 17:08:58 | **FAIL** | AC01-AC03 regressie | FUXA01 -> PLC01_OT_IP:502: 'No route to host' - MODBUS TCP FAIL. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-255` | 15-11-2026 17:13:27 | **TROUBLESHOOT** | AC01-AC03 regressie | FUXA01: route via ens36, ip neigh PLC01_OT_IP = FAILED (geen L2-bereik). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-256` | 15-11-2026 17:15:09 | **TEST** | AC01-AC03 regressie | plc01: adres PLC01_OT_IP en route aanwezig, neighbour-tabel leeg. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-263` | 15-11-2026 17:59:54 | **TEST** | Beheerpad | Browser: PFSENSE_MGMT_IP:8080/login en FUXA op PFSENSE_MGMT_IP:1881 met Motor_Control. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-264` | 15-11-2026 18:15:51 | **TROUBLESHOOT** | AC01-AC03 regressie | plc01: ping naar FUXA 3/3; controle op failed units en OpenPLC-map. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-269` | 15-11-2026 19:32:31 | **PENDING** | AC02/AC03 regressie | FUXA device PLC01-MOTOR staat nog op PLC01_TEMP_NAT_IP:502 (oud NAT-adres). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-270` | 15-11-2026 19:34:16 | **PENDING** | AC02/AC03 regressie | FUXA Connection property: Slave IP and Port nog PLC01_TEMP_NAT_IP:502. Laatste beeld in de ZIP; herconfiguratie en tagtest niet aangetoond. | Nog niet gepubliceerd (review vereist) |
