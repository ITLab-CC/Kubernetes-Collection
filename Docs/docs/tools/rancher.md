# Rancher (Not used)

Replace `IP_OF_LINUX_NODE`

```
helm repo add rancher-latest https://releases.rancher.com/server-charts/latest
kubectl create namespace cattle-system
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.11.0/cert-manager.crds.yaml
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.11.0
```

> Replace `IP_OF_LINUX_NODE` and `bootstrapPassword`

```
helm install rancher rancher-latest/rancher \
  --namespace cattle-system \
  --set hostname=IP_OF_LINUX_NODE.sslip.io \
  --set replicas=1 \
  --set bootstrapPassword=Admin123
```

Set `IP_OF_LINUX_NODE.sslip.io` to the IP of the Linux Node in your network or in the `/etc/hosts` file.

[https://172.30.62.166.sslip.io](https://172.30.62.166.sslip.io){:target="\_blank"}
