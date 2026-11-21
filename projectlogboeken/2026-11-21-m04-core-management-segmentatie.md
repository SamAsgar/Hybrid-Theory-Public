# M04 Network Citadel | CORE — Managementsegmentatie 21 november 2026

**M04-CORE IN PROGRESS · AC04/AC07 PENDING.** Dit is een gesaneerde voortgangsdelta, geen onafhankelijke audit of finale acceptatie.

## Geobserveerde testdelta
Een afzonderlijke Ubuntu-beheer-VM in de managementzone bereikte de pfSense-beheerinterface. Gerichte TCP-probes naar de PLC in het afgeschermde OT-segment werden volgens de latere sessierapportage op TCP/502, TCP/22 en TCP/44818 door de bedoelde LAN→OT-firewallregel geblokkeerd.

**Resultaat:** `TESTED / scoped PASS` voor **alle drie de getoonde poorten vanaf deze specifieke beheer-VM**, op basis van de aangeleverde sessiewaarneming. Voor TCP/22 en TCP/44818 zijn tevens bronroute en client-timeout gerapporteerd. Volledige primaire tijd-, logregel- en packetcapturecorrelatie en onafhankelijke bewijsreview staan nog open.

De oorspronkelijke F13–F15-testmatrix vermeldt een andere beheerbron. **F13–F15 blijven formeel PENDING** tot goedkeuring van de afwijkende testbron en afronding van primaire evidence-review. De eindteller van de packetcapture op de OT-interface en het bewijs van terugdraaien van het tijdelijke testpad ontbreken nog in het aangeleverde statusrapport.

## Architectuurgrenzen
- Fysieke virtualisatiehost krijgt geen permanente directe route naar OT.
- Bestaande, beperkte managementportforwards blijven voorlopig behouden.
- De beheer-VM blijft buiten OT; geen ongecontroleerde forwarding.
- PLC en HMI blijven binnen één geïsoleerd OT-segment en communiceren daar via Modbus TCP.
- De industriële DMZ en verdere beheerinrichting zijn uitgesteld tot na CORE.

## Nog open
IPv6-regelreview en alternatieve paden; veilige gesimuleerde WAN→OT-probe (F24); DNS-/NTP-bronbeleid; herstel- en bewijsreview; formele acceptatie AC04/AC07. AC01–AC03 behouden hun historische **scoped PASS**, met onafhankelijke review PENDING. AC05 is PENDING, AC06/AC08 PLANNED (EXT).

[Vorige C2-delta](2026-11-20-m04-core-c2-netwerkvalidatie.md) · [M04 issue](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/45).

**Publicatiegrens:** geen werkelijke private IP-/MAC-adressen, hostidentificatoren of ruwe firewallregels.