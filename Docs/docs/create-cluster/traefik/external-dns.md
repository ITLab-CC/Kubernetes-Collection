## Config

`<email>` and `domain-filer` in `Traefik/external-dns/values.yaml`:

```yaml
env:
  - name: CF_API_KEY
    valueFrom:
      secretKeyRef:
        name: cloudflare-api-key
        key: api-key
  - name: CF_API_EMAIL
    value: '<email>'
```

```yaml
extraArgs:
  - --domain-filter=<your-domain>
```

Both `<api-key>` in `Traefik/cf-api-secret.yaml`:

```yaml
stringData:
  api-key: '<api-key>'
```

`<email>` in `Traefik/traefik-config.yaml`:

```yaml
env:
    - name: CF_API_EMAIL
    value: '<email>'
```

```bash
# Create the external-dns namespace
kubectl create namespace external-dns
# Create the Cloudflare API Key
kubectl apply -f cf-api-secret.yaml
# Apply the config for traefik from TLS
kubectl apply -f traefik-config.yaml


# Cert-Manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.crds.yaml
helm repo add jetstack https://charts.jetstack.io
helm install cert-manager --namespace cert-manager --version v1.13.0 jetstack/cert-manager --create-namespace

# External-DNS
helm repo add external-dns https://kubernetes-sigs.github.io/external-dns/
helm upgrade --install external-dns external-dns/external-dns --values external-dns/values.yaml --namespace external-dns
```

`annotations` in your `Ingress` definitions:

```yaml
annotations:
  traefik.ingress.kubernetes.io/router.entrypoints: websecure
  traefik.ingress.kubernetes.io/router.tls: 'true'
  traefik.ingress.kubernetes.io/router.tls.certresolver: myresolver
```

Siehe:

- https://kubernetes-sigs.github.io/external-dns/v0.12.2/tutorials/hostport/#kafka-stateful-set
- proxied
