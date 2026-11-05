# Architectuur | Hybrid-Theory

Deze map beschrijft de **gerealiseerde technische basis** en de **beoogde hybride doelarchitectuur**. Niet alle componenten of verbindingen uit het ontwerp zijn geïmplementeerd of gevalideerd.

## 1. Secure Hybrid Enterprise Network — doelarchitectuur

Conceptueel doelontwerp van VMware, pfSense, Windows Server/Client, Ubuntu, GNS3 en toekomstige Azure- en IT/OT-zones. Aanvullende VLAN's, 3 × 25 VPCS en toekomstige cloudverbindingen zijn **PLANNED**, tenzij afzonderlijk getest. Verwijderde conceptdiagrammen worden hier niet als aanwezig voorgesteld.

## 2. CAT/ACE v0.4 — actuele onderzoeksreferentie

Het [CAT/ACE v0.4-onderzoeksmodel](../governance/CAT_ACE_v0.4.md) gebruikt **CAT** voor Corporate Governance & Compliance (toepasselijke eisen), Accountability & Management (eigenaarschap/besluiten) en Technology & Operations (feitelijke controls en afhankelijkheden). **ACE = Audit, Cost & Efficiency** is een **interne, externe of hybride beoordelingsfunctie**: controleer controlwerking en bewijs, onderzoek de werkelijke of geraamde kosten, vergelijk veilige optimalisaties en **hervalideer na wijzigingen**. CAT-C definieert de eis; ACE-Audit toetst haar, zonder dubbele compliance-PASS. Automatisering ondersteunt herhaalbare tests, maar is geen afzonderlijke ACE-letter.

**Onderzoeksstatus:** CAT/ACE v0.4 blijft **CONCEPT / NOT VALIDATED**, zonder formele audit- of complianceverklaring. De afzonderlijke fysieke Linux-server is **PLANNED**; de actuele voortgang staat in de [roadmap](../projectlogboeken/ROADMAP.md).

## 3. Tekstuele architectuurdocumentatie

- [Architectuurbaseline](ARCHITECTUUR_BASELINE.md)
- [Netwerkmodel en trust boundaries](NETWERKONTWERP.md)
- [pfSense implementatiegrenzen](PFSENSE_PLAN.md)
- [Linux en Cockpit](LINUX_COCKPIT_SERVICE.md)
- [Azure free-first doelontwerp](VOORBEELDMODEL-HYBRIDE-TOPOLOGIE-AZURE-GRATIS.md)

**Operationeel op componentniveau:** VMware-host, Ubuntu, pfSense, GNS3, Windows Server en Windows 11. **Gericht geverifieerd:** AD-forest, DNS/SRV, domain join, testlogin en één GPO. **Gepland:** tweede fysieke Linux-host, Azure/Arc, aanvullende subnetten en OT-labs. Volledige netwerkisolatie en onafhankelijke disaster recovery zijn nog niet aangetoond.

**GitHub-zichtbaarheid: PUBLIC** (gecontroleerd 05-11-2026). De publicatiereview blijft **OPEN**: historische bytes, beeldredactie en alle publicatiegates zijn niet volledig gecontroleerd. Dit is **geen publicatie-PASS**. Zie [publicatiebeleid](../governance/PUBLICATIEBELEID.md).
