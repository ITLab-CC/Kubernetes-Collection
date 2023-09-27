# Longhorn

[Siehe Longhorn Docs](https://longhorn.io/docs/1.5.1/deploy/install/install-with-helm/)
[Longhorn Examples](https://github.com/longhorn/longhorn/tree/master/examples)

## Requirements

```
apt install jq nfs-common -y
```

Check Script

```
curl -sSfL https://raw.githubusercontent.com/longhorn/longhorn/v1.5.1/scripts/environment_check.sh | bash
```

## Install

Use `make` in `Longhorn` folder

```
helm repo add longhorn https://charts.longhorn.io
helm repo update
helm install longhorn longhorn/longhorn --namespace longhorn-system --create-namespace --version 1.5.1
```

Check deployment (5-10 Minutes), till all pods are up

```
kubectl -n longhorn-system get pod
```

[Make the Longhorn accessable via Web Dashboard](https://longhorn.io/docs/1.5.1/deploy/accessing-the-ui/longhorn-ingress/)
