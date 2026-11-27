# M04 Network Citadel | AC05 — agentregistratie en offline installatie | 27 november 2026

**Gesaneerde voortgangsregistratie. P3/P4 TESTED / scoped PASS; AC05 integraal PENDING.** Geen werkelijke interne adressen, hostidentificatoren, sleutels, ruwe logs of originele screenshots.

## Doel

Na de vaste SIEM-adresreservering (P1) en de beperkte firewallverbinding (P2) is de volgende stap één Wazuh-agent op de HMI in de geïsoleerde OT-zone. Het doel is de software te installeren zonder de netwerkgrens te verruimen.

## P3 — registratie op de manager

De managerlijst is vooraf gecontroleerd: er was nog geen remote agent geregistreerd. Daarna is één specifieke HMI-agent met bronadresbinding handmatig aan de manager toegevoegd. De manager bevestigde de registratie en de registratie verscheen in de agentlijst.

**P3 TESTED / scoped PASS** voor de managerregistratie. De unieke sleutel is niet gepubliceerd en de sleutelimport op de HMI is nog niet uitgevoerd. De registratie is geen actieve agentverbinding.

## P4 — gecontroleerde offline installatie

| Stap | Waarneming |
|---|---|
| Platform | Ubuntu 24.04 LTS, AMD64, geen bestaande Wazuh-agent |
| Download | Wazuh-agent 4.14.9-1 via de officiële HTTPS-pakketbron op een afzonderlijke beheerhost; passend bij manager 4.14.9 |
| Pakketmetadata | Directe afhankelijkheden libc6, lsb-release, debconf, adduser en procps; alle vijf geïnstalleerd |
| Transport | Lokale SHA-256 vastgelegd; dezelfde hash bij staging en op de OT-host |
| ISO | Bestaande VMware ISO-tool gebruikt; alleen het installatiepakket naar de OT-host overgebracht via een virtuele dvd |
| Installatie | Read-only ISO, lokale Debian-pakketinstallatie zonder pakketdownload op OT; install ok installed bevestigd |
| Runtime | Agentservice inactive; bewust nog niet gestart |

De eerste poging om de pakketmetadata via een binaire PowerShell-pipeline uit te lezen mislukte. Extractie naar een apart bestand werkte. Bij de ISO-wissel bleek het virtuele dvd-station losgekoppeld; na herstel van de verbinding slaagde de read-only mount. De OT-netwerkadapter bleef op het bestaande geïsoleerde netwerk volgens de getoonde configuratie. Er is geen nieuwe firewalluitzondering of OT-internettoegang nodig gebleken.

**P4 TESTED / scoped PASS** voor offline overdracht, transportintegriteit en installatie. Een overeenkomende hash bewijst dat de kopie gelijk is aan de lokale download, niet dat de uitgevershandtekening onafhankelijk is geverifieerd. Die controle blijft open. De software is geïnstalleerd, maar een actieve dienst, runtimebelasting en applicatieregressie zijn nog niet getoetst.

## Bewijsgrenzen en vervolg

De originele sessiebeelden en individuele beschrijvingen zijn uitsluitend privé bewaard. Geen originele screenshots of ZIP in Public; de inhoudelijke review en bewijsimport van deze nieuwe set staan open. Er is geen automatische formele VERIFIED-status.

**P5:** controleer eerst de agentconfiguratie, maak een configuratieback-up, stel het managerendpoint in en importeer de geheime registratiesleutel handmatig. De bestaande specifieke TCP/1514-regel volstaat voor de beoogde agentverbinding; TCP/1515 blijft dicht vanuit OT. Verifieer de verbinding op beide kanten.

**P6:** toon een gecontroleerde File Integrity Monitoring-gebeurtenis tot in de SIEM aan.

**AC05 integraal PENDING.** AC04/AC07, CORE-acceptatie, AC06 en AC08 blijven ongewijzigd. Geen algemene isolatie-, monitoring- of herstelgarantie.

[Eerdere P2-testregistratie](2026-11-27-m04-ac05-p2-ot-siem-firewallvalidatie.md) · [Actuele M04-issue](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/45)
