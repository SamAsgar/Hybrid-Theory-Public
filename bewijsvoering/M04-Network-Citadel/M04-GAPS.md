# GAP-analyse — M04 Network Citadel

Peildatum 15-11-2026. Gebaseerd op de selectie in `EVIDENCE-INDEX.md` en de projectlogboeken van 5, 7, 8, 9 en 11 november (gelezen, niet gewijzigd).

## 1. Stand per acceptatiecriterium

| AC | Laatste logoordeel | Wat de historische bronselectie aantoont | Oordeel bewijs |
|---|---|---|---|
| AC01 PLC-motorlogica | Scoped PASS (06-11, NAT) | UIT/AAN/UIT visueel bevestigd op 05-11 en 06-11. | **Bewezen** op VMnet8. Regressie op OT: alleen 'Start PLC' en poort 502, geen Monitoring |
| AC02 PLC→FUXA 0→1→0 | Scoped PASS (06-11) | FUXA-tags 0/0 → 1/1 → 0/0 met timestamps, visueel bevestigd. Twee tags. | **Bewezen** op VMnet8. Op OT **niet**: FUXA wijst op 15-11 nog naar PLC01_TEMP_NAT_IP |
| AC03 FUXA→PLC start/stop | PASS (eigenaar + beeld) | Schermopname toont klik en TRUE→FALSE in OpenPLC (5 frames bekeken). Geen pcap. | Functioneel aannemelijk; **geen protocolbewijs**; op OT niet herhaald |
| AC04 segmentatie | PENDING | OT-interface, LAN-segmenten, statische adressen, regelvolgorde en geladen pf-regels zichtbaar. | Configuratie bewezen; **segmentatie niet getest als geheel** |
| AC05 Wazuh-agents | PENDING | Dashboard: 'no agents registered' (04-11). | PENDING terecht |
| AC06 GNS3 3×25 VPCS | PLANNED | Geen beeld. | Geen bewijs |
| AC07 allow/deny-matrix | PENDING, één rij PASS | LAB→FUXA01:1881 geblokkeerd met firewalllog ([RULE_ID_REDACTED]). OT→gateway ICMP geblokkeerd met log. Beheer 8080/1881 True. | Drie rijen bewezen; matrix **onvolledig** |
| AC08 Suricata | PLANNED | Geen beeld. | Geen bewijs |

**M04-CORE (AC04 + AC07): geen PASS.**

## 2. Wat deze ZIP toevoegt aan 'PENDING EVIDENCE IMPORT'

De logs van 9 en 11 november noemen bewijs dat nog niet geïmporteerd was. Het volgende staat wél in deze selectie:

- PLC01: VMware-adapter op OT60, Netplan-inhoud, `netplan get/generate`, `ip -br addr`, `ip route`, ARP naar de gateway.
- pfSense: LAN-regellijst in volgorde (09-11 17:05), port forwards, `pfctl -sr` en `pfctl -sn` voor en na de correctie.
- ICMP: firewalllog met Default deny, ping 4/4 met tijdelijke regel, ping 0/4 daarna.
- Beheerpad: TcpTestSucceeded True (8080 en 1881), HTTP 302 naar /login.
- SSOT-M04-005: de tijdelijke OT-ICMP-regel staat op 09-11 17:05 **uitgeschakeld** in de GUI (visueel bevestigd).
- Root cause FUXA-NAT: bron `[MALFORMED_SOURCE_ADDRESS]` in de geladen rdr-regel (visueel bevestigd), en de gecorrigeerde regel.

## 3. Ontbrekende bewijsvoering

- **AC07-rijen zonder test:** OT→LAB, OT→WAN/internet, LAB→PLC01 (8080/502), ander LAN-adres dan MGMT_CLIENT_IP → OT, host/VMnet8-bypass, IPv6.
- **Geen pcap-bestanden.** Alleen schermbeelden van de capturepagina. Geen Wireshark-capture van een Modbus-read/write.
- **AC01–AC03 op de OT-topologie:** geen Monitoring, geen tagwaarden, geen HMI-proef na migratie.
- **Firewalllog bij de 0/4-ping** na uitschakelen van de tijdelijke regel.
- **Rebootbewijs:** de beelden tonen een nieuwe consolelogin met het juiste adres, niet de reboot zelf. Voor FUXA01 toont 15-11 de container 'Up About a minute'; het adres na boot blijkt indirect uit latere tests.
- **Herstelpad:** geen revert getest. De pfSense-snapshot dateert van vóór de OT-interface. Het back-upbestand is door de eigen controle **niet** als pfSense-config herkend (zie §4).
- **AC05, AC06, AC08:** geen uitvoerend bewijs.

