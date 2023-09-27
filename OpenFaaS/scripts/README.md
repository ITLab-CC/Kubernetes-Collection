Change the user and sender in `mailme.yml`

Create the secrets:

```bash
kubectl create secret generic api-key --from-literal api-key="gr35p4inyyr4e9" --namespace openfaas-fn
kubectl create secret generic email-pass --from-literal email-pass="smtp_email_password_goes_here" --namespace openfaas-fn

```
