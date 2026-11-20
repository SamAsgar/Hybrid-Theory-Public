# M04 fase 20 — OT-segmentatie, firewallcontrole en regressietests (19 november 2026)

**Aantal afbeeldingen:** 55 gesaneerde publieke PNG-afgeleiden  
**Classificatie:** PUBLIC · onomkeerbare pixelmaskering · originele beelden uitsluitend privé  
**Status:** M04-CORE `IN PROGRESS`; integrale AC04/AC07-acceptatie **PENDING**  

[Terug naar de M04-hoofdindex](../M04-EVIDENCE-INDEX.md) · [Overzicht van alle fasen](../M04-GALERIJ.md)

**Saneringsbeperking:** technische netwerkadressen, identiteiten en gevoelige uitvoer zijn afgedekt. Bij 17 terminalopnamen is alle uitvoer verwijderd, dus de publieke afbeelding is daar uitsluitend een contextweergave en geen zelfstandig toetsbaar resultaat. Niet afleiden dat alle 55 beelden onafhankelijk een PASS bewijzen. Zie het [saneringsrapport](../M04-SANITIZATION-REPORT.md).

## Bewijsreeks

---

### M04-20261119-001 | 2026-11-19 · LOG

**Onderwerp:** Screenshot 2026-11-19 205046.png  
**Beschrijving:** pfSense-firewalllog filtert LAB→PLC01-verkeer en toont geblokkeerde TCP/502-pogingen na een regelwijziging.  
**Bewijsgrens:** Beperkt bewijs van een deny op dit bron-doelpaar; geen volledige AC04-acceptatie.  
**SHA-256 (publiek afgeleid bestand):** `bd99b7ad127c939ca8a9c061506631d3c925a718771d8110a3c45a20187fc683`

![M04-20261119-001 — gesaneerde LOG](<Screenshot 2026-11-19 205046.png>)

---

### M04-20261119-002 | 2026-11-19 · LOG

**Onderwerp:** Screenshot 2026-11-19 205131.png  
**Beschrijving:** pfSense-firewalllog filtert LAB→FUXA01-verkeer en toont geblokkeerde verbindingen na de wijziging.  
**Bewijsgrens:** Beperkt bewijs van blokkades op de getoonde verbindingen.  
**SHA-256 (publiek afgeleid bestand):** `89ad9eafa839dd80ee5d98651dd7d8b122213988bbc5e83a086f41c1b43b33e7`

![M04-20261119-002 — gesaneerde LOG](<Screenshot 2026-11-19 205131.png>)

---

### M04-20261119-003 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-175850).png  
**Beschrijving:** FUXA-verbindingsoverzicht toont de PLC01-motorverbinding met een gele statusindicator.  
**Bewijsgrens:** Beginsituatie; de betekenis van de status moet niet als succesvolle verbinding worden aangenomen.  
**SHA-256 (publiek afgeleid bestand):** `d7e646e6bb82b8cd3ebde3a8298041dfd3b46eda0bcc456dca86c17e745c1b5e`

![M04-20261119-003 — gesaneerde CONFIG](<image(20261119-175850).png>)

---

### M04-20261119-004 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** image(20261119-180020).png  
**Beschrijving:** FUXA-venster Connection Property toont Modbus TCP-instellingen en een rode indicator voor de PLC-verbinding.  
**Bewijsgrens:** Configuratie en verbindingsprobleem zichtbaar; geen PASS.  
**SHA-256 (publiek afgeleid bestand):** `1ead63fc742a853ce51c113f660f73297b3c32e39c6a7f8cac8c39605635386c`

![M04-20261119-004 — gesaneerde TROUBLESHOOT](<image(20261119-180020).png>)

---

### M04-20261119-005 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-180132).png  
**Beschrijving:** OpenPLC-webinterface toont de runtime in gestopte toestand.  
**Bewijsgrens:** Startstatus van de PLC, geen actief proces.  
**SHA-256 (publiek afgeleid bestand):** `dfc89f863127da6b4803c347f9e158481f7a53ac1588f9f656142d85bfb3cb2a`

