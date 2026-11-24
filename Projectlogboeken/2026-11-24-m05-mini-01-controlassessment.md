# M05-MINI-01 · IT/OT-controlassessment en rapportage

**Datum:** 24 november 2026 (Europe/Amsterdam) · **Werkstatus:** IN PROGRESS · **Type:** onderzoeks- en documentatiesessie; geen technische uitvoering. **Classificatie:** gesaneerde stakeholderdocumentatie, review vereist.

## Doel en uitvoering

De bestaande M04-netwerksegmentatie is als casus gebruikt om risicobeheersing, controlinterpretatie, technische evidence en besluitvorming met elkaar te verbinden. De vijfdelige kennistraining is afgerond; het casusassessment en managementadvies zijn werkversies. ISO/IEC 27001:2022 A.8.22 is de primaire control; A.8.20 en A.8.21 zijn ondersteunend. Exacte normtekst NOT VERIFIED. De fictieve koelketencasus is illustratief en geen gemeten bedrijfsincident.

De Nederlandstalige rapportage is uitgebreid tot elf pagina's met bedrijfscontext, architectuur, technische evidence, risico's, governance en aanbevelingen. Een Engelse editie met dezelfde inhoudelijke hoofdstukken en bewijsgrenzen is toegevoegd. De rapporten gebruiken uitsluitend fictieve documentatieadressen en publieke projectidentiteit; geen echte IP-/MAC-mappings. Publicatievoorstel blijft in [draft-PR #72](https://github.com/SamAsgar/Hybrid-Theory-Public/pull/72) tot afzonderlijke review en merge.

## Observaties en bewijsgrenzen

| Onderwerp | Beoordelingsstand |
|---|---|
| F13–F15 | Scoped PASS voor vervangende beheerbron; formele bronacceptatie en per-flow evidence-review open. F13 TCP/502 viel buiten het smalle OT-capturefilter. |
| F24 | Scoped PASS voor TCP/502 en TCP/8080 vanaf gesimuleerd WAN; zes SYN, zes denies, nul treffers in de bijbehorende gefilterde OT-capture. |
| F22–F23 | NO-ROUTE-VERIFIED; IPv6-handhaving en alternatieve paden niet volledig vastgesteld. Geen aangetoonde exploitroute. |
| Risico en governance | Mogelijke IPv6-beleidszwakte eerst ter beoordeling; bron- en bewijsreview blijft inhoudelijk noodzakelijk. Geen risicoacceptatie of live wijziging. |
| Assurance | Interne AI-ondersteunde self-assessment; geen onafhankelijke audit, certificering of volledige ISMS-beoordeling. |

## Vervolg

- M04: toets IPv6-beleid en alternatieve paden; review bronacceptatie en log-/capturedekking; bepaal SSH/DNS/NTP-beleid, adaptereindstand en herstelvalidatie. AC04/AC07 integraal PENDING; CORE IN PROGRESS.
- M05-MINI-01: vul de zeven methodiekvragen aan, waaronder 05.6 Cost & Efficiency en 05.7 Systemic Risk; geen gemeten inspanning of aangetoond cascade-effect beschikbaar. Review primaire evidence, toepasselijkheid en managementadvies; eigenaar beslist afzonderlijk.
- M05-MS01 blijft NOT ACHIEVED, exitcriteria DRAFT. Permanente missies worden niet afgesloten door een mini. Geen nieuwe technische PASS of wijziging van historische testuitslagen.

## Documentatie en verwijzingen

- [MINI-01 dossier](../Portfolio/M05-Compliance-Sentinel/C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/README.md)
- [Nederlandstalig rapport](../Portfolio/M05-Compliance-Sentinel/C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/M05-MINI-01-Educatief-Afsluitdossier.pdf) · [English research report](../Portfolio/M05-Compliance-Sentinel/C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/M05-MINI-01-IT-OT-Network-Segmentation-EN.pdf)
- [Controlassessment](../Portfolio/M05-Compliance-Sentinel/C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/CONTROL-ASSESSMENT.md) · [Managementadvies](../Portfolio/M05-Compliance-Sentinel/C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/MANAGEMENT-REPORT.md)
- [M04-log 21 november](2026-11-21-m04-core-management-segmentatie.md) · [M05-issue](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/46) · [Roadmap](ROADMAP.md)

