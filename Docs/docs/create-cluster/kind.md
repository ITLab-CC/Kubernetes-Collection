# Kind

With Kind we can create a local Kubernetes cluster. This is useful for testing and development.

The files are in the `kind` folder.

```bash
kind create cluster --name example-cluster --config kind-config.yaml
```

## Point kubectl to the local cluster

The context is `kind-` followed by the cluster `name`.

```bash
kubectl cluster-info --context kind-example-cluster
```

## Get the config

```bash
kubectl config view --minify --flatten --context kind-example-cluster
```