![M04-20261119-005 — gesaneerde CONFIG](<image(20261119-180132).png>)

---

### M04-20261119-006 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-180210).png  
**Beschrijving:** OpenPLC-dashboard toont de runtime na starten met een draaiende status.  
**Bewijsgrens:** Runtime draait; HMI-verkeer is daarmee nog niet bewezen.  
**SHA-256 (publiek afgeleid bestand):** `e9570ba65b3f13d669fda992d52516933e4a81aeb6ac6931409f84d5ef96e6f5`

![M04-20261119-006 — gesaneerde CONFIG](<image(20261119-180210).png>)

---

### M04-20261119-007 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-180325).png  
**Beschrijving:** FUXA toont de tags Motor_Start en Motor_Running met de op dat moment uitgelezen waarden.  
**Bewijsgrens:** Een tagoverzicht bewijst niet automatisch een succesvol schrijfactiepad.  
**SHA-256 (publiek afgeleid bestand):** `cafa2ef6c79779d2bfb49d00a6e3ecd44ead32d8d2b2da3e006c386613479d66`

![M04-20261119-007 — gesaneerde TEST](<image(20261119-180325).png>)

---

### M04-20261119-008 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-180434).png  
**Beschrijving:** De FUXA-Home/Motor_Control-weergave is geopend.  
**Bewijsgrens:** Navigatie naar het motorscherm; geen functietest.  
**SHA-256 (publiek afgeleid bestand):** `3f2699b3ef682dda1de8d84017ab84eb8d42a4cad27f19e7bbd439c309d62860`

![M04-20261119-008 — gesaneerde CONFIG](<image(20261119-180434).png>)

---

### M04-20261119-009 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-180617).png  
**Beschrijving:** FUXA-editor toont de MainView-ontwerpruimte.  
**Bewijsgrens:** Werkzaamheden aan HMI-visualisatie.  
**SHA-256 (publiek afgeleid bestand):** `f9aa7e7fd8c70ae34f655d22645c1ee89b42443b0d5c88815322c79788a9a032`

![M04-20261119-009 — gesaneerde CONFIG](<image(20261119-180617).png>)

---

### M04-20261119-010 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-180732).png  
**Beschrijving:** De Motor_Control-component is geselecteerd in de HMI-editor.  
**Bewijsgrens:** Selectie van een UI-element, geen ingestelde actie aangetoond.  
**SHA-256 (publiek afgeleid bestand):** `83fc801e8201f78240156c1d1480c1527596b3edd4f8161445ed65fcba240c84`

![M04-20261119-010 — gesaneerde CONFIG](<image(20261119-180732).png>)

---

### M04-20261119-011 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-180835).png  
**Beschrijving:** Eigenschappenpaneel toont de geselecteerde Motor_Control-component, inclusief naam en weergaveopties.  
**Bewijsgrens:** Alleen elementconfiguratie zichtbaar.  
**SHA-256 (publiek afgeleid bestand):** `460956fd35d2859e2b240fac0a60f14ef664b0cfb926014732d375d78c87efb2`

![M04-20261119-011 — gesaneerde CONFIG](<image(20261119-180835).png>)

---

### M04-20261119-012 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-181014).png  
**Beschrijving:** FUXA Button Settings toont een toggle gekoppeld aan de Motor_Start-tag.  
**Bewijsgrens:** Schrijfbestemming geconfigureerd; geslaagde schrijfactie apart verifiëren.  
**SHA-256 (publiek afgeleid bestand):** `55669f396d9866fdbd32167bfa0b425dc602d6cb346c200e903011dbb2d9ef63`

![M04-20261119-012 — gesaneerde CONFIG](<image(20261119-181014).png>)

---

