# pfSense lab-segmentatie | Historische testnotitie (afgeleid)

> Bewerkt 02-11-2026: terminologie geharmoniseerd en interne verwijzingen verwijderd; testuitslagen ongewijzigd.
>
> **TL;DR (redactionele toevoeging)**  
> **Vraag:** Welke basis-pfSense- en netwerkproeven waren op 26 oktober gedocumenteerd?  
> **Uitkomst:** Eén negatieve ICMP-proef buiten de bedoelde LAB-scope werd als geblokkeerd gemeld.  
> **Besluit:** Alleen de gerichte controles PASS; geen brede isolatieclaim.


**Datum:** 26 oktober 2026  
**Status:** historisch, gesaneerd en geabstraheerd. Dit is geen letterlijke kopie van interne sessielogs.

> Historische momentopname; zie [ROADMAP](ROADMAP.md) en [Besluitenlog](../governance/BESLUITENLOG.md) voor latere wijzigingen en actuele status.

## Scope

De virtuele pfSense-firewall werd ingericht met een gescheiden LAB-interface, een beheerkanaal en een gesimuleerde externe verbinding. De opstelling is beoordeeld met toegestane connectiviteitsproeven en gerichte negatieve tests.

## Waarnemingen

- pfSense-installatie en basisbeheer waren operationeel.
- De LAB-interface en firewallregelstructuur waren geconfigureerd.
- Specifiek toegestaan verkeer binnen de onderzochte IPv4-testscope functioneerde.
- Een gerichte negatieve ICMP-test naar een bestemming buiten de bedoelde LAB-scope werd geblokkeerd.
- Tijdens eerdere diagnostiek werd vastgesteld dat het gebruik van een NAT-verbinding op zichzelf geen waterdichte netwerkisolatie oplevert.
- Firewallregeldetails zijn later verder aangescherpt bij de installatie van de Windows-client en de DHCP-dienst.

## Beperkingen

Dit resultaat bewijst niet dat alle RFC1918-adressen, protocollen, IPv6, beheerpaden of toekomstige koppelingen aantoonbaar zijn geïsoleerd. Tests buiten de geautoriseerde scope zijn geen standaardonderdeel van de werkwijze en worden hier niet gereproduceerd.

**Verdict:** basis-pfSense en gescopeerde connectivity/deny-tests **PASS** op hun oorspronkelijke testmoment; breder isolatiemodel **OPEN / NOT VERIFIED**.

Er zijn bewust **geen** provideridentiteiten, privéroutergegevens, echte adressen, route-/firewallsecrets of instructies over systemen buiten de eigen LAB-scope opgenomen.
