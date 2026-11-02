# Netwerkontwerp en beveiligingsgrenzen

**Type:** gesaneerde logische beschrijving. Geen echte thuisnetwerk-, provider- of beheeradressen.

| Segment | Technologie | Beoogde functie | Bewijsstatus |
|---|---|---|---|
| LAB | VMware LAN Segment + pfSense | Gescheiden virtuele client/serveromgeving | **IMPLEMENTED**; gerichte IPv4-netwerk- en DHCP-tests PASS |
| MGMT | Afzonderlijk host-only beheer | Cockpit, pfSense-beheer en lokale toegang | Beheertoegang binnen beschreven tests bevestigd; algehele actuele toegangstoestand niet opnieuw getest |
| UPDATE | Tijdelijke VMware NAT | Onderhouds- en updatesessies | Alleen gecontroleerd waar gedocumenteerd |
| WAN-SIM | VMware NAT voor pfSense | Simulatie van externe verbinding | IMPLEMENTED; NAT is geen zelfstandige isolatiegarantie |
| GNS3 dataplane | VPCS–switch–VPCS | ARP/ICMP en packetanalyse | **PASS** voor kleine losstaande testopstelling |
| Azure en IT/OT | Geplande uitbreidingen | Hybride governance, monitoring en industriële simulatie | **PLANNED** |

## Laatst gedocumenteerde tijdelijke egressregel (1 november 2026)

Voor de Windows 11-testclient is in pfSense tijdelijk een **IPv4 ALLOW Any-egressregel** toegepast voor toegang tot internetdiensten en evaluatie-activatie. De bestaande RFC1918-blockregel stond **erboven**. Daardoor zijn DNS, HTTPS en browsertoegang binnen die beperkte testscope geslaagd. Dit is een **brede tijdelijke uitzondering**, geen definitieve firewallhardening en geen bewijs van algemene isolatie. **De huidige live-regelstatus is vanuit de repository niet vast te stellen.** Zie [sessielog](../projectlogboeken/2026-11-01-windows-client-pfsense-windows-server-ad-ds.md).

## Reproduceerbare netwerkverificatie

Een gerichte positieve test controleert of een expliciet toegestane verbinding functioneert. Een gerichte negatieve test controleert of relevant niet-geautoriseerd verkeer inderdaad wordt geblokkeerd. Beide resultaten worden inclusief protocol, bron/destination-scope, tijdstip en configuratiecontext beoordeeld.

**Bestaand bewijs is niet onbeperkt generaliseerbaar.** Een ICMP-test zegt bijvoorbeeld niets over alle andere protocollen, IPv6 of toekomstige routewijzigingen.

## Open ontwerpconflict

In twee **gescheiden** labs werd een overlappend adres gebruikt. Zolang deze dataplanes losstaan, is er geen bewezen productieconflict. Voor een toekomstige koppeling van GNS3 aan pfSense is een goedgekeurd, niet-overlappend adresplan nodig.

## Beheer- en publicatiegrenzen

Geen echte interne IP's, MAC-adressen, actuele domeinnaam, provideridentiteiten of privéapparaten in dit document. Nieuwe netwerkverbindingen vereisen een expliciet gekozen scope, veiligheidscheck en passende rollback.

**Statusgebruik:** [statuslegenda](../governance/STATUSLEGENDA.md).