### M04-20261119-013 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-181418).png  
**Beschrijving:** OpenPLC Monitoring toont twee motorgerelateerde booleans op TRUE tijdens de draaitest.  
**Bewijsgrens:** Momentopname van PLC-variabelen; oorzaak van de waarde apart aantonen.  
**SHA-256 (publiek afgeleid bestand):** `43d3bd50a8f4355e026ca27609c07e23a29c839bd5bae529f07567e43ee0bdda`

![M04-20261119-013 — gesaneerde TEST](<image(20261119-181418).png>)

---

### M04-20261119-014 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-181447).png  
**Beschrijving:** OpenPLC Monitoring toont dezelfde booleans weer op FALSE in de stoptoestand.  
**Bewijsgrens:** Momentopname van het stoppen van de motorsimulatie.  
**SHA-256 (publiek afgeleid bestand):** `be1feb59ff780c5d713edef7ac13bda43470d96516c4a8636fcdf29b43e03f01`

![M04-20261119-014 — gesaneerde TEST](<image(20261119-181447).png>)

---

### M04-20261119-015 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-181536).png  
**Beschrijving:** FUXA leest Motor_Start en Motor_Running beide als 0 terug.  
**Bewijsgrens:** Beperkte leesbackcontrole; end-to-end schrijf- en netwerkpad niet volledig bewezen.  
**SHA-256 (publiek afgeleid bestand):** `e464bcfd6929a11340dabd893c9e40edfb5f9cbaac007d07af75403873dbf729`

![M04-20261119-015 — gesaneerde TEST](<image(20261119-181536).png>)

---

### M04-20261119-016 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-181717).png  
**Beschrijving:** pfSense toont bestaande LAN-firewallregels, waaronder toegang voor beheer en het OT-segment.  
**Bewijsgrens:** Regeloverzicht, geen bewijs dat elke regel correct wordt afgedwongen.  
**SHA-256 (publiek afgeleid bestand):** `91bd0648f07633277566674ddd2332c65be9bf1959fca0b8caee6443437f016d`

![M04-20261119-016 — gesaneerde CONFIG](<image(20261119-181717).png>)

---

### M04-20261119-017 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-182004).png  
**Beschrijving:** PowerShell op de Lenovo-beheerhost test TCP/502 naar PLC01 en meldt een mislukte verbinding.  
**Bewijsgrens:** Negatief testresultaat, maar de bronroute maakt de segmentatieclaim beperkt. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `1a932889350c83a7383a0742750c6c59368669f869ae2bb6b92f48d060a9083f`

![M04-20261119-017 — gesaneerde TEST](<image(20261119-182004).png>)

---

### M04-20261119-018 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-182328).png  
**Beschrijving:** Een rechtstreeks vanaf de Wi-Fi-host uitgevoerde OT-verbindingspoging resulteert in een timeout.  
**Bewijsgrens:** Niet gebruiken als zelfstandig bewijs voor isolatie tussen de juiste firewallzones. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `0a90ebc9feaf40f6df9a5e46b7f21ce42bddf3a467f6d46276de8efdbf3a7290`

![M04-20261119-018 — gesaneerde TEST](<image(20261119-182328).png>)

---

### M04-20261119-019 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-183059).png  
**Beschrijving:** PowerShell op CLIENT01 in LAB test Modbus TCP/502 richting PLC01 en krijgt geen verbinding.  
**Bewijsgrens:** Negatieve test vanaf relevante bronzone; correleren met pfSense-blocklog. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `97040dfcd4530736a3cd0c2980237b37044398d5a8bd93ae6d4a6d7de81851c9`

![M04-20261119-019 — gesaneerde TEST](<image(20261119-183059).png>)

---

### M04-20261119-020 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** image(20261119-183549).png  
**Beschrijving:** pfSense Advanced Log Filter wordt voorbereid, maar de bronpoort staat verkeerd gefilterd.  
**Bewijsgrens:** Filtervoorbereiding; geen sluitend bewijs uit deze selectie.  
**SHA-256 (publiek afgeleid bestand):** `1ef8ea257780920736a3be9114a478bb99271d9cc23bf71438d8947ed5175ffc`

