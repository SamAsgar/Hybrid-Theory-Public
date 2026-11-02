> **Historische momentopname (gesaneerde export).** Deze sessie is niet retrospectief aangepast aan later werk; zie [de actuele roadmap](ROADMAP.md) en [publieke besluiten](../governance/BESLUITENLOG.md). Echte IP-adressen, domeinen, paden, privésystemen en interne bronlinks zijn verwijderd. `LAB_IP_REDACTED` is geen bruikbare configuratiewaarde.

# Projectlog | 1 november 2026

> Bewerkt 02-11-2026: terminologie geharmoniseerd en interne verwijzingen verwijderd; testuitslagen ongewijzigd.
>
> **TL;DR (redactionele toevoeging)**  
> **Vraag:** Zijn Windows-client, pfSense-DHCP/egress en de AD DS-rol op 1 november bruikbaar gemaakt?  
> **Uitkomst:** Gerichte client-/netwerk-/rolinstallatietests PASS; forestpromotie was in deze eerdere sessie nog PENDING.  
> **Besluit:** Latere 1-novemberdomeinwerkzaamheden staan afzonderlijk in het AD-rapport.
> **Tijdlijn:** AD-promotie en domeintests zijn later op 1 november uitgevoerd; zie [AD-rapport](2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md). De repository staat nu **PUBLIC**; de publicatiegates blijven **OPEN**.
## Windows-client online, pfSense LAB werkend en Windows Server klaar voor AD-promotie

**Project:** Hybrid-Theory  
**Scope:** pfSense LAB + `PS-HT-CLIENT01-Win11` + `PS-HT-VM03-WindowsServer` (hostname `PS-HT-DC01`)  
**Uitvoering:** Project Owner, met technische begeleiding door ChatGPT  
**Aanpak:** Risk-Based Validation, korte functionele tests, geen onnodige extra hardening  
**Resultaat:** **PASS** voor gerichte netwerk-, activatie- en AD DS-installatietests; **PENDING** voor domeinpromotie, AD DNS, domain join, GPO en volledige missieacceptatie  
**Volgende sessie:** maandag 2 november 2026 — focus op werkende demonstraties en vijf primaire missies

### Samenvatting voor reviewers

Deze sessie heeft de virtuele Windows-omgeving van losse installaties naar een werkende LAB-basis gebracht. De Windows 11-client krijgt een IP-adres van pfSense, kan de gateway bereiken en kan via pfSense internetdiensten bezoeken. Windows 11 Enterprise Evaluation toont na het herstellen van internettoegang **Activation state: Active**. De Microsoft Defender-antivirus en realtimebescherming zijn aantoonbaar ingeschakeld.

De Windows Server 2025 Standard Evaluation-VM heeft een vaste naam en een vast IPv4-adres. De rol **Active Directory Domain Services** is succesvol geïnstalleerd. **Dit is nog geen Domain Controller**: promotie tot het eerste forest, AD DNS, domeinjoin en GPO zijn vervolgwerk.

### Nieuw aangetoonde voortgang (ten opzichte van [31 oktober: installatie client](2026-10-31-windows11-client-installatie.md))

