# pfSense CE | Geïmplementeerde basis en open verificatie (historische bestandsnaam PFSENSE_PLAN)

**Status:** **IMPLEMENTED** als virtuele firewall met vier interfaces (WAN, LAN/MGMT, LAB en sinds 8 november 2026 OT); gerichte tests uitgevoerd. Deze pagina bevat alleen gesaneerde configuratiescope.

## Componenten

- pfSense CE 2.9.0 als virtuele firewall met onderscheiden netwerkinterfaces.
- WAN-simulatie via VMware NAT, gescheiden LAB- en beheertoegang.
- Kea DHCPv4 voor LAB-clients; lease en pfSense-allocatielog op 1 november gericht bevestigd.
- Gerichte firewallregels voor toegestane services en blokkerend beleid waar vereist.

## Interfaces en officiële aliassen

| Interface | Netwerk | IP-alias | MAC-alias | Status |
|---|---|---|---|---|
| WAN | WAN-SIM (VMware NAT) | `PFSENSE_WAN_IP` | `PFSENSE_WAN_MAC` | **IMPLEMENTED** |
| LAN / MGMT | Host-only beheernetwerk | `PFSENSE_MGMT_IP` | `PFSENSE_MGMT_MAC` | **IMPLEMENTED**; webbeheer PASS binnen scope |
| LAB | Geïsoleerd LAN Segment | `PFSENSE_LAB_GW_IP` | `PFSENSE_LAB_GW_MAC` | **IMPLEMENTED**; Kea DHCPv4 en gerichte ICMP-tests |
| OT | Eigen geïsoleerd LAN Segment | `PFSENSE_OT_IP` | `PFSENSE_OT_MAC` | **IMPLEMENTED** (8 nov.), zonder upstream-gateway; integrale isolatie (AC04/AC07) **PENDING** |

Werkelijke adressen worden niet gepubliceerd. Het actuele overzicht staat in [Architecture, diagram A](README.md).

## Aangetoonde tests

| Onderdeel | Gerapporteerd resultaat |
|---|---|
| Firewall-VM en webbeheer | Installatie en beheerfunctie aangetoond |
| LAB DHCP | Client ontvangt passende lease in testsegment |
| LAB-gateway | Gerichte ICMP-proeven met respons |
| Firewallregelvolgorde | Eén negatieve ICMP-test buiten de LAB-scope op 26 oktober als geblokkeerd gerapporteerd; latere uitzonderingen/regelvolgorde afzonderlijk op 1 november gecontroleerd |
| OT-zone: LAB→OT | Eén onbevoegde verbindingspoging vanuit het LAB is op 11 november aantoonbaar geblokkeerd, met firewalllog (**gerichte deeltest PASS**) |
| OT-zone: beheerpad | Webbeheer van PLC01 en FUXA01 bereikbaar vanaf de aangewezen beheerbron (**TESTED**, 11 en 15 november) |
| Compleet isolatiemodel | **PENDING** voor aanvullende scope: niet alle netwerken, protocollen of toestanden getest; AC04 en AC07 open |

## Laatst gedocumenteerde uitzondering (1 november 2026)

Voor één Windows 11-testclient is tijdelijk een brede **IPv4 ALLOW Any-egressregel** gebruikt voor internettoegang en evaluatie-activatie; de bestaande RFC1918-blokkering stond daarboven. De gerichte DNS/HTTPS-/browsertest was succesvol. **Dit is geen productiebeleid, algemene egress-PASS of bewijs van de huidige live-regelstatus.** Zie [sessielog](../projectlogboeken/2026-11-01-windows-client-pfsense-windows-server-ad-ds.md).

## Nog open

- Breed negatief verkeer, alle private ranges en IPv6.
- OT-zone: volledige positieve en negatieve testmatrix (AC04/AC07), egress vanuit OT en beoordeling van tijdelijke regels.
- DNS-/tijdbronontwerp en security-hardening van tijdelijke permissieve regels.
- Geslaagde configuratiehersteltest/off-host disaster recovery.
- Koppeling van de bestaande losse GNS3-tests aan pfSense na conflictvrij IP-plan.

**Bewijsgrens:** een bestaande regel of screenshot is configuratiebewijs, niet automatisch een bewezen end-to-end blokkade.

**Statusgebruik:** [statuslegenda](../governance/STATUSLEGENDA.md).

## M04 — controle- en herstelgates (20 november 2026)

Volgens de private M04-werkwijze van 20 november blijven de gerichte LAB→OT, OT→LAB en OT→externe-bestemming-denies van 19 november gescopeerde testresultaten en hoeven ze alleen opnieuw bij gewijzigde regels of onvoldoende bewijs. Voor aanvullende tests staan onder meer MGMT→ongeautoriseerde services, brede LAN IPv4-/IPv6-allowregels, OT→MGMT, UDP-egress, WAN→OT en effectieve Windows-bronroute open.

Voordat pfSense-regels opnieuw worden aangepast: controleer de configuratie-export (`config.xml`), integriteit en een herstelroute. Een downloadscherm of snapshot toont nog geen geslaagde restore. Volledige AC04/AC07-matrix, log-/pcapcorrelatie en eigenaaracceptatie blijven **PENDING**. [Fase-20-galerij](../Portfolio/M04-Network-Citadel/M04-Bewijsvoering/20_OT_segmentation_and_regression/README.md).