![M04-20261119-020 — gesaneerde TROUBLESHOOT](<image(20261119-183549).png>)

---

### M04-20261119-021 | 2026-11-19 · LOG

**Onderwerp:** image(20261119-183623).png  
**Beschrijving:** pfSense toont geblokkeerde LAB→PLC01-verzoeken op TCP/502 in de firewalllogs.  
**Bewijsgrens:** Correlatie voor de negatieve Modbus-test; beperkte scope.  
**SHA-256 (publiek afgeleid bestand):** `641bede2c578f2d2c8292c8ac0436abfb3956af0d47c3ce36a57a0d985961452`

![M04-20261119-021 — gesaneerde LOG](<image(20261119-183623).png>)

---

### M04-20261119-022 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-183816).png  
**Beschrijving:** CLIENT01 voert een TCP/1881-verbindingsproef richting FUXA01 uit; testoutput is zichtbaar.  
**Bewijsgrens:** Tussenstadium; eindresultaat volgt in volgend beeld. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `26a234251852d7933dda30d6b65016c7bcad3555c68e5b9a01473f113920a8a5`

![M04-20261119-022 — gesaneerde TEST](<image(20261119-183816).png>)

---

### M04-20261119-023 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-184048).png  
**Beschrijving:** CLIENT01 in LAB toont een mislukte TCP/1881-verbinding richting FUXA01.  
**Bewijsgrens:** Negatieve FUXA-beheertest, te combineren met firewalllog. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `82b9d3a966692a57d102baabfc87452e18b964185c82cf1937bc4c11d0fc5adc`

![M04-20261119-023 — gesaneerde TEST](<image(20261119-184048).png>)

---

### M04-20261119-024 | 2026-11-19 · LOG

**Onderwerp:** image(20261119-184425).png  
**Beschrijving:** pfSense-log laat geblokkeerd LAB→FUXA01-verkeer op TCP/1881 zien.  
**Bewijsgrens:** Deny voor dit protocol en deze route, geen universele isolatie-PASS.  
**SHA-256 (publiek afgeleid bestand):** `43105e424567f00e1bf6d2dd4a81a0d7eb80c129e1739d9d92946f81e2021ba1`

![M04-20261119-024 — gesaneerde LOG](<image(20261119-184425).png>)

---

### M04-20261119-025 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-184701).png  
**Beschrijving:** PLC01-terminal toont IP-routing via de OT-gateway.  
**Bewijsgrens:** Routeringsconfiguratie; bereikbaarheid niet afleidbaar uit een routetabel alleen. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `5eca9f12216b1339acadac2421447ecb78c5fd6aa9c3e482cb46a91d1d08e930`

![M04-20261119-025 — gesaneerde CONFIG](<image(20261119-184701).png>)

---

### M04-20261119-026 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-184915).png  
**Beschrijving:** PLC01 voert een ICMP-test richting LAB uit en ontvangt geen antwoorden.  
**Bewijsgrens:** Verlies is zichtbaar; oorzaak bevestigen aan de hand van firewalllogs. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `5eca9f12216b1339acadac2421447ecb78c5fd6aa9c3e482cb46a91d1d08e930`

![M04-20261119-026 — gesaneerde TEST](<image(20261119-184915).png>)

---

### M04-20261119-027 | 2026-11-19 · LOG

**Onderwerp:** image(20261119-185019).png  
**Beschrijving:** pfSense-logs tonen geblokkeerde ICMP-pakketten van PLC01 richting LAB.  
**Bewijsgrens:** Correlatie bij de mislukte PLC01→LAB-ping.  
**SHA-256 (publiek afgeleid bestand):** `31b4c0f7788ceadc08b307155e7d2e9ac99e6fb3ac6366bc2be62c2cc7c1689f`

![M04-20261119-027 — gesaneerde LOG](<image(20261119-185019).png>)

