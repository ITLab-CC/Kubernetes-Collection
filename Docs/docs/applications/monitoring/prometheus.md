# Prometheus

> In the `monitoring` folder

First wie create the config for the additional scrape jobs. The output is written to `prometheus/additional-scrape-configs.yaml`.

```bash
kubectl create secret generic additional-scrape-configs -n monitoring --from-file=prometheus/additional-job/prometheus-additional-job.yaml --dry-run=client -oyaml > prometheus/additional-scrape-configs.yaml
```

Then we create the Prometheus Instance with the following command:

```bash
kubectl apply -f prometheus/
```

> You can also use the `make apply-config` command in the `monitoring` folder
