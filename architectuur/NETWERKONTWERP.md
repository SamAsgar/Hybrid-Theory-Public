# Netwerkontwerp en beveiligingsgrenzen | Hybrid-Theory

**Bijgewerkt:** 20 november 2026 (M04-testdelta 19 november; diagrammen blijven momentopnamen van 15 november) (§1: OT-stand, verkeersstromen en aliassen; §2: diagram B; §4: openstaande punten) · **Classificatie:** gesaneerde architectuurpublicatie · **Herkomst:** private architectuur en HT-C-010.

Dit document heeft twee lagen die niet door elkaar mogen lopen: de **geobserveerde situatie** (§1) en de **doelarchitectuur HT-C-010** (§2–§3). Adressen staan als officiële alias; de [componenttabel met alle aliassen](README.md#11-componenten-zones-en-officiële-aliassen) staat in Architecture.

## 1. Geobserveerde infrastructuur (afgebakend bewijs)

| Onderdeel | Technologie | Status en bewijsgrens |
|---|---|---|
| LAB | VMware LAN Segment, pfSense/Kea DHCP (`PFSENSE_LAB_GW_IP`) | **IMPLEMENTED**; gerichte netwerk-/DHCP-/firewalltests PASS |
| OT-zone | VMware LAN Segment, pfSense OT-interface (`PFSENSE_OT_IP`) | **IMPLEMENTED**; gerichte LAB→OT, OT→LAB en OT→internet TCP/ICMP/HTTPS-blokkeringen met firewalllogs **TESTED / scoped PASS (19 nov.)**. Integrale AC04/AC07-matrix **PENDING**. |
| Beheer (MGMT) | VMware host-only, Cockpit/pfSense GUI (`PFSENSE_MGMT_IP`) | Beheer binnen eerdere tests bereikbaar; actuele NIC-/routingstatus deels OPEN |
| Updates en WAN-simulatie (WAN-SIM) | VMware NAT (`PFSENSE_WAN_IP`) | Tijdelijk egresspad gebruikt; NAT is geen isolatiegarantie voor het thuisnetwerk |
| Windows/Identity | Windows Server en Windows 11 | AD DS/forest, DNS/SRV, domain join, testlogin en GPO **PASS binnen scope** |
| GNS3 | VPCS, switch, Wireshark | ARP/ICMP/capture **PASS** in een losstaande simulatie |
| FUXA01 en PLC01 | Ubuntu/Docker met FUXA en OpenPLC in dezelfde OT-zone (`FUXA01_OT_IP`, `PLC01_OT_IP`) | **AC01–AC03 TESTED / scoped PASS (19 nov.)**: tweede reboot na RUN-autostartcorrectie, automatische herverbinding, gecontroleerde HMI START→STOP en PLC-readback. Onafhankelijke evidence-review en volledige acceptatie **PENDING**. Historische test van 15 nov. blijft apart geldig binnen oude scope. |
| Wazuh | SIEM-manager/indexer/dashboard in het LAB (`WAZUH_CURRENT_IP`, PENDING_CAPTURE) | Start en dashboardlogin **PASS**; 0 agents; agentingestie en detectie **NOT VERIFIED** |
| Recovery | M02 Phoenix Recovery | **PLANNED**; onafhankelijke restore niet aangetoond |
| Azure | Arc/Entra/VNets | **PLANNED**; niet gedeployed |

Deze gegevens komen uit gedateerde sessielogs en zijn **geen nieuwe live-meting**. pfSense heeft vier interfaces: WAN, LAN/MGMT, LAB en OT. Werkelijke adressen en de aliasvertaling worden niet gepubliceerd.

### 1.1 Huidige verkeersstromen (stand 19 november 2026)

![Diagram A: huidige geïmplementeerde architectuur met officiële aliassen](diagrammen/HT-ARCHITECTUUR-A-HUIDIG-PUBLIC-2026-11-15.svg)

*Figuur A. Architectuurillustratie, **geen testbewijs**.*

| # | Stroom | Pad | Status binnen de geteste scope |
|---|---|---|---|
| 1 | FUXA01 (`FUXA01_OT_IP`) → PLC01 (`PLC01_OT_IP`), Modbus TCP/502 | Rechtstreeks binnen OT-subnet, **niet** via pfSense | HMI START→STOP en PLC-readback **TESTED / scoped PASS (19 nov.)**; formele acceptatie/evidence-review **PENDING** |
| 2 | Geautoriseerde beheerbron → webbeheer van PLC01 en FUXA01 | Beheersegment → pfSense → OT; expliciete diensten | Bereikbaarheid op twee beheerpoorten **TESTED / scoped PASS (19 nov.)**; TLS/authenticatie review **OPEN** |
| 3 | LAB → OT (PLC01/FUXA01) | Via pfSense LAB→OT grens | Gerichte TCP-blokkeringen en BLOCK-logs **TESTED / scoped PASS (19 nov.)**; overige matrix **PENDING** |
| 4 | LAB → publiek IPv4 | LAB → pfSense → WAN (VMware NAT) | **PASS** binnen scope (26 okt.) |
| 5 | LAB → thuisrouter (ICMP) | LAB → pfSense | **Geblokkeerd**: **PASS** (26 okt.), alleen voor de geteste bestemming en dit protocol |
| 6 | OT (PLC01/FUXA01) → LAB en publiek internet | Via pfSense OT-interface | Gerichte ICMP- en HTTPS-deny-proeven met gerelateerde BLOCK-logs **TESTED / scoped PASS (19 nov.)**; alternatieve protocollen en IPv6 **PENDING** |
| 7 | Agents → Wazuh | Nog niet ingericht | **NOT VERIFIED**; 0 agents |
| 8 | GNS3-testnet ↔ overige netten | Geen koppeling | Losstaand; ARP/ICMP **PASS** binnen het testnet |

Stroom 1 is **geen firewallregel**: verkeer tussen twee hosts in hetzelfde subnet passeert de firewall niet en zegt dus niets over de zonegrens. Poorten, regels en adressen van het beheerpad zijn bewust niet gepubliceerd. **M04-CORE blijft IN PROGRESS.**

### 1.2 Nieuwe bewijsreeks · 19 november 2026

De [gesaneerde fase-20-galerij](../bewijsvoering/M04-Network-Citadel/20_OT_segmentation_and_regression/README.md) bevat 55 extra afbeeldingen met observaties en beperkingen. De volledige terminalinhoud is in 17 publieke afgeleiden afgedekt; privaat primaire bewijs en publieke deeltests blijven verschillende bewijsniveaus. AC04/AC07 integraal **PENDING**.

## 2. HT-C-010: doelarchitectuur en toekomstige netwerkgrenzen

![Diagram B: doelarchitectuur HT-C-010 met zes zones, twee Azure-subscriptions en M02 Phoenix Recovery](diagrammen/HT-ARCHITECTUUR-B-DOELONTWERP-PUBLIC-2026-11-15.svg)

*Figuur B. Ontwerpillustratie, **geen configuratiebewijs**. De bestaande netwerken WAN-SIM, MGMT, LAB en OT zijn **IMPLEMENTED** (figuur A). Van de zes HT-C-010-doelzones bestaat alleen OT al als eigen segment; IT-servers, IT-clients, Security, private services en GNS3 zijn als afzonderlijke zones **PLANNED**, net als Azure en M02.*

De doelarchitectuur scheidt IT-servers, clients, private services, Security/Wazuh, OT/FUXA/OpenPLC en GNS3. pfSense **default deny** met expliciet goedgekeurde diensten is de ontwerpregel, maar zulke zoneinterfaces en VLAN's zijn **niet automatisch gerealiseerd**: alleen de OT-interface bestaat.

| Van | Naar | Doeleis / status |
|---|---|---|
| IT | OT/PLC | Directe toegang blokkeren; nu één LAB→OT-deny getest (11 nov.), **nog niet als volledige zonegrens bewezen** |
| GNS3 | Andere zones | Geen route; afzonderlijk GNS3-bewijs bewijst dit niet zelfstandig |
| IT- en OT-agents | Wazuh | Alleen toegestaan agentverkeer; end-to-end ingestie nog te testen |
| FUXA01 | PLC01 | Strikt begrensde Modbus-communicatie (TCP/502) binnen de OT-zone; verkeer binnen hetzelfde segment loopt niet via de firewall. Deeltest **TESTED** (15 nov.) |
| IT-services | Azure | Alleen compatibele en toegestane uitgaande HTTPS-/proxyverbindingen |
| Labhost | Recovery-host/offsite | Onafhankelijke M02-back-uproutes volgens goedgekeurd herstelontwerp |

## 3. Recovery en Azure

De M02-doelarchitectuur houdt een toekomstige recoveryhost **buiten de virtuele labzones** en voorziet in een zelfstandig offsite-back-uppad. Geen restore-PASS of werkende immutable retentie wordt geclaimd.

De HT-C-010-baseline gebruikt **twee** voorgestelde subscriptions, elk met een eigen VNet: één voor management en één voor private-cloudoefeningen. Azure Arc vereist **op zichzelf geen VNet**. Geen cloudresource of kosten zijn op basis van deze afbeelding geautoriseerd of geïmplementeerd.

## 4. Openstaande punten en publicatiebeperkingen

- **TWIJFEL:** `LAB_NET_IP` (Ubuntu) en `DC01_LAB_IP` (Windows Server) zijn op verschillende meetdatums met dezelfde waarde vastgelegd; gelijktijdig conflict niet aangetoond. De waarde blijft privé.
- **TWIJFEL:** `GNS3_PC1_IP` in de zelfstandige GNS3-test heeft dezelfde waarde als `PFSENSE_LAB_GW_IP`. De netwerken zijn gescheiden; een daadwerkelijke botsing is daarmee niet bewezen en ontstaat pas bij koppeling.
- **OPEN:** actuele lease-/interfacegegevens (o.a. `WAZUH_CURRENT_IP`), Wazuh-agentingestie, onafhankelijke AC01–AC03-evidence-review, integrale OT-segmentatietests (AC04/AC07), brede LAN-allow- en IPv6-review, hersteltests en Azure-toegang. **PLC-RUN-autostart is binnen de tweede reboot van 19 november scoped PASS**, niet langer een open functionele autostarttest.
- **DOEL / GEEN AUTO-MIGRATIE:** nieuwe zones, routes, firewallregels of cloudresources vereisen expliciete scope, autorisatie, kostencontrole en relevante positieve/negatieve tests.

**Publicatie:** geen fysieke hostnamen, privérouteradressen, concrete IP-/MAC-adressen of private aliasvertalingen; alleen de officiële aliasnamen. Deze gesaneerde illustraties zijn geen audit- of compliancebewijs. Zie [Architecture](README.md) en [publicatiebeleid](../governance/PUBLICATIEBELEID.md).