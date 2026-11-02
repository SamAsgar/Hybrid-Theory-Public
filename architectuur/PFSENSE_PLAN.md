# pfSense CE | Geïmplementeerde basis en open verificatie (historische bestandsnaam PFSENSE_PLAN)

**Status:** **IMPLEMENTED** als virtuele firewall en LAB-gateway; gerichte tests uitgevoerd. Deze pagina bevat alleen gesaneerde configuratiescope.

## Componenten

- pfSense CE 2.9.0 als virtuele firewall met onderscheiden netwerkinterfaces.
- WAN-simulatie via VMware NAT, gescheiden LAB- en beheertoegang.
- Kea DHCPv4 voor LAB-clients; lease en pfSense-allocatielog op 1 november gericht bevestigd.
- Gerichte firewallregels voor toegestane services en blokkerend beleid waar vereist.

## Aangetoonde tests

| Onderdeel | Gerapporteerd resultaat |
|---|---|
| Firewall-VM en webbeheer | Installatie en beheerfunctie aangetoond |
| LAB DHCP | Client ontvangt passende lease in testsegment |
| LAB-gateway | Gerichte ICMP-proeven met respons |
| Firewallregelvolgorde | Eén negatieve ICMP-test buiten de LAB-scope op 26 oktober als geblokkeerd gerapporteerd; latere uitzonderingen/regelvolgorde afzonderlijk op 1 november gecontroleerd |
| Compleet isolatiemodel | **PENDING** voor aanvullende scope: niet alle netwerken, protocollen of toestanden getest |

## Laatst gedocumenteerde uitzondering (1 november 2026)

Voor één Windows 11-testclient is tijdelijk een brede **IPv4 ALLOW Any-egressregel** gebruikt voor internettoegang en evaluatie-activatie; de bestaande RFC1918-blokkering stond daarboven. De gerichte DNS/HTTPS-/browsertest was succesvol. **Dit is geen productiebeleid, algemene egress-PASS of bewijs van de huidige live-regelstatus.** Zie [sessielog](../projectlogboeken/2026-11-01-windows-client-pfsense-windows-server-ad-ds.md).

## Nog open

- Breed negatief verkeer, alle private ranges en IPv6.
- DNS-/tijdbronontwerp en security-hardening van tijdelijke permissieve regels.
- Geslaagde configuratiehersteltest/off-host disaster recovery.
- Koppeling van de bestaande losse GNS3-tests aan pfSense na conflictvrij IP-plan.

**Bewijsgrens:** een bestaande regel of screenshot is configuratiebewijs, niet automatisch een bewezen end-to-end blokkade.

**Statusgebruik:** [statuslegenda](../governance/STATUSLEGENDA.md).
