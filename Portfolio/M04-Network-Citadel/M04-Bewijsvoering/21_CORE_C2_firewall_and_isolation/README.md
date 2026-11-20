# M04 fase 21 — CORE C2 firewall- en isolatietests (20 november 2026)

**52 gesaneerde weergaven** · PRIVATE originelen niet opgenomen · **M04-CORE: IN PROGRESS**  
**Status:** F09–F12 en F16–F19 **TESTED / scoped PASS**; F13–F15 **PENDING / DESIGN-CONFIRM**; F20/F21 **DESIGN-CONFIRM**; F22/F23 **NO-ROUTE-VERIFIED**; F24 **CONFIG REVIEWED / SAFE LIVE TEST PENDING**; integrale AC04/AC07-matrix **PENDING**.

[Terug naar M04](../../README.md) · [Fasenoverzicht](../README.md) · [Galerij per fase](../../M04-GALERIJ.md) · [Saneringsrapport](M04-PHASE21-SANITIZATION-REPORT.md) · [Bewijsmanifest](M04-EVIDENCE-PHASE21.csv) · [SHA-256](SHA256SUMS.txt)

## Saneringsmethode en bewijsgrenzen

De openbare PNG's zijn afgeleiden van de private originelen. Geselecteerde woordfragmenten zijn overgenomen; de rest is opnieuw gezet met gecontroleerde technische termen, *officiële aliassen uit de private SSOT* of neutrale maskers. IPv4-, IPv6- en MAC-adressen, gebruikersnamen, machine- en segmentnamen, lokale paden en browsercontext zijn afgeschermd. De privéwaarden en koppeltabel worden niet gepubliceerd. Elk beeld is gemarkeerd als **Gesaneerde weergave**; kolommen kunnen daardoor verspringen en technische nevencontext kan ontbreken.

De opnamen staan chronologisch op tijd (CET). Voor Windows-opnamen komt de tijd uit de oorspronkelijke bestandsnaam; voor de overige opnamen is de bijlagetijd een indicatie en kan de werkelijke opname eerder liggen. Tijden die in een log of terminal zichtbaar zijn, horen bij de getoonde gebeurtenis. Test-ID's staan alleen waar de koppeling bevestigd is. Twee bronopnamen zijn byte-identiek (M04-20261120-015 en -016); beide afgeleiden zijn behouden en de hashes gelden voor de openbare afgeleiden.

Een screenshot, een firewallregel en een connectiviteitstime-out zijn ieder afzonderlijk beperkt bewijs. Configuratiebeelden gelden als contextbewijs. De onderliggende originelen blijven in de private repository; publicatie is geen onafhankelijke audit of integrale missie-PASS. [C2-projectlog](../../../../projectlogboeken/2026-11-20-m04-core-c2-netwerkvalidatie.md)

## Bewijsreeks

---

### M04-20261120-001 | 2026-11-20 · LOG

**Onderwerp:** `01-202142-M04-C2.png`  
**Tijd en test-ID:** 20:21:42 CET (bestandsnaam) · —  
**Beschrijving:** pfSense LAN-log met expliciete MGMT-regel voor PLC01/OpenPLC op TCP/8080.  
**Bewijsgrens:** Logweergave van de toegestane beheerregel. TCP-bereikbaarheid is geen authenticatie- of TLS-PASS.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `1ba39b110f58228a36e6aa14124e3e786194e1bc02e741ee59d3a51204b4c52b`

![M04-20261120-001 | LOG](<01-202142-M04-C2.png>)

---

### M04-20261120-002 | 2026-11-20 · LOG

**Onderwerp:** `02-202155-M04-C2.png`  
**Tijd en test-ID:** 20:21:55 CET (bestandsnaam) · F10  
**Beschrijving:** pfSense LAB-log gefilterd op TCP/22 naar PLC01.  
**Bewijsgrens:** Gelogde BLOCK voor het getoonde LAB→PLC01-pakket: F10 **TESTED / scoped PASS**. LAB-bronbinding op leaseniveau en integrale AC04/AC07 open.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `81fe96ab11b6897db07eadc40db7e1a81a6ceb1eec534dfa60bc072bc22b4ad9`

![M04-20261120-002 | LOG](<02-202155-M04-C2.png>)

---

### M04-20261120-003 | 2026-11-20 · LOG

**Onderwerp:** `03-202211-M04-C2.png`  
**Tijd en test-ID:** 20:22:11 CET (bestandsnaam) · F11  
**Beschrijving:** pfSense LAB-log gefilterd op TCP/44818 naar PLC01.  
**Bewijsgrens:** Gelogde BLOCK voor het getoonde LAB→PLC01-pakket: F11 **TESTED / scoped PASS**. Geen listenerbewijs voor TCP/44818; integrale AC04/AC07 open.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `1de68975cc54ff72d976ef879dc1ea5c58edcd8187a1e7496ebe384c10227167`

