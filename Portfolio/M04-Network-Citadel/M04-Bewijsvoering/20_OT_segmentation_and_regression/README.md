# M04 fase 20 — OT-segmentatie en regressietests (19 november 2026)

**55 gesaneerde screenshots** · PRIVATE originelen niet opgenomen · **M04-CORE: IN PROGRESS**  
**Status:** AC01–AC03 functionele deeltests binnen gerapporteerde scope; integrale AC04/AC07-matrix **PENDING**.

[Terug naar M04](../README.md) · [Galerij per fase](../M04-GALERIJ.md) · [Saneringsrapport](M04-PHASE20-SANITIZATION-REPORT.md)

## Saneringsmethode en bewijsgrenzen

Echte IP-adressen, MAC-adressen en identificerende gebruikers-/hostgegevens zijn onomkeerbaar vervangen door *officiële aliassen uit de private SSOT* of, waar geen gevalideerde mapping bestaat, `REDACTED_*`. De privéwaarden en koppeltabel worden niet gepubliceerd. Overige configuratie, testuitvoer en firewallacties blijven zoveel mogelijk leesbaar. Alle screenshots zijn nieuwe publieke RGB-PNG-bestanden zonder metadata.

Een screenshot, een firewallregel en een connectiviteitstimeout zijn ieder afzonderlijk beperkt bewijs. De onderliggende originelen blijven in de private repository; publicatie is geen onafhankelijke audit of integrale missie-PASS.

## Bewijsreeks

---

### M04-20261119-001 | 2026-11-19 · LOG

**Onderwerp:** `Screenshot 2026-11-19 205046.png`  
**Beschrijving:** pfSense-firewalllog filtert LAB→PLC01-verkeer en toont geblokkeerde TCP/502-pogingen na een regelwijziging.  
**Bewijsgrens:** Beperkt bewijs van een deny op dit bron-doelpaar; geen volledige AC04-acceptatie.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `6a14d39679f5ee1755f7f541e247208ee63ca4913c8578e0d905d9d555b8bb00`

![M04-20261119-001 | LOG](<Screenshot 2026-11-19 205046.png>)

---

### M04-20261119-002 | 2026-11-19 · LOG

**Onderwerp:** `Screenshot 2026-11-19 205131.png`  
**Beschrijving:** pfSense-firewalllog filtert LAB→FUXA01-verkeer en toont geblokkeerde verbindingen na de wijziging.  
**Bewijsgrens:** Beperkt bewijs van blokkades op de getoonde verbindingen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `516cef3741a950d77c7b43e1a59aeac99a42688c8e04ef0f7421039a2b579100`

![M04-20261119-002 | LOG](<Screenshot 2026-11-19 205131.png>)

---

### M04-20261119-003 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-175850).png`  
**Beschrijving:** FUXA-verbindingsoverzicht toont de PLC01-motorverbinding met een gele statusindicator.  
**Bewijsgrens:** Beginsituatie; de betekenis van de status moet niet als succesvolle verbinding worden aangenomen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `264dca8b53dacf512fede1f0d1c46684e8cb97e5b71112b9b80f76378f81bfb6`

![M04-20261119-003 | CONFIG](<image(20261119-175850).png>)

---

### M04-20261119-004 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** `image(20261119-180020).png`  
**Beschrijving:** FUXA-venster Connection Property toont Modbus TCP-instellingen en een rode indicator voor de PLC-verbinding.  
**Bewijsgrens:** Configuratie en verbindingsprobleem zichtbaar; geen PASS.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `45d744bb6958731fbe5ac1bc36e23985b58a5861dcdf23f476f4c4b64308764a`

![M04-20261119-004 | TROUBLESHOOT](<image(20261119-180020).png>)

---

### M04-20261119-005 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-180132).png`  
**Beschrijving:** OpenPLC-webinterface toont de runtime in gestopte toestand.  
**Bewijsgrens:** Startstatus van de PLC, geen actief proces.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `bfdca3db726fc2e3dc65231d25671e5af8afc642715b3f7361262b33c9e52d23`

![M04-20261119-005 | CONFIG](<image(20261119-180132).png>)

