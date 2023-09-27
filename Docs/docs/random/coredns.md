# CoreDNS

> CoreDNS always appends the domain 'it-lab.cc' to the hostname. This is not wanted in our case. Therefore we have to change the CoreDNS config.

(Did not found a better solution)

We can use the rewrite Plugin to remove the `.it-lab.cc` from the hostname.

`coredns-cm.yaml` in `dns` folder

```yaml
rewrite name substring .com.it-lab.cc .com
```

Apply the config by running `make` in the `dns` folder
