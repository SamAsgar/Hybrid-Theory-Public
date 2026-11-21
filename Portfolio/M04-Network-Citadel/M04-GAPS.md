# M04 | GAP-analyse en controles

**Bron:** voorlopige evidence-selectie 30 oktober–19 november 2026, gesaneerde publieke afgeleiden.  
**Status:** technische beeldanalyse; geen formele audit-PASS.

## M04 Network Citadel
1. **Topologiegrens:** oude VMnet8-/LAB-tests en latere LAN-segment-/OT-configuratie bewust gescheiden. Voor AC01/AC02/AC03 kunnen eerdere succesvolle tests bestaan, maar deze screenshots leveren niet automatisch regressie-PASS na de migratie.
2. **AC04 OT-interface:** er is een nulmeting zonder OT-firewallregels. Latere regellijsten en adapterinstellingen zijn zichtbaar, maar een volledige gevalideerde netwerkflow naar PLC/FUXA over het bedoelde pad is niet uit deze selectie alleen vast te stellen.
3. **AC07 allow/deny:** aparte matrix nodig per bron, bestemming, poort, resultaat, timestamp en pfSense-regel-/logcorrelatie. Screenshot van een rule is onvoldoende.
4. **NAT / host-beheerpad:** sommige schermen tonen onvolledige pfSense `Edit Redirect Entry`-velden of wijzigingen die nog kunnen wachten op Apply. Ook routekeuze via Wi-Fi in plaats van VMnet1 komt voor.
5. **Mislukte verbinding:** `Screenshot 2026-11-11 181110.png` toont expliciet `TcpTestSucceeded=False` voor `PLC01_OT_IP:1881`; dit bewaren als FAIL, niet wegpoetsen.
6. **Beperkt geslaagde verbinding:** `Screenshot 2026-11-11 185224.png` toont succes naar `PFSENSE_MGMT_IP` via VMnet1 op poorten `1881` en `8080`, maar is géén zelfstandig bewijs van PLC01 of end-to-end portforward naar het OT-segment.
7. **AC05 Wazuh:** installatie-/webinterfacebeelden tonen voorbereidende integratie, niet bewezen OT-agent-telemetrie of detectieregels.
8. **AC06 / AC08:** GNS3-schets is geen bewijs voor 75 VPCS en 3 subnetten, en er is in deze selectie geen bewijs voor een geslaagde Suricata IDS-acceptatietest.
9. **Snapshotintegriteit:** screenshots van VMware-menus zijn geen definitieve snapshotinventaris. Verifieer namen, datums, herstelbaarheid en vastgelegde rollbackstappen.

## Aanvullende observaties bij FUXA 15 november

De nieuwe screenshots M04-EV-206 t/m M04-EV-210 tonen een groene FUXA-connector, de interne verbindingsstatuswaarde `5` en booleaanse motortags met waarde `0`. Dit is **geen** zelfstandige verificatie van live Modbus-registeruitlezing. AC02-regressie na OT-migratie blijft **PENDING** totdat een gecontroleerde start/stop-overgang en PLC/FUXA-correlatie is bewezen.

Zie [`M04-Bewijsvoering/19_FUXA_followup/ADDENDUM-2026-11-15.md`](M04-Bewijsvoering/19_FUXA_followup/ADDENDUM-2026-11-15.md) voor bewijslimieten per screenshot.

## Aanvulling 19 november — gerichte deeltests

- [Fase 20](M04-Bewijsvoering/20_OT_segmentation_and_regression/README.md) toont onder meer LAB→PLC01 TCP/502 en LAB→FUXA01 TCP/1881 BLOCK-events en positieve/negatieve afgebakende regressietests.
- OpenPLC-autostart: eerste reboot FAIL; na correctie tweede reboot met functionele HMI START→STOP-keten **TESTED / scoped PASS** op basis van de sessierapportage. Onafhankelijke owner review blijft open.
- **Integrale AC04/AC07 PENDING**, inclusief alternatieve routes, IPv6, beheer/NAT, UDP en sluitende log-/capturecorrelatie.

## Publicatie-integriteit — 20 november 2026

Bij een pad- en bestandscontrole van de publieke evidence-set zijn **264 PNG-bestanden** aangetroffen tegenover **265 geregistreerde bewijsitems**. Het bewijsitem **M04-EV-113**, `Screenshot 2026-11-08 180632.png` (fase 10), staat in het register en SHA-256-manifest maar ontbreekt als publiek PNG-bestand. Dit was al vóór de mapreorganisatie het geval. De hash-/CSV-vermelding blijft als traceerbare registratie staan; de ontbrekende afbeelding telt niet als gepubliceerd bewijs. Aanvulling vereist afzonderlijke sanering en review; geen technische PASS afleiden uit deze registratie.

## C2-netwerkvalidatie — 20 november 2026

- **AC04/AC07 PENDING:** directe beheerproeven F13–F15, alternatieve paden, brede LAN IPv6-allow en veilige WAN-proef F24. Volledige log-/capturecorrelatie en eigenaaracceptatie staan open.
- **OT-afhankelijkheden:** DNS/NTP-ontwerp en geautoriseerde beheerroute wachten op een besluit. Endpointrol en authenticatie/TLS vragen verificatie.
- **Herstel en functionele regressie:** preflightcontrole, herstel-smoketest en onafhankelijke AC01–AC03-bewijsreview staan open.
- **EXT:** AC05 **PENDING** voor Wazuh OT-telemetrie. AC06 en AC08 **PLANNED**, met eigenaarbesluit over VPCS-aantal/scope en nog te bewijzen sensor- en alertketen.
- **Bestaande fase-20-beelden:** finale privacy- en leesbaarheidsreview staat open.

[C2-projectlog](../../projectlogboeken/2026-11-20-m04-core-c2-netwerkvalidatie.md).


## GAP-delta 21 november 2026 — beheerzone naar OT

De eigenaarsessie bevestigt binnen de getoonde scope drie door de firewall geblokkeerde directe verbindingen van een virtuele beheerbron naar de PLC: TCP/502, TCP/22 en TCP/44818. **TESTED / scoped PASS voor die beheerbron**; formele testbronacceptatie en volledig client-/firewall-/capturebewijs blijven open. Dit is geen algemene zone-isolatie-PASS.

Resterend: F13–F15-bronbesluit, capture-/rollbackbewijs, IPv6-regel en alternatieve paden, veilige WAN→OT-test F24, DNS/NTP-bronbeleid, herstel- en AC01–03-evidencereview. **AC04/AC07 integraal PENDING; M04-CORE IN PROGRESS.** Wazuh, GNS3 en Suricata blijven EXT. [Gesaneerd log 21 november](../../projectlogboeken/2026-11-21-m04-core-management-segmentatie.md).
