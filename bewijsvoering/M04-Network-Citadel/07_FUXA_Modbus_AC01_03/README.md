# 07 FUXA Modbus AC01 03

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 20 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

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
