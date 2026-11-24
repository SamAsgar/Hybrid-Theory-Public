# C10 · CAT/ACE

Welke claims, afhankelijkheden en kosten van de eigen methode zijn aantoonbaar?

Dit chapter onderzoekt de eigen methode. De inhoudelijke chapters en bronmissies houden hun eigen bewijsketens en besluiten.

## Overdrachtscontract C01–C09 → C10 (ontwerpafspraak)

**Doel.** C01–C09 passen CAT/ACE als onderzoekslens toe op hun eigen mini-oefeningen. C10 onderzoekt vervolgens expliciet de **claims en beperkingen van de methode zelf** via Claims Audit (MINI-02), Dependency Atlas (MINI-05) en Measured Cost Baseline (MINI-17). C10 wordt geen vierde CAT-laag, centraal bewijsarchief, tweede SSOT, technisch verdictsysteem of extra goedkeuringsorgaan.

**Eenheid van overdracht:** een *bronverwijzing naar één gescopeerde claim of bevinding*, vastgelegd in het oorspronkelijke chapter of de bronmissie. Bij een daadwerkelijk gestarte mini worden de volgende velden opgenomen **voor zover toepasselijk en beschikbaar**; ontbrekende waarden blijven expliciet `NOT VERIFIED` of `N/A` met reden. Er worden geen fictieve records vooraf ingevuld.

| Veld | Betekenis / grens |
|---|---|
| `mini_id`, `chapter_id`, `claim_id` | Stabiele herleidbare referenties; geen nieuw centraal register |
| `claim_text`, `scope`, `as_of` | Exacte uitspraak, grens van de beoordeling en peildatum |
| `source_mission`, `source_ref`, `source_revision` | Canonieke bronlocatie en bronversie/commit waar controleerbaar |
| `evidence_id_or_ref`, `evidence_integrity_ref` | Link naar oorspronkelijk bewijs; hash alleen indien vastgesteld in het brondossier |
| `risk_id`, `owner_ref`, `control_ref`, `framework_version` | Koppelingen naar toepasselijke risico-, eigenaars- en controlbesluiten |
| `design_state`, `implementation_state`, `operation_state` | Gescheiden beoordeling van opzet, implementatie en werking, zonder een nieuw technisch PASS te claimen |
| `verdict_ref`, `exceptions_ref`, `residual_risk_ref` | Verwijzing naar origineel besluit, uitzonderingen en restrisico |
| `provenance`, `reviewer_role`, `review_limits` | OBSERVED / AI-INTERPRETED / SIMULATED / HYPOTHESIS en mogelijke belangenconflicten |
| `dependency_ref`, `dependency_confidence` | Gedeelde afhankelijkheid als OBSERVED of HYPOTHESIS, inclusief bron en tegenbewijs |
| `cost_ref`, `cost_basis`, `comparison_scope` | MEASURED / ESTIMATED, periode en vergelijkbare beveiligings- en beschikbaarheidsgrens |

**Verwerkingsroute:**

1. **C01–C09:** mini legt scope, primaire framework-/criteriumkeuze en relevante bewijsverwijzingen vast; alle zeven methodiekvragen 05.1–05.7 blijven behandeld of gemotiveerd N/A.
2. **C10 / MINI-02:** toets expliciete claims aan bron, tijd, reikwijdte en tegenbewijs. Geen onafhankelijke assurance claimen op grond van een AI-review.
3. **C10 / MINI-05:** onderzoek gedocumenteerde én veronderstelde gedeelde afhankelijkheden. Een relatie is niet automatisch causaal.
4. **C10 / MINI-17:** gebruik aantoonbaar gemeten kosten waar beschikbaar en onderscheid ramingen; vergelijk alternatieven alleen onder dezelfde relevante beveiligingsgrens.
5. **Terugkoppeling:** C10 legt een eigen *methodiekbevinding* en verwijzing naar de bronclaim vast. Een technisch verdict of restrisicobesluit wijzigen kan alleen in het bevoegde brondossier met eigenaarbesluit en eventueel revalidatie.

**Publicatiegrens:** overdracht naar een publieke variant bevat uitsluitend afzonderlijk gecontroleerde, gesaneerde claimmetadata en publiek toegankelijke bronlinks. Geen private URL's, echte infrastructuuridentificatoren, interne risico-details, ongepubliceerde hashes of bewijsstukken kopiëren. Is een veld niet openbaar te onderbouwen, markeer het `REDACTED / NOT PUBLICLY VERIFIED` in plaats van een interne bron bloot te leggen. Deze procesafspraak is geen afgeronde publicatiegate, assessment of owneracceptatie.

**Status:** documentatie-/overdrachtsontwerp; bestaande mini-oefeningen behouden hun oorspronkelijke `PLANNED` of andere canonieke status. Geen automatische CAT/ACE-validatie, ISO-conformiteit of milestone-PASS.

**Mini-oefeningen**

