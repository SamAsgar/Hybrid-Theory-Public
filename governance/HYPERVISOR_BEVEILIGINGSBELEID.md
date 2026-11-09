# Hypervisor | Beveiligingsbeleid en controlecriteria

**Beleids-ID:** HT-GOV-HV-001  
**Versie:** 0.1 (opgesteld 29-10-2026) | **Documentstatus:** **APPROVED — Sam, 02-11-2026**  
**Classificatie:** PUBLIC  
**Eigenaar:** Sam  
**Onderzoekskader:** [CAT/ACE v0.4](CAT_ACE_v0.4.md) (Audit, Cost & Efficiency; experimenteel, geen formeel auditverdict)  
**Redactionele update:** 03-11-2026, alleen onderzoeksverwijzingen; bestaande HV-controls, beleidsbesluit en testuitslagen ongewijzigd.  
**Scope:** Windows-virtualisatiehost, VMware Workstation Pro, VM-grenzen, beheer, logging, herstel en gecontroleerd bewijs.

> Dit beleid is door Sam goedgekeurd op 02-11-2026. Dat betekent **niet** dat iedere control is geïmplementeerd of dat bestaande tests een bredere PASS hebben. Beleidsgoedkeuring autoriseert geen ongedocumenteerde technische wijziging.

## 1. Doel en dreigingsmodel

De virtualisatielaag vormt een trust boundary onder meerdere gastbesturingssystemen. Een gecompromitteerde host, slecht afgeschermde beheerinterface of ontbrekend hypervisor-auditspoor kan detectie in meerdere VM's ondermijnen. Monitoring moet aandacht besteden aan **afwijkend gedrag én verlies van zichtbaarheid**.

**Productverschil:** dit lab gebruikt **VMware Workstation Pro op Windows**, geen VMware ESXi/vCenter. Een kwetsbaarheidsmelding voor ESXi/ESX bewijst niet dat dezelfde fout ook in Workstation bestaat. Controleer altijd getroffen producten en versies in het actuele leveranciersadvies voordat een patch- of kwetsbaarheidsclaim wordt gemaakt.

## 2. Voorgestelde hardeningcontrols

| ID | Control | Gewenst technisch resultaat | Bewijs / beoordeling |
|---|---|---|---|
| HV-01 | Assetinventarisatie en patching | Host-/hypervisorversies vastleggen; productspecifieke updates en veilige rollback beoordelen | Versie- en leverancierscontrole, resultaat update |
| HV-02 | Beveiligd beheer | Beheertoegang beperken; gescheiden accounts, least privilege en waar passend MFA | Geschoonde review van rechten en toegang |
| HV-03 | Segmentatie en isolatie | LAB-dataplane, beheer en tijdelijke updateverbinding scheiden; ongeautoriseerde toegang tot thuisnetwerk of derden blokkeren | Bestaand positief/negatief bewijs hergebruiken; alleen nieuwe grenzen gericht testen |
| HV-04 | VM-isolatie | Gedeelde mappen, clipboard, drag-and-drop, USB-passthrough en host/guest-integraties risicogestuurd beoordelen; ondersteunde guest tools gebruiken | VM-instellingen en vastgelegde uitzonderingen |
| HV-05 | Centrale logging | Relevante logbronnen van Windows-host, VM's en firewall inventariseren; verzamelen op gecontroleerde bestemming | Logbronnenlijst en ontvangstbewijs |
| HV-06 | Continuïteitsdetectie logging | Uitval van logforwarder, ontbrekende heartbeats, gaten in ontvangst en tijdsafwijkingen detecteren; onderscheid maken tussen hostuitval, netwerkonderbreking en collectorstoring | Veilige oefening met tijdstempels voor detectie en herstel |
| HV-07 | Logintegriteit en tijd | Schrijfrechten op logs beperken, bewaartermijnen en tijdsynchronisatie vastleggen, functies scheiden | Toegangsrechten, retentie en tijdmeting |
| HV-08 | Back-up en herstel | VM-configuraties en herstelgegevens beschermen met een kopie buiten de host; herstel testen | Back-upscope en herstelbewijs; snapshot alleen is onvoldoende |
| HV-09 | Change control | Belangrijke wijzigingen aan security, routing, virtualisatie en logging vastleggen met impact en rollback | Gekoppeld besluit en wijzigingsbewijs |
| HV-10 | Incident response | Handelwijze vastleggen voor onverklaarbare beheertoegang of wegvallende telemetrie; bewijs bewaren vóór destructief herstel | Beoordeeld runbook of toegestane tabletop-oefening |

**Belangrijke beperking:** een collector buiten de host kan ontvangen events bewaren, maar niet garanderen dat hij gebeurtenissen detecteert die de host of hypervisor nooit registreert. Een collector-VM op dezelfde fysieke host is bovendien geen volledig onafhankelijke hostmonitoring.

