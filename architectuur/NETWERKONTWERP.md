# Netwerkontwerp en beveiligingsgrenzen | Hybrid-Theory

**Bijgewerkt:** 15 november 2026 (§1: OT-stand, verkeersstromen en aliassen; §2: diagram B; §4: openstaande punten) · **Classificatie:** gesaneerde architectuurpublicatie · **Herkomst:** private architectuur en HT-C-010.

Dit document heeft twee lagen die niet door elkaar mogen lopen: de **geobserveerde situatie** (§1) en de **doelarchitectuur HT-C-010** (§2–§3). Adressen staan als officiële alias; de [componenttabel met alle aliassen](README.md#11-componenten-zones-en-officiële-aliassen) staat in Architecture.

## 1. Geobserveerde infrastructuur (afgebakend bewijs)

| Onderdeel | Technologie | Status en bewijsgrens |
|---|---|---|
| LAB | VMware LAN Segment, pfSense/Kea DHCP (`PFSENSE_LAB_GW_IP`) | **IMPLEMENTED**; gerichte netwerk-/DHCP-/firewalltests PASS |
| OT-zone | Eigen VMware LAN Segment, aparte pfSense-interface (`PFSENSE_OT_IP`) | **IMPLEMENTED** (8 nov.), zonder upstream-gateway. PLC01 staat sinds 8–9 nov. in dit segment en FUXA01 sinds 11–15 nov. Eén LAB→OT-poging is aantoonbaar geblokkeerd en het afgebakende beheerpad werkt (**TESTED**, 11 nov.). Integrale isolatie van de zone (AC04/AC07) **NIET BEWEZEN**. [Log 8 nov.](../projectlogboeken/2026-11-08-m04-ot-firewallinterface.md) · [Log 9 nov.](../projectlogboeken/2026-11-09-m04-plc-migratie-governance-publiek.md) · [Log 11 nov.](../projectlogboeken/2026-11-11-m04-segmentatie-en-beheer-validatie.md) |
| Beheer (MGMT) | VMware host-only, Cockpit/pfSense GUI (`PFSENSE_MGMT_IP`) | Beheer binnen eerdere tests bereikbaar; actuele NIC-/routingstatus deels OPEN |
| Updates en WAN-simulatie (WAN-SIM) | VMware NAT (`PFSENSE_WAN_IP`) | Tijdelijk egresspad gebruikt; NAT is geen isolatiegarantie voor het thuisnetwerk |
| Windows/Identity | Windows Server en Windows 11 | AD DS/forest, DNS/SRV, domain join, testlogin en GPO **PASS binnen scope** |
| GNS3 | VPCS, switch, Wireshark | ARP/ICMP/capture **PASS** in een losstaande simulatie |
| FUXA01 en PLC01 | Ubuntu/Docker met FUXA (SCADA/HMI) en OpenPLC-runtime, beide in de OT-zone (`FUXA01_OT_IP`, `PLC01_OT_IP`) | OpenPLC-runtime draait na handmatig starten; Modbus TCP/502-listener, TCP-handshake vanaf FUXA01 en de FUXA-verbinding **TESTED** (15 nov.); twee tags uitgelezen als deelcontrole. Volledige AC02/AC03-readback-evidence **PENDING**; autostart **NOT VERIFIED**. *Historisch:* baseline AC01–AC03 **PASS binnen scope** op de eerdere NAT-topologie (6 nov.). [Log 15 nov.](../projectlogboeken/2026-11-15-m04-ot-modbus-applicatievalidatie.md) |
| Wazuh | SIEM-manager/indexer/dashboard in het LAB (`WAZUH_CURRENT_IP`, PENDING_CAPTURE) | Start en dashboardlogin **PASS**; 0 agents; agentingestie en detectie **NOT VERIFIED** |
| Recovery | M02 Phoenix Recovery | **PLANNED**; onafhankelijke restore niet aangetoond |
| Azure | Arc/Entra/VNets | **PLANNED**; niet gedeployed |

Deze gegevens komen uit gedateerde sessielogs en zijn **geen nieuwe live-meting**. pfSense heeft vier interfaces: WAN, LAN/MGMT, LAB en OT. Werkelijke adressen en de aliasvertaling worden niet gepubliceerd.

### 1.1 Huidige verkeersstromen (stand 15 november 2026)

![Diagram A: huidige geïmplementeerde architectuur met officiële aliassen](diagrammen/HT-ARCHITECTUUR-A-HUIDIG-PUBLIC-2026-11-15.svg)

*Figuur A. Architectuurillustratie, **geen testbewijs**.*

| # | Stroom | Pad | Status binnen de geteste scope |
|---|---|---|---|
| 1 | FUXA01 (`FUXA01_OT_IP`) → PLC01 (`PLC01_OT_IP`), Modbus TCP/502 | **Rechtstreeks binnen het OT-subnet**; niet via de pfSense-router | Listener, TCP-handshake en FUXA-verbinding **TESTED** (15 nov.); volledige AC02/AC03-readback **PENDING** |
| 2 | Beheerbron (`MGMT_CLIENT_IP`) → webbeheer van PLC01 en FUXA01 | MGMT → pfSense → OT; alleen vanaf de aangewezen beheerbron | **TESTED** (11 en 15 nov.); authenticatie/TLS open |
| 3 | LAB → OT | Via pfSense | **Geblokkeerd**: één gerichte deny-deeltest **PASS** met firewalllog (11 nov.); niet de hele AC07-matrix |
| 4 | LAB → publiek IPv4 | LAB → pfSense → WAN (VMware NAT) | **PASS** binnen scope (26 okt.) |
| 5 | LAB → thuisrouter (ICMP) | LAB → pfSense | **Geblokkeerd**: **PASS** (26 okt.), alleen voor de geteste bestemming en dit protocol |
| 6 | OT → andere zones en internet | Via de pfSense-OT-interface | **Niet getest**; egress-isolatie hoort bij AC04 (**PENDING**) |
| 7 | Agents → Wazuh | Nog niet ingericht | **NOT VERIFIED**; 0 agents |
| 8 | GNS3-testnet ↔ overige netten | Geen koppeling | Losstaand; ARP/ICMP **PASS** binnen het testnet |

Stroom 1 is **geen firewallregel**: verkeer tussen twee hosts in hetzelfde subnet passeert de firewall niet en zegt dus niets over de zonegrens. Poorten, regels en adressen van het beheerpad zijn bewust niet gepubliceerd. **M04-CORE blijft IN PROGRESS.**

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
- **OPEN:** actuele lease-/interfacegegevens (o.a. `WAZUH_CURRENT_IP`), Wazuh-agentingestie, volledige AC02/AC03-readback-evidence, autostart van de PLC-runtime, integrale OT-segmentatietests (AC04/AC07), hersteltests en Azure-toegang.
- **DOEL / GEEN AUTO-MIGRATIE:** nieuwe zones, routes, firewallregels of cloudresources vereisen expliciete scope, autorisatie, kostencontrole en relevante positieve/negatieve tests.

**Publicatie:** geen fysieke hostnamen, privérouteradressen, concrete IP-/MAC-adressen of private aliasvertalingen; alleen de officiële aliasnamen. Deze gesaneerde illustraties zijn geen audit- of compliancebewijs. Zie [Architecture](README.md) en [publicatiebeleid](../governance/PUBLICATIEBELEID.md).