| Component | Wat is daadwerkelijk aangetoond? | Verdict |
|---|---|---|
| Windows 11-client | VMware Tools `LAB_IP_REDACTED`, 2 vCPU, 4 GB RAM, 64 GB NVMe, bruikbaar bureaublad | **PASS** voor component- en installatiecontrole |
| Windows 11-installatiemedium | `Connect at power on` uitgezet volgens begeleide handeling; volgende start toont normaal bureaublad zonder setup | **PASS** normale boot; ISO-instelling niet nogmaals visueel nagekeken |
| Windows 11-account | Lokaal gebruikersaccount aanwezig, administrators-groepslidmaatschap zichtbaar in beperkt (UAC) token | **PASS** identificatie; volledige accountaudit niet uitgevoerd |
| Windows 11 Defender | `AntivirusEnabled=True` en `RealTimeProtectionEnabled=True` | **PASS** op deze twee controles |
| Windows 11-activatie | `Windows 11 Enterprise Evaluation`; GUI `Activation state: Active` na internetverbinding | **PASS** actuele activering; exacte evaluatie-einddatum **NOT VERIFIED** |
| pfSense Kea DHCPv4 | LAB `LAB_IP_REDACTED`, uitgiftepool `LAB_IP_REDACTED–150`, DHCPv4-service actief; Windows-client lease en pfSense DHCP-allocatielog | **PASS** |
| Windows 11 gateway | Twee pings naar LAB-gateway na specifieke ICMP-allow: telkens 4/4 antwoorden, 0% verlies | **PASS** |
| pfSense outbound NAT | Automatic Outbound NAT toont LAB-netwerk als bron via WAN | **PASS** configuratiewaarneming |
| Windows 11 DNS/HTTPS | `nslookup microsoft.com` geeft adres terug via pfSense; `Test-NetConnection microsoft.com -Port 443` geeft `TcpTestSucceeded=True`; NU.nl opent | **PASS** voor geteste DNS/HTTPS/browsertoegang |
| Windows Server 2025 | LAN Segment-adapter actief, 2 vCPU, 4 GB RAM, 80 GB virtuele schijf; tijdelijk DHCP-adres ontvangen | **PASS** adapter en LAB-DHCP |
| Windows Server IP/naam | `PS-HT-DC01`; Ethernet0 (ifIndex 6), vast `LAB_IP_REDACTED` met `AddressState: Preferred`; gateway en tijdelijk DNS via `LAB_IP_REDACTED` | **PASS** vast serveradres en hostname |
| Windows Server AD DS-rol | `Install-WindowsFeature AD-Domain-Services -IncludeManagementTools` geeft `Success=True`, `Exit Code=Success`, `Restart Needed=No` | **PASS** rolinstallatie; promotie **PENDING** |

### Nieuwe troubleshooting en verklaringen

**1. DHCP/APIPA:** De client had aanvankelijk een `169.254.x.x` APIPA-adres; `ipconfig /renew` resulteerde in een geldige Kea-lease. De pfSense-log registreerde de OFFER/ALLOC-gebeurtenissen. De gedetailleerdere technische reconstructie is niet in deze publieke sessiesamenvatting opgenomen.

**2. ICMP blokkade:** `LAB_IP_REDACTED → LAB_IP_REDACTED` werd door de RFC1918-blockregel geweigerd. Boven deze regel is een beperkte ICMP Echo Request-uitzondering toegevoegd; de hertest slaagde. Deze samenvatting herhaalt niet alle commando's uit de eerdere technische sessie.

**3. DNS/extern internet (nieuw):** Om een werkende client voor activatie en updates te krijgen, is gecontroleerd dat `Automatic Outbound NAT` het LAB-subnet bevat. De pfSense LAB-regelvolgorde luidt nu:
- ALLOW `LAB_IP_REDACTED` → pfSense LAB-adres: DNS TCP/UDP 53;
- ALLOW `LAB_IP_REDACTED` → pfSense LAB-adres: ICMP Echo Request;
- BLOCK LAB → RFC1918-bestemmingen (ingeschakelde bestaande regel);
- **TEMP** ALLOW `LAB_IP_REDACTED` → overige bestemmingen: IPv4 `Any`.

De regels zijn in de pfSense-GUI toegepast. DNS, TCP/443 en een echte browserpagina zijn daarna succesvol getest. **De TEMP-regel is breed; dit is geen definitieve egress-hardening.** De bestaande RFC1918-blockregel blijft erboven staan. Filtering naar andere private subnetten of de publieke internetbestemmingen is niet uitputtend negatief getest.

**4. Evaluation-activatie (nieuw):** Windows 11 meldde eerder 'license expired' en `slmgr` Notification mode. Na het realiseren van internettoegang toont Windows-instellingenpaneel **Active**. Dit is een waargenomen herstel van de GUI-activatiestatus; precieze oorzaak en resterende Evaluation-duur zijn niet vastgesteld. **Geen key-/rearm-omzeiling gebruikt.**

