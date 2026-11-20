# 05.3 — Control Effectiveness | M05 Compliance Sentinel

**Hoofdstukstatus:** structuur **APPROVED**; inhoudelijk werk **PENDING** · [Terug naar M05](../../README.md)

## Doel

Per control **drie afzonderlijke vragen** beantwoorden, plus een vierde over het bewijs zelf:

| Dimensie | Vraag | Typisch bewijs |
|---|---|---|
| **Design effectiveness** | Dekt het ontwerp het risico, inclusief alternatieve paden? | Architectuur, zonemodel, policy, regelontwerp |
| **Implementation verification** | Is de configuratie aantoonbaar gelijk aan het ontwerp? | Gedateerde configuratie-export of -beelden, hash, wijzigingsrecord |
| **Operating effectiveness** | Werkt de control feitelijk onder de relevante omstandigheden? | Positieve én negatieve tests met log- en tijdcorrelatie |
| **Evidence quality** | Hoe betrouwbaar is het bewijs voor elk van de drie? | Herkomst, tijdstempel, volledigheid, reproduceerbaarheid |

**Waarom configuratiebewijs niet genoeg is:** een configuratiebeeld toont wat er is *ingesteld*, niet wat er *gebeurt*. Regelvolgorde, een bredere regel die eerder matcht, NAT-paden, IPv6, verkeer dat de control niet passeert of een wijziging ná de opname kunnen de werking anders maken dan het beeld suggereert. Operating effectiveness vraagt dus een test van het gedrag, inclusief een poging die moet falen.

## Onderzoeksvragen

1. Dekt het controlontwerp het risico uit [05.2](../05.2_Risk_to_Control_Traceability/README.md), inclusief alternatieve paden (IPv6, UDP, beheerpaden, WAN)?
2. Is de geïmplementeerde configuratie gelijk aan het ontwerp, en is dat verifieerbaar (export, hash, datum)?
3. Welke werking is aangetoond met **positieve én negatieve** tests, met tijd- en logcorrelatie?
4. Hoe betrouwbaar is elk bewijsstuk?
5. Blijft een eerdere PASS geldig na een wijziging (drift, continuous assurance)?
6. Welke conclusie is herleidbaar, en welke reikt verder dan het bewijs?

## Beoordelingsmethodiek

- **Design review:** regelvolgorde, default deny, uitzonderingen, beheerpaden, NAT-associaties.
- **Implementation verification:** configuratie-export of gedateerde configuratiebeelden vergelijken met het ontwerp.
- **Operating effectiveness:** bestaande testuitslagen beoordelen. Ontbrekende tests worden doorverwezen naar de missie die de control bezit; M05 dupliceert ze niet.
- **Evidence quality:** per bron een herkomstlabel (OBSERVED / DOCUMENTED / AI-INTERPRETED / SIMULATED / HYPOTHESIS).
- **Conclusie:** per control een herleidbaar, scoped oordeel.

## Toepasselijke frameworks

ISO/IEC 27002:2022 (implementatierichtlijn per control), NIST SP 800-53A Rev. 5 (Examine / Interview / Test, diepgang en dekking), CIS Controls v8.1 Assessment Specification (meetbare Safeguards, bijv. Control 12 Network Infrastructure Management) en ISO/IEC 27008 (beoordeling van controls). Selectie per casus.

## Praktische context binnen Hybrid-Theory

**Voorbeeld (gepland, niet uitgevoerd) — A.8.22 in MINI-01**, uitsluitend op basis van publiek, gesaneerd bewijs:

| Dimensie | Publieke bron | Publiek gedocumenteerde stand (scoped, geen M05-oordeel) |
|---|---|---|
| Ontwerp | [Netwerkontwerp](../../../../architectuur/NETWERKONTWERP.md) | Zones achter de firewall met default deny als **ontwerp** (DOCUMENTED) |
| Implementatie | [M04-dossier](../../../M04-Network-Citadel/README.md) en [galerij](../../../M04-Network-Citadel/M04-GALERIJ.md) | OT-interface en regels zijn in gesaneerde beelden zichtbaar (DOCUMENTED) |
| Werking | [M04 fase 20](../../../M04-Network-Citadel/M04-Bewijsvoering/20_OT_segmentation_and_regression/README.md), [M04-GAPS](../../../M04-Network-Citadel/M04-GAPS.md#aanvulling-19-november--gerichte-deeltests) | Gerichte deny-flows met BLOCK-events (OBSERVED, scoped); integrale AC04/AC07-matrix **PENDING** |

Het publieke bewijs ondersteunt dus hooguit een **scoped** oordeel over specifieke stromen, geen integrale werking van A.8.22. Dit voorbeeld illustreert de beoordelingsvorm; het is niet het MINI-01-resultaat.

## Verwachte evidence en deliverables

- Per control drie gescheiden oordelen (design / implementation / operating effectiveness), elk met bronverwijzing.
- Een bewijskwaliteitsnotitie per bron.
- Een lijst van negatieve tests die het oordeel dragen, en van negatieve tests die ontbreken.
- Een scoped verdict volgens de onderzoeksschaal (PASS / REWORK / EXCEPTION / N/A / NOT VERIFIED).

## Kwaliteitscriteria

- Elk van de drie oordelen heeft een eigen bron; geen enkel oordeel wordt uit een ander afgeleid.
- Een werkingsoordeel steunt op ten minste één relevante negatieve test met logcorrelatie.
- Een PASS vervalt bij een relevante wijziging tot een hertest; er is geen automatische overerving.

## Beperkingen

- Een regelscreenshot is geen werkingsbewijs; een timeout is geen bewezen blokkade zonder logcorrelatie ([Statuslegenda §7](../../../../governance/STATUSLEGENDA.md#7-bewijsdiscipline)).
- Verkeer dat niet via de control loopt, kan de control niet bewijzen.
- FAILs en mislukte tests blijven als historisch bewijs staan.
- Publiek gesaneerde beelden kunnen details missen die voor een volledige beoordeling nodig zijn.

## Relaties met andere hoofdstukken

Toetst de controls uit [05.2](../05.2_Risk_to_Control_Traceability/README.md). Tekortkomingen worden gaps in [05.4](../05.4_Gaps_and_Exceptions/README.md). De sterkte van het oordeel wordt begrensd door [05.5](../05.5_Assurance_and_Independence/README.md). De testinspanning is input voor [05.6](../05.6_Cost_and_Efficiency/README.md). Controls die van dezelfde component afhangen, gaan naar [05.7](../05.7_Systemic_Risk/README.md).

## Huidige onderzoeksstatus

**PENDING.** Er is nog geen M05-controloordeel uitgevoerd. M04-testuitslagen behouden hun eigen scope en status.