---

### M04-20261119-006 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-180210).png`  
**Beschrijving:** OpenPLC-dashboard toont de runtime na starten met een draaiende status.  
**Bewijsgrens:** Runtime draait; HMI-verkeer is daarmee nog niet bewezen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `d8800afad0fc4a1881cec40fbf508bdd5d1a7d867d83f113a270df487cafc1e4`

![M04-20261119-006 | CONFIG](<image(20261119-180210).png>)

---

### M04-20261119-007 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-180325).png`  
**Beschrijving:** FUXA toont de tags Motor_Start en Motor_Running met de op dat moment uitgelezen waarden.  
**Bewijsgrens:** Een tagoverzicht bewijst niet automatisch een succesvol schrijfactiepad.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `7ed6ad852c120b174be8919c30019734c533af8200506378aa6f2817426fdb44`

![M04-20261119-007 | TEST](<image(20261119-180325).png>)

---

### M04-20261119-008 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-180434).png`  
**Beschrijving:** De FUXA-Home/Motor_Control-weergave is geopend.  
**Bewijsgrens:** Navigatie naar het motorscherm; geen functietest.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `65cd6d04774ee0d47eec51b109b3d60add9ea872d20f08dc9cefdd243b18e5dc`

![M04-20261119-008 | CONFIG](<image(20261119-180434).png>)

---

### M04-20261119-009 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-180617).png`  
**Beschrijving:** FUXA-editor toont de MainView-ontwerpruimte.  
**Bewijsgrens:** Werkzaamheden aan HMI-visualisatie.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `543e65835ed76d302da2ee56fe518116a60ea6d360f7e25fbbd9b76808574933`

![M04-20261119-009 | CONFIG](<image(20261119-180617).png>)

---

### M04-20261119-010 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-180732).png`  
**Beschrijving:** De Motor_Control-component is geselecteerd in de HMI-editor.  
**Bewijsgrens:** Selectie van een UI-element, geen ingestelde actie aangetoond.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `c8dd9d24104f9d319065d3f0945ddca076f0b7aaf20e87fcae58b9b78bca33de`

![M04-20261119-010 | CONFIG](<image(20261119-180732).png>)

---

### M04-20261119-011 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-180835).png`  
**Beschrijving:** Eigenschappenpaneel toont de geselecteerde Motor_Control-component, inclusief naam en weergaveopties.  
**Bewijsgrens:** Alleen elementconfiguratie zichtbaar.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `460956fd35d2859e2b240fac0a60f14ef664b0cfb926014732d375d78c87efb2`

![M04-20261119-011 | CONFIG](<image(20261119-180835).png>)

---

### M04-20261119-012 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-181014).png`  
**Beschrijving:** FUXA Button Settings toont een toggle gekoppeld aan de Motor_Start-tag.  
**Bewijsgrens:** Schrijfbestemming geconfigureerd; geslaagde schrijfactie apart verifiëren.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `7149ff72013624bbfd7a5e9fcf508a040b70d088cca9118eeceb533ed16d9cd9`

![M04-20261119-012 | CONFIG](<image(20261119-181014).png>)

---

### M04-20261119-013 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-181418).png`  
**Beschrijving:** OpenPLC Monitoring toont twee motorgerelateerde booleans op TRUE tijdens de draaitest.  
**Bewijsgrens:** Momentopname van PLC-variabelen; oorzaak van de waarde apart aantonen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `43d3bd50a8f4355e026ca27609c07e23a29c839bd5bae529f07567e43ee0bdda`

![M04-20261119-013 | TEST](<image(20261119-181418).png>)

---

### M04-20261119-014 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-181447).png`  
**Beschrijving:** OpenPLC Monitoring toont dezelfde booleans weer op FALSE in de stoptoestand.  
**Bewijsgrens:** Momentopname van het stoppen van de motorsimulatie.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `63d9cbc7b9655372f9f2783f9e3e44d90b0c505b3169c33e6a20ba0e6994ffea`

![M04-20261119-014 | TEST](<image(20261119-181447).png>)

---