- [M05-MINI-02 · Claims Audit](../README.md#idx-m05-mini-02)
- [M05-MINI-05 · Dependency Atlas](../README.md#idx-m05-mini-05)
- [M05-MINI-17 · Measured Cost Baseline](../README.md#idx-m05-mini-17)

**Werkwijze en bronnen**

Elke mini behandelt [de zeven permanente onderzoekshoofdstukken 05.1–05.7](../Methodiek/). Leg per vraag het bewijs, het ontbrekende bewijs of de reden voor N/A vast.

CAT/ACE v0.4 heeft de status CONCEPT / NOT VALIDATED. ISO 19011 en NIST SP 800-53A zijn mogelijke methodische referenties. Kaderbronnen: **NOT VERIFIED voor README-gebruik** tot verificatie van editie en casustoepassing. De casuskeuze, versie en rol staan in het [Framework Register](../README.md#6-framework-register).

[CAT/ACE v0.4](../../../Governance/CAT_ACE_v0.4.md) · [Statuslegenda](../../../Governance/STATUSLEGENDA.md) · [Methodiek 05.5](../Methodiek/05.5_Assurance_and_Independence/README.md) · [Methodiek 05.6](../Methodiek/05.6_Cost_and_Efficiency/README.md).

## Beoordelaar en bewijslimiet

Leg bij iedere conclusie de beoordelaar, diens betrokkenheid, de opdracht, de bron en de grens van het bewijs vast.

| Beoordeling | Wat de lezer kan controleren |
|---|---|
| Zelfbeoordeling | De eigenaar benoemt de eigen rollen in ontwerp, uitvoering en beoordeling. De conclusie geldt voor het onderzochte criterium en de gekozen casus. |
| AI-ondersteunde duiding | Scheid waarneming, interpretatie en hypothese. Herhaling door een model levert geen tweede waarneming op. |
| Technische peerreview | Leg de opdracht, geraadpleegde bronnen, eerder eigen werk van de reviewer en concrete afwijkingen vast. Claude is een tweede lezer binnen het project. |
| Formeel onafhankelijke assurance | Vereist een afzonderlijke opdracht, passende expertise, onafhankelijkheid, criteria, bewijs en een vastgesteld rapport. Voor M05 is zo’n rapport niet vastgesteld. |

De **Claims Audit** onderzoekt per claim herkomst, reikwijdte en tegenbewijs. De **Dependency Atlas** verbindt een claimpaar aan één aantoonbare of veronderstelde gedeelde afhankelijkheid. De **Measured Cost Baseline** registreert datum, activiteit en werkelijk bestede tijd met meetbasis (**MEASURED**). Een raming krijgt **ESTIMATED**. Een efficiëntievergelijking vereist een vergelijkbare scope en beveiligingsgrens. Deze drie beoordelingen zijn intern en experimenteel.

Kaderselectie begint bij [C01 · Governance, scope en ISMS](../C01_Governance_Scope_ISMS/README.md).

De technische missie beheert het bewijs en de testuitslagen. M05 documenteert bron, datum, reikwijdte en begrenzing van de interpretatie.

> **Historische bronpassage** · peilcommit `98bd282`, oorspronkelijk pad `Portfolio/M05-Compliance-Sentinel/M05-Compliance-Sentinel/README.md`. [Permalink](https://github.com/SamAsgar/Hybrid-Theory-Public/blob/98bd28252b2adde6a2c129b1d9d3d12641e4fa2d/Portfolio/M05-Compliance-Sentinel/M05-Compliance-Sentinel/README.md). De onderstaande passage bewaart de toenmalige status. De [mini-index](../README.md#mini-exercise-index) bevat de actuele werkstatus.

<!-- BEGIN HISTORISCHE BRON -->

# M05 — Compliance Sentinel | M05-assessmentdossier

**Status:** **PENDING** — nog geen M05-assessment voor deze missie · [Terug naar M05](../README.md)

Dit dossier bevat uitsluitend M05-assessments over de werkwijze van M05 zelf, zoals kaderselectie, bewijsherkomst en de grenzen van AI-ondersteunde reviews. De methodiek staat één keer in [Methodiek](../Methodiek/) en wordt hier niet herhaald. Bewijs en technische verdicts blijven in de missie zelf ([M05-overzicht](../README.md)); M05 verwijst daarnaar, kopieert geen bewijs en wijzigt geen verdicts.

| Onderdeel | Methodiek | Assessment voor M05 | Status |
|---|---|---|---|
| 05.1 | [Scope & Applicability](../Methodiek/05.1_Scope_and_Applicability/README.md) | Nog geen assessment | **PENDING** |
| 05.2 | [Risk-to-Control Traceability](../Methodiek/05.2_Risk_to_Control_Traceability/README.md) | Nog geen assessment | **PENDING** |
| 05.3 | [Control Effectiveness](../Methodiek/05.3_Control_Effectiveness/README.md) | Nog geen assessment | **PENDING** |
| 05.4 | [Gaps & Exceptions](../Methodiek/05.4_Gaps_and_Exceptions/README.md) | Nog geen assessment | **PENDING** |
| 05.5 | [Assurance & Independence](../Methodiek/05.5_Assurance_and_Independence/README.md) | Nog geen assessment | **PENDING** |
| 05.6 | [Cost & Efficiency](../Methodiek/05.6_Cost_and_Efficiency/README.md) | Nog geen assessment | **PENDING** |
| 05.7 | [Systemic Risk](../Methodiek/05.7_Systemic_Risk/README.md) | Nog geen assessment | **PENDING** |

Een submap per assessment wordt pas aangemaakt wanneer het assessment daadwerkelijk start. Uitkomsten zijn scoped onderzoeksbeoordelingen (INTERNAL / AI-ondersteund) en geen milestone-acceptatie.

<!-- EINDE HISTORISCHE BRON -->
