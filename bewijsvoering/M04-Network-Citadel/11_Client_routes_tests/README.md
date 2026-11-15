# 11 Client routes tests

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 7 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-146` | 08-11-2026 14:59:18 | **TROUBLESHOOT** | AC04 beheerpad | Host: VMnet1 = MGMT_CLIENT_IP; Find-NetRoute PFSENSE_OT_IP kiest Wi-Fi via [UNMAPPED_IPV4] - de host bereikt OT niet rechtstreeks via pfSense. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-147` | 08-11-2026 16:40:08 | **CONFIG** | NAT | Port Forward-lijst: alleen HT-WAZUH-DASHBOARD-ACCESS (LAN 8443 -> [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN]:443, bron MGMT_CLIENT_IP). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-150` | 08-11-2026 17:50:15 | **CONFIG** | AC04 beheerpad | Host: adapterdetails VMware Network Adapter VMnet1 (MAC zichtbaar). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-170` | 08-11-2026 21:59:21 | **TEST** | AC07 (beperkt) | Host: Test-NetConnection PFSENSE_MGMT_IP:22 = False (ping True). Doel is pfSense zelf; geen bewijs van OT-isolatie. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-218` | 09-11-2026 18:48:17 | **TROUBLESHOOT** | Beheerpad | Host ipconfig: Wi-Fi-gateway [UNMAPPED_IPV4] (context voor verkeerde bronkeuze). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-240` | 11-11-2026 18:11:10 | **TROUBLESHOOT** | Beheerpad | Host -> PLC01_OT_IP:1881 via Wi-Fi [UNMAPPED_IPV4]: False. Verkeerde bron én verkeerde poort; ongeldig als test. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-242` | 11-11-2026 18:17:41 | **FAIL** | Beheerpad | Host: PFSENSE_MGMT_IP:8080 False en 1881 failed (volgens log stonden VM's uit; ongeldig als firewallbewijs). | Nog niet gepubliceerd (review vereist) |