**5. PowerShell-fout zonder infrastructuurimpact:** Een als resultaatlabel getoonde tekst `TcpTestSucceeded` werd per ongeluk als zelfstandig commando ingevoerd; de daardoor ontstane rode fout is geen netwerkstoring. Het juiste `Test-NetConnection`-commando was al geslaagd.

**6. Windows Server internet / ping:** Server met statisch `LAB_IP_REDACTED` heeft geen vergelijkbare pfSense-clientuitzonderingen als Windows 11. Zijn eerdere ping naar de gateway faalde, terwijl ARP de LAB-gateway herkende. Het firewallbeleid is hiervoor de meest waarschijnlijke verklaring, **geen via server-firewalllog bewezen definitieve root cause**. Browserinternet op de server is **NIET VERIFIED** en is geen blokkade voor het offline installeren van de AD DS-rol. Alleen verder onderzoeken indien de domeinpromotie of noodzakelijke updates dat vereisen.

### Status en werkafspraak

- **Fase 3 (Windows/AD): IN PROGRESS.** Alleen de hierboven geteste onderdelen krijgen PASS; **AD DS-rol geïnstalleerd ≠ Domain Controller actief**.
- **M01 — Lab 01 — Hypervisor Security & Virtualization Hardening; M02 — Lab 02 — Backup, Recovery & Disaster Resilience; M03 — Lab 03 — Hybrid Identity & Access Management; M04 — Lab 04 — Network Segmentation & Security Architecture; M05 — Lab 05 — Regulatory Assessment & Security Assurance:** doel om maandag 2 november zo veel mogelijk aantoonbaar af te ronden. **Geen enkele volledige missie heeft in deze sessie een nieuw voltooiingsverdict gekregen.**
- **Snel en toetsbaar:** alleen stappen die vereist zijn voor functionaliteit, een noodzakelijke veiligheidsgrens of een aantoonbare missietest. Volledige hardening, niet-blokkerende klokdetails, optionele pakketten en cosmetische documentatie blijven geparkeerd.
- **Risicogrens:** vóór ingrijpende domein-/securitywijzigingen een minimale herstelmogelijkheid (VMware-snapshot of geëigende kopie en relevante configuratieback-up) controleren; snapshots zijn **niet** hetzelfde als een onafhankelijke herstelbare off-host-back-up.
- **Publicatie:** uitsluitend interne LAB-testadressen en VM-aliassen in deze log. Geen MAC-adressen, credentials, echte hostbestandslocaties, activerings-ID's of screenshots geüpload. 

### To-do volgende sessie | maandag 2 november 2026

- [ ] **P0 — AD-forest maken:** op `PS-HT-DC01` in Server Manager 'Promote this server to a domain controller' → 'Add a new forest'; voorgesteld labdomein `LAB_DOMAIN` (nog te bevestigen bij wizard). DSRM-wachtwoord veilig bewaren, geen secret in GitHub; promotie en reboot controleren.
- [ ] **P0 — AD DNS werkend:** DC gebruikt zichzelf als DNS (`LAB_IP_REDACTED`); configureer waar nodig DNS-forwarder via pfSense; controleer SRV-records, interne naamresolutie en minimaal de benodigde DNS-verbindingen. Geen blinde netwerkwijzigingen.
- [ ] **P0 — Windows 11 domain join:** client-DNS naar `LAB_IP_REDACTED` (DHCP-optie of gecontroleerde clientinstelling), join, herstart en inloggen met testdomeingebruiker. Werking aantonen.
- [ ] **P0 — Eerste GPO:** één eenvoudig, zichtbaar en reproduceerbaar beleid toepassen en het resultaat op de client verifiëren (`gpresult` of vergelijkbaar). Daarmee M03-techniek demonstreren zonder lange extra audit.
- [ ] **P1 — MISSIES 01–05:** minimale acceptatietests met eerlijk PASS/OPEN per onderdeel; prioriteer werkende hypervisor-/isolatietest, een echte hersteltest, identitytest, netwerkallow/deny en een korte audit/controlmatrix. 
- [ ] **P1 — Showcase:** na PASS gecontroleerde screenshots van client, DC/AD DS/DNS, GPO en technische tests saneren; één begrijpelijke voortgangsamenvatting publiceren in de daarvoor bestemde repo, alleen na publicatiecheck.
- [ ] **PARKED:** hardening/uitbreiding die geen directe blokkade veroorzaakt; GNS3-tijdsynchronisatie en Cockpit Networking volgens hun bestaande parkeerbesluiten. Server-internettoegang alleen indien nodig.

