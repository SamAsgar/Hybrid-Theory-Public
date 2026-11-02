# Labkader | Hybrid-Theory

**Versie:** 1.1 | **Bijgewerkt:** 02-11-2026 | **Status:** **APPROVED — Project Owner, 02-11-2026**  
**Scope:** eigen VM's, eigen hardware en expliciet geautoriseerde cloudresources voor netwerk- en identity-engineering, automatisering, security en weerbaarheid.

## Toegestane scope

Netwerken van derden, huishoudelijke diensten, productieomgevingen en gegevens van anderen vallen **buiten de scope**, tenzij daarvoor afzonderlijk en aantoonbaar toestemming is gegeven. Alleen technische bereikbaarheid betekent nooit dat een handeling geautoriseerd is.

## Trust boundaries

- Leg beheer-, LAB-, WAN- en toekomstige cloud-/clientzones, toegestane verkeersstromen en toegang vast voordat een nieuwe verbinding wordt geactiveerd.
- Labels zoals NAT of host-only bewijzen op zichzelf geen isolatie. Positieve en negatieve tests toetsen **de betreffende gewijzigde netwerkgrens**.
- Houd beheer met verhoogde rechten gescheiden, pas least privilege toe en zorg voor herstelbaarheid.
- Hergebruik eerder gevalideerd bewijs zolang configuratie en scope niet zijn veranderd; voer geen onnodige dubbele tests uit.

## Veiligheid en herstel

**Actieve uitvoeringsregel HT-011:** preflight beperkt zich tot de minimumchecks voor een veilige volgende stap. Extra hardening of uitgebreide controles zijn pas verplicht bij een concrete blokkade, onaanvaardbaar risico of tijdens de relevante goedgekeurde lab. Een passende rollback vóór een ingrijpende wijziging blijft noodzakelijk; de volledige onafhankelijke back-up-/restoretest is onderdeel van Lab 02 en geen generieke blokkade voor normale labinstallaties. Zie de [AI-werkafspraken](AI_WERKAFSPRAKEN.md#1-doelgericht-proportioneel-en-veilig).

Stop bij verkeer buiten de toegestane scope, onbedoeld blootgestelde gegevens, verlies van beheerstoegang, ongeautoriseerde handelingen of onverwachte cloudkosten. Ingrijpende wijzigingen vereisen een passende rollback en herstelvoorbereiding. Snapshots vervangen geen onafhankelijke back-ups.

## Governance en bewijs

De Project Owner keurt scope en belangrijke besluiten goed. Ontwerp, installatie en beheer worden iteratief uitgevoerd; beveiliging en troubleshooting blijven daarbij doorlopende verantwoordelijkheden. Verificatie gebeurt risicogestuurd met **PASS / REWORK / EXCEPTION**, volgens de [AI-werkafspraken](AI_WERKAFSPRAKEN.md). Waar een lab om toetsing vraagt, worden **alle relevante en toepasselijke** governance-, security-, assessment- en wettelijke referenties geselecteerd, afhankelijk van de concrete scope. Dat kan onder meer **COBIT 2019, ISO/IEC 27001, NIST CSF 2.0, CIS Controls v8.1, NIST SP 800-53A** of een passende OT-/privacyreferentie zijn. De typen en toepasbaarheid staan in [CAT/ACE v0.2 — framework- en gap-analyseonderzoek](CAT_ACE_v0.2.md). Dit onderzoeksconcept is **niet gevalideerd** en introduceert geen verplichte volledige audit of extra preflightcontrole.

Onderscheid **PLANNED / IMPLEMENTED / VERIFIED**. Screenshots zijn bewijs binnen hun testscope, geen onderbouwing voor ongeteste controls. Een AI-review vervangt geen geobserveerde resultaten.

Gedetailleerde AI-werkafspraken staan uitsluitend in [AI-werkafspraken](AI_WERKAFSPRAKEN.md). Verwijzingen naar wet- en regelgeving staan in [Wet- en regelgevingskaders](WET_EN_REGELGEVING.md). Dit document dupliceert die procedures niet.

## Publicatiegrenzen

Publiceer geen secrets, vertrouwelijke projectnamen, echte beheeridentificatoren, herkenbare privétopologie of ongeschoonde captures. Eerdere Git-commits of comments kunnen gegevens blijven bevatten, ook wanneer recente bestanden zijn opgeschoond. De werkwijze en verplichte publicatiecontrole zijn beschreven in het [Publicatiebeleid](PUBLICATIEBELEID.md).

**Documentstatus:** **APPROVED — Project Owner, 02-11-2026**. Het beleid is door Sam goedgekeurd; dit verandert geen bestaande technische configuratie en bewijst geen naleving of afgeronde publicatiereview.

**Statusgebruik:** [STATUSLEGENDA](STATUSLEGENDA.md).

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
