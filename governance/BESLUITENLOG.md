# Publiek besluitenoverzicht | Hybrid-Theory

**Type:** gesaneerde, afgeleide samenvatting. Historische beslissingen blijven onderscheidbaar van later uitgevoerde tests. Er worden geen private issues, individuele commentaren of persoons- en netwerkdetails gepubliceerd.

| ID | Datum | Onderwerp | Uitgangspunt / status |
|---|---|---|---|
| HT-001 | 25-10-2026 | Publiek technisch portfolio | Afzonderlijke gesaneerde publicatie-export, na expliciet vrijgavebesluit |
| HT-002 | 25-10-2026 | Reproduceerbare engineering | Technische testresultaten moeten per scope herleidbaar zijn |
| HT-003 | 25-10-2026 | Automation / Compliance / Efficiency | **HISTORISCH** onderzoeksperspectief; inmiddels opgevolgd door CAT/ACE v0.4, geen gecertificeerde methodiek |
| HT-004 | 25-10-2026 | Netwerkgrenzen | LAB, beheer en tijdelijke verbindingen gescheiden beoordelen |
| HT-005 | 25-10-2026 | pfSense WAN/LAB | Virtuele firewall met gerichte netwerkvalidatie, volledige isolatie blijft te testen |
| HT-006 | 25-10-2026 | Tweede fysieke Linux-host | **PLANNED**, geen restore-PASS |
| HT-007 | 25-10-2026 | Evidence-publicatie | Alleen gesaneerde, gecontroleerde bewijsstukken |
| HT-008 | 29-10-2026 | Governanceharmonisatie | Documentatie wijzigen betekent niet automatisch live systeemwijziging |
| HT-009 | 29-10-2026 | Technische engineeringworkflow | **Risk-Based Validation** blijft een operationele engineeringwerkafspraak: risicogestuurd, scopegebonden testen en geldig bewijs hergebruiken; geen gecertificeerde auditmethode |
| HT-010 | 31-10-2026 | Scheiding uitvoering en conceptonderzoek | Concepten vragen expliciete beslissing voordat ze in uitvoering worden genomen |
| HT-011 | 01-11-2026 | Flexible Security / Mission-Based Hardening | Operationele afspraak: risicogestuurd bouwen, bestaande geldige tests hergebruiken |
| HT-012 | 03-11-2026 | CAT/ACE v0.4 — onderzoeksdocumentatie | Actuele gepubliceerde onderzoeksvariant: **Audit / Cost / Efficiency**, inzetbaar intern, extern of hybride. Controlbewijs, kosteneffecten, veilige optimalisatie en Revalidation. **CONCEPT / NOT VALIDATED**; geen automatische uitvoering of attestatie |

## Latere technische observaties

- Windows 11 OS, Lab-netwerk en VMware Tools zijn gerealiseerd.
- Windows Server 2025 is tot AD-domain controller gepromoveerd. DNS, domain join en één gebruikers-GPO werken binnen de aangetoonde testscope.
- De voorgestelde pre-promotiesnapshot is **niet** genomen. Een latere snapshot bestaat; herstel is **niet** getest.
- M01 — Lab 01 (Hypervisor Security & Virtualization Hardening) is gestart en heeft deelcontrols PASS met één EXCEPTION; geen mission-wide completion.
- De fysieke backuphost, Azure Arc en off-host disaster recovery zijn niet aangetoond.

## Scopeafspraken

Het historische experiment naar verkeer over een grens buiten het eigen lab wordt alleen op hoofdlijnen beschreven. Er zijn geen provideridentiteiten, handelingen aan externe netwerkapparaten of private adresgegevens gepubliceerd. Deze observatie verleent geen nieuwe toestemming.

**CAT/ACE v0.4:** [actuele documentatie](CAT_ACE_v0.4.md), `CONCEPT / NOT VALIDATED`. **CAT-C** bepaalt eisen; **ACE-Audit** toetst controles, **ACE-Cost** onderzoekt uitgaven en **ACE-Efficiency** onderbouwt veilige verbeteringen; wijzigingen worden opnieuw beoordeeld. Intern/extern/hybride zijn opties; publicatie of inhoudelijke review is geen implementatiegoedkeuring. De [v0.2-tekst](CAT_ACE_v0.2.md) blijft uitsluitend als historisch onderzoeksdocument bewaard.

**Publicatiestatus:** **GitHub-zichtbaarheid: PUBLIC** (gecontroleerd 05-11-2026). De HT-001/HT-007-publicatiegates zijn nog niet aantoonbaar afgerond. Zie [goedgekeurd publicatiebeleid](PUBLICATIEBELEID.md); dit is **geen EXCEPTION**.

**Statusgebruik:** [STATUSLEGENDA](STATUSLEGENDA.md).

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
