# Postgres

We will use the [Postgres Operator](https://github.com/zalando/postgres-operator){:target="\_blank"} to deploy a Postgres Cluster.

## Deploy Postgres Operator

```bash
# add repo for postgres-operator
helm repo add postgres-operator-charts https://opensource.zalando.com/postgres-operator/charts/postgres-operator

# install the postgres-operator
helm install postgres-operator postgres-operator-charts/postgres-operator
```

Check if running

```bash
kubectl get pod -l app.kubernetes.io/name=postgres-operator
```

## Deploy Operator UI

```bash
# add repo for postgres-operator-ui
helm repo add postgres-operator-ui-charts https://opensource.zalando.com/postgres-operator/charts/postgres-operator-ui

# install the postgres-operator-ui
helm install postgres-operator-ui postgres-operator-ui-charts/postgres-operator-ui
```

Check if the UI is running

```bash
kubectl get pod -l app.kubernetes.io/name=postgres-operator-ui
```

[http://127.0.0.1:8081](http://127.0.0.1:8081){:target="\_blank"}

## Create a Postgres Cluster

```bash
kubectl create -f acid-cluster.yaml
```

Check if the cluster is running

```bash
# check the deployed cluster
kubectl get postgresql

# check created database pods
kubectl get pods -l application=spilo -L spilo-role

# check created service resources
kubectl get svc -l application=spilo -L spilo-role
```

### Password

As you can see in the acid-cluster.yaml there are multiple users and multiple databases.

```yaml
users:
    zalando:  # database owner
    - superuser
    - createdb
    foo_user: []  # role for application foo
  databases:
    foo: zalando  # dbname: owner
  preparedDatabases:
    bar: {}
```

The passwords are stored in secrets.
The password for the `postgres` user is stored in a secret. We can get the password with:

```bash
export PGPASSWORD=$(kubectl get secret postgres.acid-minimal-cluster.credentials.postgresql.acid.zalan.do -o 'jsonpath={.data.password}' | base64 -d)
echo $PGPASSWORD

# Use encrypted connections
export PGSSLMODE=require
```

The secret name is composed of: `<username>.<cluster-name>.credentials.postgresql.acid.zalan.do`

## For WikiJS

```bash
kubectl create -f wiki-cluster.yaml
```

Get the password for the `wikiuser` user:

```bash
export PGPASSWORD=$(kubectl get secret wikiuser.wiki-cluster.credentials.postgresql.acid.zalan.do -o 'jsonpath={.data.password}' | base64 -d)
echo $PGPASSWORD
```

The `host` is: `wiki-cluster.default.svc.cluster.local`
