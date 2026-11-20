# M04 — Network Citadel | Gesaneerde bewijsvoering

**Project:** Hybrid-Theory (publieke repository)  
**Missie:** M04 Network Citadel  
**Periode van de evidence:** 30 oktober t/m 19 november 2026  
**Status:** uitvoering en verificatie deels open (`M04-CORE = IN PROGRESS`)  
**Evidence:** **264 aanwezige gesaneerde PNG-afgeleiden** in fasen 01–20; 265 geregistreerd, één ontbreekt. Fase 21 voegt **52 gesaneerde weergaven** toe.  
**Classificatie:** PUBLIC · gesaneerde afgeleiden · de originelen blijven uitsluitend privé

> Dit is een gecontroleerde, gesaneerde migratie van de private M04-bewijsset. Elk beeld is onomkeerbaar pixelgemaskeerd: IP-, MAC- en IPv6-adressen, hostnames, gebruikersnamen, lokale paden, sessiecookies, VM- en segmentnamen en apparaat-ID's zijn verwijderd. Waar een officiële alias bestaat, staat die in de maskering, zoals `PFSENSE_MGMT_IP` of `PLC01_OT_IP`. Overige waarden zijn als `REDACTED_*` gemarkeerd. Zie het [saneringsrapport](M04-SANITIZATION-REPORT.md).

## 1. Doel

De netwerkarchitectuur en IT/OT-segmentatie van Hybrid-Theory documenteren en verifiëren. Dat omvat VMware VMnet, pfSense, OpenPLC/PLC01, FUXA, Modbus TCP, het beheerpad vanaf de host, firewallregels, NAT/port-forwarding, diagnostiek, logging en regressietests.

**Fasen 01–20:** [M04-Bewijsvoering](M04-Bewijsvoering/README.md).

## 2. Navigatie

- [Alle 210 screenshots met beschrijving en bewijsgrens](M04-EVIDENCE-INDEX.md)
- [Galerij: 19 fasen, elk met beelden en toelichting](M04-GALERIJ.md)
- [GAP-analyse en openstaande verificaties](M04-GAPS.md)
- [Saneringsrapport en publicatieverantwoording](M04-SANITIZATION-REPORT.md)
- [SHA-256-manifest van de gepubliceerde afgeleiden](M04-SHA256SUMS.txt)
- [Evidence-register (CSV)](M04-EVIDENCE.csv)
- [15 november: FUXA-vervolgonderzoek](M04-Bewijsvoering/19_FUXA_followup/ADDENDUM-2026-11-15.md)
- [19 november: OT-segmentatie, pfSense en PLC/HMI-regressie](M04-Bewijsvoering/20_OT_segmentation_and_regression/README.md) · [aanvullend saneringsrapport](M04-Bewijsvoering/20_OT_segmentation_and_regression/M04-PHASE20-SANITIZATION-REPORT.md)

## 3. Technische keten

1. **Baseline:** oorspronkelijke LAB/VMnet8-tests, interface-overzichten en voorlopige verbindingen.
2. **Inrichting:** VMware-adapters, PLC01/OpenPLC, FUXA/Modbus, de OT-interface op pfSense en firewallregels.
3. **Migratie:** snapshots, aanpassing van het OT-netwerk, routes en NAT/port-forwarding.
4. **Verificatie:** werkende en niet-werkende netwerkpaden, pfSense-logs, PowerShell-connectiviteitstests en FUXA-tags.

**Belangrijk:** een screenshot van een configuratie bewijst niet dat verkeer werkelijk werd toegestaan of geblokkeerd. Een historische PASS op VMnet8 bewijst geen werkende situatie na de OT-migratie.

## 4. Resultaten en bewijsgrenzen

| Onderdeel | Wat deze collectie toont | Acceptatiestatus |
|---|---|---|
| AC01–AC03 (historische testketen) | PLC-runtime en FUXA/Modbus-configuratie of testuitvoer op de oorspronkelijke topologie | Historische resultaten zijn niet automatisch representatief na de migratie |
| AC04 (OT-segmentatie) | OT-interface op pfSense, regels en VMnet-/routingwerk | Volledige end-to-end OT-isolatie **PENDING** |
| AC07 (allow/deny) | Regels, logvensters en diagnostiek | Volledige testmatrix (bron, bestemming, poort) **PENDING** |
| NAT/beheerpad | NAT en port-forwarding, routes, geslaagde en mislukte tests | Alleen de zichtbaar geteste afzonderlijke paden zijn onderbouwd |
| AC05/06/08 | Voorbereidende context rond Wazuh, GNS3 en Suricata | **Geen complete acceptatie-PASS aangetoond** |
| FUXA 15 november | Groene PLC01-MOTOR-indicator, statuswaarde `5`, tags `Motor_Start` en `Motor_Running` tonen `0` | Live Modbus-readback en AC02-regressie **PENDING** |

## 5. Concrete troubleshootingvoorbeelden

- `Screenshot 2026-11-11 181110.png`: `TcpTestSucceeded=False` voor `PLC01_OT_IP:1881`. Dit blijft een mislukte bereikbaarheidstest, geen PASS.
- `Screenshot 2026-11-11 185224.png`: geslaagde verbinding naar `PFSENSE_MGMT_IP` via VMnet1 op poorten `1881` en `8080`. Deze test alleen bewijst geen PLC01-route en geen OT-port-forward.
- `M04-EV-206` t/m `M04-EV-210`: de FUXA-connector toont configuratie, statuscode en motortags, maar nog geen reproduceerbare `0→1→0`-overgang van PLC-waarden.

## 6. Integriteit en herkomst

- De gepubliceerde PNG's zijn **afgeleiden**, geen originelen. Ze zijn uitsluitend gemaakt door pixels te maskeren en opnieuw op te slaan als RGB-PNG zonder metadata (geen EXIF- of tekst-chunks).
- De SHA-256-waarden in de index, de fase-README's, de CSV en het [manifest](M04-SHA256SUMS.txt) horen bij deze **publieke afgeleiden**. Hashes van de private originelen worden bewust niet gepubliceerd.
- De oorspronkelijke bestandsnamen (datum en tijd van de opname) en de indeling in 20 fasen zijn behouden. Daardoor blijft de chronologische samenhang met de private bron traceerbaar zonder die bron bloot te geven.
- Maskeringen bevatten alleen aliassen of `REDACTED_*`-labels. De koppeling tussen echte waarden en aliassen blijft privé, zoals het [publicatiebeleid](../../governance/PUBLICATIEBELEID.md) voorschrijft.

## 7. Evidence-aanvulling 19 november 2026

De [nieuwe fase-20-galerij](M04-Bewijsvoering/20_OT_segmentation_and_regression/README.md) bevat 55 met SSOT-aliassen gesaneerde beelden van PLC/HMI-regressie, firewalllogs en gerichte LAB→OT-, OT→LAB- en egress-tests. Dit zijn afgebakende deelresultaten: integrale AC04/AC07 blijft **PENDING** en handmatige privacy-/bewijsreview is nog vereist.

De [fase-21-reeks](M04-Bewijsvoering/21_CORE_C2_firewall_and_isolation/README.md) bevat de chronologisch geordende CORE C2-opnamen van 20 november 2026, met een eigen manifest en saneringsrapport.
