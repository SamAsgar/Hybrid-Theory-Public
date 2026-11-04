# M02 Phoenix Recovery | Herstelarchitectuur v0.5.1

**Project:** Hybrid-Theory · Secure Hybrid Enterprise Network  
**Datum:** 4 november 2026  
**Documenttype:** Security Architecture & Disaster Recovery Concept  
**Status:** **DRAFT — inhoudelijke goedkeuring en technische validatie open**  
**Gekozen ontwerp:** Architectuur B — afzonderlijke recoveryserver  
**Onderzoeksmethode:** CAT/ACE v0.4  
**Bewijsstatus:** Ontwerpbeoordeling uitgevoerd; **geen uitgevoerde of geslaagde M02-hersteltests aangetoond**

> **Leeswijzer voor stakeholders:** Dit document beschrijft het gekozen *ontwerp*, de te onderzoeken beveiligingsmaatregelen en het geplande bewijs. Woorden zoals "voorzien", "beoogd" en "te valideren" betekenen nadrukkelijk **niet** dat een maatregel al is geïmplementeerd. Een AI-ontwerpreview is geen onafhankelijke audit, ISO-certificering of technisch herstelbewijs.

## 1. Doel en besluit

**Onderzoeksvraag:** kan de hybride IT/OT-labomgeving aantoonbaar worden hersteld na hardwareverlies, ransomware, datacorruptie of verlies van de primaire beheeromgeving, zonder afhankelijk te zijn van de oorspronkelijke primaire host?

Phoenix Recovery onderzoekt niet alleen de aanwezigheid van back-ups, maar ook de **onafhankelijkheid, integriteit, beschikbaarheid en herstelbaarheid** ervan. De Project Owner heeft **architectuur B** als ontwerpkeuze aangewezen: een bestaande MacBook wordt uitsluitend voor **lokale recovery** gereserveerd, terwijl de primaire Lenovo **rechtstreeks** een tweede, offsite back-up naar Backblaze B2 verstuurt.

De herstelserver krijgt **geen noodzakelijke rol in de offsite back-upketen**. Afzonderlijke beheerdiensten zijn geen onderdeel van deze missie.

### Besluit en actuele voortgang

| Onderdeel | Ontwerpkeuze | Actuele M02-status |
|---|---|---|
| Primaire Lenovo met VMware Workstation Pro | Bron van VM- en configuratieback-ups | Host beschikbaar; M02-back-ups **niet aangetoond** |
| MacBook Pro 2014 | Afzonderlijke Ubuntu-recoveryserver | **Gepland; installatie en configuratie niet aangetoond** |
| Externe HDD/SSD | Lokale back-upopslag | Capaciteit en inrichting **te bevestigen** |
| Backblaze B2 | Rechtstreeks offsite back-updoel | **Ontwerp; configuratie niet geverifieerd** |
| Restic, REST-server, append-only | Versleutelde back-ups met gescheiden rechten | **Te implementeren en testen** |
| Herstel vanuit geïsoleerde omgeving | Eindproef voor onafhankelijke recovery | **Niet uitgevoerd** |

## 2. Logische topologie: twee onafhankelijke back-uppaden

Het diagram toont de **beoogde architectuur**, niet een reeds werkende koppeling. De twee gestippelde paden zijn afzonderlijke back-upjobs vanuit de Lenovo.

