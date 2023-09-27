# Redis

[Docs](https://ot-redis-operator.netlify.app/docs/){:target="\_blank"}

First we need the Redis Operator, we install it in the `ot-operators` namespace.
The Redis Operator is a Kubernetes Operator that manages the Redis instances.

## Redis Operator (Required)

```bash
helm install redis-operator ot-helm/redis-operator --namespace ot-operators --create-namespace
```

## Redis Instance

### Standalone

We can create a Redis Standalone instance by using the following command:
We will use it e.g. for [ShareLaTeX](/applications/custom/sharelatex).

```bash
helm install redis ot-helm/redis --namespace ot-operators
```

The FQDN to access the redis instance is `<name>.<namespace>.svc.cluster.local`.

So in our case it is `redis.ot-operators.svc.cluster.local`.
