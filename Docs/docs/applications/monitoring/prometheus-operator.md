# Prometheus Operator

The Prometheus Operator for Kubernetes provides easy monitoring definitions for Kubernetes services and deployment and management of Prometheus instances.

This is a helper that extends the Kubernetes API and allows you to manage Prometheus servers and configurations using Kubernetes native tools and workflows.

## Create the namepsace

```bash
kubectl create namespace monitoring
```

## Install

Use the `bundle.yaml` in the Prometheus-Operator folder to install the Operator.

```bash
kubectl apply --server-side -f bundle.yaml
```

## Check the deployment

```bash
kubectl get pods -n monitoring
```
