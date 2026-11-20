# M04 | Saneringsrapport en publicatieverantwoording

**Datum migratie:** 17 november 2026  
**Bron:** private repository, map `bewijsvoering/Lab-4 | Network Citadel` (alleen gelezen, niets gewijzigd)  
**Doel:** `bewijsvoering/M04-Network-Citadel/` in deze publieke repository  
**Principe:** maximale technische transparantie, geen gevoelige blootstelling. Bij twijfel is gemaskeerd.

## 1. Werkwijze

1. **Alleen lezen uit de private bron.** Originelen zijn niet gewijzigd, verplaatst of gecommit. De sanering is buiten beide repositories uitgevoerd.
2. **Automatische detectie per beeld.** Elk beeld is 2–3× vergroot en met Tesseract OCR gelezen in vier varianten: normaal, geïnverteerd, op basis van het helderste kanaal (gekleurde shell-prompts) en op basis van het donkerste kanaal (witte tekst op gekleurde balken). Elk woord is getoetst op IPv4/IPv6-, MAC- en hexidentifiers, `user@host`-prompts, gebruikersnamen, hostnames en FQDN's, lokale paden, sessiecookies/tokens, VM- en LAN-segmentnamen. Bij regels met een cookie, machine-ID, boot-ID, gebruikerspad of IPv6-link-local is de rest van de regel gemaskeerd.
3. **Onomkeerbare maskering.** Gevonden gebieden zijn gevuld met een ondoorzichtig vlak. Er is niet geblurd of gepixeleerd. Waar de waarde exact overeenkomt met een officiële alias staat die alias in het vlak, bijvoorbeeld `PFSENSE_MGMT_IP`. Anders staat er een `REDACTED_*`-label of niets.
4. **Individuele visuele inspectie.** Alle 210 resultaten zijn één voor één bekeken. Waar OCR iets miste, is een handmatig masker toegevoegd: in **58 beelden 104 extra maskers**. Voorbeelden: hostname in een browsertab, `/home/<user>`-pad, SSH-hostkey-fingerprint, `login: <user>`, VMware-VM- en LAN-segmentnamen, een MAC-adres in spatienotatie in `route print`, over twee regels afgebroken IP-adressen en adresfragmenten in afgesneden beeldranden.
5. **Metadata verwijderd.** Elk beeld is opnieuw opgeslagen als RGB-PNG zonder tekst- of EXIF-chunks.
6. **Tekst gesaneerd.** Index, galerij, GAP-analyse, fase-README's, addendum en CSV zijn overgezet met vervanging van echte adressen door officiële aliassen (anders `REDACTED_IP`/`REDACTED_SUBNET`). Classificatieregels zijn aangepast en alle hashes van de private originelen zijn vervangen door hashes van de publieke afgeleiden.
7. **Controle achteraf.** De definitieve beelden zijn opnieuw met OCR gescand op adres-, MAC-, gebruikers- en hostpatronen. Alle tekstbestanden zijn gescand op adressen, MAC's, private hashes, gebruikersnamen en hostnames. Resultaten staan in §5.

## 2. Overgebrachte bestanden

| Fase | Beelden | Automatische + handmatige maskers | Beelden met handmatige aanvulling |
|---|---:|---:|---:|
| `01_Pre_migration_baseline` | 23 | 1855 | 4 |
| `02_VM_Network_setup` | 3 | 188 | 1 |
| `03_FUXA_OpenPLC_baseline` | 13 | 848 | 7 |
| `04_Architecture_design` | 4 | 134 | 0 |
| `05_PLC01_provisioning` | 11 | 378 | 6 |
| `06_PLC_program_runtime` | 13 | 642 | 9 |
| `07_FUXA_Modbus_AC01_03` | 25 | 1014 | 3 |
| `08_Pre_migration_safety` | 6 | 395 | 1 |
| `09_OT_interface_rules` | 11 | 426 | 3 |
| `10_Snapshots_migration` | 4 | 286 | 3 |
| `11_Client_routes_tests` | 8 | 145 | 2 |
| `12_LAN_OT_firewall` | 5 | 68 | 0 |
| `13_LAN_port_forward` | 10 | 307 | 0 |
| `14_pfSense_logs` | 9 | 806 | 2 |
| `15_VMnet_adapters` | 11 | 824 | 3 |
| `16_OT_AC04_AC07` | 12 | 1072 | 2 |
| `17_Network_diagnostics` | 8 | 1102 | 2 |
| `18_Forward_and_regression` | 27 | 2859 | 8 |
| `19_FUXA_followup` | 7 | 58 | 2 |
| **Totaal** | **210** | **13407** | **58** |

Daarnaast overgezet en gesaneerd: `M04-EVIDENCE-INDEX.md`, `M04-GALERIJ.md`, `M04-GAPS.md`, `M04-EVIDENCE.csv`, 19 fase-README's en `19_FUXA_followup/ADDENDUM-2026-11-15.md`. Nieuw opgesteld: `README.md`, `M04-SHA256SUMS.txt` (alleen publieke afgeleiden) en dit rapport.

## 3. Toegepaste maskeringen per categorie