## 4. Tegenstrijdigheden en afwijkingen

1. **[HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN] dubbel gebruikt.** In de regels is dit 'Client01'; op 03-11 krijgt `wazuh-server` deze lease en de port forward 8443 wijst ernaar; op 11-11 heeft Client01 het adres. De Wazuh-forward en de TEMP-internetregel gelden dus voor wie het adres op dat moment heeft (SSOT-M04-001).
2. **[HISTORIC_LAB_ADDRESS_AMBIGUOUS] dubbel gebruikt.** Op 01-11 statisch op PS-HT-DC01, op 15-11 op `hybrid-theory-linux`. Mogelijk adresconflict; niet uitgezocht in de beelden.
3. **pfSense-back-up niet valide aangetoond.** Controle 08-11: HeeftPfSenseConfig False, XML False; Verkenner toont type 'Microsoft Edge HTM', 25 KB. De preflight-eis 'rollbackpad' is daarmee niet gedekt.
4. **Capturelabel.** Pagina met 'OT (em3)' geselecteerd toont uitvoerbestand `...-em2-...pcap`. Niet gebruiken als OT-egressbewijs.
5. **NAT-fout bestond sinds 08-11 23:00.** De FUXA-filterregel had de juiste bron, de rdr-regel niet. Alle FUXA-beheertests tussen 08-11 en 11-11 zeggen daardoor niets over de firewallregels.
6. **TEMP-regel 'Client01 outbound internet'** is op 01-11 als tijdelijk aangemaakt en staat op 11-11 nog actief (F1).
7. **OpenPLC-runtime start niet vanzelf.** Op 15-11 staat de PLC na opstarten op Stopped en luistert 502 niet tot handmatig 'Start PLC'.
8. **Protocollen.** Runtime-log 06-11 start ook EtherNet/IP (44818) en Snap7; op 15-11 opnieuw EtherNet/IP. Uitschakelen is besproken, niet aangetoond.
9. **Ongeldige tests** (niet als firewallbewijs gebruiken): host via Wi-Fi [UNMAPPED_IPV4] naar OT, PLC01 op poort 1881, en tests terwijl VM's uit stonden.
10. **Te verifiëren:** Netplan-bestandsnaam en `chmod`-waarde op PLC01 zijn in de OCR vervormd; vergelijk het beeld `2026-11-08 234859` met de naam in het log.
11. **Tellers 0/0 B** op de LAN-regels (09-11 17:05) ondanks eerdere geslaagde tests. Tellers zijn geen bewijs voor of tegen.

## 5. Onbewezen PASS-claims

| Claim (log) | Waarom niet bewezen |
|---|---|
| PLC01 'IPv4-persistentie na reboot' en 'TCP 8080 na reboot' | Reboot zelf niet in beeld |
| FUXA01 'lokaal HTTP 200 OK' en HTTP via beheerpad | Alleen headers zichtbaar; statusregel valt buiten beeld |
| ICMP 0/4 na uitschakelen tijdelijke regel | Geen firewalllog erbij |
| AC03 PASS | Schermopname, geen Modbus-write op pakketniveau |
| LAN→OT default deny | Regel geladen; verkeerstest alleen voor ICMP vanaf OT-zijde en LAB→OT, niet voor LAN→OT |
| 'MODBUS TCP PASS' 15-11 | TCP-poortbereik binnen hetzelfde L2-segment; loopt niet via pfSense en is geen Modbus-transactie |

## 6. Publicatiegrens

De originelen blijven ongesaneerd in Private. Dit openbare document bevat uitsluitend geabstraheerde beschrijvingen. Ze bevatten onder meer interne IP- en MAC-adressen, een sessiecookie (`2026-11-09 001637`), de standaard-inloggegevens in de Wazuh-banner, het serienummer van de host en accountnamen. Niet naar GitHub zonder sanering.

*Publicatieaanpassing: bestaande adressen en apparaatidentificatoren zijn vervangen door aliassen of redactieaanduidingen. De conclusie van de bron-GAP-analyse blijft leidend voor dit historische meetmoment.*
