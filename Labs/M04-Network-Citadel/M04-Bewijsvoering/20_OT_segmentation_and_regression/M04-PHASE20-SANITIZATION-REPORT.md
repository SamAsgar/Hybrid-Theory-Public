# M04 fase 20 — aanvullend publiek saneringsrapport (20 november 2026)

**Bron:** 55 oorspronkelijke screenshots uit de private M04-fase van 19 november. **Publicatie:** uitsluitend opnieuw geproduceerde, pixelmatig gesaneerde RGB-PNG-afgeleiden.

## Aanpak

- Originele bestandsnamen en volgorde behouden; bronbytes niet gewijzigd in Private.
- Per beeld tekstherkenning op eerder gemaakte positiescans; alleen gevoelige velden/identificatoren onomkeerbaar overschreven met officiële SSOT-aliassen of `REDACTED_*`.
- `CLIENT01_DHCP_IP`, `PLC01_OT_IP`, `FUXA01_OT_IP`, `PFSENSE_OT_IP` en andere reeds vastgestelde aliasnamen zijn labels, geen gepubliceerde vertaaltabel.
- Waar mapping ambigu is of ontbreekt, wordt geen identiteit geraden maar de waarde geanonimiseerd.
- Bij pfSense-logs zijn bron- en bestemmingsvelden specifiek hertekend; `BLOCK`, tijdstippen, interface, TCP-poorten, protocol en regelcontext zijn behouden.
- Terminalbeelden zijn **niet** integraal zwartgemaakt. Opdrachten en niet-gevoelige uitkomsten blijven waar mogelijk zichtbaar.
- Alle PNG's bevatten uitsluitend een nieuwe pixelraster: geen EXIF-, tekst-, ICC- of overige PNG-metadata. De openbare SHA-256-waarden horen alleen bij de publieke afgeleiden.

## Beperkingen

De sanering is zo doelgericht mogelijk, maar kleine, afgesneden of slecht herkende tekens blijven een residueel risico. Screenshots zijn contextbewijs, geen vervanging voor een onafhankelijk uitgevoerde securityreview. Een **individuele handmatige eigenaarreview van alle 55 beelden** blijft vereist vóór merge. Geen originele SHA-256's of SSOT-waardentabellen worden meegepubliceerd.

**Technische acceptatie:** M04-CORE IN PROGRESS. AC04/AC07 integraal PENDING. De beschreven AC01–AC03- en firewallresultaten zijn gescopeerde deeltests.

## Nacontrole van 27 november

In beelden 016, 040, 044 en 049 zijn aanvullende netwerkgegevens afgeschermd. De terminalweergave in 044 is geheel afgeschermd. De bewijsbeschrijvingen en de oorspronkelijke testscope blijven beschikbaar. De registers bevatten de hashes van de bijgewerkte publieke afbeeldingen. Eerdere versies zijn via Git bereikbaar.
