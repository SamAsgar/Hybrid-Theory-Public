# Statuslegenda | Hybrid-Theory

**Documentstatus:** **APPROVED — Sam, 02-11-2026**  
**Redactionele onderzoeksupdate:** 03-11-2026, CAT/ACE v0.4-duiding; oorspronkelijke engineeringverdicts niet gewijzigd.  
**Aanvulling:** 20-11-2026, §3a missie-, milestone- en mini-oefeningstatus (ter review in een publieke draft-PR); bestaande definities ongewijzigd.  
**Toepassing:** actuele README's, beleidsdocumenten, roadmap, labrapporten en duiding van historische logs. Een status mag alleen worden toegekend voor zover de vermelde scope en het bestaande bewijs dat ondersteunen.

## 1. Componentstatus

| Status | Betekenis |
|---|---|
| **PLANNED** | Ontworpen of voorgenomen; implementatie niet aangetoond. |
| **IMPLEMENTED** | Component of instelling aantoonbaar ingericht; dit bewijst niet automatisch alle gewenste werking. |
| **VERIFIED** | Specifieke componentfunctie daadwerkelijk gecontroleerd, met bewijs en testscope. |

## 2. Engineeringverdict (altijd met scope)

| Verdict | Betekenis |
|---|---|
| **PASS** | Vastgelegde acceptatiecriteria gehaald binnen de expliciete testscope. |
| **REWORK** | Aantoonbare afwijking of essentieel bewijs voor de betreffende controle ontbreekt; oorzaak en vervolgactie specificeren. |
| **EXCEPTION** | Door Sam bewust geaccepteerd en vastgelegd restrisico binnen afgebakende omstandigheden. Geen automatische PASS. |

**Geen vervangende verdicts:** `NOT VERIFIED`, `OPEN`, `INCONCLUSIVE` en `DONE` zijn geen afzonderlijke engineeringverdicts. Beschrijf ontbrekend bewijs in woorden en koppel het werk aan een werkstatus.

## 3. Werkstatus

| Status | Betekenis |
|---|---|
| **IN PROGRESS** | Werk is gestart; niet alle beoogde acceptatiecriteria zijn afgerond. |
| **PENDING** | Werk, besluit of meting moet nog worden uitgevoerd. |
| **PARKED** | Bewust uitgesteld met een aanleiding of voorwaarde voor heropening. |

### 3a. Missie-, milestone- en mini-oefeningstatus (20-11-2026)

