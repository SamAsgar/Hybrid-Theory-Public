> **Historische momentopname (gesaneerde export).** Deze sessie is niet retrospectief aangepast aan later werk; zie [de actuele roadmap](ROADMAP.md) en [publieke besluiten](../governance/BESLUITENLOG.md). Echte IP-adressen, domeinen, paden, privésystemen en interne bronlinks zijn verwijderd. `LAB_IP_REDACTED` is geen bruikbare configuratiewaarde.

# Hybrid-Theory-projectlog | 27 oktober 2026 — Hostcapaciteit en RAM-diagnose

> Bewerkt 02-11-2026: terminologie geharmoniseerd en interne verwijzingen verwijderd; testuitslagen ongewijzigd.
>
> **TL;DR (redactionele toevoeging)**  
> **Vraag:** Hoeveel capaciteit heeft de Windows-/VMware-host voor uitbreiding?  
> **Uitkomst:** Hostmetingen zijn vastgelegd; vijf gelijktijdige VM's niet bewezen.  
> **Besluit:** Gefaseerd bouwen en capaciteit meten; geplande RAM-waarden zijn geen gemeten VM-instellingen. **Cockpit was al op 25 oktober PASS; Ubuntu was toen met 4 GB beschreven. De 2 GB op 27 oktober was uitsluitend een budgetvoorstel.**


> **Actuele planningsreferentie (29-10-2026):** [Roadmap Fase 0–7](ROADMAP.md) is leidend. De Windows-administratieclient is **PLANNED als Windows 11 Enterprise Evaluation**. De oorspronkelijke resource-inschattingen en eerdere voorstellen hieronder blijven sessiegegevens; de client en gezamenlijke vijf-VM-belasting zijn **NOT VERIFIED**.

**Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.**  
**Scope:** Windows-host Lenovo, VMware-capaciteitsplanning voor Fase 3/4  
**Status:** Diagnose UITGEVOERD; VM-belastingstest OPEN; geen permanente systeemwijzigingen bevestigd.  
**Bewijsbasis:** door Project Owner gedeelde screenshots uit Task Manager, VMware Workstation, PowerShell en Windows Settings. Momentopnamen zijn niet simultaan en hebben verschillende achtergrondbelasting.  
**Publicatie:** geredigeerd, zonder accountinformatie, interne paden met persoonsinformatie of identifiers van het thuisnetwerk.

## 1. Hardwarebaseline (VERIFIED via Task Manager/VMware screenshots)
- Lenovo Windows host: **AMD Ryzen AI 7 350**, **8 cores / 16 logical processors**, hardwarevirtualisatie **Enabled**.
- **32 GB LPDDR5 7500 MT/s** geïnstalleerd; circa **30,7 GB bruikbaar**, **1,3 GB hardware reserved**.
- **NVMe SSD circa 954 GB**, idle diskactiviteit ongeveer 0–1%; enkele korte pieken in de grafiek. Gemeten responstijd rond 0,7 ms (momentopname).
- CPU idle circa **4–9%**. Dit valideert **geen** gelijktijdige prestaties van vijf actieve VM's.
- VMware Workstation toont bestaande Ubuntu Server VM en **PS-HT-FW01-pfSense**; pfSense **2 GB RAM**, **2 vCPU**, **20 GB disk**, adapters host-only/NAT/LAN Segment. Op getoonde VMware screenshot staat pfSense uit.
- Screenshots bevestigen niet dat Cockpit nu operationeel is.

## 2. Geheugenmetingen (VERIFIED snapshots; oorzaken NIET VERIFIED)
| Tijdvolgorde | Gebruikt | Beschikbaar | Committed | Compressed | Opmerking |
|---|---:|---:|---:|---:|---|
| Vroege Task Manager-meting | 16,6 GB | 14,1 GB | n.v.t. | circa 2,1 GB | circa 54% |
| Nadere geheugenanalyse | 17,2 GB | 13,4 GB | 28,6/44,7 GB | 2,0 GB | Cached 10,9 GB |
| PowerShell nulmeting | — | **14.691 MB** | — | — | `\Memory\Available MBytes` |
| Latere PowerShell-meting | — | **19.266 MB** | — | — | circa 4.575 MB hoger dan nulmeting; alleen correlatie |
| Laatste Task Manager-meting | **16,2 GB** | **14,4 GB** | **21,5/44,2 GB** | **323 MB** | Cached 10,4 GB, circa 53% van bruikbaar RAM |

**Interpretatie:** daling van committed memory van **28,6 naar 21,5 GB** (7,1 GB) tussen meetmomenten; beschikbaar fysiek geheugen fluctueert. Cached memory is niet bij Available op te tellen. Er is **geen bewijs** dat uitgeschakelde AI-instellingen de daling veroorzaakten.