**Sessie-einde:** de gebruiker heeft de AD DS-installatie bevestigd en de werkzaamheden gepauzeerd om te gaan slapen. **Promotie niet gestart; server netjes afsluiten indien nog actief**. De live powerstatus is niet op afstand vastgesteld.

**Bronnen:** [vorig Windows 11-installatielog](2026-10-31-windows11-client-installatie.md) · [Fase 0–7-roadmap](ROADMAP.md).

---

## Avondaanvulling | 1 november 2026 — Lab-1, evidence en CAT/ACE v0.2

**Aard van deze aanvulling:** nieuwe werkzaamheden en inzichten van later op dezelfde datum. Het eerdere gedeelte van dit log blijft een historische momentopname. De terminologie, beleidsstatus en testuitslagen van de eerdere sessie worden **niet met terugwerkende kracht herschreven**. De projectlogboeken van 25 t/m 31 oktober zijn ongewijzigd gelaten.

### 1. Lab-1 | Hypervisor Security & Virtualization Hardening

M01 (Lab 01 — Hypervisor Security & Virtualization Hardening) is voor de publieke bewijsvoering hernoemd naar **Lab 01 — Hypervisor Security & Virtualization Hardening**. Met Claude als Critical Security Auditor zijn drie gerichte controlerondes gerapporteerd voor patchniveau, beheerblootstelling en host-VM-integratie. Het aangeleverde statusrapport  geeft **PASS binnen de geteste scope, met één geaccepteerde EXCEPTION**, niet voor het volledige lab.

| Controle | Waarneming en bewijsgrens | Uitkomst binnen scope |
|---|---|---|
| HV-01 Hypervisor en host | VMware Workstation Pro 26.0.1 (26H1u1) vastgelegd; Windows Update meldde *You're up to date*. Exacte geïnstalleerde patches niet afzonderlijk geïnventariseerd. | PASS (gerichte controle) |
| HV-02 Beheerblootstelling | Onderzochte VMware-listener `vmware-authd` uitsluitend op loopback (`127.0.0.1:912`); VNC op de onderzochte VM's uit. De PowerShell-filtering is geen volledige poort- of firewall-audit. | PASS (gerichte controle) |
| HV-03 LAB-isolatie | Oudere LAB-tests hergebruikt; pfSense-regelvolgorde opnieuw bekeken. Geen nieuwe volledige live-isolatietest tijdens deze rondes. | PASS (configuratie/eerder bewijs) |
| HV-04 Shared folders | Uit op Windows Server, Windows-client en pfSense; globale standaard voor gedeelde mappen uit. | PASS (instelling) |
| HV-04 pfSense guest isolation | Clipboard en drag-and-drop op uit gezet na owner-besluit; instellingen gecontroleerd, effect na toepassen/herstart nog apart te verifiëren. | PASS (instelling); runtime-verificatie OPEN |
| HV-04 Windows guest isolation | Clipboard en drag-and-drop op server/DC en client blijven bewust aan voor beheer. | **EXCEPTION** |
| HV-04 VM-opslag | Werkdirectories van server en client buiten de cloudsynchronisatiemap gecontroleerd. | PASS (gerichte controle) |

**Restrisico EXCEPTION:** de host-guest-uitwisseling via clipboard/drag-and-drop blijft op Windows Server en client mogelijk. Geen wachtwoorden, tokens of andere secrets via deze functies overdragen. Herbeoordeling tijdens het identity-lab of bij verandering van het risicoprofiel.

