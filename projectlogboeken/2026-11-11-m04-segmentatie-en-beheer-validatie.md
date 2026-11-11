# M04 Network Citadel | Segmentatie, managementherstel en vervolgstappen — 11 november 2026

**Repository:** Hybrid-Theory-Public · beperkte portfolio-update  
**Bron:** begeleide labmetingen en screenshots van Sam; inhoud onafhankelijk opnieuw geformuleerd voor publicatie.  
**Documentstatus:** DRAFT / PENDING RELEASE REVIEW.  
**Status:** M04-CORE **IN PROGRESS**; geselecteerde deeltests **TESTED (PASS gerapporteerd)**, volledige M04-validatie **PENDING**.

## 1. Voortgang sinds 9 november

De OT-firewall en het geïsoleerde segment waren eerder ingericht en de PLC-server was gemigreerd. Tijdens de volgende sessies is ook de HMI-server naar het OT-segment verplaatst en van een statische netwerkconfiguratie voorzien. De HMI-container bleef actief; de lokale webservice en rechtstreekse bereikbaarheid vanuit de OT-firewall zijn gericht getest.

De beheertoegang naar zowel PLC als HMI is vervolgens vanaf de afzonderlijke managementhost als een **geslaagde TCP-deeltest** waargenomen. Voor de HMI was eerst troubleshooting en een gerichte correctie van een foutieve bronvoorwaarde in de bestaande portforward nodig. De PLC-toegang is daarna als regressie opnieuw getest.

## 2. Troubleshooting, fouten en diagnoses

| Onderwerp | Waargenomen probleem | Diagnose en aanpak |
|---|---|---|
| Windows-testclient zonder bruikbaar netwerk | Tijdens een eerste controle kreeg de virtuele client geen geldig DHCP-adres of gateway. | Sam stelde vast dat de firewall-VM tijdens die meting uitgeschakeld was. Na het starten van de infrastructuur had de client weer een geldig LAB-netwerkpad. Geen onnodige DHCP-aanpassing. |
| Verwarring tussen LAN en LAB | De naam van een virtueel VMware LAN-segment leek op de naam van een andere firewallinterface. | De werkelijke adapterkoppeling, bronzone, gateway en routing zijn afzonderlijk gecontroleerd. Een segmentnaam alleen bewijst geen interfacefunctie. |
| Afgewezen LAB→OT-verbinding | Een TCP-test mislukte zoals verwacht, maar alleen die foutmelding bewees nog geen firewallblokkering. | Verkeer op de LAB-ingang, de effectieve firewallregelvolgorde en een expliciet gelogde blockbeslissing zijn gecombineerd. Eén afgebakende negatieve segmentatietest werd daarmee onderbouwd. |
| Misleidende captureweergave | Een eerder getoond pakketoverzicht leek bij een andere interface te horen dan het bestandslabel aangaf. | Capturebron en bestandslabel opnieuw onderscheiden; geen conclusie over een bypass op basis van een mogelijk eerder opgeslagen capture. |
| Misleidende managementtests | Sommige tests werden vanaf de verkeerde netwerkadapter, met de verkeerde doelpoort of terwijl VM's uitgeschakeld waren uitgevoerd. Ook kwam een typefout in een opdracht voor. | Sam en ChatGPT hebben testbron, netwerkpad, servicepoort, VM-status en commando-invoer expliciet opnieuw gecontroleerd. Testopstellingsfouten zijn niet als firewallincident geregistreerd. |
| HMI-management eerst niet bereikbaar | De lokale HMI-service werkte en de firewall kon de HMI bereiken, maar de beheerclient kreeg geen TCP-verbinding. | De **actief geladen** NAT-configuratie werd vergeleken met het werkende PLC-managementpad. Een foutieve bronadresvoorwaarde werd vastgesteld, door Sam gecorrigeerd en opnieuw getest. |
| Configuratiepersistentie | Een statische HMI-netwerkconfiguratie was toegepast, maar niet opnieuw na een gecontroleerde reboot gevalideerd. | Blijft uitdrukkelijk open; geen premature PASS. |

## 3. Eigen inbreng van Sam

