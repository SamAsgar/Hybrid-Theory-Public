# M04 Network Citadel | CORE — Managementsegmentatie 21 november 2026

**M04-CORE IN PROGRESS · AC04/AC07 PENDING.** Dit is een gesaneerde voortgangsdelta, geen onafhankelijke audit of finale acceptatie.

## Geobserveerde testdelta
Een afzonderlijke Ubuntu-beheer-VM in de managementzone bereikte de pfSense-beheerinterface. Een gerichte TCP/502-probe naar de PLC in het afgeschermde OT-segment werd volgens de sessierapportage door de bedoelde LAN→OT-firewallregel geblokkeerd.

**Resultaat:** `TESTED / scoped PASS` voor deze **specifieke beheer-VM als bron**, op basis van de aangeleverde sessiewaarneming. Volledige primaire tijd-, logregel- en packetcapturecorrelatie en onafhankelijke bewijsreview staan nog open.

De oorspronkelijke F13-matrix vermeldt een andere beheerbron. Daarom blijft **F13 formeel PENDING**, tot expliciete bronacceptatie en de benodigde evidence-review. F14 (SSH, TCP/22) en F15 (EtherNet/IP, TCP/44818) blijven **PENDING**.

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