**PARKED / NOT VERIFIED:** hostdisk-encryptie; reikwijdte en veilige recovery van VM-encryptie (client encrypted, server en pfSense niet); VMware Tools-updatebehoefte; klok/tijdbron van de toekomstige DC; standaardopslaglocatie van nieuwe VM's; HV-05 t/m HV-10 (o.a. logging, continuïteit en incidentrespons). De formele acceptatiecriteria voor **Lab-1 als geheel** moeten nog worden bevestigd. **Geen voltooiingsverdict** verleend.

### 2. Lab 02 — Backup, Recovery & Disaster Resilience

Back-up en herstel zijn besproken, waaronder **Azure Storage als mogelijke off-host bestemming** naast een externe schijf en de toekomstige fysieke Linux-host. **Er is geen Azure-opslag aangemaakt, geen back-up uitgevoerd en geen restore aangetoond.** Cloudkosten, passende versleuteling, toegang, herstelbaarheid en onafhankelijkheid van de host vragen vóór uitvoering een gerichte keuze en controle. De bestaande snapshot `POST-AD-DC01` geldt **niet** als zelfstandige off-host-back-up. **Lab-2 blijft PENDING / NOT VERIFIED.**

### 3. GitHub-bewijsvoering en publicatie

De structuur onder [`bewijsvoering/`](../bewijsvoering/) is verder ingericht met korte README-teksten en inline afbeeldingen die in GitHub onder elkaar verschijnen.

| Onderdeel | Op GitHub gecontroleerde bestanden | Betekenis |
|---|---|---|
| [Lab-1](<../bewijsvoering/Lab-1 | Hypervisor Security & Virtualization Hardening/>) | README + **11** screenshots | HV-01, HV-02 en HV-04; controle- en uitzonderingsbewijs |
| [pfSense](../bewijsvoering/pfSense/) | README + **7** screenshots | Dashboard, ARP, aliassen en LAB/LAN/WAN-regels; historische configuratieopnamen |
| [VMware](../bewijsvoering/VMware/) | README + **5** screenshots | VM-infrastructuurinventarisatie en configuratieoverzicht |
| [Linux](../bewijsvoering/Linux/) | README + **7** screenshots | Ubuntu/Cockpit en Linux-omgeving |
| [Windows Server 2025](<../bewijsvoering/Windows Server 2025/>) | README + **5** screenshots | Server Manager, netwerk/DNS-basis en AD DS-rolinstallatie |

**Bewijsgrenzen:** de Windows Server-opnamen tonen een geslaagde **AD DS-rolinstallatie**, niet een geverifieerde forest-/DC-promotie. Het eerder geconstateerde mislukte ICMP-verkeer naar de labgateway blijft een troubleshootingwaarneming; geen later succes of oplossing aan deze bewijsset ontlenen. De pfSense-opnamen tonen regelconfiguratie en niet een complete end-to-end- of IPv6-beveiligingstest. De Linux- en VMware-overzichten bewijzen evenmin volledige hardening.

De nieuwe Windows Server-README verwijst momenteel alleen naar de **vijf op GitHub aanwezige** PNG's. Er bestond ook een zesde voorbereid screenshot van de mislukte ICMP-test; dit is bij controle **niet** in die GitHub-map aangetroffen en telt niet als gepubliceerd bewijs.

**Publicatiegrens:** screenshots zijn lokaal geschoond en bij de betreffende README voorzien van toelichting. Dit vormt **geen repositorybrede audit** op gevoelige informatie, oude commits of wijzigingsgeschiedenis. Gebruik vaste aliassen en behoud ruwe bewijsstukken in de private bronadministratie. Geen aanname dat oudere gepubliceerde afbeeldingen automatisch zijn beoordeeld.

### 4. Methodologie en AI-samenwerking: nieuw onderzoeksconcept

Vandaag is de richting **CAT/ACE v0.2** verder uitgewerkt als **experimenteel, nog niet gevalideerd onderzoeksconcept** voor Hybrid-Theory. De beoogde analyse betrekt drie lagen: **governance**, **administration & management** en **technische infrastructuur**. Centraal staan traceerbare controls, veranderingsimpact, zwakheden, eigenaarschap, verborgen afhankelijkheden, single points of failure en cascaderende gevolgen.