### M04-20261119-015 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-181536).png`  
**Beschrijving:** FUXA leest Motor_Start en Motor_Running beide als 0 terug.  
**Bewijsgrens:** Beperkte leesbackcontrole; end-to-end schrijf- en netwerkpad niet volledig bewezen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `c07de9db737643c8f9bdf8fe01db8b5bdf92bcb21f4bb2cb1a8ab5991b6f933e`

![M04-20261119-015 | TEST](<image(20261119-181536).png>)

---

### M04-20261119-016 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-181717).png`  
**Beschrijving:** pfSense toont bestaande LAN-firewallregels, waaronder toegang voor beheer en het OT-segment.  
**Bewijsgrens:** Regeloverzicht, geen bewijs dat elke regel correct wordt afgedwongen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `c8d919a6f99065c22bbfda325fd884bfa233ef5ae3e186dc453ef681cf8cda40`

![M04-20261119-016 | CONFIG](<image(20261119-181717).png>)

---

### M04-20261119-017 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-182004).png`  
**Beschrijving:** PowerShell op de Lenovo-beheerhost test TCP/502 naar PLC01 en meldt een mislukte verbinding.  
**Bewijsgrens:** Negatief testresultaat, maar de bronroute maakt de segmentatieclaim beperkt.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `96edc741b171bc79fdc33130ab0d37c3e59babb0ac28eac7ca03c8a81c55850c`

![M04-20261119-017 | TEST](<image(20261119-182004).png>)

---

### M04-20261119-018 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-182328).png`  
**Beschrijving:** Een rechtstreeks vanaf de Wi-Fi-host uitgevoerde OT-verbindingspoging resulteert in een timeout.  
**Bewijsgrens:** Niet gebruiken als zelfstandig bewijs voor isolatie tussen de juiste firewallzones.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `9385a316720f74557644cf359dac32e0f924e051495fc319a120bc1016188394`

![M04-20261119-018 | TEST](<image(20261119-182328).png>)

---

### M04-20261119-019 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-183059).png`  
**Beschrijving:** PowerShell op CLIENT01 in LAB test Modbus TCP/502 richting PLC01 en krijgt geen verbinding.  
**Bewijsgrens:** Negatieve test vanaf relevante bronzone; correleren met pfSense-blocklog.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `16a1daf9bdc63f4b32f06a6260256244535123ff757af1c9ee6d4e6fe7ae898a`

![M04-20261119-019 | TEST](<image(20261119-183059).png>)

---

### M04-20261119-020 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** `image(20261119-183549).png`  
**Beschrijving:** pfSense Advanced Log Filter wordt voorbereid, maar de bronpoort staat verkeerd gefilterd.  
**Bewijsgrens:** Filtervoorbereiding; geen sluitend bewijs uit deze selectie.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `6e449f7ca9bc4a146e5a14e00b4b33c0310979da30aba226cbc3ce01f5ed4a3b`

![M04-20261119-020 | TROUBLESHOOT](<image(20261119-183549).png>)

---

### M04-20261119-021 | 2026-11-19 · LOG

**Onderwerp:** `image(20261119-183623).png`  
**Beschrijving:** pfSense toont geblokkeerde LAB→PLC01-verzoeken op TCP/502 in de firewalllogs.  
**Bewijsgrens:** Correlatie voor de negatieve Modbus-test; beperkte scope.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `c661cc74a486314d00eb0ed5bdcf400f0c5fe355d524788a8d32ddf17d4b72ba`

![M04-20261119-021 | LOG](<image(20261119-183623).png>)

---

### M04-20261119-022 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-183816).png`  
**Beschrijving:** CLIENT01 voert een TCP/1881-verbindingsproef richting FUXA01 uit; testoutput is zichtbaar.  
**Bewijsgrens:** Tussenstadium; eindresultaat volgt in volgend beeld.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `223c55e92199d164e19a92bb4e8361bb8f12b5975602c2df466257780126cb94`

![M04-20261119-022 | TEST](<image(20261119-183816).png>)

---

### M04-20261119-023 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-184048).png`  
**Beschrijving:** CLIENT01 in LAB toont een mislukte TCP/1881-verbinding richting FUXA01.  
**Bewijsgrens:** Negatieve FUXA-beheertest, te combineren met firewalllog.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `9ce35222cacb212f81cdb7c4f8f3ed2c542ebae06c07f1669dcdc6cf2775ad50`

