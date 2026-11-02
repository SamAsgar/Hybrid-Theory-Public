> **Historische momentopname (gesaneerde export).** Deze sessie is niet retrospectief aangepast aan later werk; zie [de actuele roadmap](ROADMAP.md) en [publieke besluiten](../governance/BESLUITENLOG.md). Echte IP-adressen, domeinen, paden, privésystemen en interne bronlinks zijn verwijderd. `LAB_IP_REDACTED` is geen bruikbare configuratiewaarde.

# Projectlogboek Hybrid-Theory | 24 en 25 oktober 2026

> Bewerkt 02-11-2026: terminologie geharmoniseerd en interne verwijzingen verwijderd; testuitslagen ongewijzigd.
>
> **TL;DR (redactionele toevoeging)**  
> **Vraag:** Wat leverden de Ubuntu/Cockpit-, pfSense-voorbereidings- en documentatiesessies van 24–25 oktober op?  
> **Uitkomst:** Gerichte Ubuntu-/Cockpit-controles en eerste documentatie zijn gerapporteerd; overige netwerkcontroles zijn afgebakend.  
> **Besluit:** Alleen scopegeldige testresultaten behouden; niet-geteste isolatie en latere fases blijven open.


**Periode:** zaterdag 24 en zondag 25 oktober 2026  
**Werkstromen:** VMware, Ubuntu Server, netwerkbeheer, Cockpit, AI-samenwerking, GitHub-governance en pfSense-voorbereiding  
**Rapportagestatus:** retrospectief technisch voortgangsverslag  
**Publicatie:** publieke, geredigeerde versie; privénetwerkgegevens, hostidentiteiten, vertrouwelijke repositorynamen en ongeredigeerde screenshots zijn niet overgenomen.

> **Bewijsinterpretatie:** dit log is gereconstrueerd uit de vastgelegde technische sessieverslagen, sessieobservaties en GitHub-wijzigingen. Een gerapporteerde testuitslag is niet automatisch een onafhankelijke, opnieuw uitgevoerde test. We maken onderscheid tussen **UITGEVOERD**, **GETEST**, **GEPARKEERD** en **GEPLAND**.

## 24 oktober 2026 | Ubuntu-netwerk, updates en risicogestuurd werken

### 1. Linux-baseline en naamgeving: UITGEVOERD / PASS

- Bestaande **Ubuntu Server 24.04.5 LTS**-VM in **VMware Workstation Pro** gebruikt (2 vCPU, 4 GB RAM, 30 GB virtuele schijf).
- VM-weergavenaam gewijzigd naar **bestaande Ubuntu-VM**; gast-hostname ingesteld op `hybrid-theory-linux`.
- Normaal opstarten, lokale aanmelding en behoud van naam na herstart gecontroleerd. Deze kleine naamgevingswijziging is als **PASS** afgesloten, zonder onnodige hertests.
- Eerder geïnstalleerde VM en opslaglocatie bleven gehandhaafd; 23 oktober was de installatie- en accountherstelsessie, **niet** een nieuwe installatie op 24 oktober.

### 2. Diagnose: netwerkinterface niet geconfigureerd

**Symptoom:** de geïsoleerde labinterface was aanwezig, maar toonde `degraded / unmanaged` en had geen persistente IPv4-configuratie.

**Gerichte diagnose:**
- `systemctl is-active/is-enabled systemd-networkd`: dienst bleek **active / enabled**.
- Netplan aanwezig; **NetworkManager niet geïnstalleerd** (verwacht voor deze serveropzet).
- `/etc/netplan/` was leeg.
- Installer-/cloud-init-configuratie bevatte `ethernets: {}`, waardoor `ens33` geen bruikbare netwerkdefinitie kreeg.
- Een eerdere conclusie dat de netwerkdiensten inactief waren, is **ingetrokken**: er waren typefouten gemaakt in de dienstnamen (`system-networkd` en `Networkmanager` in plaats van `systemd-networkd` en `NetworkManager`).

