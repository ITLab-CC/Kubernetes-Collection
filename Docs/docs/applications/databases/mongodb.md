# MongoDB

[Docs](https://github.com/mongodb/helm-charts/tree/main/charts/community-operator){:target="\_blank"}

We will use the MongoDB Operator to manage our MongoDB instances.  
The MongoDB Operator is a Kubernetes Operator that manages the MongoDB instances.

In this example we will create a MongoDB Replica Set.
We will use it for our ShareLaTeX instance.

## Installation

```bash
helm repo add mongodb-helm-charts https://mongodb.github.io/helm-charts
# Install the MongoDB Operator
helm install my-community-operator mongodb-helm-charts/community-operator --namespace mongodb --create-namespace --set operator.watchNamespace="*"
# Deploy a MongoDB Replica Set
kubectl apply -f replicaset.yaml -n mongodb
# Check
kubectl get mdbc -n mongodb
```

### Connection String

Now you can get the connection string from the secret in the namespace `mongodb` with the pattern `<mongodb-resource-name>-<database>-<username>`. In our case it is `example-mongodb-admin-my-user`.

```bash
kubectl get secret example-mongodb-admin-my-user -n mongodb -o json | jq -r '.data | with_entries(.value |= @base64d)'
```

You can now use the `standardSrv` connection string to connect to the MongoDB Replica Set.
We will use it in our ShareLaTeX instance.

## Test

Connect with the `standardSrv` connection string to the MongoDB Replica Set.

```bash
kubectl run mongopod -i -t --image=rtsp/mongosh -- bash
> mongosh "<connection-string>"
```