![M04-20261120-003 | LOG](<03-202211-M04-C2.png>)

---

### M04-20261120-004 | 2026-11-20 · LOG

**Onderwerp:** `04-202252-M04-C2.png`  
**Tijd en test-ID:** 20:22:52 CET (bestandsnaam) · F12  
**Beschrijving:** pfSense LAB-log gefilterd op ICMP naar PLC01. De weergave bevat ook oudere logregels.  
**Bewijsgrens:** Gelogde BLOCK voor het getoonde LAB→PLC01-pakket: F12 **TESTED / scoped PASS**. Oudere logregels in beeld tellen niet als nieuwe waarneming.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `91049b2b77c597f2d195a48565f6276abd9590d03aef69935365046c8c9f9f7b`

![M04-20261120-004 | LOG](<04-202252-M04-C2.png>)

---

### M04-20261120-005 | 2026-11-20 · LOG

**Onderwerp:** `05-203056-M04-C2.png`  
**Tijd en test-ID:** 20:30:56 CET (bijlagetijd, indicatie) · F09  
**Beschrijving:** pfSense LAB-log gefilterd op TCP/8080 naar PLC01.  
**Bewijsgrens:** Gelogde BLOCK voor het getoonde LAB→PLC01-pakket: F09 **TESTED / scoped PASS**. LAB-bronbinding op leaseniveau en integrale AC04/AC07 open.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `e36cd55f0cf55c745aa80d4b2cba59816e1b50eff3c00f73c69908f68d7151e2`

![M04-20261120-005 | LOG](<05-203056-M04-C2.png>)

---

### M04-20261120-006 | 2026-11-20 · CONFIG

**Onderwerp:** `06-205657-M04-C2.png`  
**Tijd en test-ID:** 20:56:57 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** pfSense LAN-regels voor MGMT-toegang tot FUXA01 en PLC01 en de standaardblokkade richting OT.  
**Bewijsgrens:** Configuratiebewijs van de regelvolgorde; geen bewezen end-to-end blokkade.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `9a2c7cb47941a9724ad34c08be17456c49baaee30745ea8728c1b7b7c82e8211`

![M04-20261120-006 | CONFIG](<06-205657-M04-C2.png>)

---

### M04-20261120-007 | 2026-11-20 · TEST

**Onderwerp:** `07-210015-M04-C2.png`  
**Tijd en test-ID:** 21:00:15 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** Lenovo PowerShell met routeringsonderzoek naar een OT-adres.  
**Bewijsgrens:** De directe route naar OT koos de fysieke uplink, niet het beheerpad. Ondersteunt dat F13–F15 **PENDING / DESIGN-CONFIRM** blijven.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `e4d08fd0d86fc6dc64b3974caf95f4f21775807de6430d5b12db5ffac66121eb`

![M04-20261120-007 | TEST](<07-210015-M04-C2.png>)

---

### M04-20261120-008 | 2026-11-20 · CONFIG

**Onderwerp:** `08-210144-M04-C2.png`  
**Tijd en test-ID:** 21:01:44 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** Lenovo PowerShell met adapterstatus, IPv4-adressen en VMnet1-routegegevens.  
**Bewijsgrens:** Momentopname van hostadapters en routes; geen test van een verkeersstroom.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `806c0fb013e5a146ef5f55881e7d7525077e407742fa2f485453550dbf80ac77`

![M04-20261120-008 | CONFIG](<08-210144-M04-C2.png>)

---

### M04-20261120-009 | 2026-11-20 · CONFIG

**Onderwerp:** `09-210341-M04-C2.png`  
**Tijd en test-ID:** 21:03:41 CET (bestandsnaam) · —  
**Beschrijving:** Lenovo PowerShell met netwerkadapters, IPv4-adressen en routetabel.  
**Bewijsgrens:** Momentopname van hostadapters en routes; geen test van een verkeersstroom.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `0a0035b311b8b2c55898a80c4f1a710cb71820a515b984689b1d6897c40c7267`

![M04-20261120-009 | CONFIG](<09-210341-M04-C2.png>)

---

### M04-20261120-010 | 2026-11-20 · TEST

**Onderwerp:** `10-210425-M04-C2.png`  
**Tijd en test-ID:** 21:04:25 CET (bestandsnaam) · —  
**Beschrijving:** Lenovo PowerShell met VMnet1-routering en HTTPS-probe naar pfSense op TCP/443.  
**Bewijsgrens:** Firewallbeheer bereikbaar via het host-only segment; geen authenticatie- of TLS-PASS.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `5f75ac25d0f2332f55eeb07d7a7db8c2a3134cf8fe439884377acec880ed0082`

![M04-20261120-010 | TEST](<10-210425-M04-C2.png>)

---

### M04-20261120-011 | 2026-11-20 · TEST