![M04-20261119-023 | TEST](<image(20261119-184048).png>)

---

### M04-20261119-024 | 2026-11-19 · LOG

**Onderwerp:** `image(20261119-184425).png`  
**Beschrijving:** pfSense-log laat geblokkeerd LAB→FUXA01-verkeer op TCP/1881 zien.  
**Bewijsgrens:** Deny voor dit protocol en deze route, geen universele isolatie-PASS.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `fec29ca60811afd1d6be113f73cbaafe0a52479fc50a5501deaefeb4865b3faa`

![M04-20261119-024 | LOG](<image(20261119-184425).png>)

---

### M04-20261119-025 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-184701).png`  
**Beschrijving:** PLC01-terminal toont IP-routing via de OT-gateway.  
**Bewijsgrens:** Routeringsconfiguratie; bereikbaarheid niet afleidbaar uit een routetabel alleen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `7be690dde67d6798e617e0670bcab8c0cc2577626c08e1937d9764f8f292ee9b`

![M04-20261119-025 | CONFIG](<image(20261119-184701).png>)

---

### M04-20261119-026 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-184915).png`  
**Beschrijving:** PLC01 voert een ICMP-test richting LAB uit en ontvangt geen antwoorden.  
**Bewijsgrens:** Verlies is zichtbaar; oorzaak bevestigen aan de hand van firewalllogs.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `6bc1860da823f80134f33d2547659d3113cd4e82da6589da0e31245432cd4601`

![M04-20261119-026 | TEST](<image(20261119-184915).png>)

---

### M04-20261119-027 | 2026-11-19 · LOG

**Onderwerp:** `image(20261119-185019).png`  
**Beschrijving:** pfSense-logs tonen geblokkeerde ICMP-pakketten van PLC01 richting LAB.  
**Bewijsgrens:** Correlatie bij de mislukte PLC01→LAB-ping.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `c8007bae53cd6fbfbb11d0add84a2e9db65b9df7ca91b182dd3ebbb379104833`

![M04-20261119-027 | LOG](<image(20261119-185019).png>)

---

### M04-20261119-028 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-185133).png`  
**Beschrijving:** PLC01 probeert via ICMP een extern adres te bereiken; alle pakketten gaan verloren.  
**Bewijsgrens:** Isolatieobservatie; internetbeleid beperken tot getoonde proef.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `22b9be25a6ca3435db4957efde544414d70ec65fcf2a91c031f5578cc6ce3279`

![M04-20261119-028 | TEST](<image(20261119-185133).png>)

---

### M04-20261119-029 | 2026-11-19 · LOG

**Onderwerp:** `image(20261119-185239).png`  
**Beschrijving:** pfSense registreert geblokkeerde ICMP-pakketten van PLC01 richting internet.  
**Bewijsgrens:** Bevestigt blokkade van dit ICMP-verkeer.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `86069f917e46649d55b916fc7cf8863c2de22e078911e60b49daf91319904a29`

![M04-20261119-029 | LOG](<image(20261119-185239).png>)

---

### M04-20261119-030 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-185526).png`  
**Beschrijving:** PLC01 probeert een externe HTTPS-verbinding op TCP/443 te openen en krijgt een timeout.  
**Bewijsgrens:** Negatieve applicatiebereikbaarheidstest; DNS/TLS-oorzaken apart beoordelen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `87fcec2a562e20d3c53769d846db026c2c0a7854230bb0854067a78b9fe57c1d`

![M04-20261119-030 | TEST](<image(20261119-185526).png>)

---

### M04-20261119-031 | 2026-11-19 · LOG

**Onderwerp:** `image(20261119-185648).png`  
**Beschrijving:** pfSense toont geblokkeerd PLC01→internet-verkeer richting TCP/443.  
**Bewijsgrens:** Logondersteuning voor de HTTPS-test.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `fb3a1e5c0959534c2e920bf4244edaa667c37fe146a35192963de18c2b800ed3`