---

### M04-20261119-028 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-185133).png  
**Beschrijving:** PLC01 probeert via ICMP een extern adres te bereiken; alle pakketten gaan verloren.  
**Bewijsgrens:** Isolatieobservatie; internetbeleid beperken tot getoonde proef. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `5eca9f12216b1339acadac2421447ecb78c5fd6aa9c3e482cb46a91d1d08e930`

![M04-20261119-028 — gesaneerde TEST](<image(20261119-185133).png>)

---

### M04-20261119-029 | 2026-11-19 · LOG

**Onderwerp:** image(20261119-185239).png  
**Beschrijving:** pfSense registreert geblokkeerde ICMP-pakketten van PLC01 richting internet.  
**Bewijsgrens:** Bevestigt blokkade van dit ICMP-verkeer.  
**SHA-256 (publiek afgeleid bestand):** `720e5567ed89d39766bcf9ea9dd0bf3b8b832181e4274a71889f0791849837ad`

![M04-20261119-029 — gesaneerde LOG](<image(20261119-185239).png>)

---

### M04-20261119-030 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-185526).png  
**Beschrijving:** PLC01 probeert een externe HTTPS-verbinding op TCP/443 te openen en krijgt een timeout.  
**Bewijsgrens:** Negatieve applicatiebereikbaarheidstest; DNS/TLS-oorzaken apart beoordelen. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `5eca9f12216b1339acadac2421447ecb78c5fd6aa9c3e482cb46a91d1d08e930`

![M04-20261119-030 — gesaneerde TEST](<image(20261119-185526).png>)

---

### M04-20261119-031 | 2026-11-19 · LOG

**Onderwerp:** image(20261119-185648).png  
**Beschrijving:** pfSense toont geblokkeerd PLC01→internet-verkeer richting TCP/443.  
**Bewijsgrens:** Logondersteuning voor de HTTPS-test.  
**SHA-256 (publiek afgeleid bestand):** `2c1c5aa3df50851c8472f4f7683c295ead41fa7bf610f26d8f308992dad091c3`

![M04-20261119-031 — gesaneerde LOG](<image(20261119-185648).png>)

---

### M04-20261119-032 | 2026-11-19 · LOG

**Onderwerp:** image(20261119-191122).png  
**Beschrijving:** Alternatief/logoverzicht van eerder vastgelegde PLC01→internet TCP/443-blockevents.  
**Bewijsgrens:** Herhaalde weergave; niet tellen als onafhankelijke extra test.  
**SHA-256 (publiek afgeleid bestand):** `ab21b927322b9c003c3d2f577e0dd15540de568d61ce90b2d962b379e35dfc3c`

![M04-20261119-032 — gesaneerde LOG](<image(20261119-191122).png>)

---

### M04-20261119-033 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-191317).png  
**Beschrijving:** FUXA01 probeert een externe HTTPS-verbinding via TCP/443 en krijgt geen succesvolle verbinding.  
**Bewijsgrens:** Negatieve bereikbaarheidsproef vanaf FUXA01. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `5eca9f12216b1339acadac2421447ecb78c5fd6aa9c3e482cb46a91d1d08e930`

![M04-20261119-033 — gesaneerde TEST](<image(20261119-191317).png>)

---

### M04-20261119-034 | 2026-11-19 · LOG

**Onderwerp:** image(20261119-191428).png  
**Beschrijving:** pfSense toont geblokkeerde HTTPS-pogingen van FUXA01 richting internet.  
**Bewijsgrens:** Correlatie bij de FUXA01-HTTPS-timeout.  
**SHA-256 (publiek afgeleid bestand):** `04a8ef99ad05e888b2980a3619021f6bf9fb0014959b71c93de8e857b3e77601`

![M04-20261119-034 — gesaneerde LOG](<image(20261119-191428).png>)

---

