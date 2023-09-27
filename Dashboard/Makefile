full: install deploy

install:
	helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
	helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
	POD_NAME=$(kubectl get pods -n kubernetes-dashboard -l "app.kubernetes.io/name=kubernetes-dashboard,app.kubernetes.io/instance=kubernetes-dashboard" -o jsonpath="{.items[0].metadata.name}")
	kubectl expose pod ${POD_NAME} --port=8443 --target-port=8443 --type=LoadBalancer -n kubernetes-dashboard

deploy:
	kubectl create -f dashboard.admin-user.yml -f dashboard.admin-user-role.yml

get-token:
	kubectl -n kubernetes-dashboard create token admin-user --duration=24h