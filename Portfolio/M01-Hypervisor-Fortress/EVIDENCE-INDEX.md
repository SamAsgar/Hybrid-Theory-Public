# EVIDENCE-INDEX — M01 Hypervisor Fortress

**Publicatiestatus:** PUBLIC · 82 gesaneerde PNG-afgeleiden (onomkeerbare pixelmaskering, zonder metadata). De private originelen blijven privé. Zie het [saneringsrapport](M01-SANITIZATION-REPORT.md).


**Bron:** lokale evidence-export (864 bestanden) · **Onderzoeksperiode:** 31-10-2026 t/m 15-11-2026 · **Opgesteld:** 15-11-2026
**Selectie:** 82 unieke bestanden · CONFIG 55 · TROUBLESHOOT 7 · ERROR 4 · FIX 3 · TEST 7 · PASS 3 · FAIL 1 · PENDING 2

**Leeswijzer**

- De beelden in `M01-Bewijsvoering/` zijn **gesaneerde afgeleiden** van de originelen: gevoelige gegevens zijn onomkeerbaar overgeschilderd. SHA-256 van deze publieke afgeleiden staat in `MANIFEST_SHA256.txt`.
- **Datum** komt uit de bestandsnaam (Windows-knipprogramma, lokale tijd) en is gelijk aan de wijzigingstijd in de ZIP. Er is geen EXIF of onafhankelijke tijdbron; behandel de datum als *vermoedelijk*. Opnamen kort na middernacht horen bij de sessie van de vorige avond.
- **Betekenis** is gebaseerd op tekstherkenning (OCR) van elk beeld. Waar *visueel bevestigd* staat, is het beeld zelf bekeken. De overige regels zijn niet stuk voor stuk visueel nagelopen.
- **Klasse** beschrijft wat het beeld zelf laat zien. PASS/FAIL staat er alleen als het resultaat in het beeld zichtbaar is. Een CONFIG-beeld is geen testbewijs.
- Koppelingen verwijzen naar de controls/acceptatiecriteria uit de projectlogboeken (gelezen, niet gewijzigd).


## 31-10-2026

