# Ubuntu Server + Cockpit | Servicekaart

**Status:** Ubuntu Server 24.04 LTS en Cockpit **IMPLEMENTED**. De beschikbaarheid en beheerfunctie zijn in gerichte eerdere tests bevestigd.

## Componenten

Ubuntu levert Linux-systeembeheer, systemd-services, shellbeheer en netwerkdiagnostiek. Cockpit is een lokale webbeheerinterface om het beheerwerk via het gescheiden lab uit te voeren.

## Interfaces en officiële aliassen

| Interface | Netwerk | IP-alias | IPv6-alias | MAC-alias |
|---|---|---|---|---|
| LAB-interface | LAB | `LAB_NET_IP` | `LAB_NET_IPV6_LL` | `LAB_NET_MAC` (PENDING_CAPTURE) |
| Beheerinterface (Cockpit) | MGMT, host-only | `MGMT_NET_IP` | `MGMT_NET_IPV6_LL` | `MGMT_NET_MAC` (PENDING_CAPTURE) |
| Tijdelijke update-interface | WAN-SIM (VMware NAT) | `NET_02_IP` | `NET_02_IPV6_LL` | `NET_02_MAC` (PENDING_CAPTURE) |

De rollen van deze interfaces zijn vastgelegd op 25–30 oktober. Of de beheer- en update-interface na de pfSense-test van 26 oktober weer in hun normale toestand staan, is **NOT VERIFIED**. `LAB_NET_IP` heeft historisch dezelfde waarde als `DC01_LAB_IP` (**TWIJFEL**, gelijktijdig gebruik niet aangetoond). Werkelijke adressen worden niet gepubliceerd.

## Beheercontroles

1. Controleer service en luisterpoort vanuit een toegestane beheerscope.
2. Verifieer toegangsrechten en voorkom onnodig publiek bereikbare beheerservices.
3. Houd beheer-, LAB- en tijdelijke updateverbindingen uit elkaar.
4. Leg alleen gesaneerde systeem- en netwerkobservaties vast.

## Bekende beperking

Niet alle Cockpit-netwerkfuncties zijn zonder aanvullende NetworkManager-integratie beschikbaar. Een onnodige overstap van netwerkbeheerder wordt uitgesteld als dit bestaande toegang of routes kan verbreken.

**Beperking:** geen claim dat containerdiensten, private cloud of onafhankelijke hersteltests al in productie zijn.
