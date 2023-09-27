# Deployment

There are several ways to deploy applications to our cluster.
We can use the cli `kubectl` or a package manager like `helm` or `arkade`.

For continuous deployment via `git` we can use `ArgoCD`.
`ArgoCD` has a nice UI and is easy to use. It syncs with git and deploys the applications to the cluster.

Another way to deploy applications is with `terraform`. This is a good way to create services on the cluster. For example a database or a storage service. It is also possible to deploy applications with `terraform`.
It can also be used to create the cluster itself in the cloud.
