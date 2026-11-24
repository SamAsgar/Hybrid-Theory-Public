# AD DS, DNS, domeinclient en GPO | Gesaneerde technische samenvatting

**TL;DR — redactioneel toegevoegd 02-11-2026**  
**Vraag:** Werken een AD-domain controller, clientaanmelding en gebruikers-GPO?  
**Uitkomst:** Gericht PASS voor forest/DC, DNS/SRV, domain join, testlogin en één GPO.  
**Besluit:** Basis aangetoond; restore, redundantie en verdere hardening blijven buiten deze PASS.

**Datum:** 1 november 2026 | **Uitgevoerd later op 1 november 2026**, na de eerdere installatie-/pfSense-sessie  
**Classificatie:** gesaneerde publieke afgeleide samenvatting  
**Bron:** screenshots en terminalobservaties van de eigenaar, gereviewd binnen de eigen engineeringomgeving. Ruwe privéverwijzingen en werkelijke IP-/domeinwaarden zijn niet geëxporteerd.

## Doel en testscope

Een werkend Windows Server 2025 Active Directory-lab en een Windows 11 Enterprise Evaluation-domainclient opbouwen. Testen betreffen **één domain controller, één client en één testgebruiker**, niet redundantie of productie-hardening.

| Controle | Observatie | Verdict |
|---|---|---|
| Preflight netwerk | DC met statische LAB-configuratie, passende DNS/gatewayinstellingen; pfSense-regelvolgorde beoordeeld | **PASS binnen geteste scope** |
| AD DS-rol | Rol en beheertools geïnstalleerd | **PASS** |
| Forest en DC-promotie | Nieuwe forest geïnstalleerd; DC herstart na voltooide promotie | **PASS** |
| AD DNS | Relevante domein- en SRV-records succesvol opgelost | **PASS** |
| DC-diensten | AD DS en DNS operationeel na promotie | **PASS** |
| Windows 11 domain join | Client vindt DC; domeinlidmaatschap en authenticatie aangetoond | **PASS** |
| Testgebruiker | Account aangemaakt/geactiveerd en testlogin uitgevoerd | **PASS** |
| GPO | Gerichte gebruikers-GPO beperkt toegang tot het Configuratiescherm in testaccount | **PASS** |
| Negatieve rechtencheck | Standaardgebruiker krijgt beheerders-UAC-prompt, zonder directe elevation | **PASS, beperkte scope** |
| Snapshot | Een snapshot na promotie bestaat | **VERIFIED: aanwezigheid** |
| Restore | Geen daadwerkelijke hersteltest uitgevoerd | **PENDING** (werkstatus, geen technisch testverdict) |

## Transparante afwijking

Een vooraf voorgestelde pre-promotiesnapshot werd niet aangemaakt. De promotie vond plaats zonder dat beoogde herstelpunt; pas daarna is een snapshot aangetoond. Deze snapshot telt **niet** als onafhankelijke off-host back-up of bewezen restore.

## Nog open

- Volledige netwerkisolatie en uitgebreide negatieve tests richting andere segmenten.
- Afzonderlijke DNS-forwarding, externe tijdbron, redundancy/replication en hardening.
- Testen dat GPO-instellingen niet ongewenst gelden buiten de bedoelde OU.
- Onafhankelijke back-up en werkelijke restore als apart missieonderdeel.

**Eindstatus:** `AD/CLIENT BASELINE: PASS binnen beschreven testscope`. Geen claim van volledige IAM-, netwerk- of disaster-recovery-acceptatie.

**Statusgebruik:** [statuslegenda](../governance/STATUSLEGENDA.md). 

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
