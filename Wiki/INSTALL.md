# Migrate from Mysql to Postgresql

- Start the new wikijs kube deployment with the postgresql database

```bash
make
```

- Copy the wiki-storage data from the previous installation (/root/wiki-storage/) to the new one (nfs://172.30.41.5/k3s-test-sj/wikijs/storage).

- Import the data:
  - https://wiki.k3s.it-lab.cc/a/utilities
  - Import the `Content + Uploads` from `local folder`: `/app/wiki/storage`
  - **Uncheck** the "Import users" option
