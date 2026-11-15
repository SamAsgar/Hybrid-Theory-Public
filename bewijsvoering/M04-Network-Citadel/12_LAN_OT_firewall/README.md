# 12 LAN OT firewall

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 19 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-157` | 08-11-2026 18:54:23 | **CONFIG** | AC07 LAN | LAN-regels VOOR M04: Default allow LAN to any (IPv4/IPv6) + NAT-regel Wazuh-dashboard. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-161` | 08-11-2026 20:42:35 | **CONFIG** | AC07 LAN->OT | Nieuwe LAN-regel: Block, beschrijving 'M04 LAN -> OT default deny'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-162` | 08-11-2026 20:45:25 | **CONFIG** | AC07 LAN->OT | LAN-regellijst direct na toevoegen van de blokregel (positie t.o.v. de default allow in deze opname niet gecontroleerd; eindvolgorde zie 2026-11-09 170520). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-163` | 08-11-2026 20:51:32 | **TEST** | AC07 LAN->OT | Status / Filter Reload: regels geladen, 'Done'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-168` | 08-11-2026 21:46:10 | **CONFIG** | AC07 LAN | LAN-regels: 'NAT M04 MGMT -> PLC01 web' toegevoegd. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-169` | 08-11-2026 21:51:19 | **CONFIG** | AC07 LAN | LAN-regels na Apply. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-171` | 08-11-2026 22:08:43 | **CONFIG** | AC07 | pfctl -sr: default deny IPv4 in/out ([RULE_ID_REDACTED]/104). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-172` | 08-11-2026 22:13:02 | **CONFIG** | AC07 | pfctl -sr: anti-lockout en Client01 DNS-regels. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-173` | 08-11-2026 22:13:09 | **CONFIG** | AC07 | pfctl -sr (einde): TEMP Client01 outbound internet ([RULE_ID_REDACTED]) nog actief. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-174` | 08-11-2026 22:16:03 | **CONFIG** | NAT PLC01 | Regeldetails: [RULE_ID_REDACTED], 'Created 11/8/26 21:39:48 by NAT Port Forward'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-175` | 08-11-2026 22:26:52 | **CONFIG** | AC07 LAN | Zelfstandige passregel 'M04 MGMT PLC01 explicit allow'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-176` | 08-11-2026 22:29:15 | **CONFIG** | NAT PLC01 | Filter rule association omgezet naar 'None'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-177` | 08-11-2026 22:29:54 | **CONFIG** | NAT PLC01 | Port Forward / Edit: association None, aangemaakt 11/8/26 21:39:48. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-178` | 08-11-2026 22:45:47 | **TEST** | AC07 LAN->OT | pfctl -sr: 'block drop in log quick on em0 from <LAN__NETWORK> to [OT_SUBNET]' (M04 LAN -> OT default deny, id 1794167081) geladen. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-180` | 08-11-2026 23:02:17 | **CONFIG** | AC07 LAN | Zelfstandige passregel 'M04 MGMT FUXA01 explicit allow' (FUXA01 staat dan nog niet in OT). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-181` | 08-11-2026 23:03:37 | **CONFIG** | AC07 LAN | LAN-regellijst na toevoegen FUXA-regel. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-182` | 08-11-2026 23:08:54 | **TEST** | AC07 LAN | pfctl -sr: FUXA01 allow, PLC01 explicit allow ([RULE_ID_REDACTED]), daarna LAN -> OT default deny - volgorde geladen. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-207` | 09-11-2026 17:05:20 | **CONFIG** | AC07 LAN | LAN-regels 9 nov (visueel bevestigd), volgorde: Anti-Lockout; M04 MGMT FUXA01 allow (MGMT_CLIENT_IP -> FUXA01_OT_IP:1881); M04 MGMT PLC01 allow (-> PLC01_OT_IP:8080); M04 LAN -> OT default deny (LAN subnets -> [OT_SUBNET]); Default allow LAN IPv4/IPv6; NAT Wazuh. Alle tellers 0/0 B. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-208` | 09-11-2026 17:05:39 | **CONFIG** | AC07 OT / SSOT-M04-005 | OT-regels 9 nov 17:05: 'M04 TEMP PLC01 to OT gateway ICMP' staat er nog, grijs weergegeven met inschakel-icoon = uitgeschakeld (visueel bevestigd). Toont de configuratiestand, geen hertest. | Nog niet gepubliceerd (review vereist) |
