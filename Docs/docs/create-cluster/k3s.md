# K3s

[Siehe K3s Docs](https://docs.k3s.io/quick-start)

[Inspired by Rpi4Cluster.com](https://rpi4cluster.com/)

## Master

```
curl -sfL https://get.k3s.io | sh -
```

Use the kubeconfig from `/etc/rancher/k3s/k3s.yaml` to connect to the cluster.

## Nodes

Get token from `/var/lib/rancher/k3s/server/node-token`

```
curl -sfL https://get.k3s.io | K3S_URL=https://172.30.62.166:6443 K3S_TOKEN=<TOKEN>  sh -
```

## Label the Nodes

```bash
kubectl label nodes <node-name> node-role.kubernetes.io/worker=worker node-type=worker
```