Toegevoegd na het besluit van Sam van 20-11-2026 over het permanente missionmodel ([PUB-DEC-001](BESLUITENLOG.md#pub-dec-001--20-11-2026--permanent-missionmodel-en-m05-structuur)). Deze sectie voegt geen nieuwe engineeringverdicts toe; ze maakt duidelijk welke status bij welk niveau hoort.

| Niveau | Toegestane status | Afsluiting |
|---|---|---|
| **Main Mission** (M01–M05) | Missietype **PERMANENT**; werkstatus volgens §3 (**IN PROGRESS / PENDING / PARKED**) | **Nooit.** Geen `COMPLETE`, `MISSION COMPLETE` of missie-PASS |
| **Milestone** (bijv. M05-MS01) | **NOT ACHIEVED** (standaard) of **ACHIEVED**; de exitcriteria hebben een documentstatus (§4: DRAFT → PENDING OWNER APPROVAL → APPROVED; een voorstel is DRAFT) | **ACHIEVED** uitsluitend na expliciete acceptatie door Sam op vooraf vastgestelde exitcriteria |
| **Mini-oefening** (bijv. M05-MINI-01) | Werkstatus volgens §3, plus **PLANNED** vóór de start; de uitkomst is een scoped verdict (§2 of §5) | Sluit alleen de oefening zelf af; geen milestone- of missieafsluiting |
| **Afgebakende zelfstandige missie** | Nog niet gedefinieerd (latere categorie na M01–M05) | Eigen begin- en eindcriteria, na afzonderlijk besluit |

Een milestone vraagt een expliciete scope, vooraf vastgestelde acceptatiecriteria, bewijs, een beoordeling en acceptatie door Sam.

**Vijf dimensies niet vermengen:** (1) **missiestatus** (permanent + werkstatus), (2) **milestonevoortgang** (NOT ACHIEVED/ACHIEVED), (3) **technisch testverdict** (PASS/REWORK/EXCEPTION, altijd met scope), (4) **documentstatus** (§4) en (5) **owneracceptatie** (expliciet, gedateerd besluit van Sam). Een geslaagde deeltest is geen milestone-acceptatie; een APPROVED document is geen geslaagde test of geverifieerde control; een ACHIEVED milestone is geen missieafsluiting. Uitspraken die (nog) niet zijn aangetoond, heten **NOT ESTABLISHED** ([CAT/ACE §14](CAT_ACE_v0.4.md#14-roadmap-en-open-onderzoekspunten)); dat is geen verdict. Oudere formuleringen zoals "missieacceptatie" of "volledige missie-PASS" in gedateerde logs en issues blijven staan en worden gelezen als "milestone-acceptatie".

## 4. Documentstatus

| Status | Betekenis |
|---|---|
| **DRAFT** | Conceptdocument, nog niet door de eigenaar goedgekeurd. |
| **PENDING OWNER APPROVAL** | Voorgelegd aan Sam; besluit ontbreekt nog. |
| **APPROVED** | Uitdrukkelijk door Sam goedgekeurd, met datum en scope. |

**APPROVED** van een beleid betekent **niet** dat de daarin voorgeschreven technische controls zijn uitgevoerd of dat publicatiegates zijn gehaald.

## 5. Uitsluitend onderzoeksbeoordeling

**[CAT/ACE v0.4](CAT_ACE_v0.4.md):** `CONCEPT / NOT VALIDATED`. **CAT** bepaalt toepasselijke eisen, eigenaarschap en technische scope; **ACE = Audit, Cost & Efficiency** toetst controls en evidence, analyseert kosten en weegt veilige optimalisaties. ACE kan **INTERNAL, EXTERNAL of HYBRID** worden uitgevoerd, met vastgelegde onafhankelijkheidsgrenzen en **Revalidation** na wijzigingen. Dit is geen gecertificeerde auditmethode of automatische complianceverklaring.

**Onderzoeksschaal:** `PASS / REWORK / EXCEPTION / N/A / NOT VERIFIED`. Gebruik deze schaal uitsluitend voor een geselecteerde onderzoeks- of benchmarkeis en label die uitkomst als **onderzoeksbeoordeling**; vermeng haar niet met een operationeel engineeringverdict.

- `N/A`: aantoonbaar niet van toepassing op het geselecteerde onderzoeksscenario, met reden.
- `NOT VERIFIED`: onvoldoende onderzoeksbewijs om de hypothese/control te beoordelen.
- De overige drie termen hebben dezelfde basisbetekenis als in het engineeringverdict, maar gelden uitsluitend voor de betreffende **onderzoeksbeoordeling**.

## 6. Historische labels en publicatiereview

Oudere logboeken bevatten destijds gebruikte labels zoals `OPEN`, `GEPARKEERD`, `VERIFIED DIAGNOSTIC`, `INCONCLUSIVE` en `NOT FULLY VERIFIED`. Die zijn **historische formuleringen**, geen uitbreiding van de huidige statusset. Lees ze binnen de oorspronkelijke datum en scopespecificatie; actuele interpretatie staat in de latere rapporten en [roadmap](../projectlogboeken/ROADMAP.md).

**GitHub-zichtbaarheid: PUBLIC** (gecontroleerd 05-11-2026). De beeld-/PDF-review, Git-geschiedenis, identifierscan en overige publicatiegates zijn nog niet volledig aangetoond. Dit is **geen EXCEPTION en geen publicatie-PASS**. Raadpleeg het [goedgekeurde publicatiebeleid](PUBLICATIEBELEID.md).

## 7. Bewijsdiscipline

Een screenshot is `CAPTURED` als gewone beschrijving van een bestand, **geen** formeel engineeringverdict. Vermeld bij iedere PASS: component of control, protocol/toets, testmoment, scope, bron/evidence en beperkingen. AI-review, een GitHub-commit of een plannenlijst zijn op zichzelf geen technische verificatie.
