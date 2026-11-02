> **Historische momentopname (gesaneerde export).** Deze sessie is niet retrospectief aangepast aan later werk; zie [de actuele roadmap](ROADMAP.md) en [publieke besluiten](../governance/BESLUITENLOG.md). Echte IP-adressen, domeinen, paden, privésystemen en interne bronlinks zijn verwijderd. `LAB_IP_REDACTED` is geen bruikbare configuratiewaarde.

# GNS3 | Eerste boot, KVM-diagnose en parkeerregister

> Bewerkt 02-11-2026: terminologie geharmoniseerd en interne verwijzingen verwijderd; testuitslagen ongewijzigd.
>
> **TL;DR (redactionele toevoeging)**  
> **Vraag:** Wat verklaarde GNS3/KVM- en VMware-Desktop-problemen op 28 oktober?  
> **Uitkomst:** GNS3/VPCS/ARP/ICMP en Wireshark-baseline beperkt PASS; nested KVM bleef PARKED.  
> **Besluit:** GNS3 uitbreiden pas bij noodzaak, en volledige dataplane-isolatie apart toetsen.

> **Actuele statusinterpretatie (29-10-2026):** PK-HT-001 is **PARKED** met heropening bij aantoonbare KVM-afhankelijke functionaliteitsblokkade; PARKED is een workflowstatus, **geen REWORK- of PASS-verdict voor nested KVM**. De geteste lichte VPCS/ARP/ICMP-baseline heeft scoped PASS. Eerdere statuslabels blijven als sessiegeschiedenis zichtbaar. [Statuslegenda](../governance/STATUSLEGENDA.md) · [Fasering](ROADMAP.md).

> **ACTUELE STATUS | 29-10-2026 — GNS3/Wireshark-baseline afgerond; vervolgwerk geparkeerd**  
> Dit overzicht heeft voorrang boven oudere OPEN-/to-do-vermeldingen hieronder. Historische sessiegegevens blijven ongewijzigd voor traceerbaarheid. **Afronding betekent: voldoende voor huidige fase, niet dat alle validatiepunten zijn gesloten.**
>
> | Werkstroom | Actuele status | Onderbouwing / grens |
> |---|---|---|
> | GNS3 VM 2.2.61 boot en Desktop 2.2.61 | **PASS** | Bestaande VMware-appliance start en beide GNS3-servers zijn groen |
> | VMware vmrun PATH en Desktop ↔ VM beheer | **PASS** | Persistente PATH en besturing van bestaande VM via Desktop bevestigd in addendum II |
> | LAB01: VPCS–Ethernet switch–VPCS | **PASS** | Tweezijdige ICMP, ARP-mapping, Wireshark-capture met ARP/ICMP |
> | Project en .pcapng lokaal opgeslagen | **PASS (aanwezigheid)** | Restore/heropeningsproef nog niet uitgevoerd |
> | Wireshark-werkwijze / capture | **PASS op 4.6.7** | Capture bewezen vóór update; **4.6.9/Npcap 1.88 na update niet geverifieerd** |
> | Nested KVM (PK-HT-001) | **PARKED / ACCEPTED LIMITATION** | Geen host-VBS/security uitgeschakeld; alleen heropenen bij concrete QEMU-workloadbehoefte |
> | Dataplane-isolatie (PK-HT-002), storage (003), loadtest (004) | **OPEN / PARKED** | Relevant vóór netwerkkoppeling, grotere images of gelijktijdige VM-belasting |
>
> **Fasebesluit:** voor deze projectfase **GNS3 + Wireshark functioneel afgerond**. Geen extra installatie of capturewerk als voorwaarde voor de volgende fase. Open punten blijven expliciet in het parkeerregister; de bewijsgrenzen hierboven blijven geldig.
>
> **NEXT | Fase 3 — Windows-hybride lab:** (1) Windows Server 2025 Evaluation installeren/valideren; (2) Windows 11-evaluatieclient installeren/valideren; (3) AD DS, DNS, domeinlidmaatschap en GPO als afzonderlijke tests; (4) netwerkontwerp en RAM controleren vóór wijzigingen aan pfSense/GNS3-dataplane. De tweede Windows-machine is **de client**, niet nog een GNS3-appliance. ISO-download of eerdere installerstart telt niet als voltooide installatie.
>
> **Statusbeheer:** eerdere kopjes 'Actieve vervolgactiviteiten', 'Hervattingspunt volgende sessie' en 'Volgende sessie' zijn historische momentopnames van 28-10-2026; zij zijn **geen actuele actielijst**. Niet uitgevoerd werk is alleen herpland of geparkeerd, niet administratief op PASS gezet.
>
---

