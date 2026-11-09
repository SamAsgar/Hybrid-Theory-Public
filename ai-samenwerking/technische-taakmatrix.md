# Technische taakmatrix | AI Collaboration

**Sam is Lead Architect (mens)**. Alle andere hier genoemde assistenten zijn AI en hebben geen zelfstandige besluitbevoegdheid.

| Werkgebied | Primair ondersteunende rol | Review wanneer relevant | Bewijs |
|---|---|---|---|
| VMware-host en VM-hardening | ChatGPT / Sam | Claude | Gesaneerde configuraties en gerichte tests |
| pfSense, segmentatie en firewallbeleid | Sam / Claude | ChatGPT | Configuratie-observatie, gerichte allow/deny-tests |
| Windows Server, AD DNS, domain join en GPO | Sam / Microsoft Copilot | Claude / ChatGPT | Domeindiensten, testlogin en scoped GPO-test |
| Ubuntu, Cockpit en beheer | Sam / ChatGPT | Claude | Service- en connectiviteitsobservaties |
| GNS3/Wireshark | Sam / ChatGPT | Claude | VPCS, ARP, ICMP en packet captures (niet als ruwe privé-captures publiceren) |
| Scripting/automatisering | GitHub Copilot / Sam | Claude wanneer security-impact | Reproduceerbare en reviewbare code |
| CAT/ACE v0.4-onderzoek (Audit, Cost & Efficiency) | Sam / ChatGPT | Claude (kritische AI-review, geen formele onafhankelijke audit) | Internal/External/Hybrid-scope, controlbewijs, kostenbaseline, veilige optimalisatie, revalidation en afhankelijkheidstests |

**Toelichting:** dit zijn rolvoorkeuren, geen claim dat de genoemde specialist elke taak daadwerkelijk heeft uitgevoerd. Sam kan een taak gericht delegeren. Alleen echte uitgevoerde tests onderbouwen een technische PASS binnen scope. Zie [AI-rollen](ROLLEN_EN_OVERDRACHT.md) en [statuslegenda](../governance/STATUSLEGENDA.md).

**Redactie:** Opgesteld met ChatGPT op basis van metingen en besluiten van Sam.