| # | Tijd | Klasse | Koppeling | Technische betekenis | Screenshot (gesaneerd) |
|---|---|---|---|---|---|
| 001 | 10:16:55 | **TEST** | HV-01 (installatiemedia) | Get-FileHash SHA256 van de Windows 11 Enterprise Evaluation-ISO op de host. Hash is berekend; vergelijking met een referentiewaarde is niet zichtbaar. | [Screenshot 2026-10-31 101655.png](M01-Bewijsvoering/Screenshot%202026-10-31%20101655.png) |
| 002 | 10:19:47 | **CONFIG** | VM-baseline Client01 | New VM Wizard: hardware compatibility Workstation 25H2 or later. | [Screenshot 2026-10-31 101947.png](M01-Bewijsvoering/Screenshot%202026-10-31%20101947.png) |
| 003 | 10:21:33 | **CONFIG** | VM-baseline Client01 | Wizard: 'I will install the operating system later' (geen Easy Install). | [Screenshot 2026-10-31 102133.png](M01-Bewijsvoering/Screenshot%202026-10-31%20102133.png) |
| 004 | 10:24:48 | **CONFIG** | VM-baseline Client01 | Wizard: keuze gast-OS. OCR toont 'Windows Server 2025' als versie, terwijl de VM als Windows 11 x64 is aangemaakt (zie 105540). Tussenstap; afwijking niet verklaard. | [Screenshot 2026-10-31 102448.png](M01-Bewijsvoering/Screenshot%202026-10-31%20102448.png) |
| 005 | 10:26:11 | **CONFIG** | VM-baseline Client01 | Wizard: naam en locatie van de VM. | [Screenshot 2026-10-31 102611.png](M01-Bewijsvoering/Screenshot%202026-10-31%20102611.png) |
| 006 | 10:31:54 | **CONFIG** | VM-baseline Client01 / encryptie | Wizard 'Configure Encryption': gast vereist vTPM; keuze voor versleuteling van (alleen) de TPM-bestanden met wachtwoord. | [Screenshot 2026-10-31 103154.png](M01-Bewijsvoering/Screenshot%202026-10-31%20103154.png) |
| 007 | 10:34:12 | **CONFIG** | VM-baseline Client01 | Firmware type: UEFI met Secure Boot-optie. | [Screenshot 2026-10-31 103412.png](M01-Bewijsvoering/Screenshot%202026-10-31%20103412.png) |
| 008 | 10:35:03 | **CONFIG** | VM-baseline Client01 | Processorconfiguratie: 2 processors x 1 core. | [Screenshot 2026-10-31 103503.png](M01-Bewijsvoering/Screenshot%202026-10-31%20103503.png) |
| 009 | 10:36:33 | **CONFIG** | VM-baseline Client01 | Wizard 'Network Type' (bridged / NAT / host-only / geen). Gekozen optie niet leesbaar; samenvatting 105540 toont 'Network Adapter: None'. | [Screenshot 2026-10-31 103633.png](M01-Bewijsvoering/Screenshot%202026-10-31%20103633.png) |
| 010 | 10:38:03 | **CONFIG** | VM-baseline Client01 | SCSI-controllertype (LSI Logic SAS aanbevolen). | [Screenshot 2026-10-31 103803.png](M01-Bewijsvoering/Screenshot%202026-10-31%20103803.png) |
| 011 | 10:40:31 | **CONFIG** | VM-baseline Client01 | Schijftype: NVMe. | [Screenshot 2026-10-31 104031.png](M01-Bewijsvoering/Screenshot%202026-10-31%20104031.png) |
| 012 | 10:42:48 | **CONFIG** | VM-baseline Client01 | Nieuwe virtuele schijf aanmaken. | [Screenshot 2026-10-31 104248.png](M01-Bewijsvoering/Screenshot%202026-10-31%20104248.png) |
| 013 | 10:55:40 | **CONFIG** | VM-baseline Client01 | 'Ready to Create Virtual Machine': CLIENT01, Windows 11 x64, 64 GB split, 4 GB RAM, Network Adapter: None, 2 cores. | [Screenshot 2026-10-31 105540.png](M01-Bewijsvoering/Screenshot%202026-10-31%20105540.png) |
| 014 | 11:00:13 | **CONFIG** | VM-baseline Client01 | Hardware-overzicht met Trusted Platform Module aanwezig en ISO gekoppeld. | [Screenshot 2026-10-31 110013.png](M01-Bewijsvoering/Screenshot%202026-10-31%20110013.png) |
| 015 | 11:01:29 | **ERROR** | VM-baseline Client01 | Melding 'Firmware cannot be changed while the TPM device exists' (Options > Advanced). | [Screenshot 2026-10-31 110129.png](M01-Bewijsvoering/Screenshot%202026-10-31%20110129.png) |
| 016 | 11:02:02 | **CONFIG** | VM-baseline Client01 | VM-overzicht in de bibliotheek na aanmaken (devices incl. TPM). | [Screenshot 2026-10-31 110202.png](M01-Bewijsvoering/Screenshot%202026-10-31%20110202.png) |
| 017 | 11:08:01 | **TROUBLESHOOT** | VM-baseline Client01 | EFI Boot Manager-scherm bij eerste start (keuze bootdevice). | [Screenshot 2026-10-31 110801.png](M01-Bewijsvoering/Screenshot%202026-10-31%20110801.png) |
| 018 | 20:58:05 | **CONFIG** | VMware Tools | VMware Tools-installatiemedium (DVD-drive D:) in de Windows 11-gast. | [Screenshot 2026-10-31 205805.png](M01-Bewijsvoering/Screenshot%202026-10-31%20205805.png) |
| 019 | 21:14:11 | **TEST** | VM-resources | Taakbeheer in de gast: 'Virtual machine: Yes', 2 virtuele processors. | [Screenshot 2026-10-31 211411.png](M01-Bewijsvoering/Screenshot%202026-10-31%20211411.png) |
| 020 | 21:20:30 | **TEST** | VMware Tools | Gast: Settings > Installed apps gefilterd op 'vmware' - VMware Tools aanwezig na installatie. | [Screenshot 2026-10-31 212030.png](M01-Bewijsvoering/Screenshot%202026-10-31%20212030.png) |
| 021 | 21:28:50 | **ERROR** | Tijd en herstel | Gast Client01: w32tm /query geeft 'The service has not been started (0x80070426)'. | [Screenshot 2026-10-31 212850.png](M01-Bewijsvoering/Screenshot%202026-10-31%20212850.png) |
| 022 | 21:31:40 | **TROUBLESHOOT** | Tijd en herstel | Gast: sc query w32time = STOPPED (exit 1077); sc qc w32time opgevraagd. | [Screenshot 2026-10-31 213140.png](M01-Bewijsvoering/Screenshot%202026-10-31%20213140.png) |
| 023 | 21:32:07 | **TROUBLESHOOT** | Tijd en herstel | Gast: triggerconfiguratie van w32time (start bij domain join). | [Screenshot 2026-10-31 213207.png](M01-Bewijsvoering/Screenshot%202026-10-31%20213207.png) |
| 024 | 21:34:13 | **PENDING** | Tijd en herstel | Gast: Date & time - 'Last successful time synchronization: unspecified'. Tijdsynchronisatie niet aangetoond. | [Screenshot 2026-10-31 213413.png](M01-Bewijsvoering/Screenshot%202026-10-31%20213413.png) |
| 025 | 21:57:52 | **CONFIG** | VM-baseline Client01 | VM-details Client01: aangemaakt 31/10/2026, hardware compatibility 25H2. | [Screenshot 2026-10-31 215752.png](M01-Bewijsvoering/Screenshot%202026-10-31%20215752.png) |

