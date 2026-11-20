# M04 fase 21 — CORE C2 firewall- en isolatietests (20 november 2026)

**52 gesaneerde weergaven** · 20:21:42–23:27:29 CET · chronologisch gesorteerd

[Terug naar de fasen](../README.md) · [Saneringsrapport](M04-PHASE21-SANITIZATION-REPORT.md) · [Bewijsmanifest](M04-EVIDENCE-PHASE21.csv) · [SHA-256](SHA256SUMS.txt)

De reeks bevat firewalllogs, PowerShell- en terminalprobes, IPv6-routecontroles, VMware LAN Segments en pfSense-configuratie. De index vermeldt test-ID’s waar de koppeling bevestigd is. De bewijsgrens en status van de missie blijven zoals gedocumenteerd in het missieoverzicht.

| Tijd (CET) | Test | Opname |
| --- | --- | --- |
| 20:21:42 | — | [pfSense LAN-log met expliciete MGMT-regel voor PLC01/OpenPLC op TCP/8080.](01-202142-M04-C2.png) |
| 20:21:55 | F10 | [pfSense LAB-log gefilterd op TCP/22 naar PLC01.](02-202155-M04-C2.png) |
| 20:22:11 | F11 | [pfSense LAB-log gefilterd op TCP/44818 naar PLC01.](03-202211-M04-C2.png) |
| 20:22:52 | F12 | [pfSense LAB-log gefilterd op ICMP naar PLC01. De weergave bevat ook oudere logregels.](04-202252-M04-C2.png) |
| 20:30:56 | F09 | [pfSense LAB-log gefilterd op TCP/8080 naar PLC01.](05-203056-M04-C2.png) |
| 20:56:57 | — | [pfSense LAN-regels voor MGMT-toegang tot FUXA01 en PLC01 en de standaardblokkade richting OT.](06-205657-M04-C2.png) |
| 21:00:15 | — | [Lenovo PowerShell met routeringsonderzoek naar een OT-adres.](07-210015-M04-C2.png) |
| 21:01:44 | — | [Lenovo PowerShell met adapterstatus, IPv4-adressen en VMnet1-routegegevens.](08-210144-M04-C2.png) |
| 21:03:41 | — | [Lenovo PowerShell met netwerkadapters, IPv4-adressen en routetabel.](09-210341-M04-C2.png) |
| 21:04:25 | — | [Lenovo PowerShell met VMnet1-routering en HTTPS-probe naar pfSense op TCP/443.](10-210425-M04-C2.png) |
| 21:09:49 | — | [Lenovo PowerShell met HTTPS-probe en begin van de poortcontroles richting pfSense.](11-210949-M04-C2.png) |
| 21:10:33 | — | [Lenovo PowerShell met controles richting pfSense op TCP/502, TCP/22 en TCP/44818.](12-211033-M04-C2.png) |
| 21:17:36 | F16 | [PLC01-terminal met route naar MGMT en eerste TCP/8080-poging met shelltypefout.](13-211736-M04-C2.png) |
| 21:21:39 | — | [Lenovo PowerShell vergelijkt directe TCP/8080-toegang tot PLC01 met toegang via het pfSense-portforward.](14-212139-M04-C2.png) |
| 21:23:49 | — | [OpenPLC-dashboard van de M04-motorsimulatie met runtimelog en luisterpoorten.](15-212349-M04-C2.png) |
| 21:25:29 | — | [OpenPLC-dashboard van de M04-motorsimulatie met runtimelog en luisterpoorten.](16-212529-M04-C2.png) |
| 21:36:39 | F16 | [PLC01-terminal met herhaalde route- en TCP/8080-probes richting MGMT.](17-213639-M04-C2.png) |
| 21:39:23 | F16 | [PLC01-terminal met TCP/8080-probe richting MGMT en zichtbare exitcode.](18-213923-M04-C2.png) |
| 21:40:37 | F16 | [PLC01-terminal met herhaalde TCP/8080-probes richting MGMT en controle van de OpenPLC-service.](19-214037-M04-C2.png) |
| 21:42:59 | F16 | [pfSense OT-log gefilterd op TCP/8080 met standaardblokkades richting MGMT.](20-214259-M04-C2.png) |
| 21:55:40 | F17 | [FUXA01-terminal met routecontrole ter voorbereiding op de TCP/443-probe richting MGMT.](21-215540-M04-C2.png) |
| 22:02:25 | F17 | [pfSense OT-logfilter voor TCP/443 met nul overeenkomende regels in deze opname.](22-220225-M04-C2.png) |
| 22:03:40 | F17 | [FUXA01-terminal met route en eerste TCP/443-pogingen met shellsyntaxisfout.](23-220340-M04-C2.png) |
| 22:05:15 | F17 | [FUXA01-terminal met HTTPS-probe richting pfSense MGMT op TCP/443 en de weergegeven time-out.](24-220515-M04-C2.png) |
| 22:06:17 | F17 | [pfSense OT-log met TCP/443-regels voor de FUXA01-probe richting pfSense MGMT.](25-220617-M04-C2.png) |
| 22:08:14 | F18 | [PLC01-terminal met TCP/22-probe richting pfSense OT en de weergegeven time-out.](26-220814-M04-C2.png) |
| 22:09:59 | F18 | [pfSense OT-log met TCP/22-regels voor de PLC01-probe richting pfSense OT.](27-220959-M04-C2.png) |
| 22:12:11 | F19 | [PLC01-terminal met HTTP-probe naar een externe bestemming op TCP/80.](28-221211-M04-C2.png) |
| 22:13:08 | F19 | [pfSense OT-log met TCP/80-regels bij de externe HTTP-probe.](29-221308-M04-C2.png) |
| 22:15:28 | F20 | [PLC01-terminal met externe DNS-query op UDP/53 en de weergegeven time-out.](30-221528-M04-C2.png) |
| 22:18:08 | F20 | [pfSense OT-log met de UDP/53-regel bij de externe DNS-query.](31-221808-M04-C2.png) |
| 22:29:11 | F21 | [FUXA01-terminal met routecontrole en probe naar een externe NTP-bestemming op UDP/123.](32-222911-M04-C2.png) |
| 22:36:46 | F21 | [pfSense OT-log met UDP/123-regels bij de externe NTP-probe.](33-223646-M04-C2.png) |
| 22:41:23 | F23 | [FUXA01-terminal met IPv6-adressen en routes op de interfaces. Ondersteunende configuratiecontrole.](34-224123-M04-C2.png) |
| 22:41:41 | F22 | [PLC01-terminal met IPv6-adressen en routes op de OT-interface. Ondersteunende configuratiecontrole.](35-224141-M04-C2.png) |
| 22:43:31 | F22, F23 | [pfSense-interfaceoverzicht met IPv6-link-local-adressen. Ondersteunende configuratiecontrole.](36-224331-M04-C2.png) |
| 22:47:48 | F23 | [Lenovo PowerShell met IPv6-adressen en IPv6-routes voor VMware- en hostinterfaces. Ondersteunende configuratiecontrole.](37-224748-M04-C2.png) |
| 22:50:13 | F23 | [Lenovo PowerShell met IPv6-routes en een gerichte controle op de IPv6-default route. Ondersteunende configuratiecontrole.](38-225013-M04-C2.png) |
| 22:54:28 | F22 | [CLIENT01 PowerShell met inventarisatie van IPv6-adressen en routes. Ondersteunende configuratiecontrole.](39-225428-M04-C2.png) |
| 22:56:24 | F22 | [CLIENT01 PowerShell met IPv6-routegegevens en controle van de default gateway. Ondersteunende configuratiecontrole.](40-225624-M04-C2.png) |
| 23:00:05 | — | [VMware-instellingen van een OT-VM met de netwerkadapter op het geïsoleerde OT LAN Segment.](41-230005-M04-C2.png) |
| 23:02:06 | — | [VMware-instellingen van een OT-VM met de netwerkadapter op het geïsoleerde OT LAN Segment.](42-230206-M04-C2.png) |
| 23:03:12 | — | [VMware-instellingen van de Windows-test-VM met de netwerkadapter op het geïsoleerde LAB LAN Segment.](43-230312-M04-C2.png) |
| 23:09:49 | — | [VMware-instellingen van pfSense met adapter 3 op het geïsoleerde LAB LAN Segment.](44-230949-M04-C2.png) |
| 23:10:03 | — | [VMware-instellingen van pfSense met adapter 4 op het geïsoleerde OT LAN Segment.](45-231003-M04-C2.png) |
| 23:12:21 | — | [pfSense WAN-regeloverzicht met bogon-blokkade en het overzicht van gebruikersregels.](46-231221-M04-C2.png) |
| 23:16:38 | — | [pfSense IPv4-portforwards vanaf MGMT naar de webinterfaces van FUXA01 en PLC01.](47-231638-M04-C2.png) |
| 23:21:37 | — | [pfSense LAN-regeloverzicht met expliciete MGMT-toegang, OT-blokkade en LAN-defaultregels.](48-232137-M04-C2.png) |
| 23:22:26 | — | [pfSense NAT-overzicht met MGMT-portforwards voor FUXA01 en PLC01.](49-232226-M04-C2.png) |
| 23:23:40 | — | [pfSense IPv4- en IPv6-routetabellen.](50-232340-M04-C2.png) |
| 23:25:54 | — | [pfSense IP-aliasoverzicht met de RFC1918-netwerkgroep.](51-232554-M04-C2.png) |
| 23:27:29 | — | [pfSense-editor voor de IPv4-regel M04 LAN → OT default deny.](52-232729-M04-C2.png) |
