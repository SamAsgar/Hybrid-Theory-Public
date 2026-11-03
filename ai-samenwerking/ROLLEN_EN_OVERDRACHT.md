# AI Collaboration | Rollen en overdracht

| Deelnemer | Rol |
|---|---|
| **Sam** | **Project Owner & Lead Architect (mens)**; eindverantwoordelijk voor ontwerp, scope, toestemming, bewijs en risicoacceptatie |
| **ChatGPT** | **Engineering Orchestrator (AI)**; implementatiebegeleiding, samenhang, troubleshooting en testbare documentatie |
| **Claude** | **Critical Security Auditor & Chaos Engineer (AI)**; gerichte tweede securitybeoordeling waar passend, afhankelijkheden en weerbaarheid; geen formeel onafhankelijke audit |
| **Microsoft Copilot** | **Microsoft Specialist & Automation Engineer (AI)**; Windows Server, Active Directory, Entra, Azure, PowerShell |
| **GitHub Copilot** | **Coding & Automation Assistant (AI)**; scripts, IaC, code-review en testautomatisering |

## Technische overdracht

Een taak krijgt een afgebakend doel, relevante configuratie of gesaneerde bewijsbron, aannames, eventuele openstaande risico's en een terugvalroute. Reviewer en uitvoerder worden waar relevant afzonderlijk vermeld. Sam beslist als Project Owner over acceptatie. Een AI-review is geen zelfstandig bewijs van technische werking.

```text
Taak / lab:
Doel en scope:
Verantwoordelijke:
Relevante configuratie (gesaneerd):
Test en observatie:
Afhankelijkheden en risico:
Rollback / herstel:
Engineeringverdict (scope verplicht): PASS | REWORK | EXCEPTION
Ontbrekend bewijs: beschrijf concreet; werkstatus PENDING of PARKED
Akkoord Sam (Project Owner):
```

## Onderzoekscontext

Het [CAT/ACE v0.4-onderzoek](../governance/CAT_ACE_v0.4.md) verbindt **CAT** (Corporate Governance & Compliance; Accountability & Management; Technology & Operations) met **ACE = Audit, Cost & Efficiency**. ACE kan **intern, extern of hybride** worden uitgevoerd, met vastgelegde rolconflicten: eerst controlwerking en evidence beoordelen, vervolgens kosten en veilige optimalisaties vergelijken en wijzigingen **hervalideren**. Claude of een andere AI kan kritisch reviewen, maar is geen formele onafhankelijke auditor. **Status: CONCEPT / NOT VALIDATED.** De technische uitvoering blijft aan de geldende engineeringafspraken en eigenaarbesluiten gebonden.

**Statusgebruik:** [statuslegenda](../governance/STATUSLEGENDA.md). 

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