**Oplossing en resultaat:**
1. Snapshot **`voor-netplan-24oct`** gemaakt als herstelpunt.
2. Automatische cloud-init-netwerkconfiguratie uitgeschakeld met `/etc/cloud/cloud.cfg.d/99-disable-network-config.cfg` (`network: {config: disabled}`).
3. `/etc/netplan/01-hybrid-theory.yaml` aangemaakt met rechten **600**: `ens33` statisch op het geïsoleerde labsegment, `renderer: networkd`, `dhcp4/dhcp6: false`, `accept-ra: false`, **geen gateway en geen DNS**.
4. `sudo netplan try` uitgevoerd en de configuratie tijdig geaccepteerd.
5. Met `ip -br addr`, `ip route` en `networkctl list` aangetoond dat `ens33` **UP/configured** is en alleen de lokale labroute aanwezig is.
6. **Herstarttest PASS:** adres en route bleven zonder handmatige ingreep behouden. Snapshot **`na-netplan-24oct`** bevestigd.

**Grenzen van de PASS:** persistente labconfiguratie werkt; volledige netwerkisolatie met een tweede labdeelnemer was nog **niet** bewezen.

### 3. Netwerkmogelijkheden voor toekomstige lab-internettoegang: ONDERZOCHT

- Een afzonderlijk gastnetwerk op de eigen router aangemaakt en tijdelijk met de laptop getest.
- Gastapparaat ontving een ander IPv4-subnet; internetverbinding werkte en routerbeheer via het normale huishoudelijke subnet was tijdens de test niet bereikbaar.
- IPv6-blokkering en bereikbaarheid van alle andere thuisapparaten zijn **niet** volledig getest; de IPv6-beperking is toen expliciet als restrisico genoteerd.
- Overwogen: tweede fysieke wifi-adapter en bridged verbinding richting gastnetwerk.
- **Uiteindelijk besluit:** géén extra USB-wifi-adapter inzetten voor deze VM; de Ubuntu-server krijgt een **tijdelijke VMware NAT-updateadapter**. Het gastnetwerk werd daarmee **niet** de actuele updateverbinding.

### 4. Tijdelijke NAT-updateverbinding: UITGEVOERD / PASS

- Met de VM uit een **tweede VMware-netwerkadapter** toegevoegd: **NAT / VMnet8**.
- **`Connect at power on` uit**, zodat de updateverbinding normaal losgekoppeld blijft.
- Ubuntu herkende deze adapter als **`ens37`**. Netplan: `dhcp4: true`, `dhcp6: false`, `accept-ra: false`, `optional: true`.
- Verbinding op verzoek ingeschakeld; DHCP-adres, standaardroute via VMware NAT en publieke IPv4-connectiviteit via `ping -c 4 PUBLIC_TEST_IP` gecontroleerd.

**Bewuste afweging:** VMware NAT geeft tijdelijk internettoegang, maar sluit toegang tot bereikbare andere privénetwerken niet per definitie uit. Daarom bleef de updateadapter standaard losgekoppeld. Dit is een tijdelijke praktische oplossing, geen formele volledige isolatiegarantie.

### 5. Troubleshooting: APT-bronnen en eerste systeemupdate

| Waargenomen probleem | Diagnose | Correctie / eindstatus |
|---|---|---|
| `apt update` meldde dat `file:/cdrom noble Release` ontbrak | Bij de offline installatie was alleen de installatie-cd als pakketbron geconfigureerd | Oorspronkelijke `sources.list` veiliggesteld; cd-bron uitgecommentarieerd |
| Nieuwe `ubuntu.sources` in deb822-formaat gaf **`Malformed stanza 1 (type)`** | Typfout in pocketnaam gecorrigeerd en tekens gecontroleerd; vermoeden over dubbele lege regel bleek onjuist | **Root cause niet vastgesteld**; deb822-bestand als lokale back-up bewaard en werkende klassieke pakketbrondefinities gebruikt |
| `noble-backsports` en `multiverse` verkeerd ingevoerd | Pocketnaam verkeerd gespeld; component kwam op een eigen regel terecht | Gecorrigeerd naar `noble-backports` en geldige repositoryregels |
| Upgrade meldde **Pending kernel upgrade** | Nieuwe kernel stond klaar maar draaide nog niet | NAT-adapter los, VM herstart en nieuwe kernel gecontroleerd |

**Resultaat na herstel van APT:**
- Pakketlijsten succesvol opgehaald van officiële Ubuntu-archieven.
- **107 pakketten bijgewerkt**, **7 pakketten nieuw geïnstalleerd**, **0 verwijderd**; volgens het sessieverslag **78 beveiligingsupdates** en circa **322 MB** download.
- Nieuwe kernel: **`6.8.0-147-generic`**.
- Onder andere Netplan, cloud-init, OpenSSL, systemd, sudo en open-vm-tools bijgewerkt.
- Na de reboot: **0 openstaande updates** gemeld, `ens33` bleef actief, `ens37` bleef losgekoppeld en er was **geen standaardroute**.
- Lokale Netplan- en cloud-init-instellingen bleven behouden: **PASS voor de geteste update- en herstartsessie**.
- De deb822-parserfout is **geparkeerd**, omdat de werkende alternatieve configuratie het actuele probleem oploste; geen eindeloze troubleshooting zonder nieuwe aanwijzing.

