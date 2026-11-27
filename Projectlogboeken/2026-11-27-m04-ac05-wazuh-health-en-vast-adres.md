# M04 Network Citadel | AC05 — SIEM-gezondheid en vast SIEM-adres | 26–27 november 2026

**M04-EXT · AC05 PENDING.** Dit is een gesaneerde voortgangsdelta, geen onafhankelijke audit of acceptatie. Er staan geen werkelijke IP- of MAC-adressen, hostnamen of credentialdetails in.

## Doel

AC05 vraagt of de SIEM (Wazuh) security-events uit de OT-zone kan ontvangen, verwerken en tonen. Deze sessie bereidde dat voor zonder de scheiding tussen IT en OT te verzwakken. Op één goedgekeurde wijziging na was alles alleen lezen.

## Wat is vastgesteld

**Netwerkidentiteit.** De SIEM staat in het LAB-segment achter pfSense. Het adres kwam uit een dynamische DHCP-lease. Daardoor wees een bestaande, bronbeperkte beheerforward naar het dashboard niet meer naar de SIEM. Die forward is niet aangepast en blijft een open punt.

**Gezondheid (alleen lezen).** Manager, indexer, dashboard en logverzending naar de indexer waren actief. Er was ruim opslagruimte. Agentpoorten luisteren. Er is nog geen enkele agent geregistreerd. In de indexerlogs is een eerder incident teruggevonden: begin november liep de schijf vol en de indexer zette zijn indexen tijdelijk op alleen-lezen. Daarna is dat niet meer voorgekomen. **Uitkomst: PASS, alleen als observatie.** Dat de keten tot in het dashboard werkt, is nog niet aangetoond.

**OT-kant.** Het bedieningsscherm (FUXA) staat aantoonbaar in het geïsoleerde OT-segment en heeft nog geen SIEM-agent. Op de OT-interface van de firewall staat geen regel die verkeer naar de SIEM toestaat. Er zijn geen floating rules.

**Back-up vooraf.** Vóór de wijziging is een versleutelde export van de firewallconfiguratie buiten de VM bewaard en met een hash vastgelegd. Een restore is niet getest.

## Uitgevoerde wijziging: vast SIEM-adres (P1)

Na akkoord van de eigenaar kreeg de SIEM een vaste DHCP-reservering buiten de pool. Vooraf is gecontroleerd dat het adres vrij was. De SIEM haalde het nieuwe adres op zonder herstart. Daarna draaiden alle diensten nog, luisterden de agentpoorten, werkte de logverzending en antwoordde het dashboard. De firewall toonde de reservering en het nieuwe adres.

**Uitkomst: TESTED / scoped PASS** voor het vaste adres en het intact blijven van de diensten.

## Nog niet uitgevoerd

1. **P2:** één smalle firewallregel van het bedieningsscherm naar de agentpoort van de SIEM, met logging, plus positieve en negatieve tests. Geen algemene toegang van OT naar LAB en geen internet voor OT.
2. **G4:** een agent offline installeren en handmatig registreren, zonder de enrollmentpoort open te zetten.
3. **G5:** een gecontroleerde File Integrity Monitoring-test, aangetoond tot in het dashboard.
4. Los daarvan: een besluit over de verouderde dashboardforward.

Open bevindingen voor het risicoregister: hardening van beheerinterfaces en inloggegevens, de bijwerkfeed voor kwetsbaarheden die zijn bron niet kan bereiken, de audit-logging van de indexer en openstaande updates op het bedieningsscherm.

**AC05 PENDING · M04-CORE IN PROGRESS · AC04/AC07 integraal PENDING.**

[Vorige delta 21 november](2026-11-21-m04-core-management-segmentatie.md) · [M04 issue](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/45)

**Publicatiegrens:** geen werkelijke private IP-/MAC-adressen, hostidentificatoren, credentials of ruwe configuratie.
