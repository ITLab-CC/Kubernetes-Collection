run:
	kubectl apply -f a_namespace.yaml
	kubectl create configmap config-configmap --from-file=config/config.yml -n wiki-ns
	kubectl apply -f wiki-deployment.yaml,wiki-service.yaml,wiki-ingress.yaml -n wiki-ns

delete:
	kubectl delete -f a_namespace.yaml

reapply-config:
	kubectl delete configmap config-configmap -n wiki-ns
	kubectl create configmap config-configmap --from-file=config/config.yml -n wiki-ns
	kubectl apply -f wiki-deployment.yaml,wiki-service.yaml,wiki-ingress.yaml -n wiki-ns