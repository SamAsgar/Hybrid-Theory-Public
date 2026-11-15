# M04 Network Citadel | OT Modbus-applicatievalidatie — 15 november 2026

**Status:** M04-CORE **IN PROGRESS**; afgebakende technische deeltests **TESTED**; volledige AC04/AC07 en evidence-review **PENDING**.  
**Publicatievorm:** gesanitiseerde technische voortgang voor het portfolio; geen live IP-/MAC-adressen, beheerbron of firewallregelconfiguraties.  
**Bron:** door de Project Owner uitgevoerde en tijdens een begeleide sessie getoonde VM-, terminal- en webinterfacecontroles. Originele sessiebeelden zijn **niet** in deze repository gepubliceerd.

## 1. Voortgang sinds 11 november

PLC en SCADA/HMI draaien inmiddels op hetzelfde afzonderlijke, geïsoleerde virtuele OT-netwerk. Een initiële Modbus-verbindingsstoring is op applicatieniveau onderzocht en hersteld, zonder de bestaande firewallpolicy voor deze stap te wijzigen.

| Testonderdeel | Uitkomst en bewijsgrens |
|---|---|
| OT-interne bereikbaarheid | Bidirectionele ICMP- en ARP-deeltesten **TESTED**; dit valideert niet de grens naar andere netwerkzones |
| PLC-webinterface | Bereikbaar vanaf het expliciet toegestane beheerspoor (**TESTED**) |
| PLC-runtime | Aanvankelijk gestopt; handmatig gestart met geladen motorsimulatie, daarna status **Running** |
| Modbus TCP | PLC luistert aantoonbaar op **TCP 502**; TCP-handshake vanuit HMI **TESTED** |
| HMI-runtime | Docker/HMI na herstart van de HMI-VM actief; webinterface en editor bereikbaar (**TESTED**) |
| HMI→PLC-verbinding | Oude referentie naar de tijdelijke NAT-topologie vervangen door het actuele OT-endpoint; HMI rapporteert **groene verbindingsstatus** |
| Modbus-tags | Twee booleaanse motorsignalen in de HMI zichtbaar met actuele tijdstempels; de PLC-monitoring toont dezelfde nulstand |
| Motorsimulatie | Project Owner meldt dat de bestaande HMI-besturing functioneert; volledige start/stop-readback wordt nog als aparte bewijsreeks vastgelegd |

## 2. Diagnose en leerpunten

- Een bereikbare PLC-webinterface betekent niet automatisch dat de **PLC-runtime** actief is; HTTP-beheer en Modbus-service moeten afzonderlijk worden gemonitord.
- Een open TCP-poort bewijst nog niet dat registeradressering en industriële proceslogica werken.
- Bij een netwerkmigratie moet ook de **HMI-deviceconfiguratie** worden geactualiseerd. Het oude doeladres kan blijven staan, zelfs wanneer beide VM's technisch correct in het nieuwe segment draaien.
- Een groen connectie-icoon, actuele tagwaarden en controle van de PLC-monitoring geven gezamenlijk sterkere aanwijzingen dan uitsluitend een ping.
- Aangetoonde intra-OT-communicatie is **geen** bewijs van geslaagde isolatie tegenover LAB, management of andere zones.

## 3. Acceptatie en resterende werkzaamheden

| Testgate | Stand 15 november |
|---|---|
| AC01: motorsimulatie | Runtime en geladen programma gezien; volledige functionele regressiereeks nog documenteren |
| AC02: Modbus-uitlezing | Gerichte uitleesdeelcontrole **TESTED**; volledige aantoonbare waardeverandering en bewijsimport **PENDING** |
| AC03: Modbus-write en motorrespons | Door Project Owner functioneel gemeld; formele end-to-end start-stop-readback **PENDING** |
| AC04: segmentatie | Integrale zone-/route-/egressvalidatie **PENDING** |
| AC07: allow/deny | Eerdere beperkte negatieve en positieve deeltesten blijven geldig in hun scope; volledige matrix **PENDING** |
| M04-CORE | **IN PROGRESS**; geen finale missieacceptatie |

**Bewijsbeperking:** er zijn bij deze documentatie-update geen screenshots, captures, hashes of exportbestanden naar de publieke repository overgezet. De primaire evidence wordt pas toegevoegd na afzonderlijke review en pixelmatige sanering; screenshots vormen op zichzelf geen integrale PASS.

## 4. Volgende focus

AC02/AC03-reeksen met zichtbare command- en readbackovergangen documenteren, de resterende toegestane en geweigerde verbindingen voor AC04/AC07 met herleidbare firewallregistratie testen en de uitzonderingen/hardening beoordelen. Daarna volgt een expliciete security- en eigenaarreview.

Dit is een **gedateerde deelupdate**. Historische logs blijven geldig voor de toenmalige netwerkopstelling en worden niet stilzwijgend herschreven.