### 6. Windows-/VMware-review en AI-werkafspraken

- **Windows Hypervisor & VBS:** de status van Windows-virtualisatiebeveiliging en aanwezige hypervisor is via hostinformatie en Microsoft-specialistische beoordeling onderzocht. Vaststelling van VBS/hypervisor is **niet gelijk aan** bewezen VMware-executiemodus; die nuance bleef open. Geen beveiligingsfuncties uitgeschakeld puur voor prestatieverbetering.
- **Risk-Based Validation** als werkafspraak vastgelegd: maximaal drie stappen per instructieronde, geen dubbele controles, geen eindeloze troubleshooting, na een geldige PASS stoppen tenzij een aantoonbaar materieel risico overblijft.
- AI-rollen en een mogelijk toekomstig gebruik van Codex besproken. **Codex niet geactiveerd of ingezet** voor deze labsessie.
- Cockpit gekozen als volgende Linux-sidequest; op 24 oktober **nog niet geïnstalleerd**.

---

## 25 oktober 2026 | Cockpit, beheernetwerk, tijdcorrectie en publieke GitHub-baseline

### 7. Ubuntu Cockpit fase 1: UITGEVOERD / PASS binnen geteste scope

**Doel:** de bestaande Ubuntu Server vanuit de Windows-browser beheren, zonder een grafische desktop op Linux te installeren en zonder Cockpit rechtstreeks op internet te publiceren.

**VMware-netwerkrollen na de uitbreiding:**

| Linux-interface | VMware-modus | Rol | Normale toestand |
|---|---|---|---|
| `ens33` | LAN Segment | Geïsoleerd Linux-lab | Verbonden, statisch labadres, geen gateway |
| `ens37` | NAT / VMnet8 | Tijdelijke updateverbinding | **Losgekoppeld**, DHCP alleen tijdens onderhoud |
| `ens38` | Host-only / VMnet1 | Beheerinterface voor Cockpit | Eigen statisch beheeradres, geen gateway |

**Uitgevoerde configuratie:**
1. Snapshot **`na-update-24oct`** bevestigd als bijgewerkte uitgangssituatie.
2. Derde VMware-adapter voor host-only beheer toegevoegd en in Ubuntu als `ens38` geconfigureerd met Netplan; `dhcp4/dhcp6: false`, `accept-ra: false`, `optional: true`, geen gateway of DNS. `netplan try`: **Configuration accepted**.
3. Windows-host kon het beheeradres bereiken (**4/4 pingantwoorden**); Ubuntu had alleen lab- en beheerroutes, **geen default route** zolang NAT uit stond.
4. Via de tijdelijke NAT-updateverbinding **`sudo apt install --no-install-recommends cockpit`** uitgevoerd: **Cockpit 314**, **17 pakketten**, circa **4,8 MB**.
5. `cockpit-networkmanager`, `cockpit-storaged` en `cockpit-packagekit` bewust **niet geïnstalleerd**. Geen onnodige NetworkManager naast Netplan/systemd-networkd.
6. Cockpit-systemd-socket met een override beperkt tot **het host-only beheeradres op TCP 9090** (niet alle interfaces), met `FreeBind=yes`.
7. **UFW active**, standaard **deny incoming**; een specifieke regel laat TCP 9090 uitsluitend binnen op `ens38` vanaf de bedoelde Windows-beheerhost.
8. Linux `net.ipv4.ip_forward=0` en Windows-host `IP Routing Enabled: No` gecontroleerd.
9. `ss -tln` bevestigde luisteren op uitsluitend het beheeradres; aanmelding op het Cockpit-dashboard vanaf de Windows-browser lukte met het bestaande labbeheeraccount.

**Resultaat:** de beheerinterface werkte via VMnet1 zonder het geïsoleerde labsegment als beheerroute te gebruiken. Dit is **PASS voor de beschreven configuratie en positieve bereikbaarheidstests**, nog geen onafhankelijke volledige netwerksegmentatie-PASS.

