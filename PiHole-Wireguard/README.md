Pihole with Wireguard

## PiHole

You can choose between PiHole with DoH (DNS over HTTPS) with Cloudflared or PiHole with own Upstream DNS Server. `02-pihole-DoH-cloudflare.yaml` or `02-pihole-upstream-dns.yaml`

### Upstream DNS Server

Change the DNS Server in `02-pihole-upstream-dns.yaml` to your own DNS Server.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: pihole-configmap
  namespace: pihole
data:
  TZ: 'Europe/Berlin'
  ADMIN_EMAIL: 'service@it-lab.cc'
  DNS1: '192.168.178.1'
  DNS2: '192.168.178.1'
```

## Wireguard

Change the `03-wireguard.yaml` to your needs.

```yaml
SERVERURL: '192.168.178.104'
PEERS: 'sj-phone,sj-mac'
```