## 01-11-2026

| # | Tijd | Klasse | Koppeling | Technische betekenis | Screenshot (gesaneerd) |
|---|---|---|---|---|---|
| 026 | 13:45:24 | **CONFIG** | Hostinventaris | Hostgegevens Lenovo: 32 GB RAM (31,2 GB bruikbaar), BIOS-versie zichtbaar; apparaatnaam, productnummer en serienummer gemaskeerd. | [Screenshot 2026-11-01 134524.png](M01-Bewijsvoering/Screenshot%202026-11-01%20134524.png) |
| 027 | 13:51:39 | **TEST** | Hostinventaris | Taakbeheer host: AMD Ryzen AI 7 350, 16 logische processors, 'Virtualization: Enabled'. | [Screenshot 2026-11-01 135139.png](M01-Bewijsvoering/Screenshot%202026-11-01%20135139.png) |
| 028 | 15:29:14 | **CONFIG** | Herstel (snapshot) | Snapshot Manager DC01 voor het maken van de snapshot (alleen 'You Are Here'). | [Screenshot 2026-11-01 152914.png](M01-Bewijsvoering/Screenshot%202026-11-01%20152914.png) |
| 029 | 15:32:00 | **CONFIG** | Herstel (snapshot) | Snapshot Manager DC: snapshot 'POST-AD-DC' aanwezig. Geen restore getoond. | [Screenshot 2026-11-01 153200.png](M01-Bewijsvoering/Screenshot%202026-11-01%20153200.png) |
| 030 | 19:15:41 | **CONFIG** | HV-04 | VMware Preferences > Workspace: standaardlocatie voor VM's (gebruikerspad gemaskeerd). | [Screenshot 2026-11-01 191541.png](M01-Bewijsvoering/Screenshot%202026-11-01%20191541.png) |
| 031 | 19:18:23 | **CONFIG** | HV-04 Shared folders | VM Settings > Options > Shared Folders: Disabled (VM-naam in OCR onvolledig). | [Screenshot 2026-11-01 191823.png](M01-Bewijsvoering/Screenshot%202026-11-01%20191823.png) |
| 032 | 19:24:27 | **CONFIG** | HV-04 Shared folders | Client01: Shared Folders Disabled; Encryption: Encrypted; VMware Tools time sync off. | [Screenshot 2026-11-01 192427.png](M01-Bewijsvoering/Screenshot%202026-11-01%20192427.png) |
| 033 | 19:25:08 | **CONFIG** | HV-04 EXCEPTION | Client01 Guest Isolation: drag-and-drop en copy/paste AAN (visueel bevestigd). Dit is de geaccepteerde uitzondering. | [Screenshot 2026-11-01 192508.png](M01-Bewijsvoering/Screenshot%202026-11-01%20192508.png) |
| 034 | 19:28:52 | **CONFIG** | HV-04 EXCEPTION | WindowsServer (DC) Guest Isolation: drag-and-drop en copy/paste AAN (visueel bevestigd); Encryption: Not encrypted. | [Screenshot 2026-11-01 192852.png](M01-Bewijsvoering/Screenshot%202026-11-01%20192852.png) |
| 035 | 19:32:16 | **CONFIG** | VM-baseline DC | DC: Options > General (naam, gast-OS, working directory). | [Screenshot 2026-11-01 193216.png](M01-Bewijsvoering/Screenshot%202026-11-01%20193216.png) |
| 036 | 19:41:07 | **CONFIG** | VM-baseline Client01 | Client01: Options > General. | [Screenshot 2026-11-01 194107.png](M01-Bewijsvoering/Screenshot%202026-11-01%20194107.png) |
| 037 | 19:49:18 | **CONFIG** | HV-04 Shared folders | pfSense-VM: Shared Folders Disabled; Encryption: Not encrypted; Time sync off. | [Screenshot 2026-11-01 194918.png](M01-Bewijsvoering/Screenshot%202026-11-01%20194918.png) |
| 038 | 19:49:34 | **CONFIG** | HV-04 pfSense | pfSense-VM Guest Isolation VOOR wijziging: beide vinkjes AAN (visueel bevestigd). | [Screenshot 2026-11-01 194934.png](M01-Bewijsvoering/Screenshot%202026-11-01%20194934.png) |
| 039 | 19:51:40 | **TEST** | HV-01 | Host: Settings > Windows Update (status op 1 november). Statusregel uit OCR niet eenduidig leesbaar. | [Screenshot 2026-11-01 195140.png](M01-Bewijsvoering/Screenshot%202026-11-01%20195140.png) |
| 040 | 19:52:38 | **PASS** | HV-02 | Host PowerShell: Get-NetTCPConnection gefilterd op vmware-processen toont alleen 127.0.0.1:912 (vmware-authd). Beperkte scope: alleen listeners van vmware/vmnat-processen. | [Screenshot 2026-11-01 195238.png](M01-Bewijsvoering/Screenshot%202026-11-01%20195238.png) |
| 041 | 19:58:35 | **FIX** | HV-04 pfSense | pfSense-VM Guest Isolation NA wijziging: beide vinkjes UIT (visueel bevestigd). Instellingscontrole; functionele hertest ontbreekt. | [Screenshot 2026-11-01 195835.png](M01-Bewijsvoering/Screenshot%202026-11-01%20195835.png) |

