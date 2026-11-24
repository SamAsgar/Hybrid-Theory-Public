# Projectlog | 6 november 2026

> **ACTUELE STATUSUPDATE | 6 november 2026 (na de onderstaande eerdere momentopname):** AC01 lokale PLC-motorlogica **PASS**, AC02 dynamische PLC→FUXA-uitlezing **PASS** voor twee Boolean-tags, AC03 FUXA→PLC motorbediening **PASS binnen functionele testscope** op basis van project-eigenaarbevestiging en gedeelde sessiebeelden. **M04 blijft IN PROGRESS:** geen bewezen OT-segmentatie, volledige firewall-isolatie of securityacceptatie. Raadpleeg de vervolgdelta onderaan; eerdere PENDING-vermeldingen hieronder zijn historische tussenstanden.

## M04 Network Citadel — OpenPLC-motorbaseline en FUXA-voorbereiding

**Status:** M04 HIGH PRIORITY / ACTIVE; OT-baseline **gedeeltelijk functioneel gevalideerd**, eind-tot-eind-FUXA-acceptatie nog **PENDING**. Dit verslag beschrijft de uitvoeringsdelta uit de sessie van 5/6 november; het vervangt geen eerdere logboeken.

### Uitgevoerd en waargenomen
- Bestaande native OpenPLC v3 Runtime op Ubuntu Server gecontroleerd; service actief en webinterface bereikbaar.
- IEC 61131-3 Structured Text-motorsimulatie gemaakt, gecompileerd en via OpenPLC geüpload. Zowel IEC-compiler als volledige runtimebuild rapporteerden succes.
- OpenPLC Monitoring toonde de functionele testwaarden: motor UIT → `Motor_Start=FALSE`, `Motor_Running=FALSE`, `Temperature=25`, `Alarm=FALSE`; motor AAN → `TRUE`, `TRUE`, `45`, `FALSE`. **Motorlogica PASS binnen testscope**.
- FUXA-container en HMI-editor bereikbaar; van FUXA naar PLC TCP/Modbus-poort bereikbaar. De Modbus-driver geïnstalleerd en een FUXA-ModbusTCP-device toegevoegd. Een groene connectie-indicator en twee Boolean-tags met ontvangen nulwaarden/timestamps werden gezien.

### Openstaande validatie
- **AC01** OpenPLC Runtime operationeel: **PASS** binnen de uitgevoerde motorsimulatie.
- **AC02** FUXA leest correcte, dynamisch veranderende PLC-registerwaarden: **PENDING**; de volledige TRUE/FALSE-synchronisatie is nog niet onomstotelijk bewezen.
- **AC03** FUXA stuurt gecontroleerde Modbus-schrijfactie: **PENDING**.
- IT/OT-segmentatie achter pfSense, Wazuh-agentdetectie, GNS3-uitbreiding 3×25 VPCS, routing-/firewall-negatievetests en Suricata/Wazuh-integratie: **PENDING/PLANNED**.

### Architectuur en veiligheid
Tijdens deze preflight staan de PLC- en HMI-VM's tijdelijk samen op een VMware NAT-netwerk, **nog niet achter de beoogde pfSense-OT-zone**. Exacte private netwerkadressen en oorspronkelijke niet-gesaneerde screenshots worden **niet** gepubliceerd. Poortbereikbaarheid bewijst geen isolatie en een groene connectiestatus geen geslaagde registervalidatie. Securitypatching en protocolhardening volgen gecontroleerd.

### Vervolg
Eerst de dynamische FUXA-reads en een geautoriseerde HMI-write aantonen, daarna tags/dashboard completeren, vervolgens pfSense-OT-isolatie en Wazuh. De toekomstige koelsimulatie is een afzonderlijk geparkeerd idee en geen afgeronde implementatie.

**Evidence:** Sam beschikt over een lokaal privé-ZIP met 27 originele screenshots; dit bestand is nadrukkelijk **niet gesaneerd en niet publiek beschikbaar**. Publieke evidence wordt uitsluitend na afzonderlijke publicatiecontrole toegevoegd.

---

## Vervolgdelta 6 november — dynamische FUXA/PLC-integratie

**Type:** sessie-aanvulling op eerder log. **Scope:** virtuele motorsimulatie en twee Modbus Boolean-tags, geen fysieke industriële apparatuur.

### Nieuwe technische observaties
- OpenPLC-runtime **Running**; Modbus TCP-listener actief op poort 502. Verbinding vanaf Windows-host én afzonderlijk vanaf FUXA Linux-VM naar de PLC getest (**TCP PASS**).
- FUXA Docker-container actief, HMI-editor beschikbaar, Modbus TCP-device **PLC01-MOTOR** operationeel.
- Via OpenPLC werd een gecontroleerde motorcyclus OFF→ON→OFF uitgevoerd. De twee FUXA-tags **Motor_Start** en **Motor_Running** volgden de waarden **0→1→0** met bijgewerkte timestamps: **AC02 PASS binnen deze twee tags**.
- Een FUXA MainView-button is met de tag **Motor_Start** en actie **Toggle** gekoppeld. Sam bevestigde dat starten en stoppen vanuit FUXA werkt en deelde sessiebeeldmateriaal: **AC03 PASS binnen functionele scope**, niet onafhankelijk op pakketniveau geverifieerd.
- Lokale PLC Monitoring liet motor OFF (FALSE/FALSE/25) en ON (TRUE/TRUE/45) zien; Alarm bleef FALSE. Een werkende alarm- of overtemperatuurtest is niet aangetoond.

### Statusmatrix

| Subtest | Status | Afbakening |
| --- | --- | --- |
| AC01 — OpenPLC-runtime + lokale motorlogica | **PASS** | Gesimuleerde motor |
| AC02 — dynamische PLC→FUXA-uitlezing | **PASS** | Twee Boolean-tags |
| AC03 — HMI→PLC-commando | **PASS (eigenaar + sessiebeelden)** | Motor-start/stop, geen onafhankelijke packetcapture |
| AC04 — afgedwongen IT/OT-segmentatie | **PENDING** | Beide OT-VM's nog op gedeelde VMware NAT |
| AC05 — Wazuh OT-detectie | **PENDING** | End-to-end ingestie niet aangetoond |
| AC06 — GNS3-scenario-uitbreiding | **PLANNED** | Scope nog selecteren |
| AC07 — allow/deny en negatieve beveiligingstests | **PENDING** | Nieuwe zonegrens niet bewezen |
| AC08 — Suricata-alerting | **PLANNED** | Geen geïnstalleerde keten aangetoond |

### Eerstvolgend werk
1. Huidige NICs, routes en directe OT-hostconnectiviteit inventariseren; herstelpunt en terugvalplan vastleggen.
2. FUXA en OpenPLC gecontroleerd in een afgescheiden OT-zone achter pfSense plaatsen; restrictieve allowlist uitsluitend voor noodzakelijke communicatie, expliciete bloktests van ongeautoriseerde bronnen.
3. Positieve Modbus-read/write opnieuw testen over nieuwe netwerkgrens, inclusief verkeersanalyse, logging en failure/rollback.
4. Daarna Wazuh-agents/detectie en waar relevant Suricata, risicogerichte GNS3-scenario's, beheerhardening en gedocumenteerde bewijsacceptatie.

**Publicatiegrens:** geen private IP-adressen, NAT-bronadressen, login-/SSH-informatie, ongesaneerde screenshots of video geüpload. Deze log is een **gesaneerde tekstuele voortgangsregistratie**, geen onafhankelijk auditrapport. De OT-veiligheidsgrens moet nog worden bewezen.