![M04-20261119-031 | LOG](<image(20261119-185648).png>)

---

### M04-20261119-032 | 2026-11-19 · LOG

**Onderwerp:** `image(20261119-191122).png`  
**Beschrijving:** Alternatief/logoverzicht van eerder vastgelegde PLC01→internet TCP/443-blockevents.  
**Bewijsgrens:** Herhaalde weergave; niet tellen als onafhankelijke extra test.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `17e6a5dea4a28f6c34313598f4d6a03bca34e8198ad4bc1ba38a7743a020d697`

![M04-20261119-032 | LOG](<image(20261119-191122).png>)

---

### M04-20261119-033 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-191317).png`  
**Beschrijving:** FUXA01 probeert een externe HTTPS-verbinding via TCP/443 en krijgt geen succesvolle verbinding.  
**Bewijsgrens:** Negatieve bereikbaarheidsproef vanaf FUXA01.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `9ca7b9e5f9407e89558ebb68f911cdb9ede33c25d4d00b1e88c10e54e4dff9f8`

![M04-20261119-033 | TEST](<image(20261119-191317).png>)

---

### M04-20261119-034 | 2026-11-19 · LOG

**Onderwerp:** `image(20261119-191428).png`  
**Beschrijving:** pfSense toont geblokkeerde HTTPS-pogingen van FUXA01 richting internet.  
**Bewijsgrens:** Correlatie bij de FUXA01-HTTPS-timeout.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `47639cc7d2e6459b570aa5e4ff28812cf87c17e9b3d0851a9158a888c836c2f8`

![M04-20261119-034 | LOG](<image(20261119-191428).png>)

---

### M04-20261119-035 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-191629).png`  
**Beschrijving:** FUXA01 voert een ICMP-ping richting LAB uit met volledig pakketverlies.  
**Bewijsgrens:** Mislukte ICMP-test, geen zelfstandig sluitend bewijs van firewalloorzaak.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `cdb3495bdfc88710429c7eae5c593b87b472c442943cec4403493572059d16f5`

![M04-20261119-035 | TEST](<image(20261119-191629).png>)

---

### M04-20261119-036 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** `image(20261119-191707).png`  
**Beschrijving:** pfSense toont nog een filter uit de eerdere HTTPS-controle vóór de FUXA01→LAB-logcontrole.  
**Bewijsgrens:** Voorbereidingsbeeld; niet als nieuwe ICMP-blocklog tellen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `6da574621abe377e1bce8feb6914fe310d618269918b0042a8ede87290b44801`

![M04-20261119-036 | TROUBLESHOOT](<image(20261119-191707).png>)

---

### M04-20261119-037 | 2026-11-19 · LOG

**Onderwerp:** `image(20261119-191810).png`  
**Beschrijving:** pfSense laat geblokkeerde ICMP-pakketten van FUXA01 richting LAB zien.  
**Bewijsgrens:** Ondersteunt de negatieve FUXA01→LAB-ping.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `d79f9ddefb5c90b15a204dd97df8bae9079b7d326b56ced95f0d2b7945d37c25`

![M04-20261119-037 | LOG](<image(20261119-191810).png>)

---

### M04-20261119-038 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-192047).png`  
**Beschrijving:** PowerShell op de Lenovo-beheerhost toont geslaagde, beperkte TCP-bereikbaarheid naar beheerpoorten 8080 (PLC01) en 1881 (FUXA01).  
**Bewijsgrens:** Beheerroute is niet hetzelfde als onbeperkte LAB→OT-toegang.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `bb37408f838d6ad2d8cf18ee5cc15ebcc0f12adf05e6c21559ae1c70fdeba15f`

![M04-20261119-038 | TEST](<image(20261119-192047).png>)

---

### M04-20261119-039 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-192436).png`  
**Beschrijving:** pfSense LAB-regeloverzicht toont een tijdelijke brede uitgaande internetregel vóór uitschakeling.  
**Bewijsgrens:** Potentiële uitzondering; status van de regels op dit beeld onderscheiden van eindstatus.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `3c0c7ad192bdbfa74253be50e496b5c5b7e0123a4003cb711bf892609debce3c`