**Datum:** 28-10-2026
**Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.**
**Status:** Technische bevindingen gedocumenteerd; KVM-herstel GEPARKEERD
**Methodologie:** Risk-Based Validation

## Geverifieerde observaties (screenshots gebruiker)
- GNS3 VMware-appliance 2.2.61 geïmporteerd onder VM-naam `PS-HT-VM02-GNS3`; runtime onder `REDACTED_LOCAL_PATH`.
- 4 GiB (4096 MB) RAM, 2 vCPU ingesteld. OVA presenteert twee virtuele SCSI-schijven van 100 GB en 1 TB virtuele capaciteit; werkelijk ruimtegebruik en benodigde volumes nog niet gecontroleerd.
- NIC1 VMware host-only, NIC2 NAT met **Connected** en **Connect at power on** uit. Geen empirisch bewijs van volledige segmentisolatie.
- Eerste start met nested AMD-V/RVI ingeschakeld toonde `Virtualized AMD-V/RVI is not supported on this platform`. Na uitschakelen van doorgifte in VM-instellingen start de GNS3-appliance.
- Console: GNS3 server 2.2.61, VM 0.21.0, QEMU 10.2.1, `KVM support available: False`, GNS3 management-IP `GNS3_MGMT_IP` (host-only), poort 80. GNS3 Web UI vanaf Windows-host bereikbaar, door Project Owner bevestigd na correctie van verkeerd ingetikt IP. Alleen bereikbaarheids-PASS; nog geen echte appliance-workload getest.
- PowerShell `Get-CimInstance Win32_ComputerSystem | Select-Object HypervisorPresent`: **True**.
- `Win32_DeviceGuard`: `VirtualizationBasedSecurityStatus = 2` en `SecurityServicesConfigured = {2,3,4}`, `SecurityServicesRunning = {2,3,4}`. Windows Security screenshot bevestigt Memory Integrity On, Firmware Protection On, LSA Protection On, Kernel-mode hardware-enforced stack protection Off.
- VMware `vmware.log`: **`Monitor Mode: ULM`**. Dit bevestigt Windows-hypervisor-gebaseerde VMware-uitvoeringsmodus. Samen met VBS en ontbrekende KVM is dit een sterke verklaring voor het nested-virtualizationprobleem, maar niet elke afhankelijke instelling is afzonderlijk causaal getest.
- Geen hostbeveiligingsfuncties uitgezet. VMware CPU-option voor nested AMD-V uitgeschakeld voor deze GNS3-proef.

## Actieve vervolgactiviteiten
1. GNS3 Desktop 2.2.61 installeren, `Choose Components` beoordelen, serververbinding controleren.
2. Eerste lichte topologie testen (VPCS/switch), verkeer en hostbelasting meten.
3. Fase 3: Windows Server 2025-installatie-ISO voltooien/verifiëren; Windows Server en Windows Enterprise-evaluatieclient installeren, AD/DNS/GPO/domain join testen.
4. Bestaande pfSense/Ubuntu-openpunten blijven conform eerdere logs open; zijn hier niet opnieuw beoordeeld.

