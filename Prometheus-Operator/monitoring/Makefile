ALL_FOLDERS = alertmanager/,example-app/,grafana/,kube-state-metrics/,kubelet/,longhorn/,node-exporter/,traefik/

up: setup apply-config

setup:
	kubectl create namespace monitoring || true
	kubectl apply --server-side -f ../bundle.yaml


apply-config: apply-prometheus
	kubectl apply -f $(ALL_FOLDERS)

apply-prometheus:
	kubectl apply -f prometheus/ -R

delete:
	kubectl delete --ignore-not-found=true -f $(ALL_FOLDERS)
	kubectl delete namespace monitoring
