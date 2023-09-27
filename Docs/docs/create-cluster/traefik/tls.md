# Traefik - TLS

We will configure Traefik to use Letsencrypt `DNS Challenges` to automatically generate TLS certificates for our services.

## Prerequisites

We need an account with a DNS provider that supports the [ACME DNS Challenge](https://docs.traefik.io/https/acme/#dnschallenge) and a domain name.

We will use [Cloudflare](https://www.cloudflare.com/) as our DNS provider.

## Cloudflare

Get the Global API Key from your Cloudflare account.
[Get your "Global API Key"](https://dash.cloudflare.com/profile/api-tokens){target=\_blank}

## Traefik

Now we need to configure Traefik to use the Cloudflare DNS Challenge.
Refer to the `traefik/traefik-config.yml` file.

Uncomment the `additionalArguments` for the resolver and replace the `<email>` with your email address.

```yaml
- '--certificatesresolvers.myresolver.acme.dnschallenge=true'
- '--certificatesresolvers.myresolver.acme.dnschallenge.provider=cloudflare'
- '--certificatesresolvers.myresolver.acme.email=<email>'
- '--certificatesresolvers.myresolver.acme.storage=/data/acme.json'
```

Then uncomment the `env` for the Cloudflare API Key and replace the `<email>` and `<key>` with your Email and Global API Key.

```yaml
env:
  - name: CF_API_EMAIL
    value: '<email>'
  - name: CF_API_KEY
    value: '<api_key>' #<== Unter https://dash.cloudflare.com/profile/api-tokens "Global API Key"
```

## Deploy Traefik

Deploy Traefik with the new configuration.

```bash
kubectl apply -f traefik-config.yaml
```

## Usage

Now we can use the `myresolver` in our `Ingress` definitions.

```yaml
annotations:
  traefik.ingress.kubernetes.io/router.entrypoints: websecure
  traefik.ingress.kubernetes.io/router.tls: 'true'
  traefik.ingress.kubernetes.io/router.tls.certresolver: myresolver
```

Please note that the `host` in the `Ingress` definition must match the domain name.

## Trouble Shooting

Check the logs of the Traefik pod.

```bash
kubectl logs deploy/traefik -n kube-system
```

Pay attention to the name of the `certresolver`. The name in the `traefik-config.yml` must match the name in the `Ingress` definition.