**Onderwerp:** `11-210949-M04-C2.png`  
**Tijd en test-ID:** 21:09:49 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** Lenovo PowerShell met HTTPS-probe en begin van de poortcontroles richting pfSense.  
**Bewijsgrens:** De probes hebben het firewalladres als bestemming, niet PLC01; geen bewijs voor F13–F15.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `9f86314d572355382503599ae542c1d3f33d1f2b98f4fa3e4294f7a868ec782d`

![M04-20261120-011 | TEST](<11-210949-M04-C2.png>)

---

### M04-20261120-012 | 2026-11-20 · TEST

**Onderwerp:** `12-211033-M04-C2.png`  
**Tijd en test-ID:** 21:10:33 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** Lenovo PowerShell met controles richting pfSense op TCP/502, TCP/22 en TCP/44818.  
**Bewijsgrens:** Negatieve probes naar het firewalladres toetsen een andere bestemming dan PLC01. F13–F15 blijven **PENDING / DESIGN-CONFIRM**.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `c1824eecf0760194eaf646bdb2b65ebbff429a7b55e09784ab2d7aaa70276f16`

![M04-20261120-012 | TEST](<12-211033-M04-C2.png>)

---

### M04-20261120-013 | 2026-11-20 · TROUBLESHOOT

**Onderwerp:** `13-211736-M04-C2.png`  
**Tijd en test-ID:** 21:17:36 CET (bijlagetijd, indicatie) · F16  
**Beschrijving:** PLC01-terminal met route naar MGMT en eerste TCP/8080-poging met shelltypefout.  
**Bewijsgrens:** Shelltypefout; deze poging telt niet mee als testresultaat.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `a8128b60eecfde8ec5e302ba3c093fc4af9e2223f9ab38ed54b7ace5f71714b8`

![M04-20261120-013 | TROUBLESHOOT](<13-211736-M04-C2.png>)

---

### M04-20261120-014 | 2026-11-20 · TEST

**Onderwerp:** `14-212139-M04-C2.png`  
**Tijd en test-ID:** 21:21:39 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** Lenovo PowerShell vergelijkt directe TCP/8080-toegang tot PLC01 met toegang via het pfSense-portforward.  
**Bewijsgrens:** De directe TCP/8080-poging naar `PLC01_OT_IP` mislukt; via het host-only segment en de bronbeperkte beheerforward slaagt TCP/8080. Geen authenticatie- of TLS-PASS; F13–F15 open.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `25d842bfd1871c14adfab6172f80e1fd49344bc7c1f61b8ffb58718b83420b29`

![M04-20261120-014 | TEST](<14-212139-M04-C2.png>)

---

### M04-20261120-015 | 2026-11-20 · CONFIG

**Onderwerp:** `15-212349-M04-C2.png`  
**Tijd en test-ID:** 21:23:49 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** OpenPLC-dashboard van de M04-motorsimulatie met runtimelog en luisterpoorten.  
**Bewijsgrens:** Runtimecontext, geen netwerktest. De bronopname is byte-identiek aan die van M04-20261120-016; geen afzonderlijke waarneming.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `7148497a9fa4b1146f5c2047cd36b6f41d719e71baa4704ea65b951c7c7edc7a`

![M04-20261120-015 | CONFIG](<15-212349-M04-C2.png>)

---

### M04-20261120-016 | 2026-11-20 · CONFIG

**Onderwerp:** `16-212529-M04-C2.png`  
**Tijd en test-ID:** 21:25:29 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** OpenPLC-dashboard van de M04-motorsimulatie met runtimelog en luisterpoorten.  
**Bewijsgrens:** Runtimecontext, geen netwerktest. De bronopname is byte-identiek aan die van M04-20261120-015; geen afzonderlijke waarneming.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `bf5a0c415636b32a35dbf8d2ddfc6c9095e73460d616c7832edf5a3cbf09df96`

![M04-20261120-016 | CONFIG](<16-212529-M04-C2.png>)

---

### M04-20261120-017 | 2026-11-20 · TEST

**Onderwerp:** `17-213639-M04-C2.png`  
**Tijd en test-ID:** 21:36:39 CET (bijlagetijd, indicatie) · F16  
**Beschrijving:** PLC01-terminal met herhaalde route- en TCP/8080-probes richting MGMT.  
**Bewijsgrens:** Een time-out alleen is geen blokkadebewijs. Samen met de OT-log (M04-20261120-020) ondersteunt dit F16.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `9c5ba0808427ab91df80fb66342a32e17759152771f1c808a52d366d8619294b`

![M04-20261120-017 | TEST](<17-213639-M04-C2.png>)

---

### M04-20261120-018 | 2026-11-20 · TEST

