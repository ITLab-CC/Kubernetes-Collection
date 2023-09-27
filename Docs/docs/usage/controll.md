# Start/Stop Containers

Start Objects

```
kubectl apply -f folder/
```

Delete Objects

> Also deletes the storage
> {.is-danger}

```
kubectl delete -f folder/
```

"Stops" the Containers. (Real stop is not possible in k8s)

```
kubectl scale --replicas=0 -f kube/client-deployment.yaml,kube/db-deployment.yaml,kube/server-deployment.yaml,kube/proxy-deployment.yaml
```