## 3. Bestaand bewijs en openstaand werk

**Tijdlijn:** de hieronder gebruikte HV-01 t/m HV-04-observaties zijn **1 november 2026 getoetst tegen de toen nog conceptcriteria; beleid goedgekeurd op 02-11-2026**. De beleidsgoedkeuring vormt geen retrospectieve technische validatie.

| Onderdeel | Documenteerde componentstatus en controles | Beperking |
|---|---|---|
| pfSense LAB/WAN en beheer | Firewall en LAB-interfaces **IMPLEMENTED**. Op 26 oktober is **één gerichte negatieve ICMP-test** buiten de bedoelde LAB-scope als geblokkeerd gerapporteerd (**PASS voor die ene proef**). | Geen bewijs van een brede LAB→internet- én LAB→thuisnetwerkblokkade, of van volledige isolatie voor alle protocollen. |
| GNS3 VM/Desktop | **IMPLEMENTED**; lichte VPCS-ARP/ICMP-baseline op 28 oktober **PASS** binnen de uitgevoerde topologie. | Dataplane-isolatie buiten die testopstelling nog niet aangetoond. |
| Windows Server 2025 / AD | OS- en AD DS-rolinstallatie gerapporteerd. Later op **1 november** forest/DC, DNS/SRV, domain join, testlogin en één GPO **PASS binnen afgebakende scope**. | Geen volledige identity- of segmentatieacceptatie, geen onafhankelijke restore. |
| HV-01 patch-/versiecontrole | VMware Workstation-versie en Windows Update-status geïnventariseerd; gerichte controle **PASS**. | Geen volledige patch-/kwetsbaarhedenscan of bewijs van alle leveranciersadviezen. |
| HV-02 beheerblootstelling | VMware-beheerlistener lokaal waargenomen, **PASS voor gerichte luisteradrescontrole**. | Geen volledige poort- of hostfirewallaudit. |
| HV-03 netwerkcontrole | Bestaande gerichte firewall-/bereikbaarheidstests als deelscope beoordeeld. | Volledige netwerkisolatie **niet aangetoond**. |
| HV-04 VM-isolatie | Gedeelde mappen bij beoordeelde VM's uit; pfSense host-guest-integratieconfiguratie **PASS voor instellingencontrole**. | Windows Server en Windows 11 behouden clipboard/drag-and-drop als **EXCEPTION**; pfSense functionele hertest **PENDING**. |
| HV-05 t/m HV-10, off-host restore | Nog geen afgeronde integrale implementatie-/acceptatietests. | **PENDING**; snapshot ≠ onafhankelijke back-up of herstelbewijs. |

**Lab 01 (M01): IN PROGRESS.** Alleen de hierboven genoemde controluitspraken hebben scoped PASS of EXCEPTION; geen integrale labacceptatie. Bronnen: [pfSense-test 26 oktober](../projectlogboeken/2026-10-26-projectstatus.md), [GNS3-baseline](../projectlogboeken/2026-10-28-gns3-kvm-diagnose-parkeerregister.md), [AD-baselinerapport](../projectlogboeken/2026-11-01-ad-dns-domainjoin-gpo-samenvatting.md), [M01-deelreview](../projectlogboeken/2026-11-01-hypervisor-fortress-deelreview.md) en [resourcesmeting](../projectlogboeken/2026-10-27-hostcapaciteit-geheugendiagnose.md).

## 4. Risicogestuurde prioriteiten

- **Prioriteit 1:** controleer patchniveaus van host en Workstation. Behoud bestaande Windows-beveiliging en voorkom onbedoeld publiek bereikbaar beheer.
- **Prioriteit 2:** controleer rechten voor host/guest-integratie en noodzakelijke monitoring, zonder een werkende labconfiguratie onnodig te veranderen.
- **Prioriteit 3:** ontwerp centrale logging en alerts bij ontbrekende heartbeats na de essentiële VM-baseline. Kies pas een tool na resource- en kostencontrole.
- **Prioriteit 4:** verifieer werkelijk onafhankelijke off-host back-ups en herstel zodra geschikte opslag beschikbaar is.

Schakel VBS of Memory Integrity niet alleen voor nested virtualisatie uit. Iedere voorgestelde concessie aan hostbeveiliging vereist een expliciete risicoafweging, rollback en toestemming van Sam.

## 5. Technische uitvoering en CAT/ACE v0.4 als onderzoekscontext

De operationele hardeningwerkzaamheden volgen een risicogestuurde volgorde: infrastructuur inventariseren, systeem instellen, beheer organiseren en tijdens alle stappen gericht beveiligen en troubleshooten. Dat is een **praktische engineeringworkflow**, geen automatische auditmethode of bewijs van normconformiteit.

