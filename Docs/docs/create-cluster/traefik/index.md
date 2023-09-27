# Networking - Traefik

> Simply use `kubectl apply -f .` in the `Traefik` folder to apply all files.

We configure traefike to do the following:

- Expose the dashboard on port `9000`
- Middleware to redirect `http` to `https`
- Middleware for basic auth
- Middleware for cors

[Refernce](https://qdnqn.com/how-to-configure-traefik-on-k3s/){:target="\_blank"}

## Expose the Dashboard

`traefik.yaml`

```yaml
apiVersion: helm.cattle.io/v1
kind: HelmChartConfig
metadata:
  name: traefik
  namespace: kube-system
spec:
  valuesContent: |-
    additionalArguments:
      - "--api"
      - "--api.dashboard=true"
      - "--api.insecure=true"
      - "--log.level=DEBUG"
    ports:
      traefik:
        expose: true
    providers:
      kubernetesCRD:
        allowCrossNamespace: true
```

`kubectl apply -f traefik.yaml`

[Expose Services](../../usage/expose)

[http://172.30.62.166:9000/dashboard/#/](http://172.30.62.166:9000/dashboard/#/){:target="\_blank"}

## Basic Auth

First we need an Traefik Middleware. We define it in the default namespace, because we will use it in all namespaces.
The credentials are `admin:admin` and are base64 encoded.

You can encode your own credentials with:

```bash
echo -n 'admin' | base64
```

Create the Middleware:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-auth
  namespace: default
type: kubernetes.io/basic-auth
data:
  username: YWRtaW4=
  password: YWRtaW4=
---
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: my-auth-middleware
  namespace: default
spec:
  basicAuth:
    removeHeader: true
    secret: my-auth
```

### Use the Middleware in the Ingress annotation:

`<namespace>-<middleware-name>@kubernetescrd`

`default-my-auth-middleware@kubernetescrd`

> Use at the end of the list => Redirect to HTTPS before authentication

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  namespace: linkerd-viz
  annotations:
    kubernetes.io/ingress.class: traefik
    traefik.ingress.kubernetes.io/router.middlewares: default-cors@kubernetescrd,default-redirectscheme@kubernetescrd,default-my-auth-middleware@kubernetescrd
spec:
  rules:
    - host: linkerd.k3s.test
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web
                port:
                  number: 8084
```

## CORS

```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: cors
  namespace: default
spec:
  headers:
    accessControlAllowOriginList:
      - 'https://hub.k3s.it-lab.cc'
    accessControlAllowMethods:
      - HEAD
      - GET
```

## Redirect HTTP to HTTPS

```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: redirectscheme
  namespace: default
spec:
  redirectScheme:
    scheme: https
    permanent: true
```