## GEPARKEERDE PUNTEN — systematisch hervatten
| ID | Onderwerp | Waarom geparkeerd | Trigger voor heropening | Eerste controle / exitcriterium |
|---|---|---|---|---|
| PK-HT-001 | GNS3 nested AMD-V/KVM `False`; VMware `ULM`, Windows VBS | GNS3 boot en Web UI werken, geen bewezen noodzaak voor zware QEMU-workload; hostsecurity niet opofferen zonder businesscase | Een gekozen QEMU-/Cisco-appliance vereist KVM of faalt/loopt aantoonbaar onacceptabel traag | Model/image-eisen, CPU/looptijd meten; alternatieven (lichte nodes, externe Linux/KVM-host) vergelijken; pas dan risico-afweging voor wijziging VBS/Hyper-V met rollback en owner-approval; KVM True en daadwerkelijke appliance-functionaliteit testen als wijziging wordt toegestaan |
| PK-HT-002 | Volledige GNS3 network-isolation-validatie inclusief NAT-gedrag | NAT NIC administratief uit, host-only bereikbaarheid wel bevestigd; dat bewijst geen verkeersgrens | Vóór koppeling GNS3-dataplane aan pfSense, LAB of fysiek netwerk | Interface-/routeinventaris, positieve en negatieve test naar geautoriseerde/onbevoegde netwerken, evidence |
| PK-HT-003 | GNS3 virtuele SCSI-schijven (100 GB + 1 TB) en daadwerkelijke hostopslag | OVA-defaults; geen opslag- of datapadinspectie verricht | Vóór grotere image-imports of diskdruk | Thin/sparse status, daadwerkelijke grootte, doel tweede volume vastleggen; geen disk verwijderen zonder appliance-eis te controleren |
| PK-HT-004 | Vijf VM's tegelijk / RAM-headroom | Alleen snapshots, geen gezamenlijke stress/loadtest | Als alle vijf VM's geïnstalleerd zijn of simultane test noodzakelijk is | Host Available/Committed, disk swapping en VM-respons onder representatieve belasting meten |
| PK-HT-005 | MacBook Pro 2014 format safety | Project Owner wil bare-metal Ubuntu; backup/SSD/hardwarechecks ontbreken | Vóór enig wissen van macOS | Gegevensbesluit, herstelbare backup, SSD/SMART, installatiemedia, compatibiliteit en doelvolume controle; expliciete format-go |
| PK-HT-006 | Azure Arc/private cloud services op tweede host | Hardware-/OS-ready en gratis SKU/featurelimieten nog niet geverifieerd | MacBook Linux-server stabiel en netwerkroute ontworpen | Arc-agentcompatibiliteit, TLS egress, RBAC en kostencontrole; services gefaseerd |
| PK-HT-007 | pfSense/Ubuntu baseline, snapshot, netwerkroute, logtijd en bewijs | Bestaande openpunten uit 26 oktober, niet opnieuw getest | Bij hervatten core lab-netwerkwerk | Herlees bestaande log, gerichte validatie en alleen reeds geldige issues sluiten |

**Parkeerbeleid:** geparkeerd betekent niet DONE of VERIFIED. Heropen per ID bij trigger; registreer owner, datum, bewijs, risico, beslissing en definitieve status; geen automatische wijzigingen. Overlap met eerdere logs wordt niet stilzwijgend gesloten.

## Verdict
- **PASS:** GNS3 OVA geïmporteerd, eerste boot, Web UI vanaf host.
- **VERIFIED DIAGNOSTIC:** Windows hypervisor present, VBS running, VMware ULM, GNS3 KVM False.
- **GEPARKEERD / REWORK:** KVM/nested acceleration.
- **OPEN:** GNS3 Desktop-integratie, echte topologie, netwerkisolatie, prestatiebelasting.


---

## Sessie-addendum | GNS3 Desktop-installatie en vmrun-troubleshooting (28-10-2026)

**Scope:** Alleen de nieuwe gebeurtenissen na de eerste GNS3-VM-boot en KVM-diagnose. OVA-import, VBS/ULM-diagnose, parkeerregister, hostcapaciteit en MacBook/Windows-ISO-voorbereiding staan al in dit log of de andere logs en worden niet herhaald. **Dit addendum vervangt de eerdere status 'GNS3 Desktop nog te installeren' door PASS.**