**Onderwerp:** `18-213923-M04-C2.png`  
**Tijd en test-ID:** 21:39:23 CET (bijlagetijd, indicatie) · F16  
**Beschrijving:** PLC01-terminal met TCP/8080-probe richting MGMT en zichtbare exitcode.  
**Bewijsgrens:** Een time-out alleen is geen blokkadebewijs. Samen met de OT-log (M04-20261120-020) ondersteunt dit F16.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `3ac7e4e9b52f04c6224db51f4c62ffe39e1d2219f432d3d7efa1bd3d658b134d`

![M04-20261120-018 | TEST](<18-213923-M04-C2.png>)

---

### M04-20261120-019 | 2026-11-20 · TEST

**Onderwerp:** `19-214037-M04-C2.png`  
**Tijd en test-ID:** 21:40:37 CET (bijlagetijd, indicatie) · F16  
**Beschrijving:** PLC01-terminal met herhaalde TCP/8080-probes richting MGMT en controle van de OpenPLC-service.  
**Bewijsgrens:** Een time-out alleen is geen blokkadebewijs. Samen met de OT-log (M04-20261120-020) ondersteunt dit F16.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `5fcac14962478f2da1d13e3f8845076d62bc07c7f1e7c3a0d253c4a3ebf49dde`

![M04-20261120-019 | TEST](<19-214037-M04-C2.png>)

---

### M04-20261120-020 | 2026-11-20 · LOG

**Onderwerp:** `20-214259-M04-C2.png`  
**Tijd en test-ID:** 21:42:59 CET (bijlagetijd, indicatie) · F16  
**Beschrijving:** pfSense OT-log gefilterd op TCP/8080 met standaardblokkades richting MGMT.  
**Bewijsgrens:** Gelogde default-deny op de OT-ingress voor de getoonde flow: F16 **TESTED / scoped PASS**. Geen volledige OT→MGMT-garantie.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `6cdb2dcd7b3a9226d29bdc94fddb444f8cc8875cf68e3eda0f9ae3da2639a656`

![M04-20261120-020 | LOG](<20-214259-M04-C2.png>)

---

### M04-20261120-021 | 2026-11-20 · TEST

**Onderwerp:** `21-215540-M04-C2.png`  
**Tijd en test-ID:** 21:55:40 CET (bijlagetijd, indicatie) · F17  
**Beschrijving:** FUXA01-terminal met routecontrole ter voorbereiding op de TCP/443-probe richting MGMT.  
**Bewijsgrens:** Voorbereidende routecontrole; geen testresultaat.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `c967a939d15d7be95c8a76efefe3a8f17149e95242bb447e1741facada837665`

![M04-20261120-021 | TEST](<21-215540-M04-C2.png>)

---

### M04-20261120-022 | 2026-11-20 · LOG

**Onderwerp:** `22-220225-M04-C2.png`  
**Tijd en test-ID:** 22:02:25 CET (bijlagetijd, indicatie) · F17  
**Beschrijving:** pfSense OT-logfilter voor TCP/443 met nul overeenkomende regels in deze opname.  
**Bewijsgrens:** Nul overeenkomende regels in deze opname; op zichzelf geen blokkadebewijs.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `5054451583509dd0fb02a3e2d609468f41ed0f28e7b96aa33f6c426f8da866b4`

![M04-20261120-022 | LOG](<22-220225-M04-C2.png>)

---

### M04-20261120-023 | 2026-11-20 · TROUBLESHOOT

**Onderwerp:** `23-220340-M04-C2.png`  
**Tijd en test-ID:** 22:03:40 CET (bijlagetijd, indicatie) · F17  
**Beschrijving:** FUXA01-terminal met route en eerste TCP/443-pogingen met shellsyntaxisfout.  
**Bewijsgrens:** Shellsyntaxisfout; deze pogingen tellen niet mee. F17 gebruikt de daaropvolgende geldige HTTPS-probe (M04-20261120-024).  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `b6e8861f9f444766b324a3d7ffb2f76a9f6d390e6740102d9b61ac5d653ea72e`

![M04-20261120-023 | TROUBLESHOOT](<23-220340-M04-C2.png>)

---

### M04-20261120-024 | 2026-11-20 · TEST

**Onderwerp:** `24-220515-M04-C2.png`  
**Tijd en test-ID:** 22:05:15 CET (bijlagetijd, indicatie) · F17  
**Beschrijving:** FUXA01-terminal met HTTPS-probe richting pfSense MGMT op TCP/443 en de weergegeven time-out.  
**Bewijsgrens:** Time-out van de geldige HTTPS-probe. Samen met de OT-log (M04-20261120-025) ondersteunt dit F17; het beheerbeleid voor pfSense staat ter eigenaarreview.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `1737f97deff4468b302078093954530ae1cb7496520947fc9fb5f37fec958149`

![M04-20261120-024 | TEST](<24-220515-M04-C2.png>)

---

### M04-20261120-025 | 2026-11-20 · LOG