## 02-11-2026

| # | Tijd | Klasse | Koppeling | Technische betekenis | Screenshot (gesaneerd) |
|---|---|---|---|---|---|
| 042 | 20:23:53 | **CONFIG** | VM-baseline FUXA01 | Wizard FUXA-VM: hardware compatibility. | [Screenshot 2026-11-02 202353.png](M01-Bewijsvoering/Screenshot%202026-11-02%20202353.png) |
| 043 | 20:26:50 | **CONFIG** | VM-baseline FUXA01 | Wizard: OS later installeren. | [Screenshot 2026-11-02 202650.png](M01-Bewijsvoering/Screenshot%202026-11-02%20202650.png) |
| 044 | 20:29:37 | **CONFIG** | VM-baseline FUXA01 | Keuze Ubuntu Server-ISO uit de lokale ISO-map. | [Screenshot 2026-11-02 202937.png](M01-Bewijsvoering/Screenshot%202026-11-02%20202937.png) |
| 045 | 20:30:57 | **CONFIG** | VM-baseline FUXA01 | Naam van de VM (FUXA01). | [Screenshot 2026-11-02 203057.png](M01-Bewijsvoering/Screenshot%202026-11-02%20203057.png) |
| 046 | 21:03:36 | **CONFIG** | VM-baseline FUXA01 | Processorconfiguratie. | [Screenshot 2026-11-02 210336.png](M01-Bewijsvoering/Screenshot%202026-11-02%20210336.png) |
| 047 | 21:05:04 | **CONFIG** | VM-baseline FUXA01 | Geheugentoewijzing. | [Screenshot 2026-11-02 210504.png](M01-Bewijsvoering/Screenshot%202026-11-02%20210504.png) |
| 048 | 21:15:39 | **CONFIG** | VM-baseline FUXA01 | SCSI-controllertype. | [Screenshot 2026-11-02 211539.png](M01-Bewijsvoering/Screenshot%202026-11-02%20211539.png) |
| 049 | 21:17:48 | **CONFIG** | VM-baseline FUXA01 | Schijfbestand 20 GB. | [Screenshot 2026-11-02 211748.png](M01-Bewijsvoering/Screenshot%202026-11-02%20211748.png) |
| 050 | 21:47:50 | **CONFIG** | VM-baseline FUXA01 | Hardware: Memory. | [Screenshot 2026-11-02 214750.png](M01-Bewijsvoering/Screenshot%202026-11-02%20214750.png) |
| 051 | 21:47:57 | **CONFIG** | VM-baseline FUXA01 | Hardware: Processors (2). | [Screenshot 2026-11-02 214757.png](M01-Bewijsvoering/Screenshot%202026-11-02%20214757.png) |
| 052 | 21:48:07 | **CONFIG** | VM-baseline FUXA01 | Hardware: Hard Disk, pad `REDACTED_PATH` | [Screenshot 2026-11-02 214807.png](M01-Bewijsvoering/Screenshot%202026-11-02%20214807.png) |
| 053 | 21:48:14 | **CONFIG** | VM-baseline FUXA01 | Hardware: CD/DVD met Ubuntu-ISO. | [Screenshot 2026-11-02 214814.png](M01-Bewijsvoering/Screenshot%202026-11-02%20214814.png) |
| 054 | 21:48:18 | **CONFIG** | VM-baseline FUXA01 | Hardware: USB Controller (USB 3.2). | [Screenshot 2026-11-02 214818.png](M01-Bewijsvoering/Screenshot%202026-11-02%20214818.png) |
| 055 | 21:48:27 | **CONFIG** | VM-baseline FUXA01 | Hardware: Display / 3D graphics. | [Screenshot 2026-11-02 214827.png](M01-Bewijsvoering/Screenshot%202026-11-02%20214827.png) |
| 056 | 23:20:59 | **CONFIG** | VM-baseline FUXA01 | FUXA01: Options > General, working directory. | [Screenshot 2026-11-02 232059.png](M01-Bewijsvoering/Screenshot%202026-11-02%20232059.png) |

