# Wet- en regelgevingskaders | Hybrid-Theory

**Documentstatus:** **DRAFT** (referentiedocument). Dit document beschrijft reeds genoemde kaders als ontwerplens. Het bewijst geen technische implementatie, compliance of certificering.
**Versie:** 1.0 (27-10-2026)
**Eigenaar:** Sam
**Gerelateerd:** [LAB_KADER.md](LAB_KADER.md), [BESLUITENLOG.md](BESLUITENLOG.md), [statuslegenda](STATUSLEGENDA.md)

**Actuele uitvoeringsafspraak HT-011 (1 november 2026):** aanbevelingen hieronder over MFA, updates, NTP, netwerkzones, monitoring en uitgebreide audit-/hersteltests zijn referenties of doeleisen voor de betreffende oefencasus of het relevante lab. Ze zijn niet automatisch verplichte preflight-checks voor elke nieuwe VM of de eerste AD-installatie. Vóór een missie gelden de minimale veiligheidsgrenzen en risicogestuurde triggers uit [AI-werkafspraken §1](AI_WERKAFSPRAKEN.md#1-doelgericht-proportioneel-en-veilig). Waar dit document strenger lijkt, geldt HT-011 voor de **labuitvoeringsvolgorde**; wettelijke verplichtingen voor werkelijk gereguleerde organisaties blijven onaangetast.

## Doel en afbakening

Hybrid-Theory valt zelf niet onder deze wetten en standaarden. Het lab gebruikt ze om ontwerpkeuzes te toetsen aan wat organisaties in de praktijk moeten aantonen. Dat maakt de architectuur realistischer en de bevindingen beter overdraagbaar naar echte omgevingen.

Uitgangspunten:

- **Voor de nog niet geactiveerde controlmapping is ISO/IEC 27001:2022 Annex A als primaire control-sleutel voorgesteld.** Dit is een documentatiekeuze, niet de enige benchmark: de onderzoekskaders worden per toepasselijk scenario geselecteerd. Zie [CAT/ACE v0.4](CAT_ACE_v0.4.md), waarin **CAT-C** toepasselijke vereisten afbakent en **ACE-Audit** ze binnen scope toetst, ook bij interne of hybride beoordeling.
- **Geen claim zonder bewijs.** Een component krijgt slechts VERIFIED binnen een passend geteste scope. Een control krijgt uitsluitend een gescopeerd PASS als vooraf vastgelegde acceptatiecriteria met bewijs zijn gehaald. Kennis van een kader is geen naleving ervan.
- **De mapping in het controledossier blijft **PARKED**** tot besluit van Sam. Dit document is de voorbereiding daarop.
- **NIST CSF 2.0**, **CIS Controls v8.1** (met Assessment Specification) en **NIST SP 800-53A Rev. 5** zijn mogelijke **onderzoeks- en assessmentreferenties**, geen wetgeving en geen drie gelijkwaardige auditmethoden. De actieve controlmapping is **PARKED**; dit document levert geen onderbouwd besluit om NIST CSF of CIS daarvan categorisch uit te sluiten of op te nemen. Een toekomstige keuze vraagt expliciete goedkeuring en toepasselijkheidscontrole.
- **Publicatie:** conform het [labkader](LAB_KADER.md) staan in dit document en de bijbehorende bewijslast geen IP-adressen, MAC-adressen, tenant- of subscription-ID's of credentials.

## Overzicht

| Kader | Soort | Wie valt eronder / gebruikt het | Rol in Hybrid-Theory |
|---|---|---|---|
| ISO/IEC 27001:2022 | Internationale norm (certificeerbaar) | Elke organisatie, vrijwillig | Control-ruggengraat; Annex A als control-ID |
| NIS2 / Cyberbeveiligingswet | EU-richtlijn / Nederlandse wet | Essentiële en belangrijke entiteiten in 18 sectoren | Zorgplicht en meldplicht als ontwerp- en oefeneis |
| DORA | EU-verordening | Financiële entiteiten en kritieke ICT-dienstverleners | Weerbaarheidslens: segmentatie, beheernetwerk, backup, testen |
| AVG (GDPR) | EU-verordening | Iedereen die persoonsgegevens verwerkt | Privacy by design, logging, datalocatie, publicatieregels |
| ISAE 3402 | Assurance-standaard (IAASB) | Serviceorganisaties met impact op de financiële verslaglegging van klanten | Denkkader voor IT general controls en bewijs over tijd |
| ISAE 3000 | Assurance-standaard (IAASB) | Assurance op niet-financiële informatie | Denkkader voor toetsbare criteria en zekerheidsniveau |
| SOC 2 | Attestatiekader (AICPA) | Vooral SaaS- en clouddienstverleners | Trust Services Criteria; systeemgrens en subdienstverleners |

## Aanvullende onderzoeksreferenties (geen wetgeving)

De volgende bronnen kunnen bij een afgebakende technische beoordeling worden gebruikt, zonder dat ze automatisch toepasselijk of verplicht worden:

| Referentie | Onderzoeksfunctie |
|---|---|
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | Cybersecurityuitkomsten, risicocontext en governance structureren |
| [CIS Controls v8.1 en Assessment Specification](https://www.cisecurity.org/controls/v8-1) | Concrete Safeguards en geselecteerde toetsingscriteria bepalen |
| [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) | Beoordelingsprocedures en bewijs voor gekozen controls |
| [COBIT 2019](https://www.isaca.org/resources/cobit) | Governance, management en eigenaarschap van besluiten analyseren |

**ISO/IEC 27001:2022** blijft in dit document de gekozen referentie voor de **voorbereide, nog niet geactiveerde** controlmapping. COBIT en de overige bronnen zijn aanvullend; hun gebruik impliceert geen formele audit, certificering of nieuw goedgekeurd beleid. De technische onderzoeksaanpak, bewijsgrenzen en praktische **Audit / Cost / Efficiency / Revalidation**-casussen staan in [CAT/ACE v0.4 — onderzoeksconcept, frameworks en gap-analyses](CAT_ACE_v0.4.md).

## Hoe de kaders samenhangen

De kaders vormen drie lagen:

1. **Wettelijke verplichtingen** (NIS2/Cbw, DORA, AVG): wat een organisatie moet.
2. **Managementsysteem en controls** (ISO 27001): hoe een organisatie dat structureel inricht.
3. **Assurance** (ISAE 3402, ISAE 3000, SOC 2): hoe een onafhankelijke auditor vaststelt dat controls zijn opgezet en werken.

Voor financiële entiteiten gaat DORA als lex specialis vóór op NIS2 voor ICT-risicobeheer en incidentmelding. Een assurance-rapport is geen certificaat: het beschrijft controls en het oordeel van de auditor over een bepaalde datum of periode.

---

## 1. ISO/IEC 27001:2022

### Wat het is

Internationale norm voor een Information Security Management System (ISMS). De kern bestaat uit clausules 4 tot en met 10 (context, leiderschap, planning, ondersteuning, uitvoering, evaluatie, verbetering) en Annex A met 93 controls in vier thema's: organisatorisch (37), mensen (8), fysiek (14) en technologisch (34). Een organisatie bepaalt via een risicoanalyse welke controls van toepassing zijn en legt dat vast in een Statement of Applicability (SoA). Certificering gebeurt door een geaccrediteerde certificerende instelling. De overgangstermijn vanaf de 2013-versie is op 31 oktober 2025 verlopen.

### Relatie met Hybrid-Theory

ISO 27001 is de gemeenschappelijke taal tussen de andere kaders. Ontwerpkeuzes in het lab krijgen een Annex A-referentie, zodat elke maatregel herleidbaar is naar een control. Bestaande technische bevindingen passen daar direct op: de LAB-firewallregels raken 8.20 en 8.22, de afwijkende tijd in de firewalllog raakt 8.17 en de nog niet bevestigde baseline-snapshot raakt 8.13.

### Aandachtspunten netwerkarchitectuur

- **Zones vastleggen vóór uitrol (8.22 Segregation of networks).** Elke zone (WAN, beheer, LAB, later IT, server en client) krijgt een doel, toegestane stromen en een eigenaar. De allow/deny-matrix is het ontwerpdocument.
- **Netwerkbeveiliging als control, niet als installatie (8.20, 8.21).** Default deny tussen zones; elke pass-regel heeft een reden in het besluitlog.
- **Bevoorrechte toegang (8.2, 8.5).** Beheerinterfaces (firewall-webGUI, Cockpit, later Windows-beheertools) alleen bereikbaar vanuit de beheerzone, met aparte beheeraccounts.
- **Logging, monitoring en tijd (8.15, 8.16, 8.17).** Logs zijn pas bewijs als de tijd klopt. Eén tijdbron (NTP) voor alle systemen en de tijdzone expliciet vastgelegd.
- **Configuratie en change (8.9, 8.32).** Configuratie-exports van firewall en servers als baseline; wijzigingen via het besluitlog, met rollback.
- **Backup (8.13) en continuïteit (5.30).** Een snapshot is een herstelpunt, geen backup. Minstens één backup buiten de host.
- **Cloud (5.23).** Azure-onderdelen krijgen dezelfde zone- en toegangsdenkwijze als on-premises.

### Bewijs dat dit oplevert

Een SoA-achtig overzicht per zone, de allow/deny-matrix, configuratie-exports, testresultaten (positief en negatief) en het besluitlog.

---

## 2. NIS2 / Cyberbeveiligingswet (Cbw)

### Wat het is

Richtlijn (EU) 2022/2555 verhoogt het basisniveau van cyberbeveiliging in de EU. In Nederland is NIS2 geïmplementeerd in de Cyberbeveiligingswet, die op 15 augustus 2026 in werking is getreden en de Wet beveiliging netwerk- en informatiesystemen (Wbni) vervangt. Nadere regels staan in het Cyberbeveiligingsbesluit. Organisaties in 18 sectoren vallen eronder als essentiële of belangrijke entiteit en moeten zelf vaststellen of dat voor hen geldt.

Kernverplichtingen:

- **Registratieplicht.**
- **Zorgplicht (art. 21 NIS2):** passende, risicogebaseerde maatregelen, met als minimum:
  - (a) risicoanalyse en beveiligingsbeleid voor informatiesystemen;
  - (b) incidentafhandeling;
  - (c) bedrijfscontinuïteit, inclusief backupbeheer, herstel en crisisbeheer;
  - (d) beveiliging van de toeleveringsketen;
  - (e) beveiliging bij aanschaf, ontwikkeling en onderhoud, inclusief kwetsbaarheidsbeheer;
  - (f) beoordeling van de effectiviteit van maatregelen;
  - (g) cyberhygiëne en training;
  - (h) cryptografie en, waar passend, encryptie;
  - (i) personeelsbeveiliging, toegangsbeleid en assetbeheer;
  - (j) multifactorauthenticatie en beveiligde communicatie.
- **Meldplicht (art. 23 NIS2):** vroegtijdige waarschuwing binnen 24 uur, incidentmelding binnen 72 uur en een eindrapport binnen een maand na de incidentmelding.
- **Bestuursverantwoordelijkheid:** bestuurders keuren de maatregelen goed, houden toezicht en moeten zelf voldoende kennis hebben om cyberrisico's te beoordelen.

### Relatie met Hybrid-Theory

Het lab is geen entiteit onder de Cbw, maar de tien maatregelen van art. 21 vormen een bruikbare checklist voor elke fase. De rol van Sam (eindverantwoordelijkheid, akkoord vóór uitvoering) spiegelt de bestuursverantwoordelijkheid. 

### Aandachtspunten netwerkarchitectuur

- **Zorgplicht per fase toetsen.** Bij elke nieuwe VM of zone: welke van (a) tot en met (j) raakt dit, en wat is het bewijs?
- **Toeleveringsketen (d).** Leg externe afhankelijkheden vast: hypervisor, firewall-installer met online account, cloudprovider en beheertools. Bij uitval van een leverancier: wat blijft werken?
- **Kwetsbaarheidsbeheer (e).** Oefen met patchbeleid, urgente kwetsbaarheden en een gecontroleerde updateroute. Niet iedere niet-kritieke update is een verplichte stap vóór het eerste functionele labresultaat; prioriteer volgens HT-011 en de risico's van de concrete testomgeving.
- **MFA (j)** als doelcontrol voor relevante beheerinterfaces en cloudbeheercasussen; voer dit binnen de betreffende missie en licentie-/toegangsscope uit, of eerder wanneer een reëel risico dit vereist.
- **Detectie als voorwaarde voor melden.** Zonder centrale logging en betrouwbare tijd is een waarschuwing binnen 24 uur niet haalbaar. Logging is daarom een architectuurcomponent, geen bijzaak.
- **Effectiviteit aantonen (f).** Negatieve tests (wat mag níét) zijn even belangrijk als positieve.

### Bewijs dat dit oplevert

Een maatregelenoverzicht per fase volgens art. 21, een leveranciersregister, patchstatus, een MFA-overzicht en een ingevulde meldtijdlijn als oefening (duidelijk gemarkeerd als oefening).

---

## 3. DORA (Digital Operational Resilience Act)

### Wat het is

Verordening (EU) 2022/2554, van toepassing sinds 17 januari 2025, voor financiële entiteiten (onder meer banken, verzekeraars, beleggingsondernemingen en betaalinstellingen) en, via een Europees toezichtregime, kritieke ICT-dienstverleners. In Nederland houden DNB en AFM toezicht. Voor financiële entiteiten gaat DORA vóór op NIS2 voor ICT-risicobeheer en incidentmelding.

Vijf pijlers:

1. **ICT-risicobeheer (art. 5–16),** uitgewerkt in technische reguleringsnormen (RTS, Gedelegeerde Verordening (EU) 2024/1774).
2. **ICT-incidentbeheer, classificatie en melding (art. 17–23).** Voor ernstige incidenten: eerste melding binnen 4 uur na classificatie als ernstig en uiterlijk 24 uur na detectie, een tussentijds rapport binnen 72 uur na de eerste melding en een eindrapport binnen een maand na het laatste tussentijdse rapport.
3. **Testen van digitale operationele weerbaarheid (art. 24–27):** jaarlijkse basistests voor systemen die kritieke functies ondersteunen; voor aangewezen instellingen dreigingsgestuurde penetratietests (TLPT, in Nederland via TIBER-NL), minimaal elke drie jaar.
4. **Risicobeheer van ICT-derde partijen (art. 28–44),** inclusief een informatieregister van alle ICT-contracten.
5. **Informatie-uitwisseling (art. 45).**

### Relatie met Hybrid-Theory

DORA ligt het dichtst bij de opzet van Hybrid-Theory: het vraagt niet alleen om beveiliging, maar om aantoonbare weerbaarheid en herstel. Meerdere bestaande ontwerpkeuzes sluiten er direct op aan.

### Aandachtspunten netwerkarchitectuur

- **Gescheiden beheernetwerk (art. 9(4)(b) en RTS).** DORA vraagt om netwerkbeheer met segmentatie en een apart netwerk voor het beheer van ICT-assets. De host-only beheerzone van Hybrid-Theory volgt dat patroon; houd hem strikt gescheiden van LAB en WAN.
- **Automatisch kunnen isoleren (art. 9(4)(b)).** Ontwerp zo dat een getroffen segment met één regel of één schakelactie kan worden afgesloten. 
- **Toegangsbeperking en sterke authenticatie (art. 9(4)(c)–(d)).** Alleen toegang die nodig is voor de functie; MFA voor beheer.
- **Change- en patchbeheer (art. 9(4)(e)–(f)).** Wijzigingen gedocumenteerd, getest en terug te draaien.
- **Backup gescheiden van de bron (art. 12).** Herstel uit backup gebeurt op systemen die fysiek en logisch gescheiden zijn van het bronsysteem. Een VMware-snapshot op dezelfde host voldoet daar niet aan; plan een backupdoel buiten de host.
- **Detectie (art. 10) en herstel (art. 11).** Monitoring die afwijkingen opmerkt, en herstelprocedures met gemeten hersteltijd (RTO) en dataverlies (RPO).
- **Derde partijen (art. 28).** Houd een eenvoudig register bij van ICT-leveranciers in het lab (hypervisor, firewall-software, cloud) met afhankelijkheid en exitroute.
- **Testen (art. 24–25).** Kwetsbaarheidsscans, netwerkbeveiligingsbeoordelingen, scenariotests en hersteltests horen in de cyclus; 

### Bewijs dat dit oplevert

Zonedocumentatie inclusief beheernetwerk, een isolatietest, een hersteltest met gemeten RTO en RPO, een leveranciersregister, een testplan en een incidenttijdlijn als oefening.

---

## 4. AVG (Algemene verordening gegevensbescherming / GDPR)

### Wat het is

Verordening (EU) 2016/679, van toepassing sinds 25 mei 2018, met de Uitvoeringswet AVG als Nederlandse aanvulling. Toezichthouder in Nederland is de Autoriteit Persoonsgegevens (AP). Kernpunten voor IT-architectuur:

- **Beginselen (art. 5):** onder meer doelbinding, dataminimalisatie, opslagbeperking, integriteit en vertrouwelijkheid.
- **Privacy by design en by default (art. 25).**
- **Beveiliging van de verwerking (art. 32):** passende maatregelen zoals pseudonimisering en versleuteling, het waarborgen van vertrouwelijkheid, integriteit, beschikbaarheid en veerkracht, tijdig herstel na een incident en het regelmatig testen van de effectiviteit.
- **Verwerkers (art. 28):** afspraken met partijen die gegevens namens de organisatie verwerken.
- **Datalekken (art. 33–34):** melding aan de AP binnen 72 uur en in bepaalde gevallen aan betrokkenen.
- **DPIA (art. 35)** bij verwerkingen met een hoog risico, zoals stelselmatige monitoring.
- **Doorgifte buiten de EER (hoofdstuk V).**

### Relatie met Hybrid-Theory

Het lab verwerkt geen echte persoonsgegevens en dat blijft zo: alle gebruikersaccounts in AD en Entra ID zijn fictief. Toch is de AVG relevant, omdat de systemen die het lab nabootst (domein, logging, monitoring, cloud) in een echte organisatie wél persoonsgegevens bevatten. Het lab oefent de inrichting alsof dat zo is.

### Aandachtspunten netwerkarchitectuur

- **Logs zijn persoonsgegevens.** IP-adressen, gebruikersnamen en tijdstempels in firewall-, AD- en monitoringlogs zijn in een echte omgeving persoonsgegevens. Bepaal per logbron het doel, de bewaartermijn en wie toegang heeft.
- **Monitoring vraagt om een afweging.** Een centrale monitoringoplossing (zoals een SIEM) is in een echte organisatie stelselmatige monitoring van medewerkers; daar hoort een DPIA bij.
- **Datalocatie.** Kies Azure-regio's binnen de EU en documenteer welke diensten gegevens mogelijk buiten de EER verwerken.
- **Versleuteling (art. 32).** Beheer- en dataverkeer over versleutelde verbindingen; gegevensdragers en backups versleuteld.
- **Herstel (art. 32(1)(c)).** Tijdig herstel van beschikbaarheid is een AVG-eis, niet alleen een continuïteitswens. Hersteltests tellen dus dubbel.
- **Publicatie.** De repository is **PUBLIC**, maar een repo-brede controle op identificatoren in screenshots, bestanden en eerdere commits is nog niet afgerond. Het [labkader](LAB_KADER.md) verbiedt publicatie van gevoelige informatie; dit is nog geen bevestiging dat alle bestaande beelden aan die eis voldoen.

### Bewijs dat dit oplevert

Een overzicht van logbronnen met doel en bewaartermijn, de keuze en motivatie van cloudregio's, een versleutelingsoverzicht en een DPIA-oefening voor monitoring zodra die wordt ingericht.

---

## 5. ISAE 3402

### Wat het is

International Standard on Assurance Engagements 3402 van de IAASB. Een onafhankelijke auditor rapporteert over de interne beheersing van een serviceorganisatie (bijvoorbeeld een IT-dienstverlener) voor zover die relevant is voor de financiële verslaglegging van haar klanten. Er zijn twee typen:

- **Type I:** opzet en bestaan van controls op één moment.
- **Type II:** opzet, bestaan én werking van controls over een periode, meestal 6 tot 12 maanden.

In de IT-praktijk gaat het vooral om IT general controls (ITGC's): logische toegang, changebeheer, IT-operaties (zoals backup en monitoring) en soms fysieke beveiliging. Het rapport bevat een systeembeschrijving, de controls, de tests van de auditor en eventuele afwijkingen. Klanten moeten soms zelf aanvullende controls uitvoeren (complementary user entity controls). Voor onderdelen bij een subdienstverlener kiest de serviceorganisatie de carve-out- of de inclusive-methode.

### Relatie met Hybrid-Theory

ISAE 3402 helpt het onderscheid scherp te houden tussen een control die is ingericht en een control die aantoonbaar blijft werken. Het sluit aan op de bestaande statussen: IMPLEMENTED met één geslaagde test lijkt op Type I; aantonen dat een control over een periode blijft werken, lijkt op Type II.

### Aandachtspunten netwerkarchitectuur

- **Toegangscontrols aantoonbaar maken.** Wie heeft beheerrechten op welke zone, waar is dat vastgelegd en hoe blijkt dat het zo blijft? Aparte beheeraccounts en groepen in AD maken dit toetsbaar.
- **Changebeheer met spoor.** Elke wijziging aan firewallregels en serverconfiguratie is herleidbaar naar een besluit, met datum en uitvoerder. Het besluitlog en de commitgeschiedenis vormen samen dat spoor.
- **Bewijs over tijd systematisch verzamelen.** Voor een beoordeling over een periode zijn passende, gedateerde observaties nodig, bijvoorbeeld logs en configuratie-exports. Waar mogelijk kan verzameling worden geautomatiseerd om herhaalbaarheid te verbeteren. Automatiseer de bewijsvorming, niet het inhoudelijke oordeel.
- **Betrouwbare tijdstempels.** Zonder kloppende tijd is bewijs over een periode niet bruikbaar (zie ISO 27001 8.17).
- **Systeemgrens en subdienstverleners.** Leg vast welke onderdelen binnen de grens van het lab vallen en welke bij derden liggen (bijvoorbeeld Azure), en waarop het vertrouwen in die derden rust.

### Bewijs dat dit oplevert

Een systeembeschrijving van Hybrid-Theory met grens, een overzicht van ITGC-achtige controls, het changespoor en periodieke, automatisch gegenereerde exports.

---

## 6. ISAE 3000

### Wat het is

ISAE 3000 (Revised) van de IAASB is de algemene standaard voor assurance-opdrachten over andere informatie dan historische financiële informatie. In de praktijk wordt hij gebruikt voor rapportages over informatiebeveiliging, privacy (AVG), NIS2- of DORA-gereedheid en duurzaamheid. Belangrijke begrippen:

- **Redelijke zekerheid** (positief geformuleerd oordeel) tegenover **beperkte zekerheid** (negatief geformuleerd oordeel).
- **Geschikte criteria:** de auditor toetst aan vooraf vastgestelde criteria die relevant, volledig, betrouwbaar, neutraal en begrijpelijk zijn. Zonder geschikte criteria is geen assurance mogelijk.
- Net als bij ISAE 3402 kan een rapport een moment of een periode betreffen.

### Relatie met Hybrid-Theory

ISAE 3000 is breder dan ISAE 3402 en past daardoor beter op de security- en weerbaarheidsdoelen van Hybrid-Theory. De les voor het lab: een bewering als "het lab is gesegmenteerd" is pas toetsbaar als vooraf vaststaat wat "gesegmenteerd" betekent.

### Aandachtspunten netwerkarchitectuur

- **Criteria vóór claims.** Formuleer per zone toetsbare criteria, bijvoorbeeld: "Vanuit LAB is geen verkeer mogelijk naar private netwerken buiten het lab, voor alle protocollen." Dan is ook duidelijk wanneer een test volledig is en wanneer niet.
- **Reikwijdte expliciet.** Leg per bevinding vast welke protocollen, bestemmingen en periode zijn getest. In de bestaande testverslagen wordt dit aangeduid als "binnen geteste scope"; ISAE 3000 biedt hiervoor een relevant assuranceperspectief.
- **Bestaande kaders als criteria.** NIS2 art. 21, DORA art. 9 of ISO 27001 Annex A kunnen als criteria dienen. Mapping via ISO 27001 voorkomt dubbel werk.
- **Zekerheidsniveau eerlijk benoemen.** Eén ICMP-test geeft beperkte zekerheid; een volledige protocol- en bestemmingsmatrix met logbewijs komt dichter bij redelijke zekerheid.

### Bewijs dat dit oplevert

Een criteriadocument per zone of control, testverslagen met expliciete reikwijdte en een eerlijke typering van het bereikte zekerheidsniveau.

---

## 7. SOC 2

### Wat het is

SOC 2 is een attestatiekader van het AICPA (Verenigde Staten), internationaal veel gebruikt door SaaS- en clouddienstverleners. De auditor toetst controls aan de Trust Services Criteria (TSC) in vijf categorieën:

- **Security:** verplicht; de Common Criteria CC1 tot en met CC9.
- **Availability, Processing Integrity, Confidentiality en Privacy:** optioneel, afhankelijk van de dienst.

Net als ISAE 3402 kent SOC 2 een Type 1 (opzet op één moment) en een Type 2 (werking over een periode), een systeembeschrijving met duidelijke systeemgrens en de carve-out- of inclusive-methode voor subdienstverleners.

### Relatie met Hybrid-Theory

SOC 2 vertaalt goed naar een hybride omgeving, omdat de criteria expliciet gaan over systeemgrenzen, logische toegang, monitoring en beschikbaarheid. Voor Hybrid-Theory zijn Security en Availability het meest relevant; Availability sluit direct aan op herstel- en uitvalscenario's.

### Aandachtspunten netwerkarchitectuur

- **Systeemgrens beschermen (CC6.6).** De WAN-zijde van de firewall is de grens: geen beheerinterfaces aan de WAN-kant en alleen expliciet toegestane stromen naar binnen.
- **Logische toegang (CC6.1–CC6.3).** Toegang op basis van rollen, aparte beheeraccounts en periodieke controle van rechten.
- **Verkeer beschermen (CC6.7).** Versleuteld beheer- en dataverkeer tussen zones en naar de cloud.
- **Kwetsbaarheden en monitoring (CC7.1–CC7.2).** Detectie van configuratiewijzigingen en afwijkend verkeer.
- **Incidenten (CC7.3–CC7.5).** Beoordelen, reageren en herstellen, met evaluatie achteraf.
- **Changebeheer (CC8.1).** Wijzigingen geautoriseerd, getest en gedocumenteerd.
- **Leveranciers (CC9.2).** Cloud- en softwareleveranciers beoordeeld en vastgelegd.
- **Beschikbaarheid (A1.2–A1.3).** Backup- en herstelinfrastructuur en periodiek getest herstel.

### Bewijs dat dit oplevert

Een systeembeschrijving met netwerkdiagram en grens, een toegangsoverzicht, het changespoor, monitoringbewijs en verslagen van hersteltests.

---

## Kruisverband: architectuurprincipes × kaders

Per architectuurprincipe de belangrijkste referenties. ISO 27001 Annex A is de primaire sleutel; de overige kolommen tonen waar hetzelfde principe terugkomt. ISAE 3402 en ISAE 3000 staan niet als kolom, omdat zij geen eigen controls voorschrijven maar toetsen aan de controls en criteria uit de andere kaders.

| Architectuurprincipe | ISO 27001 Annex A | NIS2 art. 21(2) | DORA | AVG | SOC 2 |
|---|---|---|---|---|---|
| Segmentatie en default deny tussen zones | 8.20, 8.22 | (a) | art. 9(4)(b); RTS 2024/1774 | art. 32 | CC6.6 |
| Gescheiden beheernetwerk | 8.2, 8.22 | (i) | art. 9(4)(b); RTS 2024/1774 | art. 32 | CC6.1, CC6.6 |
| Least privilege, RBAC en MFA | 5.15, 5.18, 8.2, 8.5 | (i), (j) | art. 9(4)(c)–(d) | art. 25, 32 | CC6.1–CC6.3 |
| Logging, monitoring en tijdsynchronisatie | 8.15, 8.16, 8.17 | (b) | art. 10 | art. 5(1)(f), 33 | CC7.2 |
| Configuratie- en changebeheer | 8.9, 8.32 | (e) | art. 9(4)(e) | art. 32 | CC8.1 |
| Kwetsbaarheids- en patchbeheer | 8.8 | (e) | art. 9(4)(f) | art. 32 | CC7.1 |
| Backup en getest herstel | 5.30, 8.13 | (c) | art. 11, 12 | art. 32(1)(c) | A1.2, A1.3 |
| Versleuteling van verkeer | 8.24 | (h), (j) | RTS 2024/1774 | art. 32(1)(a) | CC6.7 |
| Cloud- en leveranciersbeheer | 5.19–5.23 | (d) | art. 28–30 | art. 28 | CC9.2 |
| Incidentrespons en meldtermijnen | 5.24–5.28 | (b); art. 23 | art. 17–19 | art. 33–34 | CC7.3–CC7.5 |
| Effectiviteit aantonen (positief én negatief testen) | clausule 9 | (f) | art. 24–25 | art. 32(1)(d) | CC4.1 |

Deze tabel is een startpunt voor het controledossier, geen volledige mapping. Elke rij wordt bij uitwerking gecontroleerd tegen de brontekst.

## Wat dit document niet is

- Geen bewijs van naleving of certificering; Hybrid-Theory valt niet onder deze kaders.
- Geen juridisch advies over de toepasselijkheid voor een echte organisatie.
- Geen vervanging van de brontekst: bij uitwerking geldt altijd de officiële tekst van de wet, verordening of norm.

## Bronnen

- Richtlijn (EU) 2022/2555 (NIS2); Cyberbeveiligingswet (Stb. 2026, 187) en Cyberbeveiligingsbesluit (Stb. 2026, 189)
- Verordening (EU) 2022/2554 (DORA) en Gedelegeerde Verordening (EU) 2024/1774 (RTS ICT-risicobeheerkader)
- Verordening (EU) 2016/679 (AVG) en Uitvoeringswet AVG
- ISO/IEC 27001:2022
- IAASB: ISAE 3402 en ISAE 3000 (Revised)
- AICPA: 2017 Trust Services Criteria (met herziene points of focus, 2022)

**Benchmarkdiscipline:** dit document beschrijft bestaande ISO-, ISAE-, SOC 2-, NIS2-, DORA- en AVG-referenties. [CAT/ACE v0.4](CAT_ACE_v0.4.md) beschrijft hun onderzoeksfunctie, gap-analysetypen en de interne, externe of hybride ACE-beoordeling; geen enkele referentie wordt daarmee automatisch toepasselijk of juridisch bindend voor het lab.

**Statusgebruik:** [STATUSLEGENDA](STATUSLEGENDA.md).

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
