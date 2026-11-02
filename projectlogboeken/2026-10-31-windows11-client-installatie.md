> **Historische momentopname (gesaneerde export).** Deze sessie is niet retrospectief aangepast aan later werk; zie [de actuele roadmap](ROADMAP.md) en [publieke besluiten](../governance/BESLUITENLOG.md). Echte IP-adressen, domeinen, paden, privésystemen en interne bronlinks zijn verwijderd. `LAB_IP_REDACTED` is geen bruikbare configuratiewaarde.

# Projectlog | 31 oktober 2026

> Bewerkt 02-11-2026: terminologie geharmoniseerd en interne verwijzingen verwijderd; testuitslagen ongewijzigd.
>
> **TL;DR (redactionele toevoeging)**  
> **Vraag:** Kon de Windows 11-evaluatieclient als VM worden geïnstalleerd?  
> **Uitkomst:** OS-installatie en eerste desktop gerapporteerd PASS; netwerk, licentie en domeinjoin waren op dit sessiemoment PENDING.  
> **Besluit:** Gerichte baselinecontroles en domeinintegratie volgen in latere sessies.
## Windows 11-client geïnstalleerd: eerste desktop bereikt

**Project:** Hybrid-Theory  
**Component:** `PS-HT-CLIENT01-Win11` (VMware Workstation Pro)  
**Sessietype:** OS-installatie en eerste inrichting (OOBE)  
**Uitvoering:** Project Owner met stapsgewijze begeleiding van ChatGPT  
**Methodologie:** Risk-Based Validation  
**Verdict:** **PASS — Windows 11 OS-installatie en eerste desktop zichtbaar**; **PENDING — configuratie, verificatie en domeinintegratie**

### Kort resultaat

De Windows 11-client is als afzonderlijke virtuele machine geïnstalleerd. De eerste Windows-desktop werd op 31 oktober 2026 zichtbaar in VMware Workstation. Daarmee is de blokkade **client nog niet geïnstalleerd** opgeheven. Windows Server 2025 en de client zijn **nog geen bewezen werkend Active Directory-domein**.

### Uitgevoerde stappen en observaties

1. Bestaande VMware-VM `PS-HT-CLIENT01-Win11` opgestart. Vanuit de UEFI Boot Manager gestart vanaf de virtuele SATA-CDROM met de Windows 11-installatiemedia.
2. Windows Setup: toetsenbord **United States-International** gekozen; nieuwe installatie (**Install Windows 11**) geselecteerd.
3. De installatiedoelschijf in Windows Setup was **Disk 0: 64,0 GB Unallocated Space**. De lege virtuele schijf is geselecteerd; Windows Setup beheert de benodigde partities.
4. Windows 11 OOBE uitgevoerd. Bij netwerkverbinding is **I don't have internet** gekozen; verdere eerste inrichting is afgerond.
5. Privacykeuzes tijdens OOBE: **Location = No** en diagnostische gegevens **Required only**.
6. De Windows 11-desktop met taakbalk en Startmenu was zichtbaar in de VMware-console. Dit is het concrete bewijs van de bereikte OS-installatiefase.
7. Onder in VMware Workstation stond nog de Easy Install-aanwijzing/knop **I Finished Installing**. Het afronden van deze VMware-wizard en de status van VMware Tools zijn **niet aangetoond**.

**Bewijsbasis:** schermopnamen tijdens de gebruikerssessie van 31-10-2026 (UEFI, installatiedoelschijf, OOBE en desktop) door de Project Owner getoond. De originele screenshots zijn **niet** naar de repository geüpload en hebben **geen afgeronde publicatie-/sanitisatiereview**.

### Afbakening van de PASS

| Onderdeel | Status | Beoordeling |
|---|---|---|
| Windows 11 Setup, 64 GB virtuele schijf en eerste desktop | **VERIFIED / PASS** binnen screenshot-scope | Nieuwe VM met bootbare Windows-desktop aangetoond |
| Gebruikersaccount en offline OOBE | **IMPLEMENTED**; accounttype en rechten **NOT VERIFIED** | Offline gekozen tijdens setup; geen bewijs van permanente fysieke of virtuele netwerkisolatie |
| Windows 11-editie, Evaluation-licentie en vervaldatum | **PENDING** | Voorgenomen editie is Enterprise Evaluation; `winver` en licentiestatus nog controleren |
| VM-resources, UEFI/Secure Boot, NIC, IP, routes en isolatie | **PENDING** | Geen verifieerbare waarden of netwerkreview binnen dit installatielog |
| VMware Tools, beeldschaal, Easy Install afronding, ISO loskoppelen | **PENDING** | Desktop staat zichtbaar in relatief klein VMware-scherm; geen Tools-test afgerond |
| AD DS/DNS, domeinjoin, gebruikersrechten en GPO | **PLANNED / NOT VERIFIED** | Server en client nog niet als domein geïntegreerd |
| Back-up, snapshot en hersteltest | **NOT VERIFIED** | Een snapshot is geen off-host back-up of bewezen restore |

