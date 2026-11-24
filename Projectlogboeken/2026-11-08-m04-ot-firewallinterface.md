# M04 Network Citadel | OT-interface op de firewall — 7–8 november 2026

**Repository:** Hybrid-Theory-Public (gesaneerde voortgangsweergave)  
**Missie:** M04 Network Citadel / Lab 04  
**Werkfase:** CORE — OT-zone aan firewallzijde inrichten  
**Missiestatus:** IN PROGRESS; **segmentatie en securityacceptatie PENDING**  
**Eerdere stappen:** [functionele OT-baseline 6 november](2026-11-06-m04-network-citadel-ot-baseline.md) · [pre-migratiecheckpoint 7 november](2026-11-07-m04-core-pre-migratie-checkpoint.md)

## Wat er is gedaan

In een begeleide avondsessie heeft Sam de firewallkant van de OT-zone gebouwd. Claude (Critical Security Auditor & Chaos Engineer) begeleidde de stappen en beoordeelde elk resultaat aan de hand van screenshots.

1. **Virtuele netwerkadapter:** de firewall-VM kreeg een vierde netwerkadapter op een eigen, afgezonderd virtueel segment dat alleen voor de OT-zone bedoeld is. Een eerste poging werd niet opgeslagen; de tweede wel. Het bestaande LAB-segment is daarbij bewust niet gekozen.
2. **Preflight na het opstarten:** de bestaande WAN-, beheer- en LAB-interfaces stonden na de wijziging nog op dezelfde adapters met dezelfde adressen. Een extra netwerkkaart kan in VMware de volgorde van adapters veranderen; dat is hier niet gebeurd.
3. **Interface toegewezen via de webinterface:** de nieuwe adapter is als interface **OT** toegevoegd. De webinterface is gekozen in plaats van het consolemenu, omdat het consolemenu vraagt alle interfaces opnieuw in te voeren.
4. **Adressering:** de OT-interface kreeg een statisch adres in het OT-subnet uit het [goedgekeurde zoneontwerp](../architectuur/NETWERKONTWERP.md), zonder upstream gateway.
5. **Firewallregels gelezen, niet gewijzigd:** op de OT-interface staan geen regels, dus verkeer dat via OT binnenkomt wordt standaard geweigerd. De LAB-regels blokkeren verkeer naar alle privé-adresbereiken; het OT-subnet valt daaronder.

## Statusoordeel

| Onderdeel | Status |
| --- | --- |
| OT-interface op de firewall | **IMPLEMENTED** |
| Bestaande interfaces na toevoegen adapter | **VERIFIED** (ongewijzigd) |
| OT → andere zones, LAB → OT | Geblokkeerd **volgens de configuratie**; nog **niet getest** |
| Beheernetwerk → OT | Nog niet beoordeeld |
| HMI en PLC in de OT-zone | **PENDING**; staan nog op het tijdelijke NAT-netwerk |
| **M04-CORE (AC04 + AC07)** | **PENDING** — geen verkeerstest, firewall-log of packetcapture |

Een lege regelset en een blokregel zijn pas bewijs na een negatieve test met een echt systeem op het segment. Dit log claimt daarom geen segmentatie-PASS.

## Aandachtspunten uit de review

- Een eerder als tijdelijk vastgelegde brede egressregel voor een testclient op het LAB staat nog in de regelset. Die moet vóór afronding van M04 worden verwijderd of vervangen door een gerichte regel.
- Het beheerpad naar de OT-zone moet bewust worden gekozen en als aparte rij in de testmatrix worden getest.
- HMI en PLC delen straks één OT-segment. Hun onderlinge Modbus-verkeer loopt dan niet via de firewall; dat wordt niet als firewallhandhaving geclaimd (besluit 6 november).

## Volgende stap

1. Beheerpad naar OT beoordelen.
2. PLC in veilige stopstand, daarna HMI en PLC naar het OT-segment verplaatsen, zonder hostadapter op dat segment.
3. Functionele regressietests AC01–AC03.
4. Positieve en negatieve tests uit de bestaande allow/deny-matrix, met firewall-logs en Wireshark-captures.

**Bewijsgrens:** de originele screenshots zijn ongesaneerd en blijven buiten deze repository. Geen IP-/MAC-adressen, segmentnamen, interface-ID's of hostidentificatoren in deze publieke update. Geen claim van onafhankelijke audit of afgeronde M04-missie.

**Redactie:** Claude, op basis van de begeleide sessie en screenshots van Sam.
