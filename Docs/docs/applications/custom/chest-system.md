# Chest-System

The Chest-System is a system developed by IT-Lab to store and manage items in chests.

## Installation

> Refers to the `chest-system` folder

### Prerequisites

!!! note

    First we need a `Postgres` database. Please refer to [Postgres](/applications/databases/postgresql).

### Config

Edit the database credentials in the `server-deployment.yaml` file:

```yaml
- name: POSTGRES_DB
    value: chest
- name: POSTGRES_HOST
    value: chest-cluster # We can use the service name without namespace because we are in the same namespace
- name: POSTGRES_PASSWORD
    valueFrom:
    secretKeyRef:
        key: password
        name: chestuser.chest-cluster.credentials.postgresql.acid.zalan.do # The secret name is composed of: <username>.<cluster-name>.credentials.postgresql.acid.zalan.do
- name: POSTGRES_USER
    value: chestuser
```

### Deploy

```bash
kubectl apply -f .
```