**Geen REWORK vastgesteld voor de OS-installatie.** Deze PASS geeft geen toestemming voor nieuwe bridges, pfSense-koppelingen, routerwijzigingen of cloudkosten.

### Bijgewerkte to-dolijst volgende sessie (prioriteit)

- [ ] **1. Windows 11-baseline afronden:** VMware Easy Install afsluiten, Windows-login en `winver`/editie/Evaluation-licentiestatus verifiëren; VMware Tools, schermresolutie, CPU/RAM en opslag vastleggen; installatie-ISO veilig ontkoppelen; lokaal beheeraccount en veiligheidsinstellingen controleren zonder credentials in screenshots/logs.
- [ ] **2. Windows Server 2025 post-reboot verifiëren:** editie/build, eerste aanmelding, VMware Tools, Secure Boot en bestaande NIC-status controleren. Eerder was voor deze VM geen NIC aangemaakt; maak **niet** direct een verbinding met het thuisnetwerk.
- [ ] **3. Veilige domeinnetwerk-preflight:** ontwerp en autoriseer een gescheiden server-/client-labnetwerk, niet-overlappende IP's, DNS-rol, DHCP-beleid, firewallgrenzen, rollback en minimale consistente back-up vóór ingrijpende wijzigingen. Verifieer de werkelijke NIC-/route- en egress-status met positieve én negatieve tests.
- [ ] **4. Active Directory-lab uitvoeren:** na geslaagde preflight AD DS en DNS op Server 2025, gecontroleerde domain join van Windows 11, OU's, testgebruikers/-groepen en eerste GPO's. Documenteer zowel geslaagde authenticatie als afwijzing van ongeoorloofde toegang.
- [ ] **5. GNS3/pfSense gescheiden houden:** vóór eventuele koppeling het bestaande potentieel overlappende labadres oplossen via goedgekeurd IP-plan. Het ontwerp **3 × 25 VPCS**, negatieve isolatietests en resource-/capaciteitsmeting blijven **PLANNED**. GNS3-tijdsynchronisatie blijft **PARKED**, met eerdere reproduceerbaarheids-REWORK nog onopgelost; heropen bij noodzaak van betrouwbare capture-/SIEM-tijden of formele hervatting van de tijdsynchronisatietests. Nested KVM blijft PARKED tot een concrete blokkade.
- [ ] **6. Ubuntu/private services ontwerpen:** extra servicezone, rollback, Nextcloud/Nginx/Podman, TLS, opslag en back-up/herstel uitwerken. Cockpit Networking blijft **PARKED**; geen NetworkManager-migratie voor alleen een menu.
- [ ] **7. Azure Arc free-first voorbereiden:** bestaand eigenaarsbesluit **DC-first** blijft van kracht; recenter **Ubuntu-first** is alleen een te beoordelen voorstel. Check agentondersteuning, outbound toegang, identiteit, telemetrie en kosten; **geen deployment** zonder review en akkoord.
- [ ] **8. Gratis Azure-basis en publicatie:** abonnement, prijsvoorwaarden en eventuele niet-gratis afhankelijkheden verifiëren vóór eventuele lege VNet-subnets/NSG's en gratis Entra/Arc-functionaliteit. Budgetalarmen zijn **geen** hard uitgavenplafond. Screenshots eerst saneren en beoordelen; bewijs pas na goedkeuring publiceren. De eerdere voorbeeld-PNG blijft een afzonderlijk open publicatiepunt.

**Volgorde:** eerst betrouwbare VM-baselines, veilige netwerkgrenzen en minimale herstelbasis; daarna AD/DNS en domeinjoin. Verdere missies 01–05 blijven voorgestelde werkpakketten in de eerdere engineeringnotities, niet automatisch voltooide implementaties.

### Vervolg en relatie tot eerdere logs

Deze log is een **aanvulling** op de afzonderlijke historische architectuurverkenning van 30–31 oktober (niet geëxporteerd) en vervangt uitsluitend diens verouderde taakstatus **Windows 11 nog niet geïnstalleerd**. De architectuursessie zelf bleef documentatie-only. Bestaande GNS3- en Cockpit-parkeerbesluiten, historische testresultaten en openstaande risico's blijven van kracht.
