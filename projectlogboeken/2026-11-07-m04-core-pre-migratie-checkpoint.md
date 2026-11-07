# M04 Network Citadel | pre-migratiecheckpoint — 7 november 2026

**Repository:** Hybrid-Theory-Public (gesaneerde voortgangsweergave)  
**Missie:** M04 Network Citadel / Lab 04  
**Werkfase:** CORE — herstelpad en preflight vóór netwerksegmentatie  
**Missiestatus:** IN PROGRESS; **segmentatie en securityacceptatie PENDING**  
**Eerdere resultaten:** [M04 functionele OT-baseline van 6 november](2026-11-06-m04-network-citadel-ot-baseline.md)

## Nieuwe voortgang sinds 6 november

De Project Owner heeft gemeld dat **drie VMware-pre-migratiesnapshots** zijn aangemaakt voor de virtuele PLC, de HMI en de firewall. Dit is een **voorbereidende herstelmaatregel**, geen geteste restore. Onafhankelijke controle van snapshotintegriteit, beheerbereikbaarheid en daadwerkelijke terugzetbaarheid staat nog open.

Op 7 november is **geen nieuwe OT-netwerkmigratie of isolatietest als uitgevoerd vastgelegd**. De huidige stand blijft daarom een voorbereidingscheckpoint.

## Geharmoniseerde acceptatiestructuur

| Blok | Resultaat |
| --- | --- |
| **Functionele baseline (AC01–AC03)** | OpenPLC-motorlogica, dynamische PLC→HMI-uitlezing en HMI→PLC-start/stop: **PASS binnen beperkte functionele testscope op 6 november** |
| **M04-CORE (AC04 + AC07)** | Afgedwongen OT-segmentatie, toegestane en verboden netwerkstromen, firewall-logging en packetcaptures: **PENDING** |
| **M04-EXT** | Wazuh-agentdetectie, Suricata-integratie en risicogerichte GNS3-uitbreiding: **PENDING / PLANNED** |

De HMI en PLC stonden in de laatst gedocumenteerde baseline op hetzelfde tijdelijke virtuele NAT-netwerk. De beoogde OT-trust boundary is nog niet aangetoond. Functionerende applicatiecommunicatie betekent niet dat toegangsbeperkingen daadwerkelijk worden afgedwongen.

## Volgende gecontroleerde stap

1. Snapshot- en rollbackpad controleren; actuele netwerkadapters, routes, beheerbereikbaarheid en firewallconfiguratie vastleggen.
2. Het bestaande goedgekeurde zoneontwerp en de allow/deny-testmatrix tegen de werkelijk gemeten configuratie controleren.
3. Pas na preflight de OT-zone gecontroleerd migreren, vervolgens functionele regressietests en positieve én negatieve firewall-/netwerktests uitvoeren.
4. Resultaten onderbouwen met passende pfSense-logs en Wireshark-captures. Eventuele latere publieke afbeeldingen worden afzonderlijk gesaneerd.

**Bewijsgrens:** geen private IP-adressen, host-/gebruikersidentificatoren, credentials, ruwe screenshots of ongesaneerde bewijsbundels in deze publieke update. Geen claim van onafhankelijke audit, geslaagde restore of afgeronde M04-missie.

**Redactie:** samenvatting van eerder vastgelegde tests, eigenaarbevestiging en een documentatiecheckpoint; geen nieuwe technische PASS.