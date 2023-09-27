# Expose

## Temporary:

```
kubectl port-forward pods/mongo-75f59d57f4-4nd6q 28015:27017
```

## Permanently:

```
kubectl expose deployment <deployment_name> --port=8765 --target-port=9376 --name=example-service --type=LoadBalancer
```

You can also replace deployment with `pod`

`target-port` = in Container