## 3. Windows AI-workloadonderzoek en troubleshooting
1. Task Manager → Details, sorteren op Commit size: meerdere `WorkloadsSessionHost.exe`-processen, aanvankelijk individuele commitwaarden tot ongeveer 2,77 GB. **Commit is niet hetzelfde als fysiek RAM**.
2. File location gevonden onder vertrouwde WindowsApps-pakketstructuur `WindowsWorkload.Manager.1`; lijst met WindowsWorkload.Manager, SessionManager, PSOnnxRuntime, PSTokenizerShared, WinMLShared, AMD VitisAI-provider. Dit ondersteunt een AI-workloadrelatie maar bewijst geen geheugenlek.
3. PowerShell `Get-Process WorkloadsSessionHost` toonde **9 processen** met circa **1,84 GB working set** en **6 GB private memory** (som); later **7 processen** met circa **3.077,6 MB working set**. Lager aantal processen betekende dus niet minder fysiek werkgeheugen.
4. `Get-Service WSAIFabricSvc`: **Windows AI Components Host**, **Running**, **Automatic**. `sc.exe queryex WSAIFabricSvc`: running, gemarkeerd **STOPPABLE**, PID beschikbaar, foutcodes 0.
5. Eerste `Stop-Service WSAIFabricSvc` faalde in niet-verhoogde PowerShell met service-openfout. `net session` gaf **Access is denied**.
6. Verhoogde **Administrator: Windows PowerShell** bevestigd via `net session` met **There are no entries in the list**.
7. Ook in verhoogde sessie faalde `Stop-Service WSAIFabricSvc` met **stop failed**. **Niet geforceerd**; geen handmatige servicebescherming omzeild, geen registry-edit, geen package-removal.
8. Windows **Privacy & security → Click to Do** stond zichtbaar **Off** op screenshot. Niet vastgesteld of het in die sessie veranderd is, of al uit stond; **Recall-configuratie niet bevestigd**.
9. `steamwebhelper.exe` werd teruggevonden onder de verwachte Steam CEF-installatiemap; geen indicatie dat deze het Windows AI-workloadproces is.

**Risicobesluit:** verder optimaliseren van Windows AI wordt **GEPARKEERD**; geen aangetoonde verbetering door stoppen en geen reden voor destructieve ingrepen.

## 4. RAM-plan vijf VM's (PROPOSED, niet geverifieerd)
| VM | Start-RAM |
|---|---:|
| pfSense | 2 GB |
| Ubuntu Server + later Cockpit | 2 GB |
| Windows Server 2025 (AD/DNS) | 4 GB |
| Windows 11 Pro IT-admin domain client | 4 GB |
| GNS3 VM | 4 GB |
| **Totaal gealloceerd** | **16 GB** |

**LET OP:** 16 GB toegewezen guest memory plus hostbelasting, virtualisatieoverhead en grotere GNS3-routerimages kan druk veroorzaken. Met een laatste hostmeting van 14,4 GB Available mag **geen PASS voor alle vijf gelijktijdig** worden afgegeven. De 19.266 MB was slechts een tussentijdse momentopname.

## 5. Sessieoordeel en vervolgstappen
- **PASS — host hardware inventory & diagnostische metingen** binnen screenshotscope.
- **PASS — voortzetting gefaseerde installatie**, onder voorwaarde van capaciteitsmonitoring.
- **OPEN / NOT VERIFIED — vijf VM's tegelijk, GNS3 onder echte netwerkbelasting, duurzame host-headroom.**
- **REWORK/INCONCLUSIVE — stoptest Windows AI Components Host**: stopt niet, geen besparing bewezen; niet verder forceren.
- **Fase 3:** Windows Server 2025 (AD/DNS) en Windows 11-domainclient installeren en domain join + DNS + GPO valideren; start met 4 GB per VM en meet host Available/Committed/CPU/disk.
- **Fase 4:** daarna pas aparte GNS3 VM inzetten met kleine topologie en metingen.
- Eerdere pfSense-openpunten (DNS/gateway, logtijd, Ubuntu-adapters/route, snapshot) blijven bestaan conform log van 26 oktober; dit RAM-log sluit ze niet af.
- **Publicatie en privacy:** geen nieuwe screenshots met identiteit, e-mail of thuisnetwerkgegevens toevoegen aan publieke repo.

**Architectuuroordeel:** hardware geschikt voor gefaseerd experimenteren; **geen onbewezen claim dat alle vijf VM's langdurig gelijktijdig probleemloos draaien**.
