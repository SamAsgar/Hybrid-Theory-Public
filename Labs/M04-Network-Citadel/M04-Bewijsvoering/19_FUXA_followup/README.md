# FUXA-vervolgcontrole 15 november | M04 Network Citadel

**Aantal beelden:** 7  
**Classificatie:** PUBLIC · Gesaneerde afgeleide (onomkeerbare pixelmaskering) · geen origineel

[Terug naar M04-hoofdindex](../../M04-EVIDENCE-INDEX.md)

---

### M04-EV-204 | 2026-11-15 · CONFIG

**Onderwerp:** FUXA na vervolgwerkzaamheden  
**Beschrijving:** FUXA dashboard toont FUXA Server en PLC01-MOTOR connector/visualisatie.  
**Bewijsgrens:** Beeld alleen; live Modbus-telemetrie niet zonder verdere verificatie claimen.  
**SHA-256 (gesaneerde publicatie):** `2d27d239020037d5322440a480ee76706636ae54dbee1b1acee7b58e51e02a14`

![M04-EV-204 — FUXA na vervolgwerkzaamheden](<Screenshot 2026-11-15 193231.png>)

---

### M04-EV-205 | 2026-11-15 · CONFIG

**Onderwerp:** FUXA na vervolgwerkzaamheden  
**Beschrijving:** FUXA Connection Property toont ModbusTCP-configuratie voor gekoppelde PLC.  
**Bewijsgrens:** Formulierstatus, niet gelijk aan een succesvolle uitleestest.  
**SHA-256 (gesaneerde publicatie):** `4eeb9b9b020291dfea7b5ab631fae6b01a763b06c8e1029f7ab9a291fd8ef456`

![M04-EV-205 — FUXA na vervolgwerkzaamheden](<Screenshot 2026-11-15 193416.png>)

---

### M04-EV-206 | 2026-11-15 · CONFIG

**Onderwerp:** FUXA: PLC01-MOTOR connector/topologie  
**Beschrijving:** FUXA toont de verbinding tussen FUXA Server en PLC01-MOTOR. De PLC-connector vermeldt PLC01_OT_IP:502, Modbus-TCP en Slave ID 1; de statusindicator is groen. Dit documenteert de ingestelde OT-endpointconfiguratie en zichtbare verbindingsindicator.  
**Bewijsgrens:** Een groene FUXA-indicator toont de UI-status, maar bewijst op zichzelf geen geslaagde live registeruitlezing of volledige AC02-regressietest.  
**SHA-256 (gesaneerde publicatie):** `d62fbdfa6b02127518aaf8e545c328b3e11c75168bfe1dd19f264cc925eae6d4`

![M04-EV-206 — FUXA: PLC01-MOTOR connector/topologie](<Screenshot 2026-11-15 194828.png>)

---

### M04-EV-207 | 2026-11-15 · TEST

**Onderwerp:** Interne FUXA-variabele PLC01-MOTOR Connection Status  
**Beschrijving:** In Connections settings, bron FUXA Server, staat de interne numerieke variabele PLC01-MOTOR Connection Status met waarde 5 en timestamp 15-11-2026 19:51:23. Dit is een FUXA-statusvariabele en geen zichtbaar uitgelezen PLC-Modbus-register.  
**Bewijsgrens:** De betekenis van statuscode 5 is zonder bijbehorende FUXA-statusdefinitie niet betrouwbaar vast te stellen; niet als PASS labelen.  
**SHA-256 (gesaneerde publicatie):** `6cd428875556dcd0d79290e993db075b4bfa3670a5bfc26ae93e1ce22292029f`

![M04-EV-207 — Interne FUXA-variabele PLC01-MOTOR Connection Status](<Screenshot 2026-11-15 195126.png>)

---

### M04-EV-208 | 2026-11-15 · TROUBLESHOOT

**Onderwerp:** Troubleshootingdocumentatie: onderscheid interne status en PLC-tags  
**Beschrijving:** Samengesteld scherm met begeleidende technische instructie links en FUXA-tagoverzicht rechts. Het legt het onderscheid vast tussen de interne FUXA-verbindingsstatus en PLC01-MOTOR Modbus-tags, en motiveert het controleren van Motor_Start en Motor_Running.  
**Bewijsgrens:** Gedeeltelijk een screenshot van assistenttekst; instructie of analyse is geen zelfstandig technisch meetresultaat. Het rechterdeel toont wel de gekozen PLC01-MOTOR-taglijst.  
**SHA-256 (gesaneerde publicatie):** `b9419b1ec0a0e40df03783905ea2baf6c3264272415d40dda1a5001391ab9677`

![M04-EV-208 — Troubleshootingdocumentatie: onderscheid interne status en PLC-tags](<Screenshot 2026-11-15 195506.png>)

---

### M04-EV-209 | 2026-11-15 · CONFIG

**Onderwerp:** FUXA PLC01-MOTOR: Motor_Running en Motor_Start tags  
**Beschrijving:** FUXA Connections settings met PLC01-MOTOR geselecteerd: Motor_Running (Address 2, Bool, Value 0) en Motor_Start (Address 1, Bool, Value 0). Beschrijvingen zijn respectievelijk Motor running status en Motor start command. Getoonde timestamps zijn 15-11-2026 19:55:31.  
**Bewijsgrens:** De tags en getoonde nulwaarden zijn zichtbaar. Het screenshot bewijst nog niet dat deze adressen correct op OpenPLC-coils zijn gemapt, dat de waarden live zijn ververst of dat een toestandsovergang is getest.  
**SHA-256 (gesaneerde publicatie):** `a11a07c32227d76a3c399602e38c67f7f415f3b6be9539e29e146f954266c071`

![M04-EV-209 — FUXA PLC01-MOTOR: Motor_Running en Motor_Start tags](<Screenshot 2026-11-15 195539.png>)

---

### M04-EV-210 | 2026-11-15 · TEST

**Onderwerp:** FUXA PLC01-MOTOR: hertest tagwaarden 20:03  
**Beschrijving:** Vervolgopname van dezelfde PLC01-MOTOR-tags. Motor_Running (Address 2, Bool) en Motor_Start (Address 1, Bool) tonen beide 0 met zichtbare timestamp 15-11-2026 20:03:18. Beide waarden zijn ook bij de eerdere opname nul.  
**Bewijsgrens:** Twee waarnemingen op verschillende tijden zijn geen bewijs van actieve registerpolling of correcte mapping. Controleer een bewuste start/stop-overgang, verse tijdstempels en PLC/FUXA-correlatie voor een AC02-PASS.  
**SHA-256 (gesaneerde publicatie):** `9c97763683f203d2fe96113e034329d20941a990e6212908977142fec5b2854e`

![M04-EV-210 — FUXA PLC01-MOTOR: hertest tagwaarden 20:03](<Screenshot 2026-11-15 200322.png>)

---