### 1. Nieuwe observaties (screenshots Project Owner)

1. **Installer gecontroleerd:** GNS3 2.2.61 all-in-one geopend; Windows Properties > Digital Signatures > Details meldde **“This digital signature is OK”**. Signer: **SolarWinds Worldwide, LLC**, signing time **30 juli 2026**, Microsoft-countersignature zichtbaar. De digitale handtekening werd gecontroleerd; onafhankelijke vergelijking met een officiële vendor-SHA-256 is **niet** uitgevoerd.
2. **Installatiecomponenten beoordeeld:** GNS3 Desktop geselecteerd; afzonderlijke GNS3 VM-installer niet nodig (appliance is reeds in VMware geïmporteerd). Opties voor Npcap, Wireshark, Dynamips, QEMU, VPCS en console-viewers besproken. De definitieve set geïnstalleerde optionele onderdelen is **niet afzonderlijk geïnventariseerd**.
3. **Npcap 1.78:** installatieopties bekeken. Advies gegeven om raw 802.11 monitor mode uit te zetten, WinPcap API-compatible mode aan te laten en administrator-only packet capture voor het huidige gebruik uit te laten. De definitieve instelling van elk vinkje is niet na installatie uitgelezen; het bredere capture-recht bij administrator-only uit is benoemd.
4. **Wireshark 4.6.7 x64:** download vanuit GNS3-installer zichtbaar. De optionele SolarWinds Engineer's Toolset-trial van 14 dagen is afgeraden; geen bewijs dat de trial is geïnstalleerd.
5. **GNS3 Desktop 2.2.61 startte.** Keuze in wizard: **Run appliances in a virtual machine**. Local server configuration: pad onder Program Files/GNS3, binding **localhost**, **3080/TCP**. Wizard toonde **“Connection to the local GNS3 server has been successful!”**. Na herstart: groene lokale server en controller-notificaties via localhost:3080 in GUI.

### 2. Troubleshooting | VMware vmrun-detectie

**Symptoom:** Wizard/GUI meldde **“VMware vmrun tool could not be found”**. Dit was een Windows VMware-integratieprobleem, **niet** het eerder geparkeerde nested-KVM-probleem.

**Verificatie en ingreep:**
- PowerShell Get-ChildItem toonde dat **vmrun.exe daadwerkelijk aanwezig** was in **C:\Program Files\VMware\VMware Workstation\vmrun.exe**.
- **where.exe vmrun** gaf eerst **“Could not find files for the given pattern(s)”**: bestand stond niet in de PATH die deze sessie gebruikte.
- Door uitsluitend in de lopende PowerShell-sessie de VMware Workstation-directory aan de omgevingsvariabele **PATH** toe te voegen, gaf een tweede **where.exe vmrun** het verwachte volledige pad. **PASS: PATH-test in PowerShell**.
- De Project Owner kreeg instructie via Windows **Advanced > Environment Variables > User variables > Path** het pad blijvend beschikbaar te maken en GNS3 opnieuw te starten. Het volgende screenshot liet GNS3 normaal starten **zonder zichtbare vmrun-foutmelding**.
- **Beperking:** er is geen aparte screenshot van blijvende User Path-configuratie en nog geen bewijs dat Desktop de GNS3 VM werkelijk kan starten/beheren. Daarom **geen end-to-end VMware-integratie-PASS**.
- Geen herinstallatie van VMware, geen wijziging van host-VBS/Hyper-V, en geen aanpassing aan pfSense of het thuisnetwerk.

### 3. Nieuwe status na sessie

