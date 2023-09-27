# Local connection

### Mac

```
brew install kubectl
brew install helm
```

Copy the Config from the `Manager Node` at `cat /etc/rancher/k3s/k3s.yaml`
to your lokal PC `~/.kube/config`

Change the `server` in the config to `https://172.30.62.166:6443`

Test the connection:

```
kubectl cluster-info dump
```