**Onderwerp:** `25-220617-M04-C2.png`  
**Tijd en test-ID:** 22:06:17 CET (bijlagetijd, indicatie) · F17  
**Beschrijving:** pfSense OT-log met TCP/443-regels voor de FUXA01-probe richting pfSense MGMT.  
**Bewijsgrens:** Gelogde BLOCK voor de getoonde flow: F17 **TESTED / scoped PASS**. Het beheerbeleid voor pfSense staat ter eigenaarreview.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `f09fa40faffd1dc508f4878e8485148adbc2def2353b09c9f323064436cfdebd`

![M04-20261120-025 | LOG](<25-220617-M04-C2.png>)

---

### M04-20261120-026 | 2026-11-20 · TEST

**Onderwerp:** `26-220814-M04-C2.png`  
**Tijd en test-ID:** 22:08:14 CET (bijlagetijd, indicatie) · F18  
**Beschrijving:** PLC01-terminal met TCP/22-probe richting pfSense OT en de weergegeven time-out.  
**Bewijsgrens:** Time-out alleen is geen blokkadebewijs. Samen met de OT-log (M04-20261120-027) ondersteunt dit F18; het SSH-beleid voor pfSense staat ter eigenaarreview.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `e6be3cb85a78e478fb0113221460dc219a910f6bcfe4b157331a96767bb12ada`

![M04-20261120-026 | TEST](<26-220814-M04-C2.png>)

---

### M04-20261120-027 | 2026-11-20 · LOG

**Onderwerp:** `27-220959-M04-C2.png`  
**Tijd en test-ID:** 22:09:59 CET (bijlagetijd, indicatie) · F18  
**Beschrijving:** pfSense OT-log met TCP/22-regels voor de PLC01-probe richting pfSense OT.  
**Bewijsgrens:** Gelogde BLOCK voor de getoonde flow: F18 **TESTED / scoped PASS**. Het SSH-beleid voor pfSense staat ter eigenaarreview.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `643970f60b1fda1a2d4929e7234b851ca55aa4b010bb657bc37f35aed7f3dad9`

![M04-20261120-027 | LOG](<27-220959-M04-C2.png>)

---

### M04-20261120-028 | 2026-11-20 · TEST

**Onderwerp:** `28-221211-M04-C2.png`  
**Tijd en test-ID:** 22:12:11 CET (bijlagetijd, indicatie) · F19  
**Beschrijving:** PLC01-terminal met HTTP-probe naar een externe bestemming op TCP/80.  
**Bewijsgrens:** Time-out alleen is geen blokkadebewijs. Samen met de OT-log (M04-20261120-029) ondersteunt dit F19.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `db97cacc5f738e56072b8df539cd3c40854ece73e95c99cb8ec30819b7599c4e`

![M04-20261120-028 | TEST](<28-221211-M04-C2.png>)

---

### M04-20261120-029 | 2026-11-20 · LOG

**Onderwerp:** `29-221308-M04-C2.png`  
**Tijd en test-ID:** 22:13:08 CET (bijlagetijd, indicatie) · F19  
**Beschrijving:** pfSense OT-log met TCP/80-regels bij de externe HTTP-probe.  
**Bewijsgrens:** Gelogde BLOCK voor de getoonde bestemming: F19 **TESTED / scoped PASS**. Geen garantie voor andere bestemmingen of protocollen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `ddc2e46b3fdb8b9a270e2be0844c46244871a00ddd4d858ee55ee58e2f87c3b6`

![M04-20261120-029 | LOG](<29-221308-M04-C2.png>)

---

### M04-20261120-030 | 2026-11-20 · TEST

**Onderwerp:** `30-221528-M04-C2.png`  
**Tijd en test-ID:** 22:15:28 CET (bijlagetijd, indicatie) · F20  
**Beschrijving:** PLC01-terminal met externe DNS-query op UDP/53 en de weergegeven time-out.  
**Bewijsgrens:** DNS-time-out in de getoonde proef. De goedgekeurde resolver is een ontwerpbesluit: F20 **DESIGN-CONFIRM**.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `66037fc5dad74e5548feb44931b5d79ec25f747524af90dbf80c98de9d40cebb`

![M04-20261120-030 | TEST](<30-221528-M04-C2.png>)

---

### M04-20261120-031 | 2026-11-20 · LOG

**Onderwerp:** `31-221808-M04-C2.png`  
**Tijd en test-ID:** 22:18:08 CET (bijlagetijd, indicatie) · F20  
**Beschrijving:** pfSense OT-log met de UDP/53-regel bij de externe DNS-query.  
**Bewijsgrens:** BLOCK waargenomen voor de getoonde DNS-query. F20 blijft **DESIGN-CONFIRM**: het toegestane DNS-ontwerp is nog niet vastgesteld.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `93f6be40c4a9816af123e595aaa91697a610aac32984a0486b7c55d0561ccb6d`

![M04-20261120-031 | LOG](<31-221808-M04-C2.png>)

---

### M04-20261120-032 | 2026-11-20 · TEST

