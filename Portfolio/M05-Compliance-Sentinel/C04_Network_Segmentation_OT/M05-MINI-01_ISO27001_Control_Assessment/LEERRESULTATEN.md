# M05-MINI-01 · Leerresultaten | 24 november 2026

**Leerstatus: vijfdelige kennistraining afgerond, 5/5 didactisch PASS.** Beoordeling: AI-ondersteunde dialoog, geen gestandaardiseerd examen, geen onafhankelijke audit. Geen totaalcijfer geconstrueerd uit onvergelijkbare deelcijfers. Deelnemer mocht bronnen raadplegen; geen timer. De 90 minuten in het draaiboek is een planningsindicatie, geen gemeten tijd. Casusassessment: IN PROGRESS; 05.6 en 05.7 PENDING.

| Leerfase | Behandelde kennis | Didactische uitkomst |
|---|---|---|
| 1 Scope & Risk | Trust boundaries, PLC-risico, bewijsgrenzen | PASS na toelichting |
| 2 ISO-controls | A.8.20–A.8.22; A.8.22 centraal; intra-OT versus IT/OT-grens | PASS na toelichting |
| 3 Evidence Assessment | Ontwerp, implementatie, werking; F24 en F13–F15 | PASS; laatste opdracht 9/10 |
| 4 Gaps, Exceptions & Residual Risk | Prioriteit, behandeling, bevoegdheid | PASS; eerste gapvraag 7/10, herzien 9/10; treatment 9/10; ownership 9,5/10 |
| 5 Assurance & Independence | Self-assessment, AI-bias, scope, herkomst en onafhankelijkheid | PASS; 6/6 (1B, 2C, 3A, 4B, 5C, 6A) |

## Leerpunten en correcties

De eerste twee fasen worden hier samengevat; geen letterlijk volledig chattranscript. F24 bewijst alleen de twee geteste WAN→OT TCP-stromen. Een scoped PASS zegt niets over niet-geteste hosts, poorten, richtingen of protocollen. F13–F15 tonen blokkades vanaf de vervangende bron; bewijsbinding en formele bronacceptatie blijven inhoudelijk nodig. Een route ontbreekt bij de onderzochte IPv6-opstelling; dit bewijst geen firewallhandhaving of bestaande exploitroute. De deelnemer koos de mogelijke IPv6-beleidszwakte als eerste bespreekpunt wegens potentiële OT-impact; de reviewer wees erop dat blootstelling, protocolondersteuning en impact nog onderzocht moeten worden.

Ontwerp = past de architectuur bij het risico? Implementatie = komt de inrichting overeen met het ontwerp? Werking = tonen allow- én deny-tests en herleidbare logs/captures het beoogde gedrag? VMware LAN Segments mogen niet zonder bewijs als VLAN-implementatie worden beschreven.

Behandelopties: verkleinen, vermijden, accepteren, overdragen/delen. Voorkeur deelnemer: verkleinen of vermijden; afhankelijkheden, backup, rollback en hertest eerst. Tijdelijke acceptatie vereist een bevoegd expliciet besluit; geen automatische uitzondering. Een ontwerpbesluit is geen risicoacceptatie. De tester signaleert, de beheerder voert uit, de risico-eigenaar besluit. Functiescheiding is wenselijk, niet noodzakelijk drie personen in elke organisatie. Een formele risicoacceptatie hoeft niet altijd een afzonderlijke beleidsuitzondering te zijn.

Assurance: de eigen waarneming en AI-interpretatie afzonderlijk labelen. Onafhankelijke beoordeling vraagt feitelijke onafhankelijkheid en competentie; meerdere AI-modellen zijn geen externe audit. De quiz testte herkenning van begrippen, niet zelfstandige volledige uitvoering.

## Grenzen en vervolg

Geen live test, wijziging, acceptatie of formele normverificatie uitgevoerd door deze leersessie. De vijf leerfasen zijn niet gelijk aan alle zeven permanente M05-methodiekvragen. De onafgeronde casusmatrix, managementadvies, 05.6 en 05.7 blijven onder review. Zie [assessment](CONTROL-ASSESSMENT.md), [managementadvies](MANAGEMENT-REPORT.md) en [educatief afsluitdossier](M05-MINI-01-Educatief-Afsluitdossier.pdf).