![M04-20261119-039 | CONFIG](<image(20261119-192436).png>)

---

### M04-20261119-040 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-192622).png`  
**Beschrijving:** Detailpagina van de tijdelijke LAB-firewallregel toont bron, bestemming, actie en beschrijving.  
**Bewijsgrens:** Instellingssnapshot, geen wijzigingsbewijs.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `b2a76fe4dd9d056a09a6e3d22cfc8f50132f61cd41394fe2c92e7ecf0b80a52c`

![M04-20261119-040 | CONFIG](<image(20261119-192622).png>)

---

### M04-20261119-041 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-193838).png`  
**Beschrijving:** pfSense Backup & Restore toont opties voor een versleutelde configuratie-export.  
**Bewijsgrens:** De aanwezigheid van opties bewijst niet dat een geldige back-up is gedownload.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `2a395acb24327a3ec96bc10366de6cc305ef995f662ac985dc113a388301231b`

![M04-20261119-041 | CONFIG](<image(20261119-193838).png>)

---

### M04-20261119-042 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** `image(20261119-193933).png`  
**Beschrijving:** Een tweede pfSense Backup & Restore-weergave toont versleutelingsopties en een validatie-/invoerwaarschuwing.  
**Bewijsgrens:** Geen geslaagde, herstelde back-up aangetoond.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `2a395acb24327a3ec96bc10366de6cc305ef995f662ac985dc113a388301231b`

![M04-20261119-042 | TROUBLESHOOT](<image(20261119-193933).png>)

---

### M04-20261119-043 | 2026-11-19 · FIX

**Onderwerp:** `image(20261119-194117).png`  
**Beschrijving:** pfSense LAB-regeloverzicht toont de tijdelijke uitgaande regel uitgeschakeld en dat de wijziging is toegepast.  
**Bewijsgrens:** Configuratiewijziging zichtbaar; effect toetsen met regressieproeven.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `9b7f56f19d1987c1aa0d2029531c3f0f6de2491a4097ead038426411b86f4a7f`

![M04-20261119-043 | FIX](<image(20261119-194117).png>)

---

### M04-20261119-044 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-194505).png`  
**Beschrijving:** CLIENT01 toont geslaagde DNS-resolutie en daarnaast eerdere mislukte verbindingsproeven.  
**Bewijsgrens:** DNS-succes betekent niet dat OT-connectiviteit is toegestaan; historische regels apart beoordelen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `50f16a8728e8345e688155d68c93d2ab9e0df2af0107e6c2c81af001036fb2a8`

![M04-20261119-044 | TEST](<image(20261119-194505).png>)

---

### M04-20261119-045 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-194856).png`  
**Beschrijving:** Na uitschakelen van de tijdelijke regel toont CLIENT01 opnieuw mislukte verbindingen richting PLC01/FUXA01.  
**Bewijsgrens:** Beperkte negatieve regressietest; vergelijken met de firewalllogs.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `9fbe510d80ff7b231d76001ff9e176df9738b34ec1b44b65ba2a3316f9c9ea20`

![M04-20261119-045 | TEST](<image(20261119-194856).png>)

---

### M04-20261119-046 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-195238).png`  
**Beschrijving:** pfSense OT-regeloverzicht toont een uitgeschakelde tijdelijke firewallregel.  
**Bewijsgrens:** Regelstatus zichtbaar, geen volledige OT-policy-review.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `809948ccbdf27f16bb3447e603a6a2ee772d3c908d4d0857f89207d8bd4e48c2`

![M04-20261119-046 | CONFIG](<image(20261119-195238).png>)

---

### M04-20261119-047 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-195351).png`  
**Beschrijving:** pfSense Floating-regeloverzicht meldt dat er geen floating firewallregels zijn geconfigureerd.  
**Bewijsgrens:** Momentopname, geen bewijs van alle mogelijke verkeerspaden.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `ac16f0d5744e0f4f01a18e647a075aed8a4bc9b66e1cec2e6ad9853bc03ecc0e`

![M04-20261119-047 | CONFIG](<image(20261119-195351).png>)

---

