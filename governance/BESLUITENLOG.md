# Publiek besluitenoverzicht | Hybrid-Theory

**Type:** gesaneerde, afgeleide samenvatting. Historische beslissingen blijven onderscheidbaar van later uitgevoerde tests. Er worden geen private issues, individuele commentaren of persoons- en netwerkdetails gepubliceerd.

| ID | Datum | Onderwerp | Uitgangspunt / status |
|---|---|---|---|
| HT-001 | 25-10-2026 | Publiek technisch portfolio | Afzonderlijke gesaneerde publicatie-export, na expliciet vrijgavebesluit |
| HT-002 | 25-10-2026 | Reproduceerbare engineering | Technische testresultaten moeten per scope herleidbaar zijn |
| HT-003 | 25-10-2026 | Automation / Compliance / Efficiency | Aanvullende onderzoeksperspectieven, geen gecertificeerde methodiek |
| HT-004 | 25-10-2026 | Netwerkgrenzen | LAB, beheer en tijdelijke verbindingen gescheiden beoordelen |
| HT-005 | 25-10-2026 | pfSense WAN/LAB | Virtuele firewall met gerichte netwerkvalidatie, volledige isolatie blijft te testen |
| HT-006 | 25-10-2026 | Tweede fysieke Linux-host | **PLANNED**, geen restore-PASS |
| HT-007 | 25-10-2026 | Evidence-publicatie | Alleen gesaneerde, gecontroleerde bewijsstukken |
| HT-008 | 29-10-2026 | Governanceharmonisatie | Documentatie wijzigen betekent niet automatisch live systeemwijziging |
| HT-009 | 29-10-2026 | Technische engineeringworkflow | **Risk-Based Validation** blijft een operationele engineeringwerkafspraak: risicogestuurd, scopegebonden testen en geldig bewijs hergebruiken; geen gecertificeerde auditmethode |
| HT-010 | 31-10-2026 | Scheiding uitvoering en conceptonderzoek | Concepten vragen expliciete beslissing voordat ze in uitvoering worden genomen |
| HT-011 | 01-11-2026 | Flexible Security / Mission-Based Hardening | Operationele afspraak: risicogestuurd bouwen, bestaande geldige tests hergebruiken |

## Latere technische observaties

- Windows 11 OS, Lab-netwerk en VMware Tools zijn gerealiseerd.
- Windows Server 2025 is tot AD-domain controller gepromoveerd. DNS, domain join en één gebruikers-GPO werken binnen de aangetoonde testscope.
- De voorgestelde pre-promotiesnapshot is **niet** genomen. Een latere snapshot bestaat; herstel is **niet** getest.
- M01 — Lab 01 (Hypervisor Security & Virtualization Hardening) is gestart en heeft deelcontrols PASS met één EXCEPTION; geen mission-wide completion.
- De fysieke backuphost, Azure Arc en off-host disaster recovery zijn niet aangetoond.

## Scopeafspraken

Het historische experiment naar verkeer over een grens buiten het eigen lab wordt alleen op hoofdlijnen beschreven. Er zijn geen provideridentiteiten, handelingen aan externe netwerkapparaten of private adresgegevens gepubliceerd. Deze observatie verleent geen nieuwe toestemming.

**CAT/ACE v0.2:** `CONCEPT / NOT VALIDATED`; afzonderlijke inhoudelijke review is geen implementatiegoedkeuring.

**Publicatiestatus (laatst gecontroleerd 02-11-2026):** GitHub-repository **PRIVATE** na eerdere **PUBLIC**-zichtbaarheid. De HT-001/HT-007-publicatiegates zijn nog niet aantoonbaar afgerond. Zie [goedgekeurd publicatiebeleid](PUBLICATIEBELEID.md); dit is **geen EXCEPTION**.

**Statusgebruik:** [STATUSLEGENDA](STATUSLEGENDA.md).

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
