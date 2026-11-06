# Projectlog | 6 november 2026
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

**Evidence:** de Project Owner beschikt over een lokaal privé-ZIP met 27 originele screenshots; dit bestand is nadrukkelijk **niet gesaneerd en niet publiek beschikbaar**. Publieke evidence wordt uitsluitend na afzonderlijke publicatiecontrole toegevoegd.
