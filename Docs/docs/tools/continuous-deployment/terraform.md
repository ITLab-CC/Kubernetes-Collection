# Terraform

With Terraform we can create services on the cluster.

Now we can connect terraform to the Cluster.
First we need to get the config for the cluster with kubectl.

```bash
kubectl config view --minify --flatten
```

This will give us the config to connect to the cluster. We need to add this to the terraform file.

Fill these values in the `terraform.tfvars` file.

```bash
host = clusters.cluster.server
client_certificate = users.user.client-certificate
client_key = users.user.client-key
cluster_ca_certificate = clusters.cluster.certificate-authority-data

# Example:
host                   = "https://127.0.0.1:32768"
client_certificate     = "LS0tLS1CRUdJTiB..."
client_key             = "LS0tLS1CRUdJTiB..."
cluster_ca_certificate = "LS0tLS1CRUdJTiB..."
```

## Example: Homer

In the `homer` folder we have an example of how to use terraform to create a service on the cluster.

First we need to declare the `terraform.tfvars` file. We can copy the `terraform.tfvars.example` file and fill in the values.

```bash
cp terraform.tfvars.example terraform.tfvars
vim terraform.tfvars
```

    Then we can run terraform.

```bash
terraform apply
```

### Config

The `configmap.tf` file holds the configmap of the service. It reads the `homer-config.yaml` file in the folder.
The `deployment.tf` file holds the deployment of the service. It mounts the configmap as a volume.

The `terraform.tfvars` file holds the variables for the connection to the cluster.
The `provider.tf` file holds the connection to the cluster.
The `service.tf` file holds the service of the service.