**Onderwerp:** `32-222911-M04-C2.png`  
**Tijd en test-ID:** 22:29:11 CET (bijlagetijd, indicatie) · F21  
**Beschrijving:** FUXA01-terminal met routecontrole en probe naar een externe NTP-bestemming op UDP/123.  
**Bewijsgrens:** UDP kent geen verbindingshandshake; een netcat-succesmelding zonder NTP-antwoord bewijst geen bereikbaarheid. F21 **DESIGN-CONFIRM**.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `363d7f9f11f9c07ee52f3f8159a64309d87f9478597a2bbc31ad56115d342870`

![M04-20261120-032 | TEST](<32-222911-M04-C2.png>)

---

### M04-20261120-033 | 2026-11-20 · LOG

**Onderwerp:** `33-223646-M04-C2.png`  
**Tijd en test-ID:** 22:36:46 CET (bijlagetijd, indicatie) · F21  
**Beschrijving:** pfSense OT-log met UDP/123-regels bij de externe NTP-probe.  
**Bewijsgrens:** BLOCK waargenomen voor de getoonde NTP-probe. F21 blijft **DESIGN-CONFIRM**: de goedgekeurde tijdbron is nog niet vastgesteld.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `63664cb2dc33c90579d4785ce043890781c55a93d6cddc67b8ac58e5d153f25f`

![M04-20261120-033 | LOG](<33-223646-M04-C2.png>)

---

### M04-20261120-034 | 2026-11-20 · CONFIG

**Onderwerp:** `34-224123-M04-C2.png`  
**Tijd en test-ID:** 22:41:23 CET (bijlagetijd, indicatie) · F23  
**Beschrijving:** FUXA01-terminal met IPv6-adressen en routes op de interfaces. Ondersteunende configuratiecontrole.  
**Bewijsgrens:** Ondersteunt **NO-ROUTE-VERIFIED** binnen de geïnspecteerde topologie; geen IPv6-firewall-PASS. De brede LAN IPv6-allow en alternatieve paden blijven onder review.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `d0f2e4a0284090a43af2df2e0d083d60e49006a8fd9ac2ab4cc3ecfa3ed60c74`

![M04-20261120-034 | CONFIG](<34-224123-M04-C2.png>)

---

### M04-20261120-035 | 2026-11-20 · CONFIG

**Onderwerp:** `35-224141-M04-C2.png`  
**Tijd en test-ID:** 22:41:41 CET (bijlagetijd, indicatie) · F22  
**Beschrijving:** PLC01-terminal met IPv6-adressen en routes op de OT-interface. Ondersteunende configuratiecontrole.  
**Bewijsgrens:** Ondersteunt **NO-ROUTE-VERIFIED** binnen de geïnspecteerde topologie; geen IPv6-firewall-PASS. De brede LAN IPv6-allow en alternatieve paden blijven onder review.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `567d6b1363276cc854aa6eaa20778156737548a3e1a61d43367a33c0e44d3710`

![M04-20261120-035 | CONFIG](<35-224141-M04-C2.png>)

---

### M04-20261120-036 | 2026-11-20 · CONFIG

**Onderwerp:** `36-224331-M04-C2.png`  
**Tijd en test-ID:** 22:43:31 CET (bijlagetijd, indicatie) · F22, F23  
**Beschrijving:** pfSense-interfaceoverzicht met IPv6-link-local-adressen. Ondersteunende configuratiecontrole.  
**Bewijsgrens:** Ondersteunt **NO-ROUTE-VERIFIED** binnen de geïnspecteerde topologie; geen IPv6-firewall-PASS. De brede LAN IPv6-allow en alternatieve paden blijven onder review.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `02895d9c0c498b5058ff7737e22c15d499a1cbb843a8bbbd2c6be0be3f923784`

![M04-20261120-036 | CONFIG](<36-224331-M04-C2.png>)

---

### M04-20261120-037 | 2026-11-20 · CONFIG

**Onderwerp:** `37-224748-M04-C2.png`  
**Tijd en test-ID:** 22:47:48 CET (bijlagetijd, indicatie) · F23  
**Beschrijving:** Lenovo PowerShell met IPv6-adressen en IPv6-routes voor VMware- en hostinterfaces. Ondersteunende configuratiecontrole.  
**Bewijsgrens:** Ondersteunt **NO-ROUTE-VERIFIED** binnen de geïnspecteerde topologie; geen IPv6-firewall-PASS. De brede LAN IPv6-allow en alternatieve paden blijven onder review.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `a5a92f55fd1350f6842b15806a26315abca10b996bcd96fb10268ace22ecfbe6`

![M04-20261120-037 | CONFIG](<37-224748-M04-C2.png>)

---

### M04-20261120-038 | 2026-11-20 · CONFIG

