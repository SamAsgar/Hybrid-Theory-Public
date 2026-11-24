# M01 — Lab 01: Hypervisor Security & Virtualization Hardening | Afgebakende review

**TL;DR — redactioneel toegevoegd 02-11-2026**  
**Vraag:** Welke eerste hypervisor- en VM-controls zijn gericht beoordeeld?  
**Uitkomst:** Controlerondes 1–3, HV-01 t/m HV-04: scoped PASS met één EXCEPTION.  
**Besluit:** Lab 01 blijft IN PROGRESS; uitgebreide hardening en herstel niet afgerond.

**Datum:** 1 november 2026  
**Werkstatus:** **IN PROGRESS** | **Controlerondes 1–3:** gerichte **PASS** met één **EXCEPTION** binnen de beschreven scope  
**Bewijs:** eerder geobserveerde VMware- en Windows-configuratie, screenshots en gerichte instellingencontrole; niet alle technische acceptatiecriteria van M01 zijn afgehandeld.

| Control | Bevinding | Uitkomst |
|---|---|---|
| HV-01 Versie- en updatestatus | VMware Workstation-versie en Windows Update-status geïnventariseerd; status op het testmoment als bijgewerkt weergegeven | PASS voor deze inventarisatie en gerichte statuscontrole; geen volledige kwetsbaarheden- of leverancierspatchaudit |
| HV-02 Beheerblootstelling | Geobserveerde VMware-beheerlistener uitsluitend lokaal; geen brede port-/firewall-audit | PASS, beperkte scope |
| HV-03 Netwerksegmentatie | Bestaande gerichte testresultaten hergebruikt; relevant firewallregelbeleid beoordeeld | PASS uitsluitend voor eerder geteste netwerkstromen; volledige isolatie niet aangetoond |
| HV-04 Shared folders | Geen gedeelde hostmappen op de beoordeelde VM's | PASS |
| HV-04 pfSense host-guest-integratie | Klembord en drag-and-drop uitgeschakeld in de configuratie | Instellingscontrole PASS; functionele hertest PENDING |
| HV-04 Windows host-guest-integratie | Klembord en drag-and-drop blijven op Windows-VM's aan voor het labwerk | **EXCEPTION** |
| Tijd en herstel | Uitgebreide tijdbron- en restoretests niet uitgevoerd | PENDING (werkstatus) |

## Geaccepteerde uitzondering

De Windows Server- en Windows 11-VM's behouden tijdelijk copy/paste en drag-and-drop voor gebruiksgemak. Het risico op host-guest gegevensuitwisseling is expliciet geaccepteerd binnen de huidige labgrenzen. **Dit is geen verklaring dat de instelling veilig is voor onbetrouwbare workloads.** Geen secrets via het klembord overdragen.

## Afbakening

HV-05 t/m HV-10 (uitgebreide logging, herstelbaarheid, logintegriteit, incidentrespons en aanvullende beheersmaatregelen) zijn niet als voltooid vastgesteld. Een snapshot is geen off-host back-up; er is nog geen onafhankelijke restore bewezen.

**Verdict:** uitsluitend de beoordeelde deelcontrols **PASS met één EXCEPTION** binnen hun scope. **Lab 01 (M01): IN PROGRESS**, geen totale labacceptatie.

**Beleidscontext:** controls op 1 november getoetst tegen toen nog conceptcriteria; het [hypervisorbeleid](../governance/HYPERVISOR_BEVEILIGINGSBELEID.md) is door Sam goedgekeurd op 02-11-2026. Dat verandert de oude testuitslag niet.

**Statusgebruik:** [statuslegenda](../governance/STATUSLEGENDA.md).

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