## 03-11-2026

| # | Tijd | Klasse | Koppeling | Technische betekenis | Screenshot (gesaneerd) |
|---|---|---|---|---|---|
| 057 | 16:13:08 | **ERROR** | HV-01 (installatiemedia) | Get-FileHash op een nog lopende download (.crdownload, Wazuh-OVA) mislukt: PathNotFound. Geen hash van het voltooide bestand in de selectie. | [Screenshot 2026-11-03 161308.png](M01-Bewijsvoering/Screenshot%202026-11-03%20161308.png) |
| 058 | 16:27:09 | **CONFIG** | VM-baseline WAZUH01 | Import OVA: naam en opslagpad van WAZUH01. | [Screenshot 2026-11-03 162709.png](M01-Bewijsvoering/Screenshot%202026-11-03%20162709.png) |
| 059 | 22:24:48 | **CONFIG** | VM-baseline WAZUH01 | VM-overzicht WAZUH01 direct na import (Network Adapter: Bridged (Automatic)). | [Screenshot 2026-11-03 222448.png](M01-Bewijsvoering/Screenshot%202026-11-03%20222448.png) |
| 060 | 22:33:26 | **CONFIG** | VM-baseline WAZUH01 | WAZUH01 hardware: 4 processors; netwerkadapterpagina. | [Screenshot 2026-11-03 223326.png](M01-Bewijsvoering/Screenshot%202026-11-03%20223326.png) |
| 061 | 22:36:31 | **ERROR** | VM-baseline WAZUH01 | Melding 'The CPU has been disabled by the guest operating system' bij starten van de Wazuh-VM. | [Screenshot 2026-11-03 223631.png](M01-Bewijsvoering/Screenshot%202026-11-03%20223631.png) |
| 062 | 22:42:24 | **TROUBLESHOOT** | VM-baseline WAZUH01 | Host-CPU opgevraagd: AMD Ryzen AI 7 350 (AuthenticAMD) - context voor de CPU-fout. | [Screenshot 2026-11-03 224224.png](M01-Bewijsvoering/Screenshot%202026-11-03%20224224.png) |
| 063 | 22:47:09 | **FIX** | VM-baseline WAZUH01 | WAZUH01.vmx in Kladblok: cpuid.1.eax/ecx/edx-maskers en featureCompat.enable = FALSE toegevoegd. | [Screenshot 2026-11-03 224709.png](M01-Bewijsvoering/Screenshot%202026-11-03%20224709.png) |
| 064 | 22:55:46 | **PASS** | VM-baseline WAZUH01 | Wazuh-VM start door tot loginprompt (Wazuh 4.14.9) na de .vmx-aanpassing. Standaard-inloggegevens uit de banner zijn in de publieke versie gemaskeerd. | [Screenshot 2026-11-03 225546.png](M01-Bewijsvoering/Screenshot%202026-11-03%20225546.png) |

