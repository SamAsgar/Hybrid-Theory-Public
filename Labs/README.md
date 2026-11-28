# Labs | Technische bewijsvoering | Hybrid-Theory

Deze index leidt naar missiegebonden bewijs, componentinventarissen en de statusgrenzen. Bewijsbestanden tonen uitsluitend de daarin beschreven observaties; ze bewijzen op zichzelf geen behaalde milestone. M01–M05 zijn permanente Main Missions; geen missie heeft Milestone 01 bereikt ([statuslegenda §3a](../Governance/STATUSLEGENDA.md#3a-missie--milestone--en-mini-oefeningstatus-20-11-2026)).

## Onderzoeksrapporten (PDF) / Research reports

Voor een compacte presentatie, zie [Portfolio](../Portfolio/README.md).

Gesaneerde rapporten voor stakeholders en IT-professionals. Netwerkadressen in deze rapporten zijn fictieve documentatievoorbeelden.

| Casus | Nederlands | English |
|---|---|---|
| **M05-MINI-01 — IT/OT-netwerksegmentatie en risicobeheersing** | [Lees rapport (PDF)](M05-Compliance-Sentinel/C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/M05-MINI-01-Educatief-Afsluitdossier.pdf) | [Read report (PDF)](M05-Compliance-Sentinel/C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/M05-MINI-01-IT-OT-Network-Segmentation-EN.pdf) |

De rapporten beschrijven een fictieve bedrijfscasus, controlinterpretatie (ISO/IEC 27001:2022), technische bewijsgrenzen en managementaanbevelingen. Het formele assessment en de eigenaarreview blijven PENDING; de rapporten vormen geen onafhankelijke audit of certificering. [Casusdossier](M05-Compliance-Sentinel/C04_Network_Segmentation_OT/M05-MINI-01_ISO27001_Control_Assessment/README.md).

## Missie-index

| Missie | Bewijs en navigatie | Huidige status |
|---|---|---|
| **M01 — Hypervisor Fortress** | **82 gesaneerde screenshots.** [Missie-overzicht](M01-Hypervisor-Fortress/README.md) · [Bewijsindex](M01-Hypervisor-Fortress/EVIDENCE-INDEX.md) · [Saneringsrapport](M01-Hypervisor-Fortress/M01-SANITIZATION-REPORT.md) | **IN PROGRESS**; geen volledige M01-PASS. |
| **M02 — Phoenix Recovery** | [Bewijslocatie](M02-Phoenix-Recovery/) · [Herstelarchitectuur en status](../Governance/M02-Phoenix-Recovery/README.md) | **PENDING**; onafhankelijke off-host restore niet aangetoond. |
| **M03 — Identity Dominion** | [Bewijslocatie](M03-Identity-Dominion/) · [AD/DNS-baselinerapport](../Projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md) | **IN PROGRESS**; bestaande AD/DNS-tests gelden alleen binnen hun beschreven scope. |
| **M04 — Network Citadel** | **354 gepubliceerde PNG's in 22 fasen (355 beeldregistraties, waarvan M04-EV-113 zonder publieke PNG)** [Missie-overzicht](M04-Network-Citadel/README.md) · [Bewijsindex](M04-Network-Citadel/M04-EVIDENCE-INDEX.md) · [Galerij per fase](M04-Network-Citadel/M04-GALERIJ.md) · [Gaps](M04-Network-Citadel/M04-GAPS.md) · [Saneringsrapport](M04-Network-Citadel/M04-SANITIZATION-REPORT.md) | **M04-CORE IN PROGRESS**; AC04/AC07 integraal **PENDING**; C2-deeltests vastgelegd op 20 november. |
| **M05 — Compliance Sentinel** | [Chapters](M05-Compliance-Sentinel/README.md#inhoudelijke-chapters) · [zeven onderzoeksvragen](M05-Compliance-Sentinel/README.md#methodiek-m05) · [mini-index](M05-Compliance-Sentinel/README.md#mini-exercise-index) · [Framework Register](M05-Compliance-Sentinel/README.md#6-framework-register) | Documentarchitectuur **OWNER APPROVED**. MINI-01 **IN PROGRESS**; formele assessmentacceptatie **PENDING**, M05-MS01 **NOT ACHIEVED**. |

M02, M03 en M05 hebben momenteel geen missiegebonden screenshotsets in hun publicatiemappen; de M05-map bevat methodiek, onderzoeksrapporten en een controlassessment in werkversie, geen formeel geaccepteerd assessment. Een lege map of een componentbewijs elders in de repository verandert de missiestatus niet.

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

Oudere componentbeelden hebben eigen bewijsgrenzen en mogelijk nog openstaande privacy-/publicatiereview; raadpleeg de bijbehorende documentatie. Zie ook het [AD-baselinerapport](../Projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md).

## Status en bewijsgrenzen

De [statuslegenda](../Governance/STATUSLEGENDA.md) is leidend:

- **IMPLEMENTED:** component of instelling ingericht; geen automatisch bewijs van werking.
- **TESTED:** een specifieke test is uitgevoerd binnen de gerapporteerde scope.
- **VERIFIED:** een componentfunctie is met bewijs binnen een vastgelegde scope gecontroleerd.
- **PASS:** acceptatiecriteria gehaald binnen de expliciete testscope.
- **EXCEPTION:** bewust geaccepteerd restrisico, geen automatische PASS.
- **PENDING:** uitvoering, besluit of meting staat nog open.

Een configuratiebeeld kan inrichting aantonen, maar geen end-to-end werking. Lees per bewijsindex ook de beperkingen, gaps en saneringsrapporten. Originele screenshots en de koppeling tussen netwerkaliassen en werkelijke waarden blijven buiten deze publieke repository.
