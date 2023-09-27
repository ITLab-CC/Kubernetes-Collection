# Linkerd

Linkerd is a service mesh for Kubernetes and other frameworks. It makes running services easier and safer by giving you runtime debugging, observability, reliability, and security—all without requiring any changes to your code.

## CLI

```bash
# Mac
brew install linkerd
```

## Install in cluster

```bash
linkerd check --pre
linkerd install --crds | kubectl apply -f -
linkerd install | kubectl apply -f -
linkerd check
```

### Run a Demo App

```bash
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/emojivoto.yml | kubectl apply -f -

# Expose (for reference)
kubectl -n emojivoto port-forward svc/web-svc 8080:80
```

[http://127.0.0.1:8080](http://127.0.0.1:8080){:target="\_blank"}

Try to vote for the **donut** emoji, you’ll get a **404** page.

Don’t worry, these errors are intentional. (In a later guide, we’ll show you how to use [Linkerd to identify the problem.](https://linkerd.io/2.14/debugging-an-app/))

Inject Linkerd

```bash
kubectl get -n emojivoto deploy -o yaml \
  | linkerd inject - \
  | kubectl apply -f -

# Check the data planes
linkerd -n emojivoto check --proxy
```

### Viz

```bash
linkerd viz install --set dashboard.enforcedHostRegexp=".*" | kubectl apply -f - # install the on-cluster metrics stack
linkerd check

linkerd viz dashboard &
```

You can now see the dashboard and navigate to the **emojivoto** namespace.

You should see the `web` deployment with a `Success Rate` below 100%.

#### Expose Permanent

```bash
kubectl apply -f linkerd
```