## 04-11-2026

| # | Tijd | Klasse | Koppeling | Technische betekenis | Screenshot (gesaneerd) |
|---|---|---|---|---|---|
| 065 | 00:24:40 | **CONFIG** | Herstel (kopie) | Verkenner: map 'REDACTED_BACKUP_FOLDER\WAZUH01' met VM-bestanden (kopie op dezelfde host-schijf C:). | [Screenshot 2026-11-04 002440.png](M01-Bewijsvoering/Screenshot%202026-11-04%20002440.png) |

## 05-11-2026

| # | Tijd | Klasse | Koppeling | Technische betekenis | Screenshot (gesaneerd) |
|---|---|---|---|---|---|
| 066 | 17:22:30 | **CONFIG** | VM-baseline PLC01 | New VM Wizard (Workstation Pro 26H1) voor PLC01. | [Screenshot 2026-11-05 172230.png](M01-Bewijsvoering/Screenshot%202026-11-05%20172230.png) |
| 067 | 17:23:39 | **CONFIG** | VM-baseline PLC01 | Gast-OS: Linux / Ubuntu 64-bit. | [Screenshot 2026-11-05 172339.png](M01-Bewijsvoering/Screenshot%202026-11-05%20172339.png) |
| 068 | 17:27:32 | **CONFIG** | VM-baseline PLC01 | Schijfgrootte 20 GB, gesplitst. | [Screenshot 2026-11-05 172732.png](M01-Bewijsvoering/Screenshot%202026-11-05%20172732.png) |
| 069 | 17:29:58 | **CONFIG** | VM-baseline PLC01 | Hardware: 2 processors; Virtualization engine-opties zichtbaar. | [Screenshot 2026-11-05 172958.png](M01-Bewijsvoering/Screenshot%202026-11-05%20172958.png) |
| 070 | 17:31:02 | **CONFIG** | VM-baseline PLC01 | CD/DVD: 'Use ISO image file'. | [Screenshot 2026-11-05 173102.png](M01-Bewijsvoering/Screenshot%202026-11-05%20173102.png) |
| 071 | 19:16:22 | **CONFIG** | VM-baseline PLC01 | VM-overzicht PLC01 in de bibliotheek. | [Screenshot 2026-11-05 191622.png](M01-Bewijsvoering/Screenshot%202026-11-05%20191622.png) |

## 11-11-2026