### M04-20261119-035 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-191629).png  
**Beschrijving:** FUXA01 voert een ICMP-ping richting LAB uit met volledig pakketverlies.  
**Bewijsgrens:** Mislukte ICMP-test, geen zelfstandig sluitend bewijs van firewalloorzaak. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `5eca9f12216b1339acadac2421447ecb78c5fd6aa9c3e482cb46a91d1d08e930`

![M04-20261119-035 — gesaneerde TEST](<image(20261119-191629).png>)

---

### M04-20261119-036 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** image(20261119-191707).png  
**Beschrijving:** pfSense toont nog een filter uit de eerdere HTTPS-controle vóór de FUXA01→LAB-logcontrole.  
**Bewijsgrens:** Voorbereidingsbeeld; niet als nieuwe ICMP-blocklog tellen.  
**SHA-256 (publiek afgeleid bestand):** `ac208ff276669db5a000db817a65ee16713cf1ca806f9c7d5f479b4941ef0c1e`

![M04-20261119-036 — gesaneerde TROUBLESHOOT](<image(20261119-191707).png>)

---

### M04-20261119-037 | 2026-11-19 · LOG

**Onderwerp:** image(20261119-191810).png  
**Beschrijving:** pfSense laat geblokkeerde ICMP-pakketten van FUXA01 richting LAB zien.  
**Bewijsgrens:** Ondersteunt de negatieve FUXA01→LAB-ping.  
**SHA-256 (publiek afgeleid bestand):** `a00969069688b09d43558d94eff287a6ad0d690ca074d3f8f728faecadf56b1f`

![M04-20261119-037 — gesaneerde LOG](<image(20261119-191810).png>)

---

### M04-20261119-038 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-192047).png  
**Beschrijving:** PowerShell op de Lenovo-beheerhost toont geslaagde, beperkte TCP-bereikbaarheid naar beheerpoorten 8080 (PLC01) en 1881 (FUXA01).  
**Bewijsgrens:** Beheerroute is niet hetzelfde als onbeperkte LAB→OT-toegang. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `f4b743ea39afe73913395db4fea63b8bb3bb825791d27d906fcc585a84d51a76`

![M04-20261119-038 — gesaneerde TEST](<image(20261119-192047).png>)

---

### M04-20261119-039 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-192436).png  
**Beschrijving:** pfSense LAB-regeloverzicht toont een tijdelijke brede uitgaande internetregel vóór uitschakeling.  
**Bewijsgrens:** Potentiële uitzondering; status van de regels op dit beeld onderscheiden van eindstatus.  
**SHA-256 (publiek afgeleid bestand):** `87fe5659348dc08c98880828239049cb734c556fc06e8a8b88596adbcf99a927`

![M04-20261119-039 — gesaneerde CONFIG](<image(20261119-192436).png>)

---

### M04-20261119-040 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-192622).png  
**Beschrijving:** Detailpagina van de tijdelijke LAB-firewallregel toont bron, bestemming, actie en beschrijving.  
**Bewijsgrens:** Instellingssnapshot, geen wijzigingsbewijs.  
**SHA-256 (publiek afgeleid bestand):** `a1f753ed8294a29907d2479b1ece4e13b2f4a9c587e43f124aeca9788a63a7f9`

![M04-20261119-040 — gesaneerde CONFIG](<image(20261119-192622).png>)

---

### M04-20261119-041 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-193838).png  
**Beschrijving:** pfSense Backup & Restore toont opties voor een versleutelde configuratie-export.  
**Bewijsgrens:** De aanwezigheid van opties bewijst niet dat een geldige back-up is gedownload.  
**SHA-256 (publiek afgeleid bestand):** `204de8fca4df844bf24dfb72ab22aab194c8b61c316f175df18ba28338929c52`

![M04-20261119-041 — gesaneerde CONFIG](<image(20261119-193838).png>)

---

