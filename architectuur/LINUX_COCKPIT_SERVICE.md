# Ubuntu Server + Cockpit | Servicekaart

**Status:** Ubuntu Server 24.04 LTS en Cockpit **IMPLEMENTED**. De beschikbaarheid en beheerfunctie zijn in gerichte eerdere tests bevestigd.

## Componenten

Ubuntu levert Linux-systeembeheer, systemd-services, shellbeheer en netwerkdiagnostiek. Cockpit is een lokale webbeheerinterface om het beheerwerk via het gescheiden lab uit te voeren.

## Beheercontroles

1. Controleer service en luisterpoort vanuit een toegestane beheerscope.
2. Verifieer toegangsrechten en voorkom onnodig publiek bereikbare beheerservices.
3. Houd beheer-, LAB- en tijdelijke updateverbindingen uit elkaar.
4. Leg alleen gesaneerde systeem- en netwerkobservaties vast.

## Bekende beperking

Niet alle Cockpit-netwerkfuncties zijn zonder aanvullende NetworkManager-integratie beschikbaar. Een onnodige overstap van netwerkbeheerder wordt uitgesteld als dit bestaande toegang of routes kan verbreken.

**Beperking:** geen claim dat containerdiensten, private cloud of onafhankelijke hersteltests al in productie zijn.
