# M04 Network Citadel | OpenPLC-autostart en OT-regressie — 19 november 2026

**M04-CORE** blijft **IN PROGRESS**. In de gemelde labtest slaagde de functionele AC01–AC03-regressie na de tweede gecontroleerde PLC-herstart.

## Reboot en herstel

| Stap | Resultaat |
|---|---|
| Eerste reboot | De OpenPLC-service was actief, maar de motorsimulatie bleef gestopt. Autostart **TESTED / FAIL**. |
| Correctie | De instelling voor automatisch starten in RUN-modus is ingeschakeld en opgeslagen. |
| Tweede reboot | De webinterface kwam automatisch beschikbaar, de motorsimulatie startte automatisch en Modbus TCP was operationeel. De start-, motor- en alarmstatus stonden bij aanvang uit. **AC01 TESTED / PASS** binnen deze scope. |
| Functionele regressie | De HMI herstelde zelfstandig de verbinding. Tijdens de gecontroleerde START→STOP-cyclus bevestigde teruglezing op de PLC dat de motorstatus eerst aan en daarna weer uit stond. **AC02–AC03 TESTED / PASS** binnen deze cyclus. |

Vooraf werd een rollbackcheckpoint vastgelegd. De herstelproef blijft **PENDING**.

## Resterende acceptatie

- **AC04 / AC07** blijven integraal **PENDING**. De gerichte netwerkdeeltests staan in [M04-log 09](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/30#issuecomment-7021079237). Nog open zijn de volledige allow/deny-matrix, log- en pakketcorrelatie en de beoordeling van beheeruitzonderingen en alternatieve netwerkpaden.
- **Formele acceptatie** blijft **PENDING**. De beschrijving is gebaseerd op de aangeleverde labresultaten. Koppeling van primair testbewijs, onafhankelijke beoordeling en expliciete eigenaaracceptatie staan nog open.
- **M04-EXT** behoudt AC05 Wazuh **PENDING** en AC06 GNS3 en AC08 Suricata **PLANNED**.

Zie de [GAP-analyse van het eerdere bewijsmateriaal](../Labs/M04-Network-Citadel/M04-GAPS.md).