\`\`\`mermaid
flowchart TB
  subgraph SITE["Primaire locatie — bestaande fysieke infrastructuur"]
    ROUTER["KPN-router / lokaal netwerk"]
    HOST["Lenovo · Windows 11 · 32 GB RAM"]
    HV["VMware Workstation Pro"]
    VMS["IT/OT-lab-VM's en configuraties"]
    MAC["MacBook Pro 2014 · Ubuntu Server (beoogd)"]
    DISK["Externe HDD/SSD · lokale repository (beoogd)"]
    ROUTER --- HOST
    ROUTER --- MAC
    HOST --> HV --> VMS
    MAC --> DISK
  end
  CLOUD["Backblaze B2 · Object Lock (te valideren)"]
  KIT["Onafhankelijk herstelpakket · offline/offsite"]
  CLEAN["Vervangende host · geïsoleerde herstelomgeving"]
  HOST -.->|"Pad A: Restic + TLS / REST-server"| MAC
  HOST -.->|"Pad B: Restic via HTTPS, rechtstreeks"| CLOUD
  CLOUD -.->|"Herstel na verlies primaire locatie"| CLEAN
  KIT -.->|"Herstelinstructies en toegangsgegevens"| CLEAN
\`\`\`

**Pad A, lokaal:** Lenovo → Restic → authenticerende REST-server op MacBook → externe opslag. **Pad B, offsite:** Lenovo → Restic → Backblaze B2 via de S3-compatibele API. Het offsite pad loopt **niet** via de MacBook.

**Trust boundaries:** (1) lab/primair beheer tegenover aparte herstelhost, (2) lokale fysieke locatie tegenover cloudopslag, en (3) normale back-uprechten tegenover onderhouds- en noodherstelrechten. Een storing van één back-upbestemming mag de andere route niet automatisch uitschakelen. Dat gedrag moet nog worden bewezen met T3 en T4.

## 3. Back-upomvang, frequentie en hersteldoelen

| Klasse | Herstelobjecten | Voorgestelde frequentie | Retentievoorstel | RPO-doel |
|---|---|---|---|---|
| **A — complete VM** | Uitgeschakelde VM-map inclusief virtuele disks en noodzakelijke VMware-configuratie | Wekelijks | 4 wekelijkse en 3 maandelijkse herstelpunten | 7 dagen |
| **B — configuratie** | Netwerkconfiguraties, pfSense-exports, ondersteunde AD DS/DNS/GPO-herstelgegevens, Linux-/Wazuh-/FUXA-instellingen, GNS3-projecten en recoverydocumentatie | Dagelijks na relevante wijzigingen | 7 dagelijkse, 4 wekelijkse en 3 maandelijkse herstelpunten | 24 uur na een wijziging, mits de job slaagt |

**Vier afzonderlijke repositories zijn voorzien:** \`lokaal-vm\`, \`lokaal-config\`, \`b2-vm\` en \`b2-config\`. Versleutelingsgeheimen en operationele rollen worden per repository beheerd; bruikbare herstelgegevens mogen niet uitsluitend op de primaire host staan.

**Consistentiegrens:** een gewone bestandskopie of snapshot van een draaiende VMware-machine is niet automatisch applicatieconsistent. Voor klasse A is een nette VM-shutdown vereist. Voor Active Directory is bovendien een **ondersteunde herstelprocedure** nodig; alleen een gekopieerde virtuele disk geldt niet als bewijs van werkend identiteitsherstel.

**RTO:** nog **niet vastgesteld**. De eerste werkelijke RTO volgt uit de gemeten duur van T2. RPO's en retentie zijn **ontwerpdoelen**, geen bewezen service levels. Retentiebeleid wordt pas definitief na controle van Restic-selectie, capaciteit, lockgedrag en restoretests.

## 4. Beveiligingsontwerp

| Controle | Beoogde werking | Wat moet worden aangetoond? |
|---|---|---|
| **Minimale netwerktoegang** | Alleen geautoriseerde back-upverbindingen naar de recoveryserver; hostfirewall default-deny, geen publieke port-forward | Positieve en negatieve connectiviteitstests, inclusief verkeer via VMware NAT |
| **Authenticatie en TLS** | REST-server vereist identiteit en versleuteld transport; een IP-allowlist is niet voldoende | Onbevoegde toegang geweigerd; certificaat- en vervalbewaking |
| **Append-only lokaal** | Normale back-upidentiteit kan nieuwe data wegschrijven maar oudere herstelpunten niet beheren/verwijderen | Pogingen tot verwijdering of wijziging mislukken |
| **Gescheiden onderhoud** | Onderhoud gebeurt met een andere identiteit vanaf de herstelserver, niet via onbeperkte beheerrechten vanaf Lenovo | Rechtenmatrix, lokale beheerprocedure, logboek en dry-run voor retentie |
| **Object Lock offsite** | B2-objectversies beschermd tegen voortijdige verwijdering | Test van Governance Mode, verwijderen, versieherstel en Restic-maintenance |
| **Geheimen en versleuteling** | Restic versleutelt back-upinhoud; afzonderlijke herstelgegevens worden beschermd | Restore zonder primaire host en controle van resterende onversleutelde hostgegevens |
| **Capaciteit en signalering** | Opslaglimieten, monitoring en waarschuwingen bij mislukte jobs | Aantoonbare melding via een kanaal dat niet uitsluitend op de Lenovo draait |

**Onderhoud:** vooraf job pauzeren, \`restic check\` uitvoeren, snapshots en tijdstempels beoordelen, \`forget --dry-run\` controleren, uitsluitend goedgekeurde retentie toepassen en opnieuw controleren. Bij object-lock kan \`prune\` worden geblokkeerd; de samenwerking tussen retentie, immutable versies en repositorybeheer moet eerst op een **testrepository** worden vastgesteld. Nooit verwijderrechten toekennen aan de normale back-upidentiteit om een onderhoudsprobleem snel te omzeilen.

**B2-configuratie:** een retentie van **30 dagen in Governance Mode** is alleen een **testkandidaat**. Lifecycle-instellingen mogen nog benodigde objectversies niet vroegtijdig verwijderen. Zonder bewezen versieherstel is er geen claim van ransomwarebestendigheid.

## 5. Onafhankelijke herstelgegevens

Twee afzonderlijk beschermde herstelpakketten zijn voorzien, waarvan één buiten de primaire locatie. Ze bevatten **geen openbaar te publiceren geheimen**, maar wel een procedure om toegang tot benodigde repositorywachtwoorden, cloudhersteltoegang, MFA-herstelmiddelen, VM-versleutelingssleutels, identiteitsherstelgegevens, softwarebronnen, netwerkinventaris en runbooks te verkrijgen.

**Acceptatiecriterium:** met vervangende hardware en het offsite herstelpakket moet een recovery mogelijk zijn zonder de oorspronkelijke Lenovo of MacBook. De feitelijke inhoud, opslagplaats en toegang worden alleen in afgeschermde operationele documentatie vastgelegd.

## 6. Herstelvolgorde en afhankelijkheden

Back-upbestanden kunnen waar mogelijk parallel worden teruggezet. **Functionele validatie** volgt de werkelijke afhankelijkheden.

\`\`\`mermaid
flowchart TD
  NEW["Vervangende hardware + VMware"]
  VMNET["VMware virtuele netwerken"]
  FW["pfSense · routing / firewall"]
  ID["Windows Server · AD DS / DNS"]
  CLIENT["Windows 11 · domeinlogin / GPO"]
  LIN["Ubuntu · applicatiediensten"]
  MON["Wazuh · monitoring"]
  OT["FUXA · HMI"]
  SIM["GNS3 · gesimuleerde topologie"]
  NEW --> VMNET
  VMNET --> FW
  FW --> ID
  ID --> CLIENT
  VMNET --> LIN
  VMNET --> MON
  VMNET --> OT
  VMNET --> SIM
\`\`\`

**Toelichting:** de pijlen geven de *beoogde herstel- en validatievolgorde* voor de belangrijkste diensten weer, niet elke mogelijke technische afhankelijkheid. Diensten zoals Ubuntu, Wazuh, FUXA en GNS3 worden afzonderlijk gevalideerd zodra hun eigen netwerk- en servicevoorwaarden zijn vervuld. Voor Windows Server gelden aanvullende AD DS-/DNS-/tijd-/systeemstateisen. Versleutelde VMware-VM's of BitLocker vereisen hun eigen herstelsleutels.

## 7. Dreigingsbeeld en resterende risico's

| Scenario | Ontwerprespons | Belangrijk restrisico |
|---|---|---|
| Uitval Lenovo | Lokale of B2-back-up op vervangende host herstellen | Beschikbaarheid vervangende hardware |
| Uitval MacBook | Rechtstreekse B2-route blijft beschikbaar | Afhankelijkheid van internet/B2 |
| Ransomware of gestolen gewone back-upcredentials | Append-only lokaal en Object Lock offsite | Onjuiste rollen, verlopen retentie, gestolen onderhoudsrechten |
| Corruptie van lokale repository | Losse offsite repository | Onontdekte corruptie of ongeldige cloudkopie |
| Verlies van de primaire locatie | B2 + apart herstelpakket | Cloudtoegang, herstelgeheimen en downloadtijd |
| Manipulatie via snapshots of opslaguitputting | Tijdvensterretentie, review, limieten, waarschuwingen | Beschikbaarheid tijdens aanval of onderhoud |
| Onjuiste cloud lifecycle | Test van versies, retentie en herstel | Niet-herstelbare verwijdering na verval van bescherming |

**Hoge prioriteit voor validatie:** onbevoegde verwijdering, cloudversieretentie, onderhoudsrechten en clean-room recovery. Daarnaast blijven fysieke concentratie op één locatie, gedeeld thuisnetwerk, stroomvoorziening en één beheerder gezamenlijke afhankelijkheden. Deze risico's verdwijnen niet door twee back-upjobs te configureren.

## 8. Test- en bewijsplan

**Alle onderstaande M02-tests staan op PENDING.** Testresultaten worden niet vooraf als PASS geregistreerd.

| Test | Kernvraag | PASS wanneer |
|---|---|---|
| **T1 — Lokale VM-restore** | Is de lokale kopie bootbaar en functioneel? | Geïsoleerde VM start, kerndienst werkt, duur gemeten |
| **T2 — Clean-room / totaalverlies** | Is herstel mogelijk zonder primaire hosts? | B2 + offsite herstelpakket herstellen pfSense, identiteit en Linux; services en hashes gecontroleerd; RTO gemeten |
| **T3 — Deletion en autorisatie** | Zijn beschermde herstelpunten bestand tegen onbevoegde verwijdering? | Negatieve tests blokkeren acties of data blijft aantoonbaar herstelbaar |
| **T4 — MacBook-uitval** | Is de offsite route echt onafhankelijk? | B2-back-up slaagt terwijl MacBook uitstaat |
| **T5 — Corruptiedetectie** | Wordt beschadigde back-updata opgemerkt? | Een gecontroleerd beschadigde testkopie faalt een passende inhouds-/integriteitscontrole |
| **T6 — Foutsignalering** | Worden mislukte jobs tijdig ontdekt? | Uitval, opslaggebrek en TLS-fout leiden tot een vastgelegde melding |
| **T12 — Onderhoud onder aanval** | Blijven legitieme herstelpunten behouden? | Dry-run en onderhoud op testrepository herkennen afwijkingen zonder noodzakelijke data te verliezen |

Per test vastleggen: **test-ID, datum, systeemscope, uitgangsconfiguratie, verwacht resultaat, feitelijke uitkomst, PASS/FAIL, tijdmeting, logs/screenshots, SHA-256 van bewijs en bekende beperkingen**. Gevoelige waarden worden vóór publieke verspreiding gesaneerd. Bestaand geldig bewijs mag worden hergebruikt, maar krijgt geen ruimere conclusie dan daadwerkelijk getest.

## 9. CAT/ACE v0.4: toetsingskader

| Onderdeel | Toepassing binnen M02 |
|---|---|
| **CAT · Corporate Governance & Compliance** | Risico-eigenaarschap, relevante ISO/IEC 27001- en NIST CSF 2.0-referenties, bewijsgrenzen |
| **CAT · Accountability & Management** | Project Owner bepaalt scope, retentie, herstelprioriteit, restrisico en formeel akkoord |
| **CAT · Technology & Operations** | Trust boundaries, toegangsrechten, versleuteling, beschikbaarheid en werkende herstelketen |
| **ACE · Audit** | Reproduceerbare positieve en negatieve tests, bewijs en onafhankelijke review waar passend |
| **ACE · Cost** | Onderscheid tussen **GESCHATTE** en **GEMETEN** kosten: opslag, objectversies, herstelverkeer, stroom en beheer |
| **ACE · Efficiency** | Aantonen of twee gescheiden paden de complexiteit beperken zonder beveiligingsverlies |

CAT/ACE is hier een **onderzoeksmodel**, geen certificering of vervanging van erkende standaarden. De ontwerpkeuze vereist herbeoordeling na wezenlijke wijzigingen aan identity, VMware-netwerken, sleutels, opslagbeleid of back-upjobs.

## 10. Gefaseerde uitvoering en beslismomenten

| Fase | Werkzaamheden | Exitcriterium |
|---|---|---|
| **1 · Lokale basis** | VM-/sleutelinventaris, MacBook + externe opslag, REST-server met TLS en append-only, gescheiden rollen, lokale jobs en alarmering | T1, T5, T6 en T12 aantoonbaar afgerond |
| **2 · Offsite herstel** | B2-testbucket, onafhankelijke cloudrepositories, Object Lock en lifecycle toetsen | T3 en T4 aantoonbaar afgerond |
| **3 · Onafhankelijke recovery** | Twee beschermde herstelpakketten, één offsite; clean-room scenario | T2 geslaagd en eerste gemeten RTO vastgesteld |

**Open beslissingen:** capaciteit externe opslag, onafhankelijk meldkanaal, definitieve B2-retentie en lifecycle, offsite opslaglocatie van herstelpakket en uitkomsten van de eerste restores. Deze punten zijn **niet** als uitgevoerde werkzaamheden geregistreerd.

## 11. Architectuurbesluit en eindbeoordeling

| Kenmerk | Stand per 4 november 2026 |
|---|---|
| **ADR** | M02-ADR-001 · Architectuur B |
| **Project Owner** | Heeft de architectuurrichting gekozen; formele documentvaststelling staat open |
| **AI-ontwerpbeoordeling** | Design PASS volgens interne AI-self-assessment; geen onafhankelijke audit |
| **Technische controles** | PENDING |
| **Herstelzekerheid** | PENDING |
| **RTO/RPO in praktijk** | RTO onbekend; RPO alleen als doel geformuleerd |
| **Compliance-/certificeringsclaim** | Geen |

**Conclusie:** Phoenix Recovery v0.5.1 is een afgebakend, uitvoerbaar **ontwerpconcept** voor lokaal en offsite herstel. Betrouwbare disaster recovery of ransomwarebestendigheid is **niet aangetoond** totdat de gespecificeerde herstel-, autorisatie- en integriteitstests met bewijs zijn uitgevoerd.

---

*Documentatie uitsluitend op ontwerp- en onderzoeksniveau. Topologiediagrammen zijn schematisch; geen live netwerkexport en geen testbewijs.*