Binnen een **afzonderlijk, nog niet gevalideerd onderzoek** koppelt CAT/ACE v0.4 de volgende CAT-lagen aan een **interne, externe of hybride ACE-beoordeling**:

- **Corporate Governance & Compliance:** beveiligingsdoelen, toepasselijke eisen en beleid rond virtualisatie.
- **Accountability & Management:** wie autoriseert beheer, host-guest-uitzonderingen, wijzigingen en restrisico?
- **Technology & Operations:** host, VMware Workstation, VM's, geïsoleerde segmenten, logbronnen en back-ups.
- **ACE-Audit:** controleer per VM de instellingen, daadwerkelijke isolatiewerking, uitzonderingen en bewijs; een screenshot is geen formele onafhankelijke audit.
- **ACE-Cost:** documenteer licenties, opslag, beheer-/hersteluren en kosten van onafhankelijke back-ups (gemeten of expliciet geraamd).
- **ACE-Efficiency:** vergelijk alternatieven onder dezelfde isolatie-, herstel- en risicogrenzen; een goedkope snapshot is geen hersteloplossing.
- **Revalidation:** hertest gewijzigde VM-isolatie en herstelcontrols binnen scope. Automatisering kan tests ondersteunen, maar is niet de ACE-definitie.

**Illustratieve gap-analyses:** control-design (isolatiedoel), technische configuratie (clipboard/shared folders), operating effectiveness (gerelateerde netwerk-/toegangsproeven), afhankelijkheden (gedeelde host/management), herstelbaarheid (off-host restore) en bewijskwaliteit (logs en testprovenance). Een bekende uitzondering op een instelling is geen brede beveiligings-PASS.

**Benchmarkselectie:** bijvoorbeeld passende ISO/IEC 27001-controls, CIS Safeguards en productbenchmarks, NIST SP 800-53A-assessmentprocedures en COBIT-rollen. Selecteer alleen kaders die relevant zijn voor de concrete controlescope; beoordeel verschillen in hun functie. De onderzoeksmethode kan na een test worden genuanceerd of weerlegd.

Zie [CAT/ACE v0.4 — volledige onderzoeksdocumentatie met VMware-praktijkcasus](CAT_ACE_v0.4.md). Deze koppeling bewijst niet dat de hier genoemde voorgestelde hypervisorcontrols al zijn geïmplementeerd.

## 6. Verificatiecriteria

- **PASS:** een specifieke hardeningcontrol voldoet aantoonbaar aan de gedocumenteerde acceptatiecriteria binnen de geteste scope.
- **REWORK:** een control faalt, verplicht bewijs ontbreekt of een veiligheidsgrens blijkt aantoonbaar onveilig.
- **EXCEPTION:** uitsluitend expliciet goedgekeurd en vastgelegd beheersbaar restrisico; geen vrijstelling voor verplichte veiligheidseisen.
- **PLANNED / IMPLEMENTED / VERIFIED:** componentstatus, geen alternatieve testverdicts.

## 7. Toegestane detectieoefeningen

Toekomstige geïsoleerde oefeningen kunnen het stoppen van een logforwarder, gecontroleerd uitschakelen van een VM, onschuldige afwijking van een testtijdbron, geautoriseerde beheerlogin of korte onderbreking van een lab-only logverbinding simuleren. Elke oefening vereist expliciete scope, toestemming, rollback en reproduceerbaar bewijs. Echte exploits, malware, destructieve logmanipulatie en ongeautoriseerde netwerktests zijn daarvoor niet nodig.

Gedetailleerde storingsscenario's en adversarial validatie horen in een afzonderlijk goedgekeurd testplan, **niet** in dit basisbeleid voor hardening.

## 8. Governance en publicatie

- [Labkader](LAB_KADER.md): toestemming, trust boundaries en veiligheid.
- [AI-werkafspraken](AI_WERKAFSPRAKEN.md): risicogestuurd werken zonder dubbele reviews.
- [Wet- en regelgevingskaders](WET_EN_REGELGEVING.md): referenties, geen compliancecertificering.
- [Publicatiebeleid](PUBLICATIEBELEID.md): regels voor te publiceren bewijs.
- [Hardwarebaseline](HARDWARE_BASELINE.md): technische componentstatus.
- [Statuslegenda](STATUSLEGENDA.md): definities van component-, werk-, document- en verdictstatus.

**Documentstatus:** **APPROVED — Sam, 02-11-2026**. De technische HV-controles van 1 november werden aan de toenmalige conceptcriteria getoetst. Beleid goedgekeurd op 2 november; geen nieuwe live configuratie of extra test uitgevoerd.

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
