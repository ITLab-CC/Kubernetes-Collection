apply-config:
	kubectl apply -f coredns-cm.yaml
	kubectl rollout restart deployment coredns -n kube-system