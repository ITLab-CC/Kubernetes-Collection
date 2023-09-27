# ArgoCD

ArgoCD is a declarative, GitOps continuous delivery tool for Kubernetes.
You can deploy applications to Kubernetes using GitOps principles.

## Install CLI

```bash
brew install argocd
```

## Install in cluster

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
# In ArgoCD Folder
kubectl apply -f configmap.yaml
kubectl apply -f ingress.yaml
# Restart the argocd-server deployment
kubectl rollout restart deployment argocd-server -n argocd
# Get the password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

[https://argocd.k3s.test/](https://argocd.k3s.test/){:target="\_blank"}

Now you can login with user `admin` and the password from above.
You should then change the password.