### M04-20261119-042 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** image(20261119-193933).png  
**Beschrijving:** Een tweede pfSense Backup & Restore-weergave toont versleutelingsopties en een validatie-/invoerwaarschuwing.  
**Bewijsgrens:** Geen geslaagde, herstelde back-up aangetoond.  
**SHA-256 (publiek afgeleid bestand):** `204de8fca4df844bf24dfb72ab22aab194c8b61c316f175df18ba28338929c52`

![M04-20261119-042 — gesaneerde TROUBLESHOOT](<image(20261119-193933).png>)

---

### M04-20261119-043 | 2026-11-19 · FIX

**Onderwerp:** image(20261119-194117).png  
**Beschrijving:** pfSense LAB-regeloverzicht toont de tijdelijke uitgaande regel uitgeschakeld en dat de wijziging is toegepast.  
**Bewijsgrens:** Configuratiewijziging zichtbaar; effect toetsen met regressieproeven.  
**SHA-256 (publiek afgeleid bestand):** `b4cbb9d68490da76149231fc8c42e1c436a15ca5863286932f6fbee9eac759cc`

![M04-20261119-043 — gesaneerde FIX](<image(20261119-194117).png>)

---

### M04-20261119-044 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-194505).png  
**Beschrijving:** CLIENT01 toont geslaagde DNS-resolutie en daarnaast eerdere mislukte verbindingsproeven.  
**Bewijsgrens:** DNS-succes betekent niet dat OT-connectiviteit is toegestaan; historische regels apart beoordelen. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `dbe0dece4ead44f574f97d13aa12305f7a7de4d79ef79938ca21fc38f66fb8da`

![M04-20261119-044 — gesaneerde TEST](<image(20261119-194505).png>)

---

### M04-20261119-045 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-194856).png  
**Beschrijving:** Na uitschakelen van de tijdelijke regel toont CLIENT01 opnieuw mislukte verbindingen richting PLC01/FUXA01.  
**Bewijsgrens:** Beperkte negatieve regressietest; vergelijken met de firewalllogs. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `09c6567c2f2531a5a33eaaa427296e905e833ea207637eb51ff3ebb6e44eeef9`

![M04-20261119-045 — gesaneerde TEST](<image(20261119-194856).png>)

---

### M04-20261119-046 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-195238).png  
**Beschrijving:** pfSense OT-regeloverzicht toont een uitgeschakelde tijdelijke firewallregel.  
**Bewijsgrens:** Regelstatus zichtbaar, geen volledige OT-policy-review.  
**SHA-256 (publiek afgeleid bestand):** `a052d17e9e54541e75920772b303d7e75d92b75746824785bdda36cdf96e66e9`

![M04-20261119-046 — gesaneerde CONFIG](<image(20261119-195238).png>)

---

### M04-20261119-047 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-195351).png  
**Beschrijving:** pfSense Floating-regeloverzicht meldt dat er geen floating firewallregels zijn geconfigureerd.  
**Bewijsgrens:** Momentopname, geen bewijs van alle mogelijke verkeerspaden.  
**SHA-256 (publiek afgeleid bestand):** `fc128a3bd6b4f93b5ddf43fead21f57b78fb2d7328f74a9c91eab4c69a8a24b6`

![M04-20261119-047 — gesaneerde CONFIG](<image(20261119-195351).png>)

---

### M04-20261119-048 | 2026-11-19 · TROUBLESHOOT

**Onderwerp:** image(20261119-195706).png  
**Beschrijving:** pfSense State Table-filter toont geen bijpassende state voor CLIENT01.  
**Bewijsgrens:** Ontbrekende state is geen onafhankelijk bewijs van een specifieke firewall-deny.  
**SHA-256 (publiek afgeleid bestand):** `fbf0cbcae08e517a69147ad05328c9b446b144898f2d004bdd3d5eb8170ce1a2`

![M04-20261119-048 — gesaneerde TROUBLESHOOT](<image(20261119-195706).png>)

---

