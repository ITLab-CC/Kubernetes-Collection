# Service Monitor

The Files are in seperate folders for each application.

## Longhorn

Apply the Longhorn Service Monitor

```bash
kubectl apply -f longhorn/
```

### Check the Deamonset

```bash
➜  kubectl get daemonset -n longhorn-system

NAME DESIRED CURRENT READY UP-TO-DATE AVAILABLE NODE SELECTOR AGE
longhorn-manager 2 2 2 2 2 <none> 2d19h

```

## Kube State Metrics

Kube State Metrics (KSM) is a simple service that listens to the Kubernetes API server and generates metrics about the state of the objects.

Apply the Kube State Metrics Service Monitor

```bash
kubectl apply -f kube-state-metrics/
```

## Node-Exporter

The Prometheus Node Exporter exposes a wide variety of hardware- and kernel-related metrics.

Apply the Node-Exporter Service Monitor

```bash
kubectl apply -f node-exporter/
```

## Kubelet

The Kubelet is the primary “node agent” that runs on each node. It can register the node with the apiserver using one of: the hostname; a flag to override the hostname; or specific logic for a cloud provider.

Apply the Kubelet Service Monitor

```bash
kubectl apply -f kubelet/
```

## Traefik

Traefik is an open-source Edge Router that makes publishing your services a fun and easy experience. It receives requests on behalf of your system and finds out which components are responsible for handling them.

We will also use it to expose the Prometheus and Alertmanager UIs.

Apply the Traefik Service Monitor

```bash
kubectl apply -f traefik/
```

## Check the Service Monitors

```bash
➜  Monitoring git:(main) ✗ kubectl get ServiceMonitor -n monitoring
NAME                                 AGE
longhorn-prometheus-servicemonitor   39h
node-exporter                        39h
kube-state-metrics                   39h
kubelet                              39h
traefik                              38h
```
