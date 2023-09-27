# Manifests

## Create a Manifest from a Docker Image

```bash
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > nginx-deployment.yaml
```
