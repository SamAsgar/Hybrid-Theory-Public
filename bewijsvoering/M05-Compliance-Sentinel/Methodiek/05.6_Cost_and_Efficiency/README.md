# 05.6 — Cost & Efficiency | M05 Compliance Sentinel

**Hoofdstukstatus:** structuur **APPROVED**; inhoudelijk werk **PENDING** · [Terug naar M05](../../README.md)

## Doel

Inzichtelijk maken wat beveiliging en de **beoordeling** ervan kosten, en onderzoeken of een alternatief **dezelfde of een betere beveiligingsuitkomst** met minder middelen bereikt. Efficiëntie is veilig resultaat per ingezette middelen, niet de laagste rekening. "Geen verantwoorde besparing gevonden" is een legitieme uitkomst.

## Onderzoeksvragen

1. Wat zijn de **directe** kosten (hardware, licenties, cloud, energie) en de **indirecte** kosten (beheertijd, complexiteit, downtime, hersteltijd) van een control?
2. Hoeveel **audit- en beheerinspanning** kost het om de werking van die control aan te tonen en te onderhouden?
3. Welke **alternatieve beheersmaatregelen** bereiken een vergelijkbare risicoreductie, en tegen welke kosten?
4. Is de maatregel **proportioneel** ten opzichte van het risico en de context?
5. Wat is de **beveiligingseffectiviteit** van elk alternatief, en blijft die gelijk of beter?
6. Welke kosten zijn **gemeten** en welke zijn **geschat**? Wanneer kost automatisering meer onderhoud en foutkans dan ze bespaart?

## Beoordelingsmethodiek

- Tijdregistratie van beoordelingsstappen per casus (**MEASURED**).
- Een kostenbaseline en aannameregister, met periode en eenheid (**ESTIMATED** waar niet gemeten).
- Vergelijking van de status quo met ten minste één alternatief onder **dezelfde** beveiligings-, beschikbaarheids- en risicogrenzen.
- Een trade-offmatrix met kosten, beveiligingseffect, complexiteit en onderhoudslast.
- Toepassing van **ACE-Cost** en **ACE-Efficiency** uit [CAT/ACE v0.4 §2–§3](../../../../governance/CAT_ACE_v0.4.md#2-conceptueel-model-cat-structuur-en-ace-beoordelingsfunctie).

| Vergelijkingsas | Wat wordt vastgelegd | Voorwaarde |
|---|---|---|
| Directe kosten | Hardware, licenties, cloud, energie | Zelfde periode en eenheid |
| Indirecte kosten | Beheer- en hersteltijd, downtime, complexiteit | Bron en aanname expliciet |
| Auditinspanning | Tijd om werking aan te tonen en te herhalen | Gemeten waar mogelijk |
| Onderhoudslast | Updates, regelreview, scriptonderhoud | Over de levensduur bezien |
| Beveiligingseffectiviteit | Dezelfde getoetste uitkomst (bijv. dezelfde deny-flows geblokkeerd) | Gelijk of beter, anders geen efficiëntiewinst |
| Proportionaliteit | Verhouding tot risico en context | Gemotiveerd, niet aangenomen |

## Toepasselijke frameworks

CAT/ACE v0.4 (Audit, Cost & Efficiency; experimenteel), COBIT 2019 (waardecreatie en resource-optimalisatie), CIS Controls v8.1 Implementation Groups (prioritering naar context) en ISO/IEC 27001:2022 hoofdstuk 6.1.3 (proportionele risicobehandeling). Er bestaat geen algemeen aanvaarde norm voor "security-ROI"; claims daarover blijven hypothesen.

## Praktische context binnen Hybrid-Theory

- Voor M04 bestaan alleen **interne planningsramingen** (ESTIMATED); er zijn nog geen gemeten beoordelingsuren. Interne financiële en planningsgegevens worden niet gepubliceerd.
- **Voorbeeld (gepland, niet uitgevoerd):** in MINI-01 de werkelijke beoordelingstijd registreren en afzetten tegen het rekenvoorbeeld in [CAT/ACE §3.3](../../../../governance/CAT_ACE_v0.4.md#33-praktijkvoorbeeld-1-pfsense--segmentatie-tijdelijke-internetregel-en-rule-review). Dat voorbeeld is daar uitdrukkelijk HYPOTHETICAL.
- **Kandidaat-trade-off (HYPOTHESIS):** een brede toestaanregel tegenover smalle least-privilege-regels met een herhaalbare regressietest. De smalle variant vraagt meer ontwerp- en testtijd, maar mogelijk minder auditlast per wijziging.

## Verwachte evidence en deliverables

- Eén ACE-kosten/efficiëntieregel per casus in de casusmatrix.
- Tijdregistratie (MEASURED) en een aannameregister (ESTIMATED), met periode.
- Een trade-offnotitie met het gekozen of afgewezen alternatief en de reden.

## Kwaliteitscriteria

- MEASURED en ESTIMATED worden nooit vermengd.
- Een besparing telt alleen bij een aantoonbaar gelijkwaardige beveiligingsuitkomst.
- Elke kostenregel noemt periode, eenheid en bron.

## Beperkingen

- Geen gefingeerde besparingen.
- Labkosten (eigen hardware, evaluatielicenties) zijn niet representatief voor een organisatie; extrapolatie blijft een hypothese.
- Kostenonderzoek mag lopen terwijl een control REWORK is, maar autoriseert geen verlaging van beveiliging.

## Relaties met andere hoofdstukken

Gebruikt de controlkeuze uit [05.2](../05.2_Risk_to_Control_Traceability/README.md) en de testinspanning uit [05.3](../05.3_Control_Effectiveness/README.md). Weegt herstellen tegenover accepteren in [05.4](../05.4_Gaps_and_Exceptions/README.md) en de kosten van onafhankelijkheid in [05.5](../05.5_Assurance_and_Independence/README.md). Redundantie tegenover concentratie van afhankelijkheden ([05.7](../05.7_Systemic_Risk/README.md)) is vaak een kostenvraag.

## Huidige onderzoeksstatus

**PENDING.** Er is nog geen M05-kostenmeting uitgevoerd.