### 8. Troubleshooting tijdens de Cockpit-installatie

| Fout / symptoom | Oorzaak of uitleg | Herstel en resultaat |
|---|---|---|
| Eerste `apt update`: **Temporary failure resolving** | VMware NAT-updateadapter was niet verbonden; er was geen bruikbare externe route voor DNS | Updateadapter tijdelijk aangesloten; daarna werkte pakketinstallatie |
| **Permission denied / directory not writable** bij `listen.conf` | Configuratiebestand geopend zonder beheerdersrechten | Opnieuw bewerkt met `sudo`; socket-override kon worden opgeslagen |
| `Freebind` in plaats van `FreeBind` | systemd-configuratiesleutels zijn hoofdlettergevoelig | Gecorrigeerd vóór het opslaan; socketbinding werkte |
| Cockpit was aanvankelijk op alle interfaces gebonden | Standaard `ListenStream` luisterde breed | Standaardlistener met lege `ListenStream=` gewist; expliciete binding op alleen het beheeradres en `FreeBind=yes` toegevoegd |
| Cockpit-toegang zou vanaf het geïsoleerde LAN Segment niet direct in Windows werken | LAN Segment is niet hetzelfde als host-only; de host zit niet vanzelf in het labsegment | Apart VMnet1-beheerpad ingericht; browserlogin geslaagd |
| Browser toont **Not secure** bij Cockpit HTTPS | Zelfondertekend TLS-certificaat in het lab | Geregistreerd als bekend labrestrisico; **niet** als mislukte installatie aangemerkt |

### 9. Troubleshooting systeemtijd in Cockpit: OPGELOST

- Cockpit toonde een **rood waarschuwingsteken bij Systeemtijd**.
- `timedatectl` wees uit dat de machine wel tijd had, maar `System clock synchronized: no` rapporteerde en externe NTP probeerde te gebruiken zonder permanente internetroute.
- Het schijnbare verschil van **één uur** kwam overeen met **UTC tegenover Nederlandse wintertijd**, na de klokwisseling op 25 oktober; geen bewezen klokdefect.
- Gekozen: **VMware Tools-tijdsynchronisatie met Windows-host** als bron; `sudo timedatectl set-ntp false`; tijdzone **`Europe/Amsterdam`**.
- Controle daarna: lokale tijd gelijk aan host, `synchronized: yes`, NTP-service inactief, waarschuwing verdwenen: **PASS**.
- De keuze voor lokale tijd blijft bewust; bij toekomstige Active Directory-implementatie kan een ander tijdbronontwerp nodig zijn.

### 10. Verificatie updateverbinding via Cockpit-terminal: PASS

- Tijdelijke NAT-adapter ingeschakeld: standaardroute verscheen; `ping PUBLIC_TEST_IP` en DNS-resolutie met `ping ubuntu.com` beide **4/4 succesvol**.
- NAT-adapter weer losgekoppeld: standaardroute verdween.
- Cockpit bleef vóór, tijdens en ná deze test bereikbaar via de afzonderlijke beheerinterface.
- Hiermee is de **scheiding van beheerpad en tijdelijke updateroute in de geteste configuratie** aangetoond; er is geen alomvattende negatieve isolatietest van alle routes uitgevoerd.

### 11. VMware-opruiming, snapshots en open restrisico's

**Afgerond:**
- Installatie-ISO daadwerkelijk ontkoppeld van automatische VM-start.
- Shared Folders en VNC uitgeschakeld; geen camera- of Bluetooth-passthrough gebruikt.
- VMware Tools-tijdsynchronisatie ingeschakeld.
- Drie genoemde herstelpunten bevestigd: **`na-update-24oct`**, **`cockpit-geinstalleerd-25oct`** en **`cockpit-afgeschermd-25oct`**; het laatste is de nieuwe Cockpit-baseline.

**Nog open, niet opnieuw testen zonder gerichte aanleiding:**
- Controleren of het Windows-hostadres op VMnet1 duurzaam vastligt en of het statische beheeradres buiten de DHCP-uitgiftereeks valt.
- Negatieve tests voor ongewenste toegang tot Cockpit vanaf het labsegment en voor eventueel doorsturen tussen zones.
- NAT kan gedurende open onderhoudsvensters mogelijk andere bereikbare privénetwerken bereiken.
- Zelfondertekend TLS-certificaat is een geaccepteerd labrestrisico.
- Verschil in historische naamgeving van een VMware-segment, PMF-instelling van het aparte gastnetwerk waar nog werkelijk nodig.
- Een VMware-snapshot is geen vervanging voor een onafhankelijke back-up.

