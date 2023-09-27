# Troubleshooting

## Run a curl Pod

```bash
kubectl run mycurlpod --image=curlimages/curl -i --tty -- sh
```

## Dns Lookup

```bash
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml
kubectl exec -i -t dnsutils -- nslookup kubernetes.default
```
