# Technische bewijsvoering | Hybrid-Theory

Deze index leidt naar missiegebonden bewijs, componentinventarissen en de statusgrenzen. Bewijsbestanden tonen uitsluitend de daarin beschreven observaties; ze bewijzen op zichzelf geen missieafronding.

## Missie-index

| Missie | Bewijs en navigatie | Huidige status |
|---|---|---|
| **M01 — Hypervisor Fortress** | **82 gesaneerde screenshots.** [Missie-overzicht](M01-Hypervisor-Fortress/README.md) · [Bewijsindex](M01-Hypervisor-Fortress/EVIDENCE-INDEX.md) · [Saneringsrapport](M01-Hypervisor-Fortress/M01-SANITIZATION-REPORT.md) | **IN PROGRESS**; geen volledige M01-PASS. |
| **M02 — Phoenix Recovery** | [Bewijslocatie](M02-Phoenix-Recovery/) · [Herstelarchitectuur en status](../governance/M02-Phoenix-Recovery/README.md) | **PENDING**; onafhankelijke off-host restore niet aangetoond. |
| **M03 — Identity Dominion** | [Bewijslocatie](M03-Identity-Dominion/) · [AD/DNS-baselinerapport](../projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) | **IN PROGRESS**; bestaande AD/DNS-tests gelden alleen binnen hun beschreven scope. |
| **M04 — Network Citadel** | **265 gesaneerde screenshots in 20 fasen.** [Missie-overzicht](M04-Network-Citadel/README.md) · [Bewijsindex](M04-Network-Citadel/M04-EVIDENCE-INDEX.md) · [Galerij per fase](M04-Network-Citadel/M04-GALERIJ.md) · [Gaps](M04-Network-Citadel/M04-GAPS.md) · [Saneringsrapport](M04-Network-Citadel/M04-SANITIZATION-REPORT.md) | **M04-CORE IN PROGRESS**; AC04/AC07 integraal **PENDING**; 19 november scoped deeltests toegevoegd. |
| **M05 — Compliance Sentinel** | [Bewijslocatie](M05-Compliance-Sentinel/) · [Regelgevings- en assurancekaders](../governance/WET_EN_REGELGEVING.md) | **PENDING**; geen afgeronde assurance-acceptatie. |

M02, M03 en M05 hebben momenteel geen missiegebonden screenshotsets in hun publicatiemappen. Een lege map of een componentbewijs elders in de repository verandert de missiestatus niet.

## Componentdocumentatie

Herbruikbare VMware- en platforminventarissen staan apart van de missie-indexen:

- [VMware-bewijsindex en inventaris](VMware/README.md)
- [Windows 11 Client](<VMware/Windows%2011%20Client/>)
- [Windows Server 2025](<VMware/Windows%20Server%202025/>)
- [pfSense](VMware/pfSense/)
- [Ubuntu / Cockpit](VMware/Linux/)
- [GNS3 / Wireshark](VMware/GNS3/)
- [FUXA](VMware/FUXA/)
- [OpenPLC Runtime](VMware/OpenPLC/)

Oudere componentbeelden hebben eigen bewijsgrenzen en mogelijk nog openstaande privacy-/publicatiereview; raadpleeg de bijbehorende documentatie. Zie ook het [AD-baselinerapport](../projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md).

## Status en bewijsgrenzen

De [statuslegenda](../governance/STATUSLEGENDA.md) is leidend:

- **IMPLEMENTED:** component of instelling ingericht; geen automatisch bewijs van werking.
- **TESTED:** een specifieke test is uitgevoerd binnen de gerapporteerde scope.
- **VERIFIED:** een componentfunctie is met bewijs binnen een vastgelegde scope gecontroleerd.
- **PASS:** acceptatiecriteria gehaald binnen de expliciete testscope.
- **EXCEPTION:** bewust geaccepteerd restrisico, geen automatische PASS.
- **PENDING:** uitvoering, besluit of meting staat nog open.

Een configuratiebeeld kan inrichting aantonen, maar geen end-to-end werking. Lees per bewijsindex ook de beperkingen, gaps en saneringsrapporten. Originele screenshots en de koppeling tussen netwerkaliassen en werkelijke waarden blijven buiten deze publieke repository.