**Onderwerp:** `38-225013-M04-C2.png`  
**Tijd en test-ID:** 22:50:13 CET (bijlagetijd, indicatie) · F23  
**Beschrijving:** Lenovo PowerShell met IPv6-routes en een gerichte controle op de IPv6-default route. Ondersteunende configuratiecontrole.  
**Bewijsgrens:** Ondersteunt **NO-ROUTE-VERIFIED** binnen de geïnspecteerde topologie; geen IPv6-firewall-PASS. De brede LAN IPv6-allow en alternatieve paden blijven onder review.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `66e51248d3fc5310d19dfc9c257597925377250723678809081c459306b26587`

![M04-20261120-038 | CONFIG](<38-225013-M04-C2.png>)

---

### M04-20261120-039 | 2026-11-20 · CONFIG

**Onderwerp:** `39-225428-M04-C2.png`  
**Tijd en test-ID:** 22:54:28 CET (bijlagetijd, indicatie) · F22  
**Beschrijving:** CLIENT01 PowerShell met inventarisatie van IPv6-adressen en routes. Ondersteunende configuratiecontrole.  
**Bewijsgrens:** Ondersteunt **NO-ROUTE-VERIFIED** binnen de geïnspecteerde topologie; geen IPv6-firewall-PASS. De brede LAN IPv6-allow en alternatieve paden blijven onder review.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `d78b67a6c9e7436fb07e3c1806923a135ca7b342ac35c5661afd2c959974f66e`

![M04-20261120-039 | CONFIG](<39-225428-M04-C2.png>)

---

### M04-20261120-040 | 2026-11-20 · CONFIG

**Onderwerp:** `40-225624-M04-C2.png`  
**Tijd en test-ID:** 22:56:24 CET (bijlagetijd, indicatie) · F22  
**Beschrijving:** CLIENT01 PowerShell met IPv6-routegegevens en controle van de default gateway. Ondersteunende configuratiecontrole.  
**Bewijsgrens:** Ondersteunt **NO-ROUTE-VERIFIED** binnen de geïnspecteerde topologie; geen IPv6-firewall-PASS. De brede LAN IPv6-allow en alternatieve paden blijven onder review.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `02f0767b111314b6a328ccfaad14f214d65fe920c8c286384b4da4f04f33617a`

![M04-20261120-040 | CONFIG](<40-225624-M04-C2.png>)

---

### M04-20261120-041 | 2026-11-20 · CONFIG

**Onderwerp:** `41-230005-M04-C2.png`  
**Tijd en test-ID:** 23:00:05 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** VMware-instellingen van een OT-VM met de netwerkadapter op het geïsoleerde OT LAN Segment.  
**Bewijsgrens:** Adaptertoewijzing in VMware; ondersteunt gescheiden L2-segmenten, maar is geen firewall- of verkeerstest.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `491d5e4fa45c1b240bf6c9b90d6a4cc6363f91a6d8d17803ed62ede40ad56cca`

![M04-20261120-041 | CONFIG](<41-230005-M04-C2.png>)

---

### M04-20261120-042 | 2026-11-20 · CONFIG

**Onderwerp:** `42-230206-M04-C2.png`  
**Tijd en test-ID:** 23:02:06 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** VMware-instellingen van een OT-VM met de netwerkadapter op het geïsoleerde OT LAN Segment.  
**Bewijsgrens:** Adaptertoewijzing in VMware; ondersteunt gescheiden L2-segmenten, maar is geen firewall- of verkeerstest.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `2e3627660f100683cc2375d29b92d3ada8af84a777fa7b8013b372849300b7a0`

![M04-20261120-042 | CONFIG](<42-230206-M04-C2.png>)

---

### M04-20261120-043 | 2026-11-20 · CONFIG

**Onderwerp:** `43-230312-M04-C2.png`  
**Tijd en test-ID:** 23:03:12 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** VMware-instellingen van de Windows-test-VM met de netwerkadapter op het geïsoleerde LAB LAN Segment.  
**Bewijsgrens:** Adaptertoewijzing in VMware; ondersteunt gescheiden L2-segmenten, maar is geen firewall- of verkeerstest.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `cfe638f78e29fde61c596cc0ab9f042e6f14c1d1a0c4953ead3443e89fc48549`

![M04-20261120-043 | CONFIG](<43-230312-M04-C2.png>)

---

### M04-20261120-044 | 2026-11-20 · CONFIG

**Onderwerp:** `44-230949-M04-C2.png`  
**Tijd en test-ID:** 23:09:49 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** VMware-instellingen van pfSense met adapter 3 op het geïsoleerde LAB LAN Segment.  
**Bewijsgrens:** Adaptertoewijzing in VMware; ondersteunt gescheiden L2-segmenten, maar is geen firewall- of verkeerstest.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `e83c79e464c05c64e96bd5c1d41e283e80e649121e410f71c02d9a1a4565e317`

![M04-20261120-044 | CONFIG](<44-230949-M04-C2.png>)

---

