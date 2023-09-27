# Storage

This is a collection of storage solutions for k3s.

NFS is used for the production environment.
Longhorn is more for testing purposes.

You can use the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) `local-path` for testing purposes. It is not recommended for production use.
