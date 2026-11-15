# 18 Forward and regression

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 8 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-243` | 11-11-2026 18:25:14 | **PASS** | Beheerpad PLC01 | Host: PFSENSE_MGMT_IP:8080 = True (bron MGMT_CLIENT_IP). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-244` | 11-11-2026 18:34:11 | **FAIL** | Beheerpad FUXA01 | Host: PFSENSE_MGMT_IP:1881 = False terwijl 8080 True is. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-261` | 15-11-2026 17:26:19 | **FAIL** | AC01-AC03 regressie | FUXA01 -> PLC01_OT_IP:502: 'Connection refused' - MODBUS TCP FAIL (runtime draait niet). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-262` | 15-11-2026 17:33:28 | **TROUBLESHOOT** | AC01-AC03 regressie | plc01: niets op :502, wel python3 op :8080; geen failed units. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-265` | 15-11-2026 18:57:00 | **TEST** | AC01 regressie | OpenPLC-dashboard via beheerpad: programma M04 Motor Simulation v1.0, 'Status: Stopped'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-266` | 15-11-2026 18:57:59 | **FIX** | AC01 regressie | Start PLC: runtime-log 'start_modbus() ... port 502', EtherNet/IP 44818 gestart. Titelregel in OCR toont nog 'Stopped'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-267` | 15-11-2026 19:06:19 | **TEST** | Modbus OT | plc01: ss toont openplc LISTEN op [WILDCARD_BIND]:502. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-268` | 15-11-2026 19:10:08 | **PASS** | Modbus TCP (OT-topologie) | FUXA01: eerst 'Connection refused', daarna 'MODBUS TCP PASS' naar PLC01_OT_IP:502. Poortbereik, geen Modbus-transactie. | Nog niet gepubliceerd (review vereist) |
