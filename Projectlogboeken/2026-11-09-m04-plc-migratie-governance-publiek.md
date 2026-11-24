# M04 Network Citadel | OT-migratie, troubleshooting en documentatiebeheer — 8–9 november 2026

**Repository:** Hybrid-Theory-Public · gesanitiseerde portfolio-update  
**Registratie:** 9 november 2026  
**Periode:** terugblik op de circa 22 voorafgaande uren  
**Status:** M04-CORE **IN PROGRESS**; PLC-netwerkmigratie **IMPLEMENTED**, geselecteerde deeltests **TESTED (door Sam gerapporteerd)**; bewijsimport en overige acceptatietests **PENDING**  
**Aansluiting op historie:** [OT-firewallinterface 7–8 november](2026-11-08-m04-ot-firewallinterface.md), [pre-migratiecheckpoint](2026-11-07-m04-core-pre-migratie-checkpoint.md), [functionele OT-baseline](2026-11-06-m04-network-citadel-ot-baseline.md)

## 1. Samenvatting

De OT-firewallinterface die in de vorige sessie was ingericht, is gevolgd door de gecontroleerde migratie van de PLC-server vanaf een tijdelijk virtueel NAT-netwerk naar een eigen geïsoleerd OT-segment. Daarbij zijn een statische netwerkconfiguratie, een begrensd beheerpad via pfSense en expliciete allow/deny-regels ingericht en gericht getest.

De HMI-server is **nog niet** naar het nieuwe segment gemigreerd. De oorspronkelijke functionele PLC/HMI-testresultaten blijven historische resultaten op de oude topologie; zij zijn niet automatisch geldig als regressie op de nieuwe omgeving.

## 2. Uitgevoerde werkzaamheden en troubleshooting

| Werkstap | Probleem of aandachtspunt | Aanpak en waarneming |
|---|---|---|
| Firewall/NAT-beheerpad | Automatisch geassocieerde filterregels kregen niet de bedoelde effectieve volgorde ten opzichte van een algemene blokregel. | NAT en expliciete firewallpassregels gescheiden beheerd; actief geladen regelvolgorde gecontroleerd via pfSense. |
| PLC-netwerkmigratie | Het nieuwe geïsoleerde segment biedt geen DHCP-adres aan de PLC. | VMware-adapter gecontroleerd overgezet; statische IPv4-configuratie via Netplan/systemd-networkd aangebracht. |
| Netplan-toepassing | Een proefconfiguratie meldde een rollback na timeout terwijl de actieve interface de beoogde configuratie toonde. | Niet op tussentijdse uitvoer vertrouwd: gecontroleerde herstart en nieuwe route-/adrescontrole uitgevoerd. |
| Gatewaytest | De eerste ICMP-proef werd door default deny geblokkeerd. | Een beperkte tijdelijke uitzondering liet ICMP toe; na uitschakelen werd hetzelfde verkeer weer geblokkeerd. |
| Beheerconnectiviteit | De PLC-webinterface moest via een afgebakend managementpad bereikbaar blijven. | TCP-bereik en HTTP-redirect naar de inlogpagina waargenomen, ook na reboot. |
| SSH-controle | Een niet-bereikbare beheerspoort kan verkeerd worden geïnterpreteerd. | Alleen als poorttest geregistreerd, **niet** als zelfstandig bewijs van volledige netwerkisolatie. |

**Bewijsgrens:** deze deelresultaten zijn gerapporteerde tests uit de begeleide labsessie. De volledige onderliggende evidencebundel is nog niet publiek beschikbaar of onafhankelijk beoordeeld. Een gemelde PASS is daarom uitsluitend geldig binnen de beschreven testscope.

## 3. Actuele status

| Onderdeel | Status |
|---|---|
| Firewall-OT-interface en gescheiden virtueel segment | **IMPLEMENTED** |
| PLC-server op nieuw OT-segment, statische IP-configuratie | **IMPLEMENTED** |
| Statisch adres en route blijven na reboot behouden | **TESTED — PASS gerapporteerd** |
| Begrensde HTTP-beheertoegang via firewall | **TESTED — PASS gerapporteerd** |
| Tijdelijke ICMP-allow en daaropvolgende block | **TESTED binnen beperkte scope** |
| Publicatieklare screenshots en gedetailleerd testbewijs | **PENDING REVIEW / EVIDENCE IMPORT** |
| HMI-migratie en HMI↔PLC-communicatie | **PENDING** |
| Functionele AC01–AC03 regressie op OT-segment | **PENDING** |
| AC04 volledige segmentatievalidatie | **PENDING** |
| AC07 volledige allow/deny-testmatrix | **PENDING** |
| **M04-CORE** | **IN PROGRESS**, geen volledige security-PASS |

## 4. Governance en plannen

Parallel aan het labwerk is het documentatie- en wijzigingsproces aangescherpt:

- **Single Source of Truth:** geverifieerde technische waarnemingen worden vastgelegd in canonieke private registers; publieke documentatie is daarvan een geselecteerde, gesanitiseerde weergave.
- **Wijzigingscontrole:** formele scheiding tussen plan, goedkeuring, uitvoering, verificatie, harmonisatie en review/merge.
- **Repositorybrede impactanalyse:** een private impactmatrix helpt bepalen welke afhankelijke documenten door technische wijzigingen geraakt worden. Deze matrix wordt **niet** rechtstreeks geëxporteerd.
- **Public Release Harmonization:** publicatie-impactcheck, gegevensclassificatie en sanitization, expliciet eigenaarakkoord voor de scope, een afzonderlijke publieke draft-PR en finale review vóór merge.
- **Rolafbakening:** één uitvoerende assistent per publieke PR; een afzonderlijke beveiligingsreview waar relevant; Sam neemt publicatiebesluiten.

**Vervolgplan:** eerst HMI en PLC functioneel op het nieuwe segment controleren, daarna de complete segmentatie- en negatieve beveiligingstests afronden. Tussentijdse publieke statusupdates mogen nooit suggereren dat de hele M04-missie is afgerond.

## 5. Publicatie- en sanitizationgrens

Deze publieke samenvatting bevat geen werkelijke interne IP-, IPv6- of MAC-adressen, geen host-specifieke mapping, geen interne subnet-/VMware-segmentnaam, geen herstelgeheimen, geen raw configuraties en geen private PR- of commitlinks. Ze beschrijft technische methoden en testuitkomsten, zonder een herleidbare netwerkinventaris te publiceren.

Originele screenshots en ruwe uitvoer blijven buiten deze publicatie. Eventuele latere evidence-publicatie vereist afzonderlijke controle van pixels, metadata, hyperlinks en commitinhoud.

**Redactie:** gesanitiseerde afgeleide rapportage van waarnemingen van Sam; geen claim van externe onafhankelijke audit of certificering.
