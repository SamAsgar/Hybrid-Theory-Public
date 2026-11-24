# Projectlogboek | 4 november 2026

**Project:** Hybrid-Theory · Secure Hybrid Enterprise Network  
**Type sessie:** architectuuronderzoek, dreigingsmodellering en ontwerpafwegingen  
**Methodiek:** CAT/ACE v0.4  
**Uitvoeringsstatus:** **RESEARCH / DESIGN ONLY — geen technische labuitvoering**

> **Afbakening:** Op deze datum zijn geen nieuwe VM-installaties, configuratiewijzigingen, operationele back-ups, restores, aanvalssimulaties of validatietests uitgevoerd. Ontwerpkeuzes en AI-beoordelingen zijn geen technisch bewijs.

## Nieuw ten opzichte van de bestaande publieke logboeken

De eerdere logboeken beschrijven onder andere de inrichting en gerichte tests van VMware, pfSense, Windows/AD, Linux en GNS3. Dit verslag **herhaalt die resultaten niet** en registreert uitsluitend de nieuwe onderzoeks- en architectuurinzichten van 4 november.

| Onderwerp | Nieuwe uitkomst op ontwerp- of onderzoeksniveau | Status |
|---|---|---|
| **M02 Phoenix Recovery v0.5.1** | **Architectuur B geselecteerd:** een afzonderlijke fysieke herstelserver voor lokale, versleutelde Restic-back-ups en een **rechtstreekse** tweede route vanaf de primaire host naar Backblaze B2. De offsite route mag niet van de herstelserver afhangen. | **Ontwerpbesluit; implementatie en technische validatie PENDING** |
| **Beveiliging van herstelpunten** | Scheiding van gewone back-up-, onderhouds- en herstelrechten; append-only opslag, cloud Object Lock, retentie, versieherstel en een onafhankelijke herstelprocedure als onderzoekspunten. | **Niet technisch getest** |
| **Private cloud** | Onderzoeksvergelijking van een zelfstandige Linux-server, externe opslag en NAS-/routeropslag. Belangrijkste criteria: onafhankelijkheid, beschikbaarheid, toegangsbeheer, beheerlast en herstelbaarheid. | **Opties verkend; geen nieuwe dienst ingericht** |
| **Hybride beheer en Azure Arc** | Beheer- en cloudexperimenten gescheiden houden van de herstelserver; een bestaande Linux-labomgeving is het voorgestelde vertrekpunt. Cloudbeheer mag geen noodzakelijke herstelafhankelijkheid worden. | **Concept; niet uitgerold** |
| **Ransomware- en cloudopslagonderzoek** | Restic/Backblaze B2 vergeleken met onder meer Storj en andere opslag- of recoverymodellen op onveranderbaarheid, toegangsrechten, afhankelijkheden, herstel en kosten. **Object Lock voorkomt geen gegevensdiefstal vanaf een gecompromitteerd endpoint.** | **Dreigingsmodel en alternatieven; geen aankoop of migratie** |
| **Gecombineerde HR/IT/OT-scenario's** | Nieuwe testideeën rond identiteit, foutieve rechten, DNS/DHCP/GPO, netwerkisolatie, monitoring, OT-koppelingen en cascadefouten. Focus blijft op circa **30 relevante labs** binnen het beschikbare geheugenbudget. | **Scenario-ontwerp; geen fault injection uitgevoerd** |

## Beoordelingskader

De besproken ontwerpen worden later via **CAT/ACE v0.4** onderzocht op governance en verantwoordelijkheid, technische afhankelijkheden, aantoonbare controlwerking, kosten en efficiëntie. Voor recovery horen daarbij zowel positieve restores als negatieve tests voor toegangsrechten, verwijdering en storingen.

**Onderzoeksgrens:** een AI-ontwerpbeoordeling is geen onafhankelijke audit. Het herstelontwerp is **niet** gevalideerd als ransomwarebestendig, onafhankelijk herstelbaar of ISO-conform. Kostenvergelijkingen zijn onderzoeksindicaties, geen gemeten projectuitgaven.

## Conclusie en overdracht

**Nieuw op 4 november:** een expliciete scheiding tussen lokale recovery en cloudbeheer, een tweesporen-back-uparchitectuur, aangescherpte herstel- en ransomware-dreigingsmodellen en kandidaat-scenario's voor toekomstige CAT/ACE-proeven.

**Niet gewijzigd:** de eerder gedocumenteerde technische labstatus en testverdicts. **M02 blijft PENDING** totdat daadwerkelijke back-ups en onafhankelijke hersteltests met bewijs zijn uitgevoerd.

Voor achtergrond en eerdere technische resultaten: [projectlogboeken](README.md), [projectroadmap](ROADMAP.md) en [CAT/ACE v0.4](../governance/CAT_ACE_v0.4.md).

*Publieke, geabstraheerde onderzoeksnotitie. Geen operationele identificatoren, herstelgeheimen of privé-bronlinks opgenomen.*
