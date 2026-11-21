# M04 Network Citadel | CORE — Managementsegmentatie 21 november 2026

**M04-CORE IN PROGRESS · AC04/AC07 PENDING.** Dit is een gesaneerde voortgangsdelta, geen onafhankelijke audit of finale acceptatie.

## Geobserveerde testdelta
Een afzonderlijke Ubuntu-beheer-VM in de managementzone bereikte de pfSense-beheerinterface. Gerichte TCP-probes naar de PLC in het afgeschermde OT-segment werden volgens de latere sessierapportage op TCP/502, TCP/22 en TCP/44818 door de bedoelde LAN→OT-firewallregel geblokkeerd.

**Resultaat:** `TESTED / scoped PASS` voor **alle drie de getoonde poorten vanaf deze specifieke beheer-VM**, op basis van de aangeleverde sessiewaarneming. Voor TCP/22 en TCP/44818 zijn tevens bronroute en client-timeout gerapporteerd. Volledige primaire tijd-, logregel- en packetcapturecorrelatie en onafhankelijke bewijsreview staan nog open.

De oorspronkelijke F13–F15-testmatrix vermeldt een andere beheerbron. **F13–F15 blijven formeel PENDING** tot goedkeuring van de afwijkende testbron en afronding van primaire evidence-review. Voor TCP/22 en TCP/44818 eindigde de gefilterde OT-capture op nul. TCP/502 is op LAN met het bloklog onderbouwd. De tijdelijke LAN-hostroute is aantoonbaar verwijderd.

## Architectuurgrenzen
- Fysieke virtualisatiehost krijgt geen permanente directe route naar OT.
- Bestaande, beperkte managementportforwards blijven voorlopig behouden.
- De beheer-VM blijft buiten OT; geen ongecontroleerde forwarding.
- PLC en HMI blijven binnen één geïsoleerd OT-segment en communiceren daar via Modbus TCP.
- De industriële DMZ en verdere beheerinrichting zijn uitgesteld tot na CORE.

## WAN-eindmeting

**F24 · scoped PASS voor TCP/502 en TCP/8080.** pfSense ontving zes SYN-pakketten op de gesimuleerde WAN-grens, drie per doelpoort. De IPv4-default-deny blokkeerde ze alle zes. De gelijktijdige, op bron, doel en beide poorten gefilterde OT-capture bevat nul pakketten. De beheer-VM gebruikte tijdelijk de WAN-simulator. De WAN-hostroute is verwijderd en het Host-only-beheer is hersteld.

## Nog open

**M04-CORE IN PROGRESS · Milestone 01 open · AC04/AC07 integraal PENDING.**

1. Leg de VMware-eindstand vast (NAT uit, LAN Segment en Host-only aan). De beelden vóór F24 tonen de uitgangsstand. De afgeronde F24-proef hoeft niet opnieuw.
2. Accepteer de beheer-VM als formele bron voor F13–F15 of plan een gecontroleerde hertest vanaf de voorgeschreven fysieke host. Beoordeel de tijddekking per poort en bevestig het SSH-beheerbeleid voor F14.
3. Bepaal de OT-resolver en tijdbron en toets F20/F21 aan dat beleid. Beoordeel de brede LAN IPv6-allow en alternatieve paden voor F22/F23. Verifieer de LAB-bron en de doelrol van de beheerforward waar de conclusie daarvan afhangt.
4. Verifieer de pfSense-configback-up, het PLC-checkpoint van ná de autostartfix en herstel in isolatie. OpenPLC-autostart en de START→STOP-keten hebben sinds 19 november een scoped PASS. Rond de AC01–AC03-bewijsreview af en herhaal alleen ontbrekende onderdelen.
5. Registreer per resterende flow de uitkomst of gemotiveerde uitzondering en laat de eigenaar AC04/AC07 aftekenen. Daarna volgen Wazuh-events (AC05), de vast te stellen GNS3-scope en test (AC06) en Suricata → Wazuh (AC08).

[Vorige C2-delta](2026-11-20-m04-core-c2-netwerkvalidatie.md) · [M04 issue](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/45).

**Publicatiegrens:** geen werkelijke private IP-/MAC-adressen, hostidentificatoren of ruwe firewallregels.