| # | Tijd | Klasse | Koppeling | Technische betekenis | Screenshot (gesaneerd) |
|---|---|---|---|---|---|
| 072 | 15:22:48 | **TEST** | Host-integriteit | Host: sfc /verifyonly - 'did not find any integrity violations'; DISM /ScanHealth gestart. | [Screenshot 2026-11-11 152248.png](M01-Bewijsvoering/Screenshot%202026-11-11%20152248.png) |
| 073 | 15:42:21 | **TEST** | Host-integriteit | Host: DISM ScanHealth - 'The component store is repairable'; Get-PhysicalDisk: Healthy / OK. | [Screenshot 2026-11-11 154221.png](M01-Bewijsvoering/Screenshot%202026-11-11%20154221.png) |
| 074 | 16:00:55 | **FIX** | Host-integriteit | Host: DISM /RestoreHealth - 'The restore operation completed successfully'. | [Screenshot 2026-11-11 160055.png](M01-Bewijsvoering/Screenshot%202026-11-11%20160055.png) |
| 075 | 16:17:25 | **PASS** | Host-integriteit | Host: sfc /scannow 100% - geen integriteitsschendingen. | [Screenshot 2026-11-11 161725.png](M01-Bewijsvoering/Screenshot%202026-11-11%20161725.png) |
| 076 | 16:22:56 | **FAIL** | Host-integriteit | Host: DISM /ScanHealth NA RestoreHealth meldt opnieuw 'The component store is repairable'. Herstel is dus niet bevestigd. | [Screenshot 2026-11-11 162256.png](M01-Bewijsvoering/Screenshot%202026-11-11%20162256.png) |
| 077 | 16:25:19 | **TROUBLESHOOT** | Host-integriteit | Host: uittreksel CBS.log - 'CSI Payload Corruption: 27', 'Total Repaired Corruption: 0'. | [Screenshot 2026-11-11 162519.png](M01-Bewijsvoering/Screenshot%202026-11-11%20162519.png) |
| 078 | 16:26:45 | **TROUBLESHOOT** | Host-integriteit | Host: uittreksel dism.log met foutregel 0x8007007b. | [Screenshot 2026-11-11 162645.png](M01-Bewijsvoering/Screenshot%202026-11-11%20162645.png) |
| 079 | 16:30:38 | **CONFIG** | HV-01 | Host: System > About - Windows 11 Home 26H2, OS build 26300.9818. | [Screenshot 2026-11-11 163038.png](M01-Bewijsvoering/Screenshot%202026-11-11%20163038.png) |
| 080 | 16:32:38 | **PENDING** | HV-01 | Host Windows Update 11 november: 'Updates available to install' incl. 2026-11 Security Update (KB5132061). Niet bijgewerkt op dit moment. | [Screenshot 2026-11-11 163238.png](M01-Bewijsvoering/Screenshot%202026-11-11%20163238.png) |
| 081 | 16:32:51 | **CONFIG** | HV-01 | Host: Windows Update > Windows Insider Program-pagina. | [Screenshot 2026-11-11 163251.png](M01-Bewijsvoering/Screenshot%202026-11-11%20163251.png) |

## 15-11-2026

| # | Tijd | Klasse | Koppeling | Technische betekenis | Screenshot (gesaneerd) |
|---|---|---|---|---|---|
| 082 | 17:35:02 | **TROUBLESHOOT** | Hostcapaciteit | Taakbeheer host 15 november: geheugengebruik (context: geheugendiagnose WorkloadsSessionHost). | [Screenshot 2026-11-15 173502.png](M01-Bewijsvoering/Screenshot%202026-11-15%20173502.png) |

## Technische chronologie M01

| Fase | Wat de beelden laten zien | Bewijs (#) |
|---|---|---|
| **Beginsituatie** | Host Lenovo (32 GB, AMD Ryzen AI 7 350, virtualisatie aan). Bestaande VM's pfSense, GNS3, WindowsServer, Linux. Nieuwe Client01-VM wordt opgebouwd met vTPM, UEFI/Secure Boot en gedeeltelijke encryptie. | 2026-10-31 101655 t/m 110202; 2026-11-01 134524, 135139 |
| **Configuratie** | VM-wizards en hardware voor Client01 (31-10), FUXA01 (02-11), WAZUH01 (03-11, OVA-import) en PLC01 (05-11). VMware Tools in de Windows-gast. Snapshot `POST-AD-DC` op de DC. | wizardreeksen per VM; 2026-10-31 205805, 212030; 2026-11-01 153200 |
| **Probleem** | (a) Firmware niet te wijzigen zolang TPM bestaat. (b) Windows Time-service in Client01 niet gestart; laatste synchronisatie 'unspecified'. (c) Wazuh-VM: 'The CPU has been disabled by the guest operating system'. (d) Host: DISM meldt 'component store is repairable'. | 110129; 212850–213413; 2026-11-03 223631; 2026-11-11 154221 |
| **Oplossing** | (c) `.vmx` aangepast met cpuid-maskers en `featureCompat.enable = FALSE`. (d) DISM /RestoreHealth 'completed successfully'. HV-04: klembord en drag-and-drop op de pfSense-VM uitgezet. Voor (a) en (b) is geen oplossing in beeld. | 2026-11-03 224709; 2026-11-11 160055; 2026-11-01 195835 |
| **Verificatie** | Wazuh-VM start tot loginprompt. HV-02: alleen `127.0.0.1:912` (vmware-authd). HV-04: instellingen voor en na zichtbaar. sfc /scannow zonder schendingen, **maar** DISM meldt na het herstel opnieuw 'repairable' en op 11-11 staan beveiligingsupdates open. | 2026-11-03 225546; 2026-11-01 195238, 194934→195835; 2026-11-11 161725, 162256, 163238 |
