# M04 | Publiek evidence-register en brongrenzen

**Periode private bron:** 30 oktober t/m 15 november 2026 · **Private collectie:** 210 PNG's / 19 fasen · **Public release:** gecureerde selectie, **geen volledige export**.

## Bronnenindex (private fasen op hoofdlijn)

| Fase | Onderwerp | Private bronbeelden | Publieke behandeling |
|---|---|---:|---|
| 01 | Baseline vóór migratie | 23 | Historisch beschreven; geen ruwe beelden |
| 02 | VMware-netwerkconfiguratie | 3 | Alleen zoneconcepten, geen werkelijke adapteridentificatoren |
| 03 | FUXA/OpenPLC-baseline | 13 | Gedateerde historische scope, geen nieuwe PASS |
| 04 | Architectuur en ontwerp | 4 | Gebruik afzonderlijk gereviewde publieke architectuur |
| 05 | PLC01-provisioning | 11 | Componentstatus op hoofdlijn, geen inlog- of installatiedetails |
| 06 | PLC-programma/runtime | 13 | Alleen gerapporteerde runtime- en teststatus |
| 07 | FUXA/Modbus, AC01–AC03 | 25 | Historische tests onderscheiden van nieuwe OT-regressie |
| 08 | Migratievoorbereiding | 6 | Geen private snapshots of herstelidentificatoren |
| 09 | pfSense OT-interface en regels | 11 | Implementatieconcept, geen complete regels |
| 10 | Migratiesnapshots | 4 | Geen oorspronkelijke snapshots of metadata |
| 11 | Clientroutes en tests | 8 | Alleen testconclusies met scope |
| 12 | LAB/OT-firewall | 5 | Geen volledige filterinventaris |
| 13 | LAN-portforwarding | 10 | Geen werkelijke NAT-mappings |
| 14 | pfSense-logs en diagnose | 9 | Geen ruwe logs of bron-/doelidentificatoren |
| 15 | VMnet-adapters | 11 | Geen MAC's, echte IP's of hostpaden |
| 16 | OT/AC04/AC07 | 12 | Geen integrale PASS; gericht testresultaat mogelijk |
| 17 | Netwerkdiagnostiek | 8 | Geen ruwe shell-/routergegevens |
| 18 | Portforward en regressietests | 27 | Eén gesaneerde, beperkte management-TCP-test |
| 19 | FUXA-vervolgcontrole 15 nov. | 7 | Twee afgeleide diagramweergaven van connector en tags |
| **Totaal** | | **210** | **1 gewijzigde PNG + 2 illustraties** |

## Publiceerde subset en onzekerheden

| Referentie | Type | Publiek bewijs/resultaat | Wat dit nadrukkelijk NIET bewijst |
|---|---|---|---|
| `M04-EV-161` | Private TEST, niet rechtstreeks gepubliceerd | Managementpoorttest met HTTP-redirect; originele opname bevat een sessiecookie en is daarom uitgesloten | Geen volledige OT-isolatie, geen publicatie van ruwe HTTP-headers |
| `M04-EV-196` | Private FAIL, alleen tekst | Een directe poorttest vanuit een verkeerd netwerkpad mislukte | Geen generieke firewall-deny-PASS |
| `M04-EV-202` | **Gesaneerde PNG** | TCP naar `PFSENSE_MGMT_IP` op de twee geteste managementpoorten was bereikbaar vanaf `MGMT_CLIENT_IP` | Geen bewijs dat OT-doel of hele portforward-route functioneert |
| `M04-EV-206` | Afgeleide SVG | FUXA-connector met groene status naar `PLC01_OT_IP`, TCP/502 | Geen bewezen live PLC-registerniveau |
| `M04-EV-207` | Private TEST, alleen tekst | FUXA-interne connection-statuscode weergegeven | Zonder vendorsemantiek geen interpretatie van numerieke code |
| `M04-EV-209/210` | Afgeleide SVG | `Motor_Start` en `Motor_Running` beide `0` op twee tijdstippen | Geen start/stop, actieve polling of end-to-end command/readback-PASS |

De overige private screenshots zijn **niet** gepubliceerd, omdat zij gevoelige identificatoren, configuratiedetails, logging, lokale paden, sessieinformatie of niet-verifieerbare context kunnen bevatten. Ook een screenshot zonder expliciet adres kan door correlatie te veel blootgeven.

**Herleidbaarheid:** de canonieke private evidence-index, SHA-256-manifesten en bronscreenshots blijven intact onder `bewijsvoering/Lab-4 | Network Citadel/` in Private. Public bevat geen private alias-waardevertaling of kopie van dat manifest. Het bron-ID dient voor de Project Owner als verwijzing naar de private audittrail, niet als openbaar toegankelijke originallink.