### M04-20261119-049 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-195743).png  
**Beschrijving:** pfSense LAN-regeloverzicht toont zowel specifieke beheerregels als brede standaard-allow-regels.  
**Bewijsgrens:** Reviewpunt: daadwerkelijke exposure hangt van regelvolgorde en relevante interface af.  
**SHA-256 (publiek afgeleid bestand):** `39971e08dee0301b0deb25c91a9c5b123e555e9f760d1cc2bd4ac038b80c1ed9`

![M04-20261119-049 — gesaneerde CONFIG](<image(20261119-195743).png>)

---

### M04-20261119-050 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-195836).png  
**Beschrijving:** Detailpagina van de brede LAN IPv4-allow-regel toont de bron-/bestemmingsscope en actie Pass.  
**Bewijsgrens:** Configuratieobservatie; afgedwongen toegang niet rechtstreeks getest.  
**SHA-256 (publiek afgeleid bestand):** `306998a49859257321e530e7e39e809381d2924fbf37c08abedfeac591855809`

![M04-20261119-050 — gesaneerde CONFIG](<image(20261119-195836).png>)

---

### M04-20261119-051 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-195933).png  
**Beschrijving:** Detailpagina van een brede LAN IPv6-allow-regel toont actie Pass en ruime bron-/bestemmingsscope.  
**Bewijsgrens:** IPv6-policy aandachtspunt, niet automatisch bewijs voor een bereikbaar IPv6-pad.  
**SHA-256 (publiek afgeleid bestand):** `ebd531c779c1b1ff11a89725fa4f677374178798f16a41fc165b9a148c0737b0`

![M04-20261119-051 — gesaneerde CONFIG](<image(20261119-195933).png>)

---

### M04-20261119-052 | 2026-11-19 · CONFIG

**Onderwerp:** image(20261119-200026).png  
**Beschrijving:** pfSense OT-interfaceconfiguratie toont IPv6 Configuration Type op None.  
**Bewijsgrens:** Interface-instelling; andere IPv6-paden blijven afzonderlijk te toetsen.  
**SHA-256 (publiek afgeleid bestand):** `6fccc06a7ac59fb70544e22a2963091376ae909f348cd1578d19d0d2dbdf7dab`

![M04-20261119-052 — gesaneerde CONFIG](<image(20261119-200026).png>)

---

### M04-20261119-053 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-200227).png  
**Beschrijving:** PLC01-terminal toont IPv6-adressen en routetabel zonder zichtbare bruikbare globale IPv6-route.  
**Bewijsgrens:** Momentopname; link-local IPv6 kan nog aanwezig zijn. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `5eca9f12216b1339acadac2421447ecb78c5fd6aa9c3e482cb46a91d1d08e930`

![M04-20261119-053 — gesaneerde TEST](<image(20261119-200227).png>)

---

### M04-20261119-054 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-200353).png  
**Beschrijving:** Herhaalde PLC01-terminalweergave van de IPv6-route- en adrescontrole.  
**Bewijsgrens:** Duplicaat/aanvullende zichtbaarheid, geen nieuwe onafhankelijke test. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `5eca9f12216b1339acadac2421447ecb78c5fd6aa9c3e482cb46a91d1d08e930`

![M04-20261119-054 — gesaneerde TEST](<image(20261119-200353).png>)

---

### M04-20261119-055 | 2026-11-19 · TEST

**Onderwerp:** image(20261119-200554).png  
**Beschrijving:** FUXA01-terminal toont IPv6-adressen en routetabel zonder zichtbare bruikbare globale IPv6-route.  
**Bewijsgrens:** Momentopname; link-local IPv6 is niet hetzelfde als extern IPv6-bereik. De terminalinhoud is in de publieke afgeleide geheel gemaskeerd. De testuitkomst is daarom niet zelfstandig publiek verifieerbaar.  
**SHA-256 (publiek afgeleid bestand):** `b1ff8e9606c1cc62acd820eb442229d0213597fbd88680b24f243969ac1a0095`

![M04-20261119-055 — gesaneerde TEST](<image(20261119-200554).png>)