### M04-20261119-048 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** `image(20261119-195706).png`  
**Beschrijving:** pfSense State Table-filter toont geen bijpassende state voor CLIENT01.  
**Bewijsgrens:** Ontbrekende state is geen onafhankelijk bewijs van een specifieke firewall-deny.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `eb5bedf52e84c2f11047c136f0409d56563c5b45d1f2fec80681745995f5bdca`

![M04-20261119-048 | TROUBLESHOOT](<image(20261119-195706).png>)

---

### M04-20261119-049 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-195743).png`  
**Beschrijving:** pfSense LAN-regeloverzicht toont zowel specifieke beheerregels als brede standaard-allow-regels.  
**Bewijsgrens:** Reviewpunt: daadwerkelijke exposure hangt van regelvolgorde en relevante interface af.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `e9775abd4673f3b6a3ea834c3c0ae73834844e72026ca64bce34c7862eac517f`

![M04-20261119-049 | CONFIG](<image(20261119-195743).png>)

---

### M04-20261119-050 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-195836).png`  
**Beschrijving:** Detailpagina van de brede LAN IPv4-allow-regel toont de bron-/bestemmingsscope en actie Pass.  
**Bewijsgrens:** Configuratieobservatie; afgedwongen toegang niet rechtstreeks getest.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `2b7527e8e3e073be94540fa58a71941e3b45187e68a644242ecfab310205b4ec`

![M04-20261119-050 | CONFIG](<image(20261119-195836).png>)

---

### M04-20261119-051 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-195933).png`  
**Beschrijving:** Detailpagina van een brede LAN IPv6-allow-regel toont actie Pass en ruime bron-/bestemmingsscope.  
**Bewijsgrens:** IPv6-policy aandachtspunt, niet automatisch bewijs voor een bereikbaar IPv6-pad.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `ba3b2644373f5df882f244877d87a7fff38f7e404ece7b2a86fac3146b3485bd`

![M04-20261119-051 | CONFIG](<image(20261119-195933).png>)

---

### M04-20261119-052 | 2026-11-19 · CONFIG

**Onderwerp:** `image(20261119-200026).png`  
**Beschrijving:** pfSense OT-interfaceconfiguratie toont IPv6 Configuration Type op None.  
**Bewijsgrens:** Interface-instelling; andere IPv6-paden blijven afzonderlijk te toetsen.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `3d90970c14d66a895d7a8c82a6c88a911cc54858b3cbc746a8ee2b74b8572313`

![M04-20261119-052 | CONFIG](<image(20261119-200026).png>)

---

### M04-20261119-053 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-200227).png`  
**Beschrijving:** PLC01-terminal toont IPv6-adressen en routetabel zonder zichtbare bruikbare globale IPv6-route.  
**Bewijsgrens:** Momentopname; link-local IPv6 kan nog aanwezig zijn.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `09835152b7d05e88c0ee1fe98f1b80a7a5ee6a8e0d5b0990066abc1aedf36920`

![M04-20261119-053 | TEST](<image(20261119-200227).png>)

---

### M04-20261119-054 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-200353).png`  
**Beschrijving:** Herhaalde PLC01-terminalweergave van de IPv6-route- en adrescontrole.  
**Bewijsgrens:** Duplicaat/aanvullende zichtbaarheid, geen nieuwe onafhankelijke test.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `09835152b7d05e88c0ee1fe98f1b80a7a5ee6a8e0d5b0990066abc1aedf36920`

![M04-20261119-054 | TEST](<image(20261119-200353).png>)

---

### M04-20261119-055 | 2026-11-19 · TEST

**Onderwerp:** `image(20261119-200554).png`  
**Beschrijving:** FUXA01-terminal toont IPv6-adressen en routetabel zonder zichtbare bruikbare globale IPv6-route.  
**Bewijsgrens:** Momentopname; link-local IPv6 is niet hetzelfde als extern IPv6-bereik.  
**SHA-256 (alleen publiek gesaneerde afgeleide):** `f44ed3e46793d21c6a58b98192a6815973578f0bb09f4105cfd2289efb19f46f`

![M04-20261119-055 | TEST](<image(20261119-200554).png>)