# Statuslegenda | Hybrid-Theory

**Documentstatus:** **APPROVED — Project Owner, 02-11-2026**  
**Redactionele onderzoeksupdate:** 03-11-2026, CAT/ACE v0.4-duiding; oorspronkelijke engineeringverdicts niet gewijzigd.  
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
| **EXCEPTION** | Door de Project Owner bewust geaccepteerd en vastgelegd restrisico binnen afgebakende omstandigheden. Geen automatische PASS. |

**Geen vervangende verdicts:** `NOT VERIFIED`, `OPEN`, `INCONCLUSIVE` en `DONE` zijn geen afzonderlijke engineeringverdicts. Beschrijf ontbrekend bewijs in woorden en koppel het werk aan een werkstatus.

## 3. Werkstatus

| Status | Betekenis |
|---|---|
| **IN PROGRESS** | Werk is gestart; niet alle beoogde acceptatiecriteria zijn afgerond. |
| **PENDING** | Werk, besluit of meting moet nog worden uitgevoerd. |
| **PARKED** | Bewust uitgesteld met een aanleiding of voorwaarde voor heropening. |

## 4. Documentstatus

| Status | Betekenis |
|---|---|
| **DRAFT** | Conceptdocument, nog niet door de eigenaar goedgekeurd. |
| **PENDING OWNER APPROVAL** | Voorgelegd aan de Project Owner; besluit ontbreekt nog. |
| **APPROVED** | Uitdrukkelijk door de Project Owner goedgekeurd, met datum en scope. |

**APPROVED** van een beleid betekent **niet** dat de daarin voorgeschreven technische controls zijn uitgevoerd of dat publicatiegates zijn gehaald.

## 5. Uitsluitend onderzoeksbeoordeling

**[CAT/ACE v0.4](CAT_ACE_v0.4.md):** `CONCEPT / NOT VALIDATED`. **CAT** bepaalt toepasselijke eisen, eigenaarschap en technische scope; **ACE = Audit, Cost & Efficiency** toetst controls en evidence, analyseert kosten en weegt veilige optimalisaties. ACE kan **INTERNAL, EXTERNAL of HYBRID** worden uitgevoerd, met vastgelegde onafhankelijkheidsgrenzen en **Revalidation** na wijzigingen. Dit is geen gecertificeerde auditmethode of automatische complianceverklaring.

**Onderzoeksschaal:** `PASS / REWORK / EXCEPTION / N/A / NOT VERIFIED`. Gebruik deze schaal uitsluitend voor een geselecteerde onderzoeks- of benchmarkeis en label die uitkomst als **onderzoeksbeoordeling**; vermeng haar niet met een operationeel engineeringverdict.

- `N/A`: aantoonbaar niet van toepassing op het geselecteerde onderzoeksscenario, met reden.
- `NOT VERIFIED`: onvoldoende onderzoeksbewijs om de hypothese/control te beoordelen.
- De overige drie termen hebben dezelfde basisbetekenis als in het engineeringverdict, maar gelden uitsluitend voor de betreffende **onderzoeksbeoordeling**.

## 6. Historische labels en publicatiereview

Oudere logboeken bevatten destijds gebruikte labels zoals `OPEN`, `GEPARKEERD`, `VERIFIED DIAGNOSTIC`, `INCONCLUSIVE` en `NOT FULLY VERIFIED`. Die zijn **historische formuleringen**, geen uitbreiding van de huidige statusset. Lees ze binnen de oorspronkelijke datum en scopespecificatie; actuele interpretatie staat in de latere rapporten en [roadmap](../projectlogboeken/ROADMAP.md).

**Repositoryzichtbaarheid (laatst gecontroleerd 02-11-2026): PRIVATE; eerder PUBLIC.** De beeld-/PDF-review, Git-geschiedenis, identifierscan en overige publicatiegates zijn nog niet volledig aangetoond. Dit is **geen EXCEPTION en geen publicatie-PASS**. Raadpleeg het [goedgekeurde publicatiebeleid](PUBLICATIEBELEID.md) en de [migratiestatus](../MIGRATIE_STATUS.md).

## 7. Bewijsdiscipline

Een screenshot is `CAPTURED` als gewone beschrijving van een bestand, **geen** formeel engineeringverdict. Vermeld bij iedere PASS: component of control, protocol/toets, testmoment, scope, bron/evidence en beperkingen. AI-review, een GitHub-commit of een plannenlijst zijn op zichzelf geen technische verificatie.
