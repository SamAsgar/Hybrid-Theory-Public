# Technische bewijsvoering | Hybrid-Theory

**GitHub-zichtbaarheid: PUBLIC** (gecontroleerd 05-11-2026). **Telling 05-11-2026: 33 bewijs-PNG's.** De galerijen tonen de aanwezige bestanden. Sommige beelden bevatten nog herkenbare lokale paden of hostlabels: pixelredactie en volledige publicatiereview staan **OPEN**. Vier grote bewijs-PNG's ontbreken nog in deze repository.

| Bewijsmap | Aanwezig | Publicatie-/testgrens |
|---|---:|---|
| [Windows 11 Client](<Windows%2011%20Client/>) | **8** | Gesaneerde installatie-, activatie- en netwerkbewijzen |
| M01 · Lab 01 — Hypervisor Security & Virtualization Hardening | **0** | **Niet gepubliceerd** in deze repository; twee VM-settings-screenshots tonen nog lokale paden (pixelredactie OPEN) |
| [pfSense](pfSense/) | **6** | Dashboard met grote afbeelding ontbreekt nog; firewallbeelden zijn geen volledige isolatietest |
| [Windows Server 2025](<Windows%20Server%202025/>) | **5** | Oud eerste Server Manager-beeld heeft een automatisch hostlabel |
| [Ubuntu / Cockpit](Linux/) | **4** | Drie grote PNG's ontbreken nog; volledige beeldcontrole OPEN |
| [GNS3 / Wireshark](GNS3/) | **3** | Basistopologie en ARP/ICMP; aanvullende review voor publicatie |
| [VMware](VMware/) | **7** | Sommige beelden tonen delen van lokale installatiepaden; privacyreview OPEN |
| [FUXA](FUXA/) | **0** (verwijst naar VMware-opname 08) | Alleen hardware-inventaris; geen functioneel FUXA/PLC-bewijs |
| **Totaal** | **33 PNG's** | **PUBLIC; reviewgates OPEN** |

De eerder aanwezige architectuur-WebP's zijn verwijderd. De actuele [architectuurdocumentatie](../architectuur/README.md) is tekstueel.

## Evidence en status

- **Componentstatus:** `PLANNED / IMPLEMENTED / VERIFIED`.
- **Test- of reviewresultaat:** `PASS / REWORK / EXCEPTION` binnen de vastgelegde scope.
- **Lab 01 (M01): IN PROGRESS.** Deelcontrols PASS met één EXCEPTION, maar geen integrale labacceptatie.
- **Lab 02 (M02): PENDING.** Onafhankelijke off-host restore niet aangetoond.
- **AD/DNS/domain join/GPO:** zie het afzonderlijke [gesaneerde AD-baselinerapport](../projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md).

**GitHub-zichtbaarheid: PUBLIC** (gecontroleerd 05-11-2026). **Beeldredactie, secretscan en geschiedenisreview staan nog OPEN.** Screenshots zijn geen publicatie-PASS. Zie [goedgekeurd publicatiebeleid](../governance/PUBLICATIEBELEID.md) en [statuslegenda](../governance/STATUSLEGENDA.md).

## Aanvulling 4 november 2026 — FUXA VM-inventaris

Nieuwe **gesanitized VMware-hardwareopname** toegevoegd onder [VMware](VMware/08-FUXA-VMware-Inventory-Sanitized.png) en beschreven in de [VMware-bewijsindex](VMware/README.md). **2 GB RAM, 2 processors, 20 GB SCSI, Custom (VMnet8)**; VM uitgeschakeld. Naamgeving en lokaal ISO-pad geredigeerd. **CAPTURED, geen isolatie- of functionele FUXA-PASS.** De eerder vermelde aantallen dateren uit een oude inventaris en zijn niet opnieuw integraal geteld.
