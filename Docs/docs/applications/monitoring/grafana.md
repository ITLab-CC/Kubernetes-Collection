# Grafana

Deploy Grafana

```bash
kubectl apply -f grafana/
```

Login with `admin` and `admin`

Go to **Settings** > **Data Sources** and add the Prometheus Data Source with the following URL: `http://prometheus:9090`

Import the dashboard with the ID `8171` from the Grafana Dashboard Store.
