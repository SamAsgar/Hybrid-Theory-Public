# Architectuur | Hybrid-Theory

Deze map beschrijft de **gerealiseerde technische basis** en de **beoogde hybride doelarchitectuur**. Niet alle componenten of verbindingen uit het ontwerp zijn geïmplementeerd of gevalideerd.

## 1. Secure Hybrid Enterprise Network — doelarchitectuur

Conceptueel doelontwerp van VMware, pfSense, Windows Server/Client, Ubuntu, GNS3 en toekomstige Azure- en IT/OT-zones. Aanvullende VLAN's, 3 × 25 VPCS en toekomstige cloudverbindingen zijn **PLANNED**, tenzij afzonderlijk getest. Verwijderde conceptdiagrammen worden hier niet als aanwezig voorgesteld.

## 2. CAT/ACE v0.2 — onderzoeksreferentie

Het [onderzoeksmodel](../governance/CAT_ACE_v0.2.md) gebruikt **CAT**: Corporate Governance & Compliance, Accountability & Management, Technology & Operations. **ACE** staat voor Automation, Compliance & Efficiency. Genoemde kaders zoals NIST, CIS en ISO/IEC 27001 dienen als mogelijke onderzoeksreferenties; dit bewijst geen compliance.

**Onderzoeksstatus:** CAT/ACE v0.2 is **CONCEPT / NOT VALIDATED**. De afzonderlijke fysieke Linux-server is **PLANNED**; de actuele voortgang staat in de [roadmap](../projectlogboeken/ROADMAP.md).

## 3. Tekstuele architectuurdocumentatie

- [Architectuurbaseline](ARCHITECTUUR_BASELINE.md)
- [Netwerkmodel en trust boundaries](NETWERKONTWERP.md)
- [pfSense implementatiegrenzen](PFSENSE_PLAN.md)
- [Linux en Cockpit](LINUX_COCKPIT_SERVICE.md)
- [Azure free-first doelontwerp](VOORBEELDMODEL-HYBRIDE-TOPOLOGIE-AZURE-GRATIS.md)

**Operationeel op componentniveau:** VMware-host, Ubuntu, pfSense, GNS3, Windows Server en Windows 11. **Gericht geverifieerd:** AD-forest, DNS/SRV, domain join, testlogin en één GPO. **Gepland:** tweede fysieke Linux-host, Azure/Arc, aanvullende subnetten en OT-labs. Volledige netwerkisolatie en onafhankelijke disaster recovery zijn nog niet aangetoond.

**GitHub-zichtbaarheid (laatst gecontroleerd 02-11-2026): PRIVATE; eerder PUBLIC.** De publicatiereview blijft **OPEN**: historische bytes, beeldredactie en alle publicatiegates zijn niet volledig gecontroleerd. Dit is **geen publicatie-PASS**. Zie [publicatiebeleid](../governance/PUBLICATIEBELEID.md) en [migratiestatus](../MIGRATIE_STATUS.md).
