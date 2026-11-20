# M01 | Saneringsrapport en publicatieverantwoording

**Datum migratie:** 17 november 2026  
**Bron:** private repository, map `Portfolio/M01-Hypervisor-Fortress` (alleen gelezen, niets gewijzigd)  
**Doel:** `Portfolio/M01-Hypervisor-Fortress/` in deze publieke repository  
**Principe:** maximale technische transparantie, geen gevoelige blootstelling. Bij twijfel is gemaskeerd.

## 1. Werkwijze

1. **Alleen lezen uit de private bron.** Originelen zijn niet gewijzigd, verplaatst of gecommit. De sanering is buiten beide repositories uitgevoerd.
2. **Automatische detectie per beeld.** Elk beeld is vergroot en met Tesseract OCR gelezen in vier kleurvarianten. Elk woord is getoetst op IP-, IPv6-, MAC- en hexidentifiers (UUID, machine-ID), `user@host`-prompts, e-mailadressen, gebruikers- en hostnamen, lokale paden, VM-namen, hypervisorsleutels (`ethernet*.address`, `uuid.*`, `extendedConfigFile` en vergelijkbare) en serie- en productnummers. Regels met een gebruikerspad, machine-ID, UUID, MAC-sleutel of wachtwoordprompt zijn vanaf de trigger tot het einde van de regel gemaskeerd.
3. **Onomkeerbare maskering.** Gevonden gebieden zijn gevuld met een ondoorzichtig vlak, niet geblurd of gepixeleerd. In het vlak staat een `REDACTED_*`-label of niets.
4. **Individuele visuele inspectie.** Alle 82 resultaten zijn één voor één bekeken. Tien beelden zijn byte-identiek aan beelden uit de eerder gepubliceerde [M04-set](../M04-Network-Citadel/) en hebben daar dezelfde behandeling gekregen. Waar OCR iets miste, is een handmatig masker toegevoegd: in **19 beelden 22 extra maskers**. Voorbeelden:
   - **Hostname:** de apparaatnaam van de host, zowel in de fabrikant-app als in Instellingen > Systeem > Info.
   - **Hardware-identificatie:** het productnummer van de host.
   - **Account:** de lokale accountnaam en het accounttype in Instellingen, op drie beelden.
   - **Persoonlijke mapnamen** in het navigatiepaneel van de Verkenner, op twee beelden.
   - **VM-namen** in venstertitels en dialoogkoppen.
   - **Pad- en VM-naamfragmenten** in `.vmdk`-velden.
   - **IP-fragmenten** van een pfSense-console die achter een wizard zichtbaar is.
5. **Metadata verwijderd.** Elk beeld is opnieuw opgeslagen als RGB-PNG zonder tekst- of EXIF-chunks.
6. **Tekst gesaneerd.**
   - Index en GAP-analyse zijn overgezet. VM-namen zijn vervangen door de logische namen uit de publieke architectuurdocumentatie: CLIENT01, DC01, FUXA01, WAZUH01, PLC01, pfSense, GNS3.
   - Lokale paden en persoonlijke mapnamen zijn `REDACTED_*` geworden.
   - De hashes van de private originelen zijn vervangen door hashes van de publieke afgeleiden.
7. **Controle achteraf.**
   - De definitieve beelden zijn opnieuw met OCR gescand.
   - Alle tekstbestanden zijn gescand op adressen, private hashes, VM-namen, paden en de hostname.
   - De al gepubliceerde M04-set is aanvullend gescand op de hostname, omdat die niet in de oorspronkelijke M04-zoekpatronen stond. Resultaat: **0 treffers**.

## 2. Overgebrachte bestanden

| Bestand | Behandeling |
|---|---|
| `M01-Bewijsvoering/` (82 PNG) | Gesaneerde afgeleiden; 58 beelden met automatische en/of handmatige maskers, in totaal 2971 maskervakken |
| `EVIDENCE-INDEX.md` | Gesaneerd: VM-namen naar logische namen, paden geredigeerd, statuskop en leeswijzer aangepast aan publicatie |
| `GAP-ANALYSE.md` | Gesaneerd overgezet; inhoudelijke bevindingen ongewijzigd |
| `MANIFEST_SHA256.txt` | Nieuw: alleen hashes van de publieke afgeleiden |
| `README.md` | Nieuw opgesteld voor publicatie |
| `M01-SANITIZATION-REPORT.md` | Dit rapport |