### 12. Router-, hardware- en continuïteitsplanning

- DHCP-reservering van de primaire Windows-host in de eigen router ingesteld en visueel vergeleken met de actieve Windows-netwerkconfiguratie: **PASS voor huidige adresinstelling**. Er is geen claim van een latere leasevernieuwing.
- Architectuur voor een **tweede fysieke Linux-host** besproken: een oudere laptop met circa 8 GB RAM waarop Ubuntu Server op bare metal kan draaien, onafhankelijk van het VMware-platform. Mogelijke taken: Cockpit/SSH, lichte containers, monitoring, back-ups en hersteltests. **Nog niet geïnstalleerd.**
- Toekomstig Azure VNet, identity, monitoring en private-cloudcomponenten blijven ontwerp/roadmap; geen Azure-deployment of cloudrekening op basis van deze sessies bevestigd.

### 13. Publieke GitHub-repositories en documentatie: UITGEVOERD

- Een **zelfstandige publieke Hybrid-Theory-repository** ingericht met dezelfde categorieën hoofdmappen als de eerder gebruikte interne structuur, maar met **nieuw geschreven en voor publicatie geschoonde inhoud**.
- README, `.gitignore`, architectuur-, governance-, evidence-, AI-collaboration- en projectlogdocumenten toegevoegd. Onder meer de Linux/Cockpit-servicekaart, netwerkmatrix, pfSense-plan, AI-taakmatrix, roadmap en besluitlog zijn als werkdocumenten aangemaakt.
- de destijds gebruikte (inmiddels vervallen) architectuurblueprint v1.0 (PDF) gepubliceerd en daarna voorzien van **PROVISIONAL DESIGN** en een formele vermelding dat validatie en goedgekeurde ontwerpbesluiten tot wijzigingen kunnen leiden.
- In **de projectdocumentatie** is berichtuitwisseling via GitHub getest door ChatGPT, Claude en GitHub Copilot. Dit is een test van **GitHub-communicatie**, niet van infrastructuurconnectiviteit.
- Op verzoek een uitgebreide **pfSense-review** geplaatst en daarna **hetzelfde commentaar** in het Nederlands herschreven, zonder dubbel bericht.

**Troubleshooting van de publicatieworkflow:** een automatische controle markeerde een legitieme verwijzing naar de **andere publieke** projectrepository als mogelijk gevoelig. Het onderscheid tussen publieke en vertrouwelijke verwijzingen is gecorrigeerd; daarna zijn bestanden in één commit gepubliceerd. Geen gedeeltelijke ongewenste publicatie aangetoond.

### 14. AI Work Policies: UITGEVOERD EN BIJGEWERKT

- Bestand `governance/AI_WERKAFSPRAKEN.md` (aanvankelijk leeg) ingevuld met **12 onderdelen** over gerichte, risicogestuurde uitvoering.
- Vastgelegd: **niet onnodig dubbelchecken**, maximaal drie uitvoerstappen per ronde, symptoomgestuurde troubleshooting, na PASS stoppen tenzij materieel risico, geen eindeloze AI-reviewrondes, geen ongevraagde herontwerpen en Project Owner als eindbeslisser.
- Extra instructie van de eigenaar verwerkt: **niet té voorzichtig werken**, zodat onomkeerbare of daadwerkelijk risicovolle handelingen relevante controles behouden en eenvoudige taken niet in bureaucratie vastlopen.
- Na inhoudelijke controle **twee onduidelijkheden gecorrigeerd**:
  - `READY FOR IMPLEMENTATION` is een **fase-aanduiding**, geen vierde formele reviewuitkomst.
  - `EXCEPTION` vervangt nooit verplichte veiligheidscontroles of essentiële herstelvoorwaarden.
- **Vaste wijzigingsprocedure** toegevoegd: bij ieder nieuw beleidsvoorstel eerst controleren op **bestaande regels, overlap en tegenspraken**; bestaande regel bijwerken in plaats van beleid te dupliceren. Daarna één gerichte eindcontrole.

### 15. pfSense op VMware: BESPROKEN EN AKKOORD VOOR VERVOLG, NOG NIET GEÏNSTALLEERD