| Label in beeld | Aantal |
|---|---:|
| `REDACTED_IP` | 2730 |
| `REDACTED` | 2326 |
| `REDACTED_USER@HOST` | 1984 |
| `REDACTED_LINE (regel vanaf trigger)` | 1163 |
| `REDACTED_ID` | 701 |
| `PFSENSE_LAB_GW_IP` | 618 |
| `PFSENSE_MGMT_IP` | 572 |
| `MGMT_CLIENT_IP` | 569 |
| `CLIENT01_DHCP_IP` | 481 |
| `REDACTED_IPV6` | 410 |
| `FUXA01_OT_IP` | 308 |
| `LAB_NET_IP` | 281 |
| `REDACTED_MAC` | 277 |
| `PLC01_TEMP_NAT_IP` | 226 |
| `PLC01_OT_IP` | 207 |
| `FUXA_TEMP_NAT_IP` | 173 |
| `REDACTED_USER` | 129 |
| `PFSENSE_OT_IP` | 86 |
| `NET_02_DNS_IP` | 31 |
| `PFSENSE_WAN_IP` | 22 |
| `REDACTED (zonder label)` | 20 |
| `REDACTED_VM` | 18 |
| `REDACTED_MAC_LINE` | 12 |
| `NET_02_IP` | 8 |
| `MGMT_NET_IP` | 7 |
| `NET_02_PEER_02_IP` | 7 |
| `VM` | 5 |
| `IP` | 5 |
| `REDACTED_PATH` | 5 |
| `PATH` | 4 |
| `USER` | 4 |
| `REDACTED_LAN_SEGMENT` | 4 |
| `REDACTED_PROMPT` | 3 |
| `REDACTED_HOSTNAME` | 2 |
| `REDACTED_VM_TABS` | 2 |
| `REDACTED_FQDN` | 2 |
| `REDACTED_HOSTKEY` | 1 |
| `REDACTED_USER@IP` | 1 |
| `REDACTED_LAN_SEGMENTS` | 1 |
| `ID` | 1 |
| `PFSENSE_MGMT_IP:1881` | 1 |

*Aantallen zijn OCR-vakken. Eén zichtbare waarde kan door meerdere OCR-varianten overlappend gemaskeerd zijn.*

## 4. Uitgesloten of niet overgenomen

| Item | Reden |
|---|---|
| Private originele PNG's (210) | Alleen gesaneerde afgeleiden gepubliceerd |
| Hashes van de private originelen (`SHA256_original`, `bytes`, `M04-SHA256SUMS.txt` van de bron) | Vervangen door hashes van de publieke afgeleiden; originele hashes zouden de private bron herleidbaar maken |
| `README.md` van de private bronmap | Vervangen door een nieuw opgestelde publieke README; de private versie verwijst naar private beheer en ruwe herkomst |
| Private staging (`_M04-PRIVATE-SANITIZATION-STAGING`), private reviewtools en -bevindingen, alias-/SSOT-register, private projectlogboeken | Buiten scope; bevatten de koppeling echt↔alias of private procesinformatie |

Er is **geen** M04-screenshot volledig uitgesloten. Na maskering bleef van elk beeld voldoende technische inhoud over. Bij twijfel is binnen het beeld ruim gemaskeerd in plaats van het beeld te laten vallen.

## 5. Restrisico's en bewuste keuzes

- **OCR-afhankelijkheid.** De detectie is OCR-gestuurd en daarna visueel gecontroleerd. Zeer kleine, schuine of half afgesneden tekst kan theoretisch nog een fragment bevatten. Alle beelden zijn op schermresolutie geïnspecteerd, maar niet elk beeld op 1:1 pixelniveau over het volledige oppervlak.
- **Overmaskering.** Versienummers met een IP-patroon (bijvoorbeeld DISM-versies), generieke RFC1918-voorbeelden, enkele pfSense-helpteksten en docker-layer-ID's zijn soms mee gemaskeerd. Dat kost wat leesbaarheid, maar raakt de bewijswaarde niet.
- **Bewust zichtbaar gelaten:** poortnummers (502, 1881, 8080, 8443, 443, 22), interfacenamen (`em0`–`em3`, `ens33`, `ens36`, `VMnet1`/`VMnet8`), firewallregelbeschrijvingen, ruletracker-ID's, snapshotnamen (`M04-CORE-PRE-MIGRATION-*`), pfSense- en Ubuntu-versies, het hardwaremodel van de host-SSD (geen serienummer), `127.0.0.1`/`0.0.0.0`/broadcast/netmaskers en de logische systeemnamen PLC01/FUXA01/Client01. Die staan al in de publieke architectuurdocumentatie.
- **Productstandaardaccounts** (pfSense-`admin`, OpenPLC-`openplc`, Wazuh) zijn waar zichtbaar gemaskeerd. Het bestaan van een standaardaccount blijft afleidbaar uit de context van de productschermen.
- **Aliassen** onthullen de netwerkrol van een adres, niet de waarde. De echte koppeling staat alleen in het private aliasregister.
- **Interpretatie.** De publicatie verandert niets aan de bewijsstatus: AC02/AC03-regressie, AC04 en AC07 blijven **PENDING**; `M04-CORE = IN PROGRESS`.
- **Publicatiegate.** Deze migratie staat op een aparte branch met een pull request. **Niet automatisch mergen**: eigenaar-review en een eigen visuele steekproef vóór merge worden aanbevolen.

## 6. Aanvulling 20 november 2026 — fase 20

Voor de set van 19 november zijn **55 aanvullende publieke PNG-afgeleiden** gemaakt (totaal 265 in 20 fasen). De originelen blijven in Private. Zie de [aparte saneringsverantwoording](M04-PHASE20-SANITIZATION-REPORT.md). Bij **17 terminalbeelden is de uitvoer volledig afgedekt**: dit beperkt de publieke bewijswaarde. De eerdere saneringsanalyse van 210 beelden blijft uitsluitend op die oorspronkelijke set van toepassing; de nieuwe 55 hebben een afzonderlijke methode en een eigen publicatiegate. Integrale AC04/AC07-acceptatie blijft PENDING.
