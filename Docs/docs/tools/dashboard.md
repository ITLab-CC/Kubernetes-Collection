# Kubernetes-Dashboard

> I prefer to use the [Lens](https://k8slens.dev/) Dashboard instead of the Kubernetes Dashboard.

> Use `make` in `Dashboard` folder

[Siehe Helm Hub](https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard)

<details>
<summary>Click for Installation</summary>

```bash
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard

export POD_NAME=$(kubectl get pods -n kubernetes-dashboard -l "app.kubernetes.io/name=kubernetes-dashboard,app.kubernetes.io/instance=kubernetes-dashboard" -o jsonpath="{.items[0].metadata.name}")
kubectl expose pod $POD_NAME --port=8443 --target-port=8443 --type=LoadBalancer -n kubernetes-dashboard

```

`dashboard.admin-user.yml`

```bash

apiVersion: v1
kind: ServiceAccount
metadata:
name: admin-user
namespace: kubernetes-dashboard

```

`dashboard.admin-user-role.yml`

```bash

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
name: admin-user
roleRef:
apiGroup: rbac.authorization.k8s.io
kind: ClusterRole
name: cluster-admin
subjects:

- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard

```

Deploy the configs

```bash

sudo k3s kubectl create -f dashboard.admin-user.yml -f dashboard.admin-user-role.yml



```

</details>

## Get the Token

```bash
kubectl -n kubernetes-dashboard create token admin-user --duration=24h
```

https://172.30.62.166:8443/#/login
