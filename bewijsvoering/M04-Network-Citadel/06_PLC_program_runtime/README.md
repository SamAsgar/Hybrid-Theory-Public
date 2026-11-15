# 06 PLC program runtime

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 25 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
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
