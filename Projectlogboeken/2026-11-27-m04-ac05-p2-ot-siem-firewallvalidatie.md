# M04 Network Citadel | AC05 — gecontroleerde OT→SIEM-firewallverbinding | 27 november 2026

**Publicatie:** gesaneerde technische voortgang, afgeleid van het private M04-AC05/P2-uitvoeringslog en de bijbehorende private harmonisatie-impactmatrix. **Geen** originele screenshots, ruwe logs, private netwerkidentificatoren of configuratie-extracten.  
**Status:** **P2 TESTED / scoped PASS** voor vier specifiek geteste IPv4 TCP-stromen. **AC05 integraal PENDING**; geen onafhankelijke acceptatie of algemene segmentatiegarantie.

## Doel

Na de eerder uitgevoerde vaste adresreservering voor de Wazuh-SIEM moest de geïsoleerde OT-omgeving slechts één noodzakelijke verbinding naar de beveiligingsmonitoring krijgen. Andere beheer- en registratiepoorten zouden niet bereikbaar mogen worden. De firewall moet die keuze **niet alleen configureren, maar ook aantoonbaar handhaven**.

## Uitvoering

1. De bestaande OT-regels zijn geïnspecteerd. Er was nog geen specifieke HMI→SIEM-regel. Een tijdelijke historische ICMP-testregel is ongemoeid gelaten.
2. In pfSense is één **bron- en bestemmingsspecifieke IPv4 TCP PASS-regel** op de OT-interface aangemaakt met logging, voor de HMI-host richting de Wazuh-agentcommunicatiepoort **TCP/1514**. Geen algemene OT→LAB-regel, geen OT-internetuitzondering en geen wijziging aan de bestaande dashboardforward.
3. Vanaf de OT-HMI is TCP-connectiviteit getest. De verbinding op **TCP/1514** slaagde.
4. Vanaf dezelfde OT-bron zijn drie aanvullende TCP-tests uitgevoerd naar **1515** (agent-enrollment), **443** (dashboard) en **55000** (API). Alle drie leverden timeouts op.
5. De bijbehorende pfSense-filterlogs op de **OT-interface** zijn gecontroleerd. Ze tonen voor de geteste positieve verbinding een **PASS** op de specifieke regel en voor elk van de drie negatieve tests **BLOCK** op de standaard IPv4-default-deny-regel. Per negatieve test zijn drie SYN-blokkeringen teruggevonden.

## Testresultaten en bewijsgrenzen

| Test | Clientresultaat | Firewallresultaat | Verdict binnen scope |
|---|---|---|---|
| OT-HMI → SIEM TCP/1514 | TCP-verbinding geslaagd | Specifieke PASS-regel | **TESTED / scoped PASS** |
| OT-HMI → SIEM TCP/1515 | Timeout | Default-deny BLOCK, 3 SYN-events | **TESTED / scoped PASS** |
| OT-HMI → SIEM TCP/443 | Timeout | Default-deny BLOCK, 3 SYN-events | **TESTED / scoped PASS** |
| OT-HMI → SIEM TCP/55000 | Timeout | Default-deny BLOCK, 3 SYN-events | **TESTED / scoped PASS** |

**Waarom de firewalllogs belangrijk zijn:** een timeout op zichzelf bewijst niet dat een firewall iets heeft tegengehouden. De combinatie van een clientprobe en een bijpassend blokevent op de OT-interface maakt het resultaat controleerbaar voor de geteste bron, bestemming, poort en sessie.

**Niet aangetoond:** agentinstallatie, cryptografisch geauthenticeerde agentcommunicatie, Wazuh-eventingestie, FIM-alerts in het dashboard, blokkering van elk denkbaar netwerkpad of protocol (waaronder IPv6), en de integrale AC05-, AC04- of AC07-acceptatie.

## Bewijs en resterende werkzaamheden

De oorspronkelijke beelden van configuratie, CLI-tests en filterlogs zijn in een **lokaal privéarchief** met tekstbeschrijvingen opgeslagen. Ze zijn **niet** als ruwe bestanden naar Public geëxporteerd of formeel als repository-evidence geverifieerd. Daarom blijft de status **TESTED / scoped PASS** op basis van de gerapporteerde, gecorreleerde sessietests.

De volgende fase controleert eerst op de Wazuh-manager welke agents al geregistreerd zijn. Daarna volgen de eerder gekozen **handmatige sleutelregistratie zonder TCP/1515-openstelling**, een **offline agentinstallatie**, de controle van de agentverbinding en een end-to-end **File Integrity Monitoring**-test. De verouderde dashboardforward en openstaande CORE-acceptatiepunten blijven afzonderlijke aandachtspunten.

**Handover:** P2 afgerond; agentregistratie en -installatie nog niet uitgevoerd. **AC05 PENDING.**

[Voorgaande AC05-delta (SIEM-gezondheid en vast adres)](2026-11-27-m04-ac05-wazuh-health-en-vast-adres.md) · [M04 actuele issue](https://github.com/SamAsgar/Hybrid-Theory-Public/issues/45)

**Publicatiegrens:** geen echte IP-/MAC-/IPv6-adressen, interne hostnamen, gebruikersnamen, ruwe firewallregels, log-ID's, private archiefhashes, back-uppaden of secrets.

**Bewijs bij de review.** [PART2 · 13 tekstbestanden, waaronder negen bewijsbeschrijvingen](../Portfolio/M04-Network-Citadel/M04-Bewijsvoering/AC05-PART2/M04-AC05-PART2-PUBLIC-EVIDENCE-20261127.zip). De bestandsintegriteit is gecontroleerd. De inhoudelijke beoordeling staat open.
