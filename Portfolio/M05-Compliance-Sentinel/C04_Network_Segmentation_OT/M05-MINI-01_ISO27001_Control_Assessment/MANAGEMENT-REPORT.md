# Managementadvies · M05-MINI-01 (concept)

**DRAFT / PENDING OWNER REVIEW · 24-11-2026** · Aan: Project Owner / eigenaar segmentatierisico. Van: AI-ondersteunde self-assessment; geen onafhankelijke attestatie.

## Besluit gevraagd

Prioriteer review van de mogelijke IPv6-beleidszwakte (B1), zonder bestaande toegang te veronderstellen. Beslis vervolgens over bronacceptatie en correlatie van de IPv4-deeltests (B2). Stel toegestane SSH/DNS/NTP-stromen vast. Geen live wijziging of restrisicoacceptatie zonder afzonderlijk besluit.

## Reikwijdte en conclusie

De labcasus beoordeelt netwerksegmentatie aan de hand van A.8.22, met A.8.20 en A.8.21 ondersteunend. Ontwerp is beschreven; implementatie en werking zijn niet integraal aangetoond. F13–F15 hebben scoped PASS vanaf een vervangende bron en F24 heeft scoped PASS op twee IPv4/TCP-poorten. F22–F23 tonen geen geverifieerd routepad; IPv6-handhaving is open. Zie [casusmatrix](CONTROL-ASSESSMENT.md) B1–B4, E1–E5.

## Actie en volgorde (voorstel)

| Prioriteit | Actie | Eigenaar / sluitcriterium |
|---|---|---|
| 1 | Beoordeel brede IPv6-allow en alternatieve paden; bepaal benodigde policy | Project Owner; onderbouwd besluit, backup/rollback voor wijziging, relevante hertest |
| 2 | Review bronvervanging, tijdcorrelatie en bewijsdekking F13–F15; beheerbeleid | Project Owner; besluit en evidence per flow |
| 3 | Bevestig adaptereindstand, herstelvalidatie, regressie en resterende matrix | Project Owner; AC04/AC07 integraal toetsen vóór formele acceptatie |
| 4 | Voltooi MINI-01: 05.6 kosten/inspanning, 05.7 afhankelijkheden, drie mappings en bewijsreview | Deelnemer / reviewer; alle zeven methodiekregels gevuld of gemotiveerde N/A; ownerreview |
| 5 | M04-EXT en overige milestonecriteria volgens aparte planning; M05-MS01 blijft NOT ACHIEVED | Project Owner; afzonderlijke scope en acceptatiecriteria |

Termijnen zijn aan de eigenaar: geen kalenderdeadline of gemeten tijd vastgesteld. Onderzoeksinspanning is niet gemeten. De kennistraining is afgerond (5/5); de assessmentwerkversie en managementadvies zijn nog niet geaccepteerd.

**Advies:** rond de open beleids- en bewijsvragen eerst af; claim alleen de afgebakende testresultaten. De permanente M04/M05-missies worden niet gesloten door deze mini.
