install-full: install-longhorn install-ui	

install-longhorn:
	helm repo add longhorn https://charts.longhorn.io
	helm repo update
	helm install longhorn longhorn/longhorn --namespace longhorn-system --create-namespace --version 1.5.1

install-ui:
	kubectl -n longhorn-system create secret generic basic-auth --from-file=auth
	kubectl -n longhorn-system apply -f ingress.yaml
