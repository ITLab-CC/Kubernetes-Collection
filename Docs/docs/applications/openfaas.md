# OpenFaaS

OpenFaaS is a framework for building serverless functions with Docker and Kubernetes which has first class support for metrics. Any process can be packaged as a function enabling you to consume a range of web events without repetitive boiler-plate coding.

## Deploy

Use `make install` in the `OpenFaaS` folder to install in the Cluster.

### Get Password

```bash
PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)
	echo "OpenFaaS admin password: ${PASSWORD}"
```

Add the password to the `~/.bashrc` (or `~/.zshrc`) file:

```bash
export OPENFAAS_URL=http://openfaas.k3s.test:8080
```

Reload the shell.
Login to OpenFaaS:

```bash
echo -n $PASSWORD | faas-cli login --username admin --password-stdin
```

## OpenFaaS-Cli

```bash
# Mac
brew install faas-cli
```

[First Function](https://rpi4cluster.com/k3s/k3s-openfaas-function/){:target="\_blank"}
