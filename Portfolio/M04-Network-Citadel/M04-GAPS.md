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
