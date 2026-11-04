# M02 — Phoenix Recovery

**Onderdeel:** Governance · Disaster Recovery & Resilience  
**Ontwerpversie:** v0.5.1 · 4 november 2026  
**Status:** **DRAFT / TECHNICAL VALIDATION PENDING**

Phoenix Recovery onderzoekt hoe een hybride IT/OT-lab **onafhankelijk kan worden hersteld** als de primaire host en de lokale herstelomgeving verloren gaan. Het gekozen ontwerp combineert een **afzonderlijke lokale herstelserver** met een **rechtstreeks offsite back-uppad naar Backblaze B2**.

## Document

- [**M02 Phoenix Recovery — Herstelarchitectuur v0.5.1**](M02_PHOENIX_RECOVERY_v0.5.1.md): doel, twee back-uppaden, Mermaid-topologieën, dreigingsbeeld, CAT/ACE v0.4, herstelafhankelijkheden en test-/bewijsplan.

## Beoordelingsstatus

| Onderwerp | Stand |
|---|---|
| Architectuur B geselecteerd | **Ja, ontwerpbesluit** |
| Lokale en offsite recovery geïmplementeerd | **Niet aangetoond** |
| Restic-restore en B2-immutability bewezen | **Nee, tests gepland** |
| RTO daadwerkelijk gemeten | **Nee** |
| Onafhankelijke audit of certificering | **Nee** |

De documentatie beschrijft **wat is gekozen en wat nog bewezen moet worden**. Er worden geen toekomstige acties als afgeronde werkzaamheden gepresenteerd.