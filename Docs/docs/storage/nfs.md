# NFS Storage

```

helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/

helm install nfs-subdir-external-provisioner --namespace nfs-subdir-external-provisioner --create-namespace nfs-subdir-external-provisioner/nfs-subdir-external-provisioner --set nfs.server=172.30.41.5 --set nfs.path=/k3s-test-sj

```

Set NFS as default

```

# Mark local-path as non-default

kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'

# Mark nfs-client as default

kubectl patch storageclass nfs-client -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

kubectl get storageclass

```
