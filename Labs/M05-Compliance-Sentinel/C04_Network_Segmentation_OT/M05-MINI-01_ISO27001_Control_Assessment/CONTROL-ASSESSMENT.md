# M05-MINI-01 · Controlassessment (werkversie)

**IN PROGRESS · DRAFT / PENDING OWNER REVIEW** · 24-11-2026. Deelnemer: Project Owner; reviewer: ChatGPT (AI-INTERPRETED). Interne AI-ondersteunde self-assessment, geen attestatie. Bronnen op peilcommit: 8989e267225aa3075a6534772e14041eb6d1b83f. Normeditie ISO/IEC 27001:2022; precieze normtekst NOT VERIFIED. Geen live tests of volledige SoA.

## Scope en risico

Trust boundary IT/LAB/MGMT/WAN→OT, inclusief toegestane beheerflows en binnen-OT-verkeer als afbakeningscontext; bronnen 20–21 november 2026, beoordeling 24 november. Risico: ongeautoriseerde toegang tot procesbesturing kan procesverstoring, uitval en financiële schade veroorzaken (SIMULATED). Kans niet gekwantificeerd; impact potentieel hoog binnen fictieve bedrijfscontext. Risico-eigenaar: Project Owner; bestaande open punten inzake netwerkbeleid, beheer en bewijsreview. Behandelvoorkeur deelnemer: verkleinen/vermijden; niet goedgekeurd.

## Controlmapping en gescheiden oordelen

| Control | Toepasselijkheid en criterium (werkinterpretatie) | Ontwerp | Implementatie | Werking / beperking |
|---|---|---|---|---|
| A.8.20 Networks security | Relevant ondersteunend: beheersing netwerkgrens en beheer | Zones en beheerbeleid beschreven | Firewall en gescheiden virtuele netwerken gerapporteerd; volledige baseline niet beoordeeld | Deeltests; geen integraal oordeel |
| A.8.21 Security of network services | Ondersteunend: noodzakelijke netwerkdiensten en overeengekomen beveiliging | Dienst- en beheereisen deels open (SSH/DNS/NTP) | Dienstconfiguratie niet integraal gereviewd | Geen zelfstandig werkzaamheidsverdict; toets dienstbeleid en evidence |
| A.8.22 Segregation of networks | Primair: toegestane stromen expliciet, ongeautoriseerde stromen geblokkeerd per zone | IT/OT-scheiding en beperkt beheer als doel; IPv6/alternatieve paden open | Gerichte IPv4-regels en geïsoleerd virtueel OT-segment gerapporteerd; configuratie/eindstand niet volledig gereviewd | Scoped blokkades F13–F15 en F24; integrale werking NOT VERIFIED |

## Bewijsspoor (bronmatrix, AI-INTERPRETED samenvatting)

| ID / flow | Waarneming volgens M04 | Beperking |
|---|---|---|
| E1 / F13 TCP/502 | Vervangende beheerbron: LAN-deny, scoped PASS | Oorspronkelijke bronacceptatie en correlatie open; poort buiten smal OT-filter |
| E2 / F14 TCP/22 | Vervangende bron: LAN-deny en gefilterde OT-capture nul treffers | Tijddekking, bronacceptatie en SSH-beleid open |
| E3 / F15 TCP/44818 | Vervangende bron: LAN-deny en gefilterde OT-capture nul treffers | Tijddekking en bronacceptatie open |
| E4 / F24 TCP/502,8080 | Gesimuleerd WAN: 6 SYN, 6 denies, gelijktijdige gefilterde OT-capture 0 | Twee geteste poorten, geen uitspraak over overige flows |
| E5 / F22–F23 | NO-ROUTE-VERIFIED voor onderzochte IPv6-paden | Handhaving, brede allow en alternatieve paden open; geen exploit aangetoond |

De gesaneerde matrix is de bron; ruwe logs en interface-identifiers zijn niet publiek. Herkomst: M04-evidence door eigenaar gerapporteerd (OBSERVED waar bronwaarneming); deze interpretatie is AI-INTERPRETED. Bewijsreview per poort en formele dekking blijven PENDING.

## Bevindingen en besluitvragen (werkvoorstel, geen acceptatie)

| Record | Bevinding / impact | Voorgestelde behandeling | Owner en sluitbewijs |
|---|---|---|---|
| B1 / E5 | Mogelijke IPv6-beleidszwakte; route en serviceblootstelling niet bewezen | Prioriteit 1 ter bespreking: beleid/afhankelijkheden controleren, gecontroleerde wijziging indien nodig | Project Owner; besluit, bewezen rollback en relevante allow/deny-hertests |
| B2 / E1–E3 | Bewijsgat oorspronkelijke versus vervangende bron | Bronacceptatie motiveren of gecontroleerde test; correlatie per flow | Project Owner; primaire logs, tijddekking en capturefilterreview |
| B3 / E4 | Positieve scoped blokkade, beperkte dekking | Behoud resultaat; valideer overige grenzen volgens M04-matrix | Project Owner; integrale AC04/AC07-review |
| B4 / E2 | SSH-beheerbeleid niet vastgesteld; ook DNS/NTP-beleid open | Leg toegestane beheer-/dienststromen vast | Project Owner; beleid en relevante tests |

## Zeven methodiekvragen

| Methodiek | Stand |
|---|---|
| 05.1 | Scope voorlopig beschreven; definitieve normtoepasselijkheid en bronpassage controleren |
| 05.2 | Risicoketen en eigenaar beschreven; kans/impact-schaal en aannames nog formaliseren |
| 05.3 | Drie werkinterpretaties, gescheiden oordelen en bewijsspoor; primaire evidence-review PENDING |
| 05.4 | B1–B4, behandelvoorkeur en besluitvragen; geen risico geaccepteerd |
| 05.5 | Self-assessment, beperkte onafhankelijkheid; audittrail aanvullen bij review |
| 05.6 | PENDING. Geen gemeten oefentijd. Registreer inspanning per stap als MEASURED of onderbouwde ESTIMATED; vergelijk status quo met least privilege + herhaalbare regressietests onder gelijke beveiligingseisen. Geen besparing geclaimd. |
| 05.7 | PENDING. Kandidaat: firewall draagt zowel segmentatie als beheer/logbewijs; configuratie/rol beschreven, gezamenlijk faaleffect HYPOTHESIS. Beoordeel afhankelijkheid en gevolg afzonderlijk; geen fault injection. |

**Voorlopige conclusie:** A.8.22 relevant en gescopeerde netwerkblokkades ondersteund door M04-bronnen; integrale effectiviteit en A.8.20/A.8.21-oordelen niet vastgesteld. AC04/AC07 PENDING; M04 blijft eigenaar van de tests. Geen mini-eindacceptatie.

## Bronnen
- [Gesaneerde M04-testmatrix, peilcommit 24-11-2026](https://github.com/SamAsgar/Hybrid-Theory-Public/blob/8989e267225aa3075a6534772e14041eb6d1b83f/Portfolio/M04-Network-Citadel/M04-AC04-AC07-TESTMATRIX.csv)
- [M04-overzicht](../../../M04-Network-Citadel/README.md)
- [M05-methodiek en kaderselectie](../../README.md)
- [ISO/IEC 27001:2022 (catalogus)](https://www.iso.org/standard/27001)

