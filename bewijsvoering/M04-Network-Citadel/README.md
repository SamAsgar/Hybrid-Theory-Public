# M04 Network Citadel | Publieke bewijsbibliotheek

**Project:** Hybrid-Theory  
**M04-CORE:** IN PROGRESS  
**Publieke evidence:** documentair overzicht; de 269 ruwe binaries zijn **niet** gepubliceerd.  
**Historische bewijsperiode:** 31 oktober t/m 15 november 2026.

## Navigatie

- [Volledige chronologische evidence-index (270 records)](M04-EVIDENCE-INDEX.md)
- [Downloadbaar evidence-register (CSV)](M04-EVIDENCE.csv)
- [GAP-analyse en testbeperkingen](M04-GAPS.md)
- [Status van elke afbeelding](M04-PUBLICATIESTATUS.md)
- [Crosswalk: 122 exact SHA-geverifieerde historische evidence-ID-koppelingen](M04-EVIDENCE-CROSSWALK.md)
- [3 aanvullende gesaneerde historische beelden (30 oktober)](M04-LEGACY-BEELDEN.md) (eigenaarsreview in Draft PR).
- 19 genummerde submappen voor thematische navigatie, ook voor FAIL, ERROR en troubleshooting.

## Architectuur (schematisch, niet als technische bewijsopname)

```text
Beheerclient [MGMT_CLIENT_IP]
        | historische beheerportforwards (TCP 8080 / 1881)
        v
pfSense [PFSENSE_MGMT_IP]
        | beleid LAB -> OT (gedeeltelijk getest)
        +------ OT-zone -----------+
        | PLC01 [PLC01_OT_IP]      |
        | FUXA01 [FUXA01_OT_IP]    |
        +--------------------------+
      FUXA01 -- Modbus TCP/502 --> PLC01
        (zelfde OT-segment; niet via pfSense)
```

## Stand van acceptatie

| AC | Onderbouwde status |
|---|---|
| AC01 | Historische UIT/AAN/UIT-motorlogica in NAT-topologie; OT-regressie onvolledig |
| AC02 | Historische FUXA-tagreeks 0→1→0 in NAT-topologie; volledige OT-readback PENDING |
| AC03 | Functionele HMI-start/stop historisch onderbouwd via video-analyse, géén packet-level Modbus-writebewijs; MP4 ontbreekt hier |
| AC04 | Segmentatieconfiguratie zichtbaar; integrale acceptatie PENDING |
| AC05 | Wazuh-agentbewijs PENDING |
| AC06 | GNS3 3×25 VPCS PLANNED |
| AC07 | Beperkte deny- en allowtests bewezen; volledige matrix PENDING |
| AC08 | Suricata PLANNED |

**Bewijsgrens:** TCP/502-connectiviteit bewijst niet een functionele Modbus-transactie. Een groene FUXA-connector bewijst geen AC02-PASS. Positieve beheerpoorttests bewijzen geen end-to-end netwerkisolatie. Historische FAIL's blijven in het register staan. De aangeleverde ZIP eindigt met een historisch oud NAT-doel in de FUXA-configuratie; privé geregistreerde latere correcties worden daarmee niet ontkend.

## Veiligheid en herleidbaarheid

Deze publicatie bevat géén ongesaneerde screenshots of oorspronkelijke bronhashes, MAC-adressen, niet-openbare netwerkadressen, sessietokens of het volledige private SSOT-register. Het oorspronkelijke manifest en de originele bestanden blijven in Private. De ingebrachte ID-reeks `M04-ZIP` is afzonderlijk van de eerdere private `M04-EV`-reeks. Officiële aliasnamen volgen de private `architectuur/OFFICIELE ALIASCONVENTIE.md`; echte adressen worden nooit in Public uitgelegd. Een afbeelding mag pas worden toegevoegd na onomkeerbare pixelsanering, metadata-verwijdering, visuele nacontrole en nieuwe publieke SHA-256-berekening.

**Dit is een afgeleide evidence-catalogus, geen nieuwe Single Source of Truth en geen claim van afgeronde M04-CORE.**
