# Publicatiebeleid | Portfolio-export

**Documentstatus:** **APPROVED — Project Owner, 02-11-2026**. De goedkeuring betreft het beleid, **niet** de naleving van de publicatiegates.

## Classificatie

| Klasse | Betekenis | Regel |
|---|---|---|
| Public | Algemene techniek, gescopeerde tests, veilige fictieve voorbeelden | Publicatie pas na review |
| Internal | Werkelijke infrastructuurdetails, lokale beheerinformatie en interne documenten | Verwijderen of abstraheren |
| Confidential | Persoonsgegevens, interne risicostrategie en private projectdetails | Niet publiceren |
| Secret | Tokens, wachtwoorden, sleutels en herstelgeheimen | Nooit in repository opnemen; bij blootstelling roteren |

## Sanitisatie

1. Houd echte beheer-IP's, MAC-adressen, IPv6 link-local identifiers, domeinnamen, lokale gebruikerspaden, tokens en persoonlijke metadata uit publicatie.
2. Gebruik goedgekeurde neutrale aliassen en maak geen mapping tussen echte identifiers en die aliassen bekend.
3. Bewerk beelden in de uiteindelijke pixels met onomkeerbare afscherming; verwijder onnodige metadata.
4. Controleer ook browserbalken, shellprompts, screenshots, diagrammen, commitmetadata, issuecomments en bijlagen.
5. Bewaar historische, gescopeerde testuitslagen eerlijk: een configuratiescreenshot maakt geen component `VERIFIED` zonder relevante test.

## Publicatiegates

- Duidelijk manifest van exportbestanden en uitgesloten bronnen.
- Gerichte secret- en identifierscans voor alle bytes.
- Individuele beeldinspectie en metadatareview.
- Werkende relatieve en externe links, geen private repositoryverwijzingen.
- Een **schone, onafhankelijke Git-geschiedenis** zonder historische gevoelige commits.
- Expliciet eigenaar-PASS vóór wijziging naar PUBLIC; daarna controle als anonieme bezoeker.

**Feitelijke GitHub-zichtbaarheid (laatste controle 02-11-2026): PRIVATE, eerder dezelfde dag PUBLIC.** De hierboven goedgekeurde publicatiegates staan echter **OPEN**. De geschiedenis is niet aantoonbaar volledig gescand/opgeschoond, een afgeronde secrets-/identifierscan ontbreekt, pixelredactie en metadatareview van alle binaire bestanden zijn niet afgerond en vier eerdere bewijs-PNG's ontbreken. Dit is **geen EXCEPTION, geen eigenaar-PASS voor publicatie en geen bewijs van veilige vrijgave**. De inmiddels uitgevoerde wijziging naar PRIVATE herstelt eerdere publieke blootstelling niet.

**Statusgebruik:** [STATUSLEGENDA](STATUSLEGENDA.md). Zie tevens [migratiestatus](../MIGRATIE_STATUS.md).

**Documentstatus:** **APPROVED — Project Owner, 02-11-2026**.

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
