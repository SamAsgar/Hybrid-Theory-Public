# Hybrid-Theory

Hybrid-Theory is een cybersecuritylab voor IT en industriële besturing (OT). In een virtuele omgeving met VMware en pfSense onderzoek ik hoe je systemen van elkaar scheidt, wie toegang krijgt en hoe je met tests en logs kunt vaststellen of die grenzen werken.

**Begin bij [Network Citadel](Portfolio/M04-Network-Citadel/README.md).** In deze missie stuurt een FUXA-bedieningsscherm een OpenPLC-controller aan. De start-stoptest laat zien hoe de controller reageert. De [netwerktests van 20 november](projectlogboeken/2026-11-20-m04-core-c2-netwerkvalidatie.md) laten vervolgens zien welke verbindingen de firewall blokkeerde en welke daarvan in de logs terug te vinden zijn.

[Bekijk de eenvoudige topologie](architectuur/diagrammen/HT-TOPOLOGIE-EENVOUDIG-PUBLIC-2026-11-20.svg) · [Topologie met netwerkzones en aliassen](architectuur/diagrammen/HT-ARCHITECTUUR-A1-TOPOLOGIE-PUBLIC-2026-11-20.svg) · [Alle architectuurdiagrammen](architectuur/README.md)

## Missies

Stand op 20 november 2026. Elke missie heeft eigen acceptatiecriteria. Voor alle vijf staat de eerste milestone nog open.

| Missie | Voortgang |
|---|---|
| [M01 · Hypervisor Fortress](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/42) | Een deel van de controles op host en hypervisor is uitgevoerd. Voor klembord en slepen tussen host en gast geldt een uitzondering op geselecteerde Windows-VM’s. |
| [M02 · Phoenix Recovery](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/43) | Het herstelontwerp ligt er. Een restore op een afzonderlijke host moet nog worden aangetoond. |
| [M03 · Identity Dominion](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/44) | AD en DNS, aanmelden op het domein en één groepsbeleid zijn getest. De uitbreiding met Entra ID is gepland. |
| [M04 · Network Citadel](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/45) | De bediening van de PLC en specifieke firewallblokkades zijn getest. De volledige toets op segmentatie en toegestane verkeersstromen (AC04/AC07) staat open. |
| [M05 · Compliance Sentinel](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/46) | De onderzoeksopzet is goedgekeurd. De eerste geplande casus toetst de M04-netwerksegmentatie aan ISO/IEC 27001 A.8.22. |

## Bewijs en logboeken

Het [publieke portfolio](Portfolio/README.md) koppelt tests aan gesaneerd bewijsmateriaal. De [M01-bewijsindex](Portfolio/M01-Hypervisor-Fortress/EVIDENCE-INDEX.md) bevat 82 screenshots. De [M04-galerij](Portfolio/M04-Network-Citadel/M04-GALERIJ.md) bevat 316 gepubliceerde beelden verdeeld over 21 fasen.

[Projectlogboeken](projectlogboeken/README.md) · [Roadmap](projectlogboeken/ROADMAP.md) · [Statuslegenda](governance/STATUSLEGENDA.md)