- Voerde de labhandelingen en herhaalde netwerk- en firewalltests zelf uit en controleerde resultaten met screenshots.
- Herkende dat de firewall tijdens een eerdere DHCP-/poortproef niet aanstond, zodat een verkeerde diagnose werd voorkomen.
- Stelde voor om de **Windows 11-test-VM voor securitysegmentatie** te gebruiken en de managementhost afzonderlijk te houden; dat maakt de bewijsvoering per zone zuiverder.
- Vroeg gericht naar routering, VLAN-/LAN-segmenten, verschil tussen LAB en beheer-LAN en de gekozen Windows-bronadapter.
- Vergeleek de positieve PLC-test met de mislukte HMI-test, corrigeerde de bronvoorwaarde van de HMI-portforward en bewees de werking met een nieuwe positieve test.
- Bewaakte dat een niet-bereikbare poort pas als security-PASS telt nadat de bedoelde filterbeslissing werkelijk is aangetoond.

## 4. Status bij deze tussenpublicatie

| Onderdeel | Scope en status |
|---|---|
| PLC op geïsoleerd OT-netwerk | **IMPLEMENTED**; geselecteerde managementdeeltests **TESTED PASS** |
| HMI op geïsoleerd OT-netwerk | **IMPLEMENTED**; statisch netwerk en lokale service **TESTED** |
| Management → PLC en management → HMI | **TESTED PASS**, TCP-bereik; volledige applicatielogin en beveiliging niet aangetoond |
| LAB → HMI, ongeautoriseerde TCP-toegang | **Gerichte negatieve deeltest PASS** met expliciete firewall-blockregistratie |
| HMI-netwerkconfiguratie persistent na reboot | **PENDING** |
| Functionele PLC/HMI-regressie en industriële communicatie | **PENDING** |
| AC04 volledige segmentatie | **PENDING** |
| AC07 volledige allow/deny-testmatrix | **PENDING** |
| Evidence-import, review en missieacceptatie | **PENDING** |
| **M04-CORE** | **IN PROGRESS**; geen volledige PASS |

De eerdere succesvolle PLC/HMI-functietests op een vorige topologie blijven historische resultaten; ze gelden **niet automatisch** als bewijs voor de nieuwe segmentatiearchitectuur.

## 5. Wat is nodig om M04 af te sluiten?

1. HMI-statische netwerkconfiguratie en dienstverlening na gecontroleerde reboot herbevestigen.
2. HMI-webfunctionaliteit via het geautoriseerde beheerpad en bijbehorende authenticatie binnen scope toetsen.
3. PLC-runtime, HMI-uitlezing en toegestane industriële commando's na de migratie opnieuw functioneel testen.
4. De resterende positieve en negatieve netwerkzone-/protocoltests uitvoeren en correlatie met firewallregels en captures vastleggen.
5. Tijdelijke uitzonderingen en restrisico's beoordelen en de technische documentatie en evidence consistent afronden.
6. Eigenaar-/securityreview uitvoeren op de formele acceptatiecriteria voor M04-CORE; aanvullende detectie-, schaal- en IDS-werkpakketten afzonderlijk scopen voor een eventuele volledige M04-closure.

Er is **geen betrouwbaar voltooiingspercentage** zolang de complete acceptatiematrix niet formeel is vastgesteld en afgetekend.

## 6. Publicatiegrens

Deze update publiceert **geen concrete IP-/MAC-adressen, hostnamen, interne segmentnamen, persoonlijke herstelpaden, netwerkexports, firewallconfiguratiedumps, credentials of private repositorylinks**. Ook de historische foutieve adreswaarde en exacte managementmapping blijven buiten Public.

Ruwe screenshots, pcaps, hashes en privélogboeken zijn niet overgenomen. Voordat deze draft-PR wordt gemerged, blijft een afzonderlijke review van de volledige publieke diff en publicatiegeschiedenis vereist. Een gefilterde TCP-deeltest is geen onafhankelijke penetratietest of certificeringsclaim.

**Redactie:** afgeleide gesanitiseerde sessieregistratie met door Sam uitgevoerde metingen; oorspronkelijke historische logs blijven intact.
