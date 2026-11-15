# M04 — Network Citadel | Publieke bewijsselectie

**Bronpeildatum:** 15 november 2026 · **Publicatiescope:** beperkte afgeleide van private Lab-4-evidence · **Reviewstatus:** DRAFT / PENDING OWNER REVIEW · **Technische status:** M04-CORE **IN PROGRESS**.

Deze map geeft een **publiek controleerbare, gesaneerde selectie** van de M04-onderzoekslijn. De canonieke, onbewerkte evidence staat uitsluitend in de private repository onder `bewijsvoering/Lab-4 | Network Citadel/`. Die private map bevat **210 originele PNG's in 19 fasen**. **Dit is geen één-op-één-kopie en geen volledige publieke evidence-import.** Alleen expliciet geselecteerde, gesaneerde weergaven worden gepubliceerd; de overige bronbeelden blijven privé.

## Visuele bewijsselectie

| Publiek bestand | Onderliggende private bron | Wat is zichtbaar? | Bewijsgrens |
|---|---|---|---|
| [Gesaneerde management-TCP-test](screenshots/M04-PUB-EV-202-gesaneerd.png) | `M04-EV-202`, 11 nov. | Vanaf VMnet1 twee `TcpTestSucceeded: True`-resultaten tegen `PFSENSE_MGMT_IP`, poorten 1881 en 8080. Bronadres is `MGMT_CLIENT_IP`. | **PASS-LIMITED:** bewijst alleen die twee TCP-verbindingen met het pfSense-managementadres. Geen zelfstandig bewijs voor de volledige NAT-/OT-keten. **Dit beeld is deels opnieuw gezet na onomkeerbare pixelredactie**. |
| [HMI/PLC-verbinding](visualisaties/M04-FUXA-PLC-verbinding-publiek.svg) | `M04-EV-206`, 15 nov. | FUXA-connector wijst naar `PLC01_OT_IP`, Modbus TCP/502, Slave ID 1; groene indicator | **Afgeleide reconstructie, geen screenshot**; groen bevestigt geen live register-readback |
| [Motortags in FUXA](visualisaties/M04-Motortags-publiek.svg) | `M04-EV-209` en `M04-EV-210`, 15 nov. | `Motor_Start` en `Motor_Running` tonen in twee opnamen beide `0` | **Afgeleide reconstructie, geen screenshot**; geen `0→1→0`-overgang of end-to-end write/readback bewezen |

De beelden tonen **gesaneerde publicatieweergaven**. De ongecensureerde originelen, onbewerkte screenshots en hun originele hashes zijn nadrukkelijk niet naar Public gekopieerd. De gepubliceerde PNG is een gemodificeerde transcriptweergave: vertrouwelijke identificatoren werden in de uiteindelijke pixels verwijderd en de betreffende regels zijn met officiële aliassen opnieuw gezet. Gebruik deze afgeleide niet als zelfstandig forensisch origineel.

## Wat M04 daadwerkelijk aantoont

- **Historische basis (vóór migratie):** PLC/OpenPLC, FUXA en Modbus werden in de tijdelijke NAT-topologie gebruikt. Eerdere succesvolle deeltests blijven tijd- en topologiegebonden; ze leveren **geen automatische AC02/AC03-regressie-PASS** op het nieuwe OT-segment.
- **OT-netwerk:** pfSense heeft een aparte OT-interface; PLC01 en FUXA01 bevinden zich na migratie op hetzelfde geïsoleerde VMware OT LAN Segment. De hostnamen en IP-/MAC-waarden zijn uitsluitend via officiële aliassen beschreven.
- **Intra-OT-communicatie:** FUXA01 bereikt PLC01 rechtstreeks binnen het OT-netwerk via Modbus TCP/502. Dit verkeer is **geen** test van de pfSense-zonegrens.
- **PLC/HMI:** OpenPLC-runtime werd na handmatig starten actief, de TCP 502-listener en HMI-verbinding zijn in de private uitvoeringssessie gericht getest; de HMI toont twee tags met nulwaarden.
- **Management:** de gesaneerde TCP-resultaten bevestigen beperkte bereikbaarheid naar het pfSense-managementadres op twee poorten. Ze bewijzen niet zelfstandig dat de hele beheerkoppeling tot aan de PLC/HMI correct is afgeschermd.
- **Segmentatie:** enkele gerichte positieve en negatieve tests zijn vastgelegd; de **integrale AC04- en AC07-acceptatiematrix is PENDING**.

## Acceptatie per criterium

| Controle | Publieke evidence-uitspraak | Status |
|---|---|---|
| AC01 — PLC-motorsimulatie | Runtime en programma gerapporteerd als actief in de latere sessie; volledige reproduceerbare regressiereeks ontbreekt | **PENDING finale evidence** |
| AC02 — Modbus-read | Verbinding en zichtbare tags; nog geen bevestigde live registertransitie | **PENDING** |
| AC03 — Modbus-write | Historische deeltetst / functionele werking door Project Owner gemeld; `0→1→0`-readback ontbreekt | **PENDING** |
| AC04 — IT/OT-segmentatie | OT-zone technisch ingericht, maar egress/zonegrenzen nog niet integraal getest | **PENDING** |
| AC05 — OT-detectie via Wazuh | Geen geverifieerde agenttelemetrie of alertdetectie | **PENDING** |
| AC06 — 75 VPCS / drie subnetten | Ontwerp/voorbereiding, geen volledige uitvoering | **PLANNED** |
| AC07 — allow/deny | Deelscope getest; volledige testmatrix, bron-/doel-/poort-/logcorrelatie ontbreekt | **PENDING** |
| AC08 — Suricata | Geen aangetoonde voltooide IDS-test | **PLANNED** |

## Navigatie en verificatie

- [Publiek bewijsregister, herkomst en uitsluitingen](EVIDENCE-REGISTER-PUBLIC.md)
- [Sanitization en releasecontrole](PUBLICATIECONTROLE.md)
- [Publieke OT-validatie van 15 november](../../projectlogboeken/2026-11-15-m04-ot-modbus-applicatievalidatie.md)
- [Publieke architectuur met officiële aliassen](../../architectuur/README.md)

**Geen live managementadres, MAC-/IPv6-adres, cookie, credential, intern pad of volledige pfSense-regelset gepubliceerd.** Een gesaneerde afbeelding behoudt haar bewijsgrens. **Geen M04-PASS** en **geen publicatie-PASS zonder afzonderlijke eigenaarreview**.