## 3. Toegepaste maskeringen per categorie

| Label in beeld | Aantal |
|---|---:|
| `REDACTED` | 1142 |
| `REDACTED_ID` | 623 |
| `REDACTED_USER@HOST` | 399 |
| `REDACTED_LINE (regel vanaf trigger)` | 384 |
| `REDACTED_IP` | 291 |
| `REDACTED_IPV6` | 54 |
| `REDACTED_MAC_LINE` | 34 |
| `REDACTED_USER` | 16 |
| `REDACTED (zonder label)` | 6 |
| `REDACTED_MAC` | 6 |
| `REDACTED_VM` | 4 |
| `REDACTED_PATH` | 3 |
| `REDACTED_HOSTNAME` | 3 |
| `REDACTED_ACCOUNT` | 3 |
| `REDACTED_PERSONAL_FOLDERS` | 2 |
| `REDACTED_PRODUCT_NO` | 1 |

*Aantallen zijn OCR-vakken plus handmatige vlakken. Eén zichtbare waarde kan door meerdere OCR-varianten overlappend gemaskeerd zijn.*

## 4. Uitgesloten of niet overgenomen

| Item | Reden |
|---|---|
| 82 private originele PNG's | Alleen gesaneerde afgeleiden gepubliceerd |
| Bron-`README.md` | Vervangen door een publieke versie; de private versie beschrijft private branches, importprocedures en waarschuwingen over ruwe inhoud |
| `IMPORT-VERIFICATION-2026-11-15.md` | Niet overgenomen: private importprocedure (private PR's, ZIP-herkomst, Git-blobcontroles op de originelen) zonder publieke bewijswaarde |
| `M01-Bewijsvoering/README.md` | Niet overgenomen; de map wordt beschreven in de publieke README |
| Private originele SHA-256-waarden | Vervangen; zouden de private bron herleidbaar maken |

Er is **geen** M01-screenshot volledig uitgesloten.

## 5. Restrisico's en bewuste keuzes

- **OCR-afhankelijkheid.** Alle beelden zijn op schermresolutie geïnspecteerd, maar niet elk beeld pixel voor pixel. Zeer kleine of afgesneden tekst kan theoretisch een fragment bevatten.
- **Hypervisorconfiguratie (#063, `.vmx`).** Sleutelnamen zoals `cpuid.1.eax`, `featureCompat.enable = FALSE`, `tools.syncTime`, `pciBridge*` blijven zichtbaar als technisch bewijs. Waarden die een machine kunnen identificeren zijn gemaskeerd, net als de cpuid-maskerwaarden zelf. Dat laatste is bewust voorzichtig: de waarden zijn generiek, maar de opdracht noemde hypervisorconfiguratie expliciet als gevoelig.
- **Overmaskering.** Windows-versie- en buildreeksen in terminaluitvoer (patroon lijkt op een IP-adres), de SHA-256 van installatiemedia en hele promptregels met een gebruikerspad zijn gemaskeerd. De opgegeven commando's zijn daardoor niet altijd leesbaar; de index beschrijft ze wel.
- **Bewust zichtbaar gelaten:**
  - de hardwareconfiguratie van de host (CPU-model, RAM, BIOS-versie, SSD-model zonder serienummer, apparaatmodel);
  - de Windows-editie, versie en build in Instellingen;
  - KB-nummers, snapshotnamen (`POST-AD-DC01`) en de VMware-instellingen per VM;
  - `127.0.0.1:912`;
  - ISO-bestandsnamen van publieke producten.
- **Observatie voor de eigenaar (geen wijziging aangebracht).** Beeld #057 toont naast de mislukte `.crdownload`-poging ook een **geslaagde** `Get-FileHash`-berekening op het voltooide `wazuh-4.14.9.ova`-bestand. De GAP-analyse zegt dat die hash ontbreekt. De hashwaarde is in de publieke versie gemaskeerd. Inhoudelijke herbeoordeling ligt bij de eigenaar.
- **Interpretatie.** De publicatie verandert geen controlstatus. HV-01, HV-03 en HV-04 (gedeeltelijk) blijven onbewezen of PENDING; er is geen volledige M01-PASS.
- **Publicatiegate.** Deze migratie staat op een aparte branch met een pull request. **Niet automatisch mergen.**
