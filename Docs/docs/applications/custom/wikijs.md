# WikiJS

WikiJS is a modern, lightweight and powerful wiki app built on NodeJS, Git and Markdown.

[Docs](https://docs.requarks.io/){:target="\_blank"}

## Requirements

!!! note

    First we need a `Postgres` database. Please refer to [Postgres](../../databases/postgresql).

## Install

> You can simply use the `make` command in the `Wiki` folder to make the config and apply the files

### Namespace

Create the namespace for the application:

```bash
kubectl create ns wiki-ns
```

### Config

Edit the database `config/config.yml` based on the [Postgres](../../databases/postgresql) config.

- `db.host`: `<postgres-service-name>.<namespace>.svc.cluster.local`
- `db.port`: `5432`
- `db.user`: The user you defined for the database
- `db.pass`: The password for the user from the secret.

Create the configmap from the file:

```bash
kubectl create configmap config-configmap --from-file=config/config.yml -n wiki-ns
```

### Deployment

Deploy the application:

```bash
kubectl apply -f wiki-deployment.yaml,wiki-service.yaml,wiki-ingress.yaml -n wiki-ns
```

Access the application:
[https://wiki.k3s.test](https://wiki.k3s.test){:target="\_blank"}
