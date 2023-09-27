install:
	arkade install openfaas
	kubectl apply -f .
	PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)
	echo "OpenFaaS admin password: ${PASSWORD}"