| Onderdeel | Status | Bewijsgrens |
|---|---|---|
| GNS3 Desktop 2.2.61 geïnstalleerd en gestart | **PASS** | Desktopvenster/version |
| Digitale handtekening installer | **PASS** | Windows: signature OK |
| Lokale GNS3-server localhost:3080 | **PASS** | Wizard-success + groene server |
| VMware vmrun aanwezig en via aangepaste sessie-PATH vindbaar | **PASS** | PowerShell-output |
| vmrun-popup na GNS3-herstart | **Niet meer waargenomen** | Screenshot zonder fout; VM-control niet getest |
| GNS3 Desktop koppelen met bestaande GNS3 VMware-appliance | **OPEN** | GNS3 VM Preferences nog niet afgerond |
| Lichte virtuele topologie, packets en VM-prestaties | **OPEN** | Nog geen netwerkproef |
| KVM nested AMD-V | **PARKED / ACCEPTED LIMITATION (PK-HT-001)** | Eerder owner-besluit, niet opnieuw onderzoeken |
| GNS3 dataplane/netwerkisolatie | **OPEN (PK-HT-002)** | Nog geen grensvalidatie |

### 4. Hervattingspunt volgende sessie

1. In GNS3 Desktop **Edit > Preferences > GNS3 VM** openen, VMware als hypervisor selecteren en **bestaande** GNS3 VM configureren; geen nieuwe appliance importeren.
2. Werkelijke GNS3 Desktop ↔ GNS3 VM-status testen en vastleggen. Bij fout pas nieuwe gerichte vmrun-diagnose.
3. Geïsoleerd proefnetwerk **VPCS — Ethernet switch — VPCS** maken: IP's instellen, ping/ARP, project bewaren en zo mogelijk Wireshark packet capture. **Geen Cloud-node, bridge, fysieke adapter of pfSense-verbinding** voordat PK-HT-002 gericht is beoordeeld.
4. RAM/CPU en responstijd meten onder lichte belasting. Dit bewijst niets over vijf gelijktijdige VM's.
5. Na GNS3-basisvalidatie terug naar geplande **Fase 3**: Windows Server 2025-installatiemedia en Windows-evaluatieclient beoordelen, daarna AD DS/DNS/domain join/GPO testen. Bestaande andere openpunten blijven open.

**Risk-Based Validation:** geverifieerde tussenresultaten apart houden van nog niet geteste integratie. Geen dubbele logregistratie en geen stilzwijgende sluiting van geparkeerde taken.


---

## Sessie-addendum II | LAB01 Network Baseline en Wireshark-update (28-10-2026)

**Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.** | **Werkwijze:** Risk-Based Validation
**Scope:** uitsluitend nieuwe werkzaamheden na het vorige GNS3 Desktop/vmrun-addendum. Eerder beschreven VM-import, VBS/ULM-analyse, MacBook, Windows-media en parkeerpunten niet opnieuw geregistreerd.

### VERIFIED / PASS (gebruikersscreenshots en terminal)
1. **Persistente Windows User PATH hersteld:** `where.exe vmrun` in nieuwe PowerShell-sessie retourneert `C:\Program Files\VMware\VMware Workstation\vmrun.exe`. GNS3 opent vervolgens VMware en start bestaande `PS-HT-VM02-GNS3`; geen nieuwe appliance aangemaakt.
2. **VM boot / beperking:** eerste poging met nested AMD-V/RVI gaf incompatibiliteitsmelding en `FeatureCompatLate`/ `hv.capable`-startfout. CPU-checkbox `Virtualize Intel VT-x/EPT or AMD-V/RVI` uitgeschakeld; GNS3 VM start. Console: GNS3 2.2.61, `KVM support available: False`. PK-HT-001 blijft **PARKED**, niet opgelost.
3. **Desktop ↔ VM:** GNS3 Desktop toont twee groene servers: lokale server en `PS-HT-VM02-GNS3`. PASS voor beheerverbinding en lichte workload, niet voor brede appliance-compatibiliteit.
4. **Topologie:** `HT-GNS3-LAB01-Network-Baseline`; VPCS PC1 — Ethernet Switch1 — VPCS PC2; geen Cloud/NAT/bridge/pfSense toegevoegd. PC1 `LAB_IP_REDACTED`, PC2 `LAB_IP_REDACTED`.
5. **Connectivity en ARP:** Project Owner bevestigde ping in beide richtingen. Screenshot PC1 toont vijf ICMP-antwoorden van `LAB_IP_REDACTED`; daarna `show arp` met een geldige MAC-mapping. Tijdelijke lege ARP-cache vóór ping is verklaard.
6. **Wireshark capture:** capture op PC1–Switch1; screenshot met **12 frames**: 2 ARP (request/reply), 10 ICMP (5 requests/5 replies). PASS voor L2/L3-verkeer in deze topologie.
7. **Lokale opslag:** File Explorer toont projectbestand `HT-GNS3-LAB01-Network-Baseline.gns3` (~9 KB), capture `HT-LAB01-ARP-ICMP-Baseline.pcapng` (~2 KB), en `project-files` onder lokale `GNS3/projects/HT-GNS3-LAB01-Network-Baseline`. Aanwezigheid bevestigd; heropenings-/restoretest nog OPEN.

