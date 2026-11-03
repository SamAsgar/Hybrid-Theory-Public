# Azure free-first | Conceptueel hybride doelontwerp

**Type:** ontwerpvoorstel / **PLANNED**, niet gedeployed.  
**Onderzoekskader:** [CAT/ACE v0.4](../governance/CAT_ACE_v0.4.md) — **Audit / Cost / Efficiency**, intern, extern of hybride; **NOT VALIDATED**. Voor Azure is Cost relevant om onverwachte verbruikskosten te voorkomen; dit doelontwerp is nog niet uitgerold.

## Doel

Een bestaande VMware/pfSense/Windows/Ubuntu-labomgeving gebruiken als on-premises zijde van een toekomstige hybride Azure-opstelling. Het onderzoek richt zich op cloudidentiteit, policies, netwerk- en afhankelijkheidsanalyse zonder onverwachte kosten.

| Onderdeel | Voorstel | Werkelijke status |
|---|---|---|
| On-premises virtualisatie | VMware met Windows Server, Windows 11, pfSense, Ubuntu en GNS3 | **IMPLEMENTED** voor basiscomponenten |
| Azure Arc | **Domain Controller als eerste beoogde onboardingserver**, afhankelijk van geschiktheid en kosten | **PLANNED** |
| Azure VNet / NSG | Lege netwerken en regels voor cloudontwerp leren | **PLANNED** |
| Azure identity | Microsoft Entra ID als toekomstig cloudidentiteitscomponent | **PLANNED** |
| Azure VMs / VPN Gateway / Firewall / storage | Alleen na afzonderlijke kosten- en veiligheidsreview | **PLANNED**; niet geautoriseerd of geïmplementeerd in het €0-ontwerp |
| Afzonderlijke Linux-back-uphost | Een onafhankelijke fysieke host voor herstelbaarheid | **PLANNED** |
| IT/OT-gesegmenteerd netwerk | Toekomstige geïsoleerde simulatie | **PLANNED** |

## IP-plan

Er is **geen live subnet- of VLAN-lijst gepubliceerd**. Alle voorgestelde client-, server-, beheer- en OT-zones moeten vóór implementatie worden getoetst aan de bestaande LAB-adresruimte en een goedgekeurd conflictvrij ontwerp. Bestaande netwerkadressen uit de private bron zijn geen fictieve voorbeelden.

## Kosten en compliance

Een Azure budget alert is **geen harde uitgavenlimiet**. Free-tier-geschiktheid verschilt per resource, regio, tijd en abonnement; geen API-aanroep of VM-deployment zonder toestemming. Compliance volgt de daadwerkelijk toepasselijke kaders en controles, niet een illustratief diagram.

**Resultaat:** dit is een **target architecture**, zonder claim dat cloud, routeverkoppelingen of OT-security operationeel zijn. 
