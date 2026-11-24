# M01 — Hypervisor Fortress | Gesaneerde bewijsvoering

**Project:** Hybrid-Theory (publieke repository)  
**Missie:** M01 Hypervisor Fortress  
**Periode van de evidence:** 31 oktober t/m 15 november 2026  
**Evidence:** **82 gesaneerde PNG-afgeleiden**  
**Status:** technische review en eigenaar-review **PENDING**; geen volledige M01-PASS geclaimd  
**Classificatie:** PUBLIC · gesaneerde afgeleiden · de originelen blijven uitsluitend privé

> Dit is een gecontroleerde, gesaneerde migratie van de private M01-bewijsset. Elk beeld is onomkeerbaar pixelgemaskeerd. Weggehaald zijn: hostname en apparaat-, product- en serienummers, accountnamen en e-mailadressen, lokale gebruikerspaden en persoonlijke mapnamen, VM-namen en -paden, uniek identificerende delen van de hypervisorconfiguratie (`.vmx`: MAC-, UUID- en pad-sleutels, cpuid-maskerwaarden), Windows-versie- en buildreeksen in terminaluitvoer, en de standaard-inloggegevens in de loginbanner van de Wazuh-VM. Zie het [saneringsrapport](M01-SANITIZATION-REPORT.md).

## Bestanden

| Bestand | Functie |
|---|---|
| [EVIDENCE-INDEX.md](EVIDENCE-INDEX.md) | **82 screenshotbeschrijvingen**, per datum en gekoppeld aan HV-controls; FAIL, ERROR en PENDING blijven behouden |
| [GAP-ANALYSE.md](GAP-ANALYSE.md) | Voorlopige assessment per control en de nog ontbrekende M01-controles |
| [MANIFEST_SHA256.txt](MANIFEST_SHA256.txt) | SHA-256 van alle 82 **gepubliceerde afgeleiden** |
| [M01-SANITIZATION-REPORT.md](M01-SANITIZATION-REPORT.md) | Werkwijze, maskeringen, uitsluitingen en restrisico's |
| [M01-Bewijsvoering/](M01-Bewijsvoering/) | De 82 gesaneerde PNG's (oorspronkelijke bestandsnamen = opnamedatum en -tijd) |

## Methode en kwaliteitsgrenzen

1. Selectie en beschrijvingen zijn eerder opgesteld met hulp van AI-assistenten (Claude, ChatGPT), deels op basis van OCR en deels visueel bevestigd. Voor deze publicatie is elk beeld opnieuw afzonderlijk bekeken op gevoelige inhoud.
2. De opnamedatum is afgeleid uit de bestandsnaam, **niet** uit een onafhankelijke tijdbron.
3. Het onderscheid **CONFIG / TROUBLESHOOT / ERROR / FIX / TEST / PASS / FAIL / PENDING** blijft behouden. Een instellingenscherm bewijst geen functionele test.
4. De publicatie verandert geen M01-acceptatiestatus.

## Technische evidencesamenvatting

| Onderwerp | Concrete waarneming en bewijsbeperking |
|---|---|
| HV-01 host en updates | Hostinventaris en Windows Update getoond. Bewijs voor blijvend actuele patches en voor de VMware-versie is onvoldoende. Op 11 november staat een beveiligingsupdate open. |
| HV-02 beheerpoort | Filter op VMware-processen toont alleen `127.0.0.1:912` (vmware-authd); **PASS uitsluitend binnen die beperkte filterscope** |
| HV-03 netwerkgrenzen | **Geen M01-eigen integrale segmentatie-PASS**; zie [M04](../M04-Network-Citadel/) afzonderlijk |
| HV-04 gedeelde mappen en guest isolation | Shared Folders Disabled en een voor/na-configuratie voor enkele VM's, niet voor alle. Windows Client en DC met **expliciete uitzondering** |
| Hostintegriteit (11 nov.) | `sfc` zonder schendingen, maar **DISM-vervolgcontrole blijft 'repairable'** ondanks een eerdere geslaagde RestoreHealth-melding |
| Herstelbaarheid | Snapshot op de DC aanwezig, maar **geen geslaagde restore**. De Wazuh-kopie staat op dezelfde hostschijf en is geen onafhankelijke back-up. |

## Integriteit

De gepubliceerde PNG's zijn afgeleiden, geen originelen. De hashes in [MANIFEST_SHA256.txt](MANIFEST_SHA256.txt) horen bij deze publieke bestanden. Hashes van de private originelen worden bewust niet gepubliceerd. Controle vanuit `Portfolio/`:

```bash
sha256sum -c M01-Hypervisor-Fortress/MANIFEST_SHA256.txt
```

**Geen geclaimde volledige M01-PASS.** Zie de [GAP-analyse](GAP-ANALYSE.md) en de [statuslegenda](../../Governance/STATUSLEGENDA.md).