### Wireshark / Npcap (NIET voorbarig PASS)
- Wireshark 4.6.7 was operationeel tijdens capture.
- Wireshark 4.6.9 x64 setup gestart; vorige versie eerst verwijderen; componentselectie inclusief Wireshark/TShark besproken.
- Npcap 1.78 aanwezig; installer bood Npcap 1.88 aan. USBPcap optioneel niet geselecteerd. Npcap 1.88 Installation Options getoond; advies administrator-only aan, andere opties uit.
- **Nog geen screenshots van voltooide installatie of Help > About**: Wireshark 4.6.9, Npcap 1.88 en capturefunctionaliteit na update blijven **PENDING VERIFICATION**. Geen securityinstellingen van Windows gewijzigd.

### Verdict
- **LAB01 LIGHT NETWORK BASELINE: PASS** — topologie, bidirectionele connectiviteit, ARP, ICMP-capture, bestanden aanwezig.
- **OPEN** — heropenen GNS3-project en replay/herhaaltest, Wireshark/Npcap-versies na installatie, resource-/performancebewijs.
- **PARKED / NO CHANGE** — PK-HT-001 t/m PK-HT-007 volgens bestaand parkeerregister; in het bijzonder PK-HT-002 (segmentisolatie) nog niet empirisch gevalideerd. Binnen-LAB ping is geen bewijs van externe netwerkisolatie.

### Volgende sessie (prioriteit)
1. **Afsluitcontrole update:** Wireshark Help > About: 4.6.9; Npcap 1.88 via Apps of capture-informatie verifiëren; korte testcapture vanuit GNS3. Bij afwijking gerichte troubleshooting, niet blind herinstalleren.
2. **Reproduceerbaarheid:** project opnieuw openen, PC1/PC2 starten, ping/ARP opnieuw uitvoeren; opgeslagen `.pcapng` openen; screenshot/evidence redigeren en bestandsinventaris registreren.
3. **Lichte resources meten:** GNS3 VM/Lenovo CPU/RAM met LAB01; geen claims over vijf gelijktijdige VM's.
4. **PK-HT-002 vóór grensverandering:** host-only/NAT-interface-, route- en negatieve connectiviteitstests; geen koppeling aan thuisnetwerk, pfSense, fysieke NIC of Cloud-node zonder expliciet ontwerp en eigenaarstoestemming.
5. **Daarna Fase 3:** juiste Windows Server 2025 Evaluation-installatie-ISO en Windows 11 Enterprise Evaluation ISO op volledigheid/geschiktheid verifiëren; capaciteit toetsen; daarna Windows Server AD DS/DNS en domeinclient/GPO opbouwen en testen.
6. **Geparkeerde punten intact:** KVM/VBS (PK-HT-001) alleen heropenen bij aantoonbare workloadblokkade; MacBook format hold, storage, multi-VM-capaciteit, pfSense/Ubuntu-baselines blijven onder hun bestaande voorwaarden.

**Publicatiegrens:** geen interne vertrouwelijke projectnamen, lokale gebruiker-/MAC-/IP-identifiers, wachtwoorden of ongefilterde captures in publieke showcases. Bewijs lokaal houden totdat geredigeerd en vrijgegeven.