Als vergelijkingsmateriaal zijn o.a. **NIST CSF 2.0, CIS Controls v8.1 en NIST SP 800-53A** benoemd. Dat impliceert **geen** formele methodiekvalidatie, certificering of complianceclaim. De langetermijnambitie blijft empirische toetsing in **100+ labs**; de praktische labs behouden prioriteit boven theorievorming.

Het bestand [`ai-samenwerking/ROLLEN_EN_OVERDRACHT.md`](../ai-samenwerking/ROLLEN_EN_OVERDRACHT.md) is **vandaag** gericht aangepast: oude methodologieverwijzingen daar zijn vervangen door **CAT/ACE v0.2**, met onderzoekskader en benchmarkreferenties. Dit is een **documentatieaanpassing in één bestand** en geen geautoriseerde projectbrede conversie van de bestaande governance. De nog bestaande verwijzingen naar de eerdere Risk-Based Validation-werkdefinitie in andere documenten en oude logs blijven vooralsnog als historische of nog niet geharmoniseerde context staan. **Geen stilzwijgende vervanging van HT-009 of oudere testuitslagen.**

Voor operationele uitvoering blijven de geldende eigenaarafspraken leidend, met name **HT-011: Flexible Security / Mission-Based Hardening**, bestaande trust boundaries, autorisatie, secretsbescherming en passende rollback. Een concept is niet automatisch een uitvoeringsbesluit.

### 5. Vastgestelde afwijkingen en volgende prioriteiten

- **Documentstatusverschil:** de hoofd-README van Hybrid-Theory noemt Lab-01 momenteel **COMPLETE**, terwijl de gedetailleerde Lab-1-README het lab als **in uitvoering** registreert. Tot formele acceptatie is de voorzichtige status **IN PROGRESS**; een latere gerichte documentcorrectie is gewenst. In deze logupdate zijn geen README's buiten dit log aangepast.
- **Windows Server 2025 / AD:** forestpromotie, AD DNS, domain join, testlogin en eerste GPO blijven **PENDING**. AD DS-roleinstallatie is niet gelijk aan een operationele DC.
- **Lab 01 — Hypervisor Security & Virtualization Hardening:** formele criteria vastleggen, scopegebonden open controles afronden en de Windows-clipboard-EXCEPTION bewaken.
- **Lab 02 — Backup, Recovery & Disaster Resilience:** keuze voor onafhankelijke off-host back-up (eventueel Azure Storage), daarna een **echte restore-test** met bewijs; snapshot alleen is onvoldoende.
- **Overige labs:** Lab 03 — Hybrid Identity & Access Management, Lab 04 — Network Segmentation & Security Architecture en Lab 05 — Regulatory Assessment & Security Assurance blijven vervolgwerk. Geen onnodige controles herhalen als geldig bewijs ongewijzigd kan worden hergebruikt.
- **Publieke bewijsvoering:** periodiek controleren op kapotte afbeeldingslinks, aliasconsistentie, gevoelige metadata en onbedoelde publicatie van private informatie.

**Verificatieregel:** `PLANNED / IMPLEMENTED / VERIFIED` betreft componentstatus; `PASS / REWORK / EXCEPTION` betreft een geteste uitspraak binnen een vastgelegde scope. Een GitHub-commit of screenshot is niet op zichzelf een technische PASS.

**Bronnen voor deze aanvulling:** [Lab 01 README](<../bewijsvoering/Lab-1 | Hypervisor Security & Virtualization Hardening/README.md>) · [pfSense README](../bewijsvoering/pfSense/README.md) · [Windows Server 2025 README](<../bewijsvoering/Windows Server 2025/README.md>) · [Rollen en overdracht](../ai-samenwerking/ROLLEN_EN_OVERDRACHT.md).

**Einde aanvulling:** status op basis van op 1 november beschikbare logs, screenshots en repositorycontrole; geen nieuwe live-VM-test door deze logboekupdate.
