# Install K8s

Install packages

```bash
apt update
apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y
```

Kernel modules for k8s networking

```bash
modprobe overlay
modprobe br_netfilter
cat <<EOF | tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF
```

Natting

```bash
cat <<EOF | tee /etc/sysctl.d/99-kubernetes-cri.conf
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF
sysctl --system
```

Add containerd keys and repos

```bash
curl https://download.docker.com/linux/debian/gpg | apt-key add
echo "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" > /etc/apt/sources.list.d/docker.list
```

Install containerd

```bash
apt update
apt install containerd.io -y
```

Configure containerd

```bash
containerd config default > /etc/containerd/config.toml
# set SystemdCgroup to true
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/g' /etc/containerd/config.toml
```

Disable swap!

```bash
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
swapoff -a
```

Restart containerd

```bash
systemctl enable containerd
systemctl restart containerd
```

Add k8s repos and install it

```bash
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
# install k8s and hold packags
apt update
apt install kubelet kubeadm kubectl -y
apt-mark hold kubelet kubeadm kubectl
```

Switch iptables to legacy

```bash
update-alternatives --config iptables
# --> select iptables-legacy
reboot
```

## Cluster erstellen:

POD-CIDR -> internal used to give every pod a unique ipv4
CRI Socket ->path to containerd/container runtime socket
Control-Plane-Endpoint: for single Control Plane: IP-OF-MASTER:6443, else IP:Port to use a Loadbalancer

```bash
kubeadm init --pod-network-cidr 10.244.0.0/16 --cri-socket /run/containerd/containerd.sock --control-plane-endpoint=<MASTER_IP>:6443
```

Copy kubectl config to home folder

```bash
mkdir -p $HOME/.kube
udo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

Setup Canal Network

```bash
mkdir ~/kube/config -p
cd ~/kube/config
curl https://raw.githubusercontent.com/projectcalico/calico/v3.26.0/manifests/canal.yaml -O
kubectl apply -f canal.yaml
```
