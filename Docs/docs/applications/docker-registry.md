# Docker Registry

```bash
echo "192.168.178.104 registry registry.k3s.test" >> /etc/hosts

```

```bash
ctr image pull --platform linux/amd64 docker.io/rancher/coredns-coredns:1.6.3
ctr content fetch --platform linux/amd64 docker.io/rancher/coredns-coredns:1.6.3
ctr image tag docker.io/rancher/coredns-coredns:1.6.3 registry.k3s.test:5000/test
ctr image push --platform linux/amd64 --plain-http registry.k3s.test:5000/test
curl http://registry.k3s.test:5000/v2/_catalog
    => {"repositories":["test"]}
```
