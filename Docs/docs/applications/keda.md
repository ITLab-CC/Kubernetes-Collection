# KEDA

KEDA is a Kubernetes-based Event Driven Autoscaler. With KEDA, you can drive the scaling of any container in Kubernetes based on the number of events needing to be processed.

## Install in Cluster

```bash
helm repo add kedacore https://kedacore.github.io/charts
helm repo update
helm install keda kedacore/keda --namespace keda --create-namespace
```

## Scalers

[KEDA Scalers](https://keda.sh/docs/2.11/scalers/){:target="\_blank"}

### Prometheus

```bash
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: prometheus-scaledobject
  namespace: whoami-ns
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: instrumented
  triggers:
    - type: prometheus
      metadata:
        serverAddress: http://prometheus.monitoring.svc.cluster.local:9090
        metricName: http_request_total
        query: http_requests_total{code="200",handler="prometheus",method="get", service="instrumented-service"}
        threshold: '50'
  idleReplicaCount: 0
  minReplicaCount: 3
  maxReplicaCount: 10
```

### CPU

```bash
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: prometheus-scaledobject
  namespace: whoami-ns
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: instrumented
  triggers:
    - type: cpu
      metricType: Utilization # Allowed types are 'Utilization' or 'AverageValue'
      metadata:
        value: '180'
  idleReplicaCount: 0
  minReplicaCount: 3
  maxReplicaCount: 10
```
