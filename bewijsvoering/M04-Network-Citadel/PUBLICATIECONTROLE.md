# M04 | Sanitization en publicatiecontrole

**Status:** DRAFT — onafhankelijk security-/eigenaarakkoord nog vereist.

## Uitgevoerde selectieve controles

| Controle | Uitvoering | Resultaat |
|---|---|---|
| Scope Private | Private M04-bewijsindex, README, GAP-analyse en FUXA-addendum geraadpleegd | 210 originele screenshots / 19 fasen; niet integraal gepubliceerd |
| Primaire bestandsovereenkomst | Originele `M04-EV-202`-PNG uit aangeleverde M04-evidence vergeleken met SHA-256 in private bron | **Exacte bronhashmatch** |
| Pixelredactie `M04-EV-202` | Werkelijke doel- en bronadressen en identificerende promptregels in de uiteindelijke pixels overschreven; IP's vervangen door `PFSENSE_MGMT_IP` en `MGMT_CLIENT_IP`; uitvoer opnieuw gerenderd | Alleen gesaneerde afgeleide opname in Public; **niet origineel** |
| Afbeeldingsmetadata | Nieuwe PNG als zwart-wit PNG zonder overgenomen EXIF/profielmetadata opgeslagen | Geen oorspronkelijke metadata meegekopieerd |
| Extra FUXA-visualisaties | Nieuwe SVG's opgebouwd uit private beschrijvingen van EV-206 en EV-209/210 | **Afgeleide illustraties**, geen bewijsoriginelen |
| Echte IPv4-/IPv6-/MAC-waarden | Niet overgenomen in publieke tekst en illustraties | Officiële aliassen gebruikt |
| Sessiecookies | Het ruwe scherm van EV-161 expliciet **niet** gekopieerd, omdat de HTTP-uitvoer een cookie bevat | Geen cookie in de publieke evidence-set |
| Firewall/NAT-config | Geen volledige private rule-exports, redirect mappings of logextracten gepubliceerd | Alleen abstracte testconclusies |
| Bewijsoordeel | Positieve TCP-poorttests niet gelijkgesteld aan end-to-end NAT/OT-PASS | AC04/AC07 en AC02/AC03 open |

## Belangrijke beperking

De geplaatste PNG is **een gewijzigde transcriptweergave op basis van een origineel screenshot**. Na het verwijderen van informatie zijn regels met de officiële aliassen opnieuw gezet. Dit is nuttig voor de publieke technische uitleg, maar heeft niet dezelfde integriteit als het ongewijzigde private origineel.

De FUXA-SVG's zijn **illustraties** die geselecteerde velden uit gedateerde private waarnemingen samenvatten. Hun vorm en plaatsing zijn opnieuw ontworpen. Gebruik deze nooit als zelfstandig bewijs van applicatiegedrag.

**Voor definitieve publicatie vereist:** de Project Owner controleert de complete PR-diff, zichtbaar SVG-/PNG-resultaat, bestandsmetadata, blootstelling van configuratiepatronen en de actuele publicatiegrenzen. Geen automatische Public-merge.

## Geen impliciete vrijgave

De aanwezigheid van een Draft PR maakt de bestanden nog niet goedgekeurd voor `main`; houd Private originelen buiten alle publiek bereikbare branches, PR-comments en artifacts. Nieuwe afbeeldingen vereisen afzonderlijke pixelscan en, waar relevant, handmatige metadata-inspectie.
