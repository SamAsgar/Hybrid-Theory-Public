# 03 FUXA OpenPLC baseline

**M04 Network Citadel · documentaire, historisch gedateerde evidence.**

Deze themamap bevat 28 bronrecords uit een private 270-records selectie. Originelen blijven privé. De afbeeldingstatus is geen technisch acceptatieoordeel.

| Evidence-ID | Datum/tijd | Klasse | Control | Technische betekenis | Publieke afbeelding |
|---|---|---|---|---|---|
| `M04-ZIP-044` | 02-11-2026 23:10:49 | **ERROR** | FUXA netwerk | FUXA01 eerste login: ens36 DOWN, 'Network is unreachable', DNS-resolutie mislukt. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-045` | 02-11-2026 23:13:04 | **TROUBLESHOOT** | FUXA netwerk | FUXA01: ens36 UP zonder IPv4; /etc/netplan/ is leeg. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-046` | 02-11-2026 23:19:15 | **ERROR** | FUXA netwerk | netplan: '01-fuxa.yaml:4:12: Error in network definition: expected mapping (check indentation)'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-047` | 02-11-2026 23:22:02 | **CONFIG** | AC04 | FUXA01-VM: adapter Custom (VMnet8, NAT) - FUXA staat buiten pfSense. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-048` | 02-11-2026 23:40:51 | **PASS** | FUXA netwerk | FUXA01: ping github.com 3/3 na correctie van de netplan-YAML. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-049` | 02-11-2026 23:44:44 | **CONFIG** | FUXA installatie | apt-installatie docker.io op FUXA01. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-050` | 02-11-2026 23:56:00 | **ERROR** | FUXA installatie | docker run verkeerd afgebroken ('--name: command not found'); daarna het volledige run-commando (poort 1881, volumes, frangoteam/fuxa:latest). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-051` | 03-11-2026 00:06:07 | **CONFIG** | FUXA installatie | Image 'frangoteam/fuxa:latest' binnengehaald (digest zichtbaar) en container-ID teruggegeven. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-052` | 03-11-2026 01:38:44 | **TEST** | FUXA web | Browser: [REDACTED_URL] bereikbaar; security-setupwizard toont 'Authentication with Token: Disabled'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-053` | 03-11-2026 22:49:31 | **CONFIG** | AC05 context | WAZUH01-VM: adapter op LAN segment S-HT-LAN01-ISOLATED (LAB-zone achter pfSense). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-054` | 03-11-2026 22:58:58 | **ERROR** | AC05 context | Wazuh-VM: 'ip -4 addr' toont alleen loopback - geen IPv4-adres. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-055` | 03-11-2026 23:01:58 | **TROUBLESHOOT** | AC05 context | Wazuh-VM: nmcli niet aanwezig (command not found). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-056` | 03-11-2026 23:05:49 | **TROUBLESHOOT** | AC05 context | Wazuh-VM: networkctl status eth0 (link up, geen IPv4). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-057` | 03-11-2026 23:08:23 | **TROUBLESHOOT** | AC05 context | Wazuh-VM: systemd-networkd-log met 'lease lost' / service gestopt. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-058` | 03-11-2026 23:12:53 | **CONFIG** | DHCP LAB | pfSense DHCP Server (Kea) instellingenpagina. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-059` | 03-11-2026 23:21:08 | **CONFIG** | DHCP LAB | pfSense Services / DHCP Server / LAB. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-060` | 03-11-2026 23:23:36 | **PASS** | DHCP LAB | Status / DHCP Leases: [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN] uitgegeven aan 'wazuh-server' (03-11 23:11). Let op: [HISTORIC_DHCP_LEASE_IDENTITY_UNCERTAIN] is in de firewallregels 'Client01'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-061` | 03-11-2026 23:24:07 | **TEST** | AC05 context | Wazuh-VM: eth0 heeft dynamisch IPv4-adres. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-062` | 03-11-2026 23:28:17 | **PASS** | AC05 context | Wazuh-VM: wazuh-manager, wazuh-indexer en wazuh-dashboard 'active'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-063` | 03-11-2026 23:35:55 | **CONFIG** | Beheer | pfSense System / Advanced / Admin Access. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-064` | 03-11-2026 23:38:31 | **CONFIG** | NAT | Firewall / NAT / Port Forward: lijst nog leeg. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-065` | 03-11-2026 23:45:34 | **CONFIG** | NAT | Port forward 'Edit Redirect Entry' voor het Wazuh-dashboard; 'Add associated filter rule'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-066` | 03-11-2026 23:47:43 | **TEST** | NAT | Host: VMware Network Adapter VMnet1 = MGMT_CLIENT_IP (bron voor de port forward). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-067` | 03-11-2026 23:59:53 | **ERROR** | AC05 context | Wazuh-dashboard via port forward bereikbaar, maar 'Invalid username or password'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-068` | 04-11-2026 00:00:52 | **ERROR** | AC05 context | Wazuh-healthcheck: index geblokkeerd, 'disk usage exceeded flood-stage watermark'. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-069` | 04-11-2026 00:17:41 | **TROUBLESHOOT** | AC05 context | Wazuh-VM: partitietabel/GPT-melding en df -hT / (root-FS kleiner dan de schijf). | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-070` | 04-11-2026 00:35:52 | **FIX** | AC05 context | Wazuh-VM na herstel: lsblk toont sda1 op 50G. | Nog niet gepubliceerd (review vereist) |
| `M04-ZIP-071` | 04-11-2026 00:38:50 | **PENDING** | AC05 | Wazuh-dashboard overzicht: 'This instance has no agents registered'. AC05 niet aangetoond. | Nog niet gepubliceerd (review vereist) |