### M04-20261120-045 | 2026-11-20 · CONFIG

**Onderwerp:** `45-231003-M04-C2.png`  
**Tijd en test-ID:** 23:10:03 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** VMware-instellingen van pfSense met adapter 4 op het geïsoleerde OT LAN Segment.  
**Bewijsgrens:** Adaptertoewijzing in VMware; ondersteunt gescheiden L2-segmenten, maar is geen firewall- of verkeerstest.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `b98257aef962a0a154a55dcdbe24891aea54b4d1e66d636227d93ad539474357`

![M04-20261120-045 | CONFIG](<45-231003-M04-C2.png>)

---

### M04-20261120-046 | 2026-11-20 · CONFIG

**Onderwerp:** `46-231221-M04-C2.png`  
**Tijd en test-ID:** 23:12:21 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** pfSense WAN-regeloverzicht met bogon-blokkade en het overzicht van gebruikersregels.  
**Bewijsgrens:** Configuratiereview van de WAN-zijde; een veilige live WAN→OT-proef blijft open.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `bdf4cfb63e100a2c59770e883c4a65a8f0e11d9a659060712e98055f973544f7`

![M04-20261120-046 | CONFIG](<46-231221-M04-C2.png>)

---

### M04-20261120-047 | 2026-11-20 · CONFIG

**Onderwerp:** `47-231638-M04-C2.png`  
**Tijd en test-ID:** 23:16:38 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** pfSense IPv4-portforwards vanaf MGMT naar de webinterfaces van FUXA01 en PLC01.  
**Bewijsgrens:** Configuratie van de bronbeperkte beheerforwards; geen end-to-end test en geen authenticatie- of TLS-PASS.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `cbde6f80305a70ea17d574c86add6fa712e36357ed99398dc4556298ebfec6f7`

![M04-20261120-047 | CONFIG](<47-231638-M04-C2.png>)

---

### M04-20261120-048 | 2026-11-20 · CONFIG

**Onderwerp:** `48-232137-M04-C2.png`  
**Tijd en test-ID:** 23:21:37 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** pfSense LAN-regeloverzicht met expliciete MGMT-toegang, OT-blokkade en LAN-defaultregels.  
**Bewijsgrens:** Configuratiebewijs van de regelvolgorde. De brede LAN IPv4-/IPv6-allows blijven onder review; geen bewezen end-to-end blokkade.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `cdb7ad1d3e6b06abfdbbf1fb37e63f52fb4a16391c03c8b72679e020a47310ab`

![M04-20261120-048 | CONFIG](<48-232137-M04-C2.png>)

---

### M04-20261120-049 | 2026-11-20 · CONFIG

**Onderwerp:** `49-232226-M04-C2.png`  
**Tijd en test-ID:** 23:22:26 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** pfSense NAT-overzicht met MGMT-portforwards voor FUXA01 en PLC01.  
**Bewijsgrens:** Configuratie van de bronbeperkte beheerforwards; geen end-to-end test.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `f637e11272ce9b7430926ed8fbfb09c1bf3cd8ac91256273ed96488ed522ad6f`

![M04-20261120-049 | CONFIG](<49-232226-M04-C2.png>)

---

### M04-20261120-050 | 2026-11-20 · CONFIG

**Onderwerp:** `50-232340-M04-C2.png`  
**Tijd en test-ID:** 23:23:40 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** pfSense IPv4- en IPv6-routetabellen.  
**Bewijsgrens:** Routetabel als configuratiecontext; geen verkeerstest.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `4a1d59af8134abc2270f9a368e1279b403462291288bcc90b981b91fa1ac8811`

![M04-20261120-050 | CONFIG](<50-232340-M04-C2.png>)

---

### M04-20261120-051 | 2026-11-20 · CONFIG

**Onderwerp:** `51-232554-M04-C2.png`  
**Tijd en test-ID:** 23:25:54 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** pfSense IP-aliasoverzicht met de RFC1918-netwerkgroep.  
**Bewijsgrens:** Aliasobject als configuratiecontext; zegt niets over matchend verkeer.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `98644675889012ff28ccee640f68a7708aa2d7cad0b791bc88b80d054d86d56f`

![M04-20261120-051 | CONFIG](<51-232554-M04-C2.png>)

---

### M04-20261120-052 | 2026-11-20 · CONFIG

**Onderwerp:** `52-232729-M04-C2.png`  
**Tijd en test-ID:** 23:27:29 CET (bijlagetijd, indicatie) · —  
**Beschrijving:** pfSense-editor voor de IPv4-regel M04 LAN → OT default deny.  
**Bewijsgrens:** Regeldefinitie; op zichzelf geen bewijs van matchend verkeer.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `13ea28acb7aeff921d364d89df457dcfd3fc2d96b22dfe04079279886a66c298`

![M04-20261120-052 | CONFIG](<52-232729-M04-C2.png>)
