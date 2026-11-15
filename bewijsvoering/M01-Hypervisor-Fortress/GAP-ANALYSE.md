# Publieke GAP-analyse — M01 Hypervisor Fortress

**Documentversie:** 16 november 2026, Public/alias. De oordelen zijn overgenomen uit de aangeleverde GAP-analyse en worden niet tot nieuwe PASS-statussen gepromoveerd. Voor 7 screenshots geldt WITHHELD.

Peildatum 15-11-2026. Gebaseerd op de selectie in `EVIDENCE-INDEX.md` en het deelreviewlog van 1 november (HV-01 t/m HV-04). Verdictvoorstel per control; het besluit is aan de Project Owner.

## 1. Stand per control

| Control | Claim in log 01-11 | Wat de ZIP aantoont | Oordeel bewijs |
|---|---|---|---|
| HV-01 versie/updates | PASS (inventarisatie) | Windows Update-scherm 01-11 (status niet eenduidig leesbaar). Geen 'About VMware Workstation'. Op 11-11: beveiligingsupdate KB5132061 staat open. | **Onbewezen PASS**; op 11-11 aantoonbaar niet actueel |
| HV-02 beheerblootstelling | PASS, beperkte scope | Alleen `127.0.0.1:912` vmware-authd. Filter beperkt tot vmware/vmnat-processen. | PASS binnen die scope **bewezen** |
| HV-03 netwerksegmentatie | PASS op eerdere stromen | Geen M01-eigen bewijs in de periode; steunt op M04. | **Onbewezen** binnen M01 |
| HV-04 shared folders | PASS | Disabled voor LAB-CLIENT01 en pfSense zichtbaar; één beeld zonder leesbare VM-naam. LAB-FUXA01, LAB-PLC01, LAB-WAZUH01, GNS3 en Linux ontbreken. | Deels bewezen |
| HV-04 pfSense host-guest | Instelling PASS, hertest PENDING | Voor (aan) en na (uit) visueel bevestigd. | Instelling **bewezen**; functionele hertest ontbreekt |
| HV-04 Windows host-guest | EXCEPTION | Klembord/drag-and-drop aan op LAB-CLIENT01 en DC, visueel bevestigd. | Uitzondering klopt met het beeld |
| Tijd en herstel | PENDING | w32time gestopt in LAB-CLIENT01, laatste sync 'unspecified'; alle VM's 'Time sync off'. Snapshot `POST-AD-DC`; geen restore. | PENDING terecht |
| HV-05 t/m HV-10 | niet vastgesteld | Geen enkel beeld. | Geen bewijs |

## 2. Ontbrekende bewijsvoering

- VMware Workstation-versie en updatestatus (Help > About / Check for Updates).
- Guest Isolation en Shared Folders van LAB-FUXA01, LAB-PLC01, LAB-WAZUH01, GNS3 en de Linux-VM.
- Functionele hertest dat kopiëren/plakken naar de pfSense-VM echt niet meer werkt.
- Eén geslaagde snapshot-revert of restore. De Wazuh-kopie staat op dezelfde schijf (C:) en is geen off-host back-up.
- Referentiehash bij de Windows 11-ISO; hash van de voltooide Wazuh-OVA (alleen een mislukte poging op de `.crdownload`).
- Encryptie: pfSense en DC staan op 'Not encrypted'; er is geen besluit of uitzondering in beeld.

## 3. Tegenstrijdigheden

- **Host-integriteit 11-11:** RestoreHealth 'completed successfully' (16:00), daarna meldt ScanHealth opnieuw 'repairable' (16:22). sfc vindt niets, terwijl CBS.log 'Payload Corruption: 27, Total Repaired: 0' toont.
- **HV-01:** 'bijgewerkt' op 01-11 tegenover openstaande beveiligingsupdates op 11-11. De oude uitslag blijft historisch geldig, maar de control is niet doorlopend aangetoond.
- **LAB-CLIENT01-wizard:** stap 'Guest OS' toont Windows Server 2025, de samenvatting Windows 11 x64. De wizard toont een netwerkkeuze, de samenvatting 'Network Adapter: None'.
- **Niet opgenomen:** `Screenshot 2026-11-01 194259.png` bevat alleen de tekst 'Annotatie buiten de originele VMware-interface | Sanitization: PASS'. Dat is een latere annotatie, geen systeemuitvoer en geen bewijs van sanering.

## 4. Onbewezen PASS-claims

HV-01 (versie + updates), HV-03 (binnen M01), HV-04 shared folders voor 'de beoordeelde VM's' als geheel, en de functionele werking van de pfSense-isolatie.

## 5. Eerstvolgende bewijsstappen (geen nieuwe scope)

1. About VMware + Windows Update na installatie van KB5132061.
2. DISM ScanHealth herhalen en uitkomst vastleggen.
3. Guest Isolation/Shared Folders van de vijf ontbrekende VM's.
4. Plakproef op de pfSense-console (negatieve test).