- Via de oorspronkelijke engineeringnotities is aanvankelijk een technisch ontwerp besproken voor een VMware NAT-WAN, geïsoleerd lab-LAN, veilige webGUI-toegang en restrictief firewallbeleid.
- De Project Owner heeft daarna expliciet gevraagd om **minder overmatige voorzichtigheid** en ingestemd met **internet tijdens de pfSense-installatie**. Claude heeft het plan vereenvoudigd om overbodige voorbereidende rondes te vermijden.
- **Laatst overeengekomen uitvoerrichting (voorstel van Claude, akkoord eigenaar):** pfSense-VM met **2 vCPU, 2 GB RAM, 20 GB disk** en **drie adapters**: VMware NAT voor WAN, host-only voor beheer en LAN/webGUI, geïsoleerd VMware LAN Segment als extra labinterface. Dit wijkt af van het oudere twee-interface-ontwerp; het documenteren van die afwijking betekent **niet** dat de wijziging reeds is uitgevoerd.
- Het bestaande Ubuntu-lab krijgt **nog geen gateway naar pfSense**. Zodra firewallregels passend zijn ingericht, kunnen gecontroleerde bereikbaarheidstests plaatsvinden.
- Claude verzorgt de praktische uitvoering met de eigenaar; ChatGPT is beschikbaar voor een **gerichte second opinion bij daadwerkelijk troubleshooting**. **Geen bevestigde pfSense-installatie, interfaceconfiguratie, firewalltest of snapshot** in de geraadpleegde verslagen.

---

## Gecombineerde status per einde 25 oktober

| Onderwerp | Status | Reikwijdte |
|---|---|---|
| Ubuntu VM, naamgeving en persistente Netplan-labconfiguratie | **PASS** | Boot, netwerkadres en behoud na herstart |
| Eerste systeemupdate via tijdelijke NAT | **PASS** | 107 pakketupdates; nieuwere kernel; update-NIC na afloop los |
| APT deb822-parserfout | **GEPARKEERD** | Niet opgelost, maar werkende klassieke APT-bronnen in gebruik |
| Cockpit-installatie en beheer via VMnet1 | **PASS** | Installatie, gerichte socketbinding, firewallregel en Windows-browserlogin |
| Cockpit systeemtijdwaarschuwing | **OPGELOST** | VMware-hosttijdbron en tijdzone bevestigd |
| Cockpit zelfondertekend certificaat | **GEACCEPTEERD LABRESTRISICO** | Geen externe publicatie |
| VMware ISO-ontkoppeling en Cockpit-snapshots | **AFGEROND** | Lokaal gerapporteerde herstelpunten |
| Integrale negatieve netwerkisolatietests | **OPEN** | Niet gelijkstellen aan positieve pings of ontbrekende default route |
| Windows VBS-/VMware-uitvoeringsmodus | **DEELS ONDERZOCHT / FORMEEL OPEN** | Geen onnodige Windows-beveiliging uitgeschakeld |
| GitHub-projectstructuur, PDF en AI Work Policies | **GEPUBLICEERD** | Publiek geschoonde documentatie en governance |
| pfSense-VM, fysieke Linux-host en Azure | **GEPLAND** | Nog geen uitvoering of functionele PASS bevestigd |

## Vervolg (alleen de actuele, zinvolle acties)

1. **pfSense stap voor stap opbouwen** volgens het laatste akkoord in de oorspronkelijke engineeringnotities, met internet tijdens installatie, beheer via host-only en een afgescheiden labinterface; Ubuntu-gateway niet voortijdig aanpassen.
2. **Bestaand bewijs gebruiken** en alleen openstaande, relevante checks uitvoeren bij de eerstvolgende risicovolle wijziging; geen herhaaltests op reeds bewezen kleine configuratiestappen.
3. **Documentatie bijwerken wanneer de feitelijke infrastructuur wijzigt**: na een werkende pfSense-installatie de huidige blueprint, netwerkdocumentatie en besluiten aan de gerealiseerde situatie toetsen. De voorlopige blueprint hoeft niet preventief opnieuw ontworpen te worden.

**Samenvatting:** op 24 oktober is Ubuntu-netwerkconfiguratie en patchbaarheid opgebouwd en gerepareerd; op 25 oktober is via een apart beheernetwerk werkend en afgeschermd Cockpit toegevoegd, zijn tijdsync en diverse kleine fouten opgelost, en is een publieke documentatie- en governancebasis ingericht. De pfSense-implementatie is voorbereid, maar niet als afgerond geregistreerd.
