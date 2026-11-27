# M04 Network Citadel | CORE C2 — 20 november 2026

**M04-CORE IN PROGRESS.** De sessie toetste aanvullende verkeerspaden tussen het LAB-testnetwerk, de OT-zone, het beheersegment en de gesimuleerde WAN-zijde. De applicatiebaseline blijft de [functionele PLC/HMI-regressie van 19 november](2026-11-19-m04-openplc-autostart-en-ot-regressie.md), met AC01–AC03 historisch **TESTED / scoped PASS**. Deze update bevat uitsluitend de gecontroleerde netwerkdelta.

| Tests | Waarneming en status |
|---|---|
| F09–F12 LAB → PLC01 | De firewall logde BLOCK voor TCP/8080, TCP/22, TCP/44818 en ICMP vanuit LAB naar de PLC. **Scoped PASS** voor de getoonde pakketten. |
| F13–F15 Beheer → PLC01 | De directe route naar de PLC koos de fysieke uplink. Negatieve TCP-probes naar het firewallbeheeradres toetsen een andere bestemming. Directe PLC-proeven voor TCP/502, TCP/22 en TCP/44818 over een goedgekeurd beheerpad blijven **PENDING / DESIGN-CONFIRM**. |
| F16–F19 OT → beheer, firewall, extern | Timeouts met bijbehorende default-deny-logs op de OT-ingress. **Scoped PASS** voor PLC→beheerhost TCP/8080, HMI→firewallbeheer TCP/443, PLC→firewall OT TCP/22 en PLC→externe HTTP-bestemming TCP/80. |
| F20–F21 OT → externe DNS/NTP | UDP/53 en UDP/123 zijn in de getoonde proeven geblokkeerd. De DNS-query liep af. UDP heeft geen verbindingshandshake. Netcat kan lokaal succes melden zonder NTP-antwoord. Goedgekeurde resolvers en tijdbronnen blijven **DESIGN-CONFIRM**. |
| F22–F23 IPv6 | **NO-ROUTE-VERIFIED** binnen de geïnspecteerde topologie. LAB en OT bevinden zich in gescheiden virtuele L2-segmenten. Voor de onderzochte hosts en paden is geen bruikbare globaal routeerbare IPv6-verbinding naar OT aangetoond. De brede LAN IPv6-allow en alternatieve paden blijven onder review. |
| F24 WAN → OT | **CONFIG REVIEWED / SAFE LIVE TEST PENDING**. De bekeken WAN-regellijst toont geen gebruikers-PASS en het NAT-overzicht geen WAN-portforwards. Een veilige live proef blijft open. |

## Beheer- en bewijsgrenzen

Via het host-only beheersegment is TCP/8080 naar de OpenPLC-forward opnieuw bevestigd. De firewallconfiguratie toont daarnaast een beperkte forward naar FUXA op TCP/1881. De relevante IPv4-block naar OT staat na de gerichte beheeruitzonderingen en vóór de brede LAN IPv4-allow. Het Modbus-pad tussen HMI en PLC blijft binnen OT.

De gerichte firewallobservaties ondersteunen **AC04/AC07**, beide integraal **PENDING**. Volledige tijd-/regel-/packetcorrelatie, passend herstelbewijs, autorisatie/TLS-review, onafhankelijke bewijsreview en eigenaaracceptatie blijven open. De eigenaar heeft de preflightcontrole en de AC01–AC03-bewijsreview uitgesteld. **AC05 PENDING**, **AC06/AC08 PLANNED**. De eigenaar bepaalt AC06-scope en cliëntaantal vóór uitvoering.

[Actuele architectuur](../Architectuur/NETWERKONTWERP.md) · [Open gaten](../Portfolio/M04-Network-Citadel/M04-GAPS.md) · [M04-missie](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/45).
