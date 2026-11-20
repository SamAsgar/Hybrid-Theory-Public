# 05.5 — Assurance & Independence | M05 Compliance Sentinel

**Hoofdstukstatus:** structuur **APPROVED**; inhoudelijk werk **PENDING** · [Terug naar M05](../../README.md)

## Doel

Bepalen **hoeveel vertrouwen** een uitspraak over een control verdient, gegeven wie het bewijs heeft gemaakt, wie het heeft beoordeeld en met welke methode. Assurance is geen eigenschap van de control maar van de beoordeling. Dit hoofdstuk begrenst ook expliciet wat compliance- en auditclaims **niet** kunnen bewijzen.

## Begrippen

| Begrip | Betekenis in M05 |
|---|---|
| **Internal assurance** | Beoordeling door de eigen organisatie (security, risk, interne audit). Kan objectief zijn, maar is niet per definitie onafhankelijk |
| **External assurance** | Beoordeling door een externe partij met afgesproken scope en bewijstoegang. Extern is niet automatisch onafhankelijk (bijv. bij eigen advieswerk) |
| **Hybrid review** | Interne voorbereiding en tests, gevolgd door een risicogerichte tweede beoordeling door een andere partij |
| **AI-assisted review** | Duiding of kritiek door een AI-assistent; ondersteunend, nooit zelfstandig bewijs of formele audit |
| **Shared assumptions** | Dezelfde aannames in ontwerp, uitvoering én beoordeling, waardoor een fout niet wordt opgemerkt |
| **Circular assurance** | Een beoordeling die steunt op bewijs dat door dezelfde partij of hetzelfde hulpmiddel is ontworpen en geduid |
| **Audit trail** | De herleidbare keten bron → beoordeling → conclusie → besluit, met datums en beoordelaars |
| **Evidence reliability** | De mate waarin bewijs authentiek, volledig, tijdgebonden en reproduceerbaar is |

## Onderzoeksvragen

1. Is de beoordeling intern, extern of hybride, en welke onafhankelijkheid is feitelijk aanwezig ([CAT/ACE §3.2](../../../../governance/CAT_ACE_v0.4.md#32-wie-voert-ace-uit-internal-external-en-hybrid))?
2. Welke audit trail verbindt bewijs, beoordelaar, datum en conclusie, en is die reproduceerbaar?
3. Welk deel van het bewijs heeft Sam zelf waargenomen, en welk deel heeft een AI geïnterpreteerd?
4. Waar ontstaat circulaire assurance?
5. Welke blinde vlekken heeft AI-assisted review: gedeelde trainingsbias, geen live toegang tot systemen, afhankelijkheid van aangeleverde tekst en overtuigende maar onjuiste duiding?
6. Wat mag op basis van deze beoordeling wél worden geclaimd, en wat uitdrukkelijk niet?

## Beoordelingsmethodiek

- Per beoordeling vastleggen: wie maakte de control, wie voerde de test uit, wie beoordeelde, welke adviesrol speelde mee en welke belangenconflicten bestaan.
- Een audit trail per casus: bron → beoordeling → conclusie → besluit, met links en datums.
- Een herkomstlabel per bewijsstuk (OBSERVED / DOCUMENTED / AI-INTERPRETED / SIMULATED / HYPOTHESIS).
- Een assurance-statement met expliciete grenzen.
- Bij een hybride review de tweede beoordelaar en een eventuele onafhankelijke hertest benoemen.

## Toepasselijke frameworks

ISO 19011:2026 (auditprincipes, bewijs, onafhankelijkheid, competentie; alleen bij auditvragen), ISAE 3000, ISAE 3402 en SOC 2 als **denkkader** voor zekerheidsniveaus en systeemgrenzen ([Wet- en regelgevingskaders](../../../../governance/WET_EN_REGELGEVING.md)), NIST SP 800-53A (assessorrollen en assessmentdiepgang), en het three-lines-model als begripskader voor interne verdedigingslinies.

## Praktische context binnen Hybrid-Theory

- **Feitelijke situatie:** één persoon ontwerpt, bouwt en test. AI-assistenten (onder meer ChatGPT en Claude) begeleiden en reviewen ([AI-samenwerking](../../../../ai-samenwerking/README.md)). Elke M05-beoordeling is daarom **INTERNAL / AI-ONDERSTEUND (SELF-ASSESSMENT)**, tenzij aantoonbaar een werkelijke onafhankelijke review plaatsvindt.
- **Circulariteit:** M04-tests zijn deels met AI-begeleiding ontworpen en worden in MINI-01 opnieuw met AI-ondersteuning beoordeeld. MINI-01 legt daarom per bewijsstuk vast of het OBSERVED of AI-INTERPRETED is.
- **Meerdere AI-reviews vormen geen onafhankelijke, geaccrediteerde audit.** Twee of meer AI-modellen die het eens zijn, zijn geen onafhankelijke bevestiging: ze kunnen dezelfde aannames delen en zien dezelfde aangeleverde tekst.

## Verwachte evidence en deliverables

- Een assurance-statement per casus: scope, beoordelingsvorm, onafhankelijkheidsgraad, zekerheidsniveau (beperkt of redelijk als denkkader, niet als attestatie) en uitgesloten claims.
- Een herkomsttabel van het gebruikte bewijs.
- Een lijst van bekende AI-blinde vlekken die in de casus relevant waren.

## Kwaliteitscriteria

- Elke conclusie is via de audit trail terug te voeren op een bron en een beoordelaar.
- De onafhankelijkheidsgraad is feitelijk beschreven, niet aangenomen.
- Een tegenstrijdige of negatieve bevinding wordt even zichtbaar gerapporteerd als een positieve.

## Beperkingen

- Geen uitspraak als "voldoet aan ISO 27001", "compliant" of "geaudit" op basis van een lab-assessment.
- Een Annex A-controlassessment bewijst geen werkend ISMS (hoofdstukken 4–10) en geen certificeerbaarheid.
- Intern is niet automatisch subjectief, en extern is niet automatisch onafhankelijk; de feitelijke rollen tellen.
- Voor publieke lezers is een deel van het onderliggende bewijs niet publiek en dus niet onafhankelijk verifieerbaar.

## Relaties met andere hoofdstukken

Begrenst de conclusies van [05.3](../05.3_Control_Effectiveness/README.md) en [05.4](../05.4_Gaps_and_Exceptions/README.md). De scope uit [05.1](../05.1_Scope_and_Applicability/README.md) bepaalt wat de assurance kan dekken. De kosten van meer onafhankelijkheid vallen onder [05.6](../05.6_Cost_and_Efficiency/README.md). Afhankelijkheid van één beoordelaar en dezelfde hulpmiddelen is zelf een gedeelde afhankelijkheid in [05.7](../05.7_Systemic_Risk/README.md).

## Huidige onderzoeksstatus

**PENDING.** Er is nog geen M05-assurance-uitspraak gedaan. Een volledige compliance- of assuranceverklaring is **NOT ESTABLISHED**.
