#sudo apt-get update && sudo apt-get upgrade -y
#sudo apt-get install -y curl wget apt-transport-https ca-certificates gnupg lsb-release

## Disable swap now
#sudo swapoff -a
#
## Disable swap permanently
#sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
#
## Verify swap is off
#free -h
#
## Load required modules
#sudo tee /etc/modules-load.d/k8s.conf <<EOF
#overlay
#br_netfilter
#EOF
#
#sudo modprobe overlay
#sudo modprobe br_netfilter
#
## Verify modules loaded
#lsmod | grep br_netfilter
#lsmod | grep overlay

#sudo tee /etc/sysctl.d/k8s.conf <<EOF
#net.bridge.bridge-nf-call-iptables  = 1
#net.bridge.bridge-nf-call-ip6tables = 1
#net.ipv4.ip_forward                 = 1
#EOF
#
## Apply settings
#sudo sysctl --system
#
## Verify
#sysctl net.bridge.bridge-nf-call-iptables
#sysctl net.ipv4.ip_forward


## Add Docker repo (contains containerd)
#sudo install -m 0755 -d /etc/apt/keyrings -y
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
#  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
#sudo chmod a+r /etc/apt/keyrings/docker.gpg
#
#echo \
#  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
#  https://download.docker.com/linux/ubuntu \
#  $(lsb_release -cs) stable" | \
#  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
#
#sudo apt-get update
#sudo apt-get install -y containerd.io
#
## Configure containerd
#sudo mkdir -p /etc/containerd
#sudo containerd config default | sudo tee /etc/containerd/config.toml
#
## Enable SystemdCgroup (very important!)
#sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' \
#  /etc/containerd/config.toml
#
## Restart and enable containerd
#sudo systemctl restart containerd
#sudo systemctl enable containerd
#
## Verify
#sudo systemctl status containerd
#
#
## Add Kubernetes repo
#curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.32/deb/Release.key | \
#  sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
#
#echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] \
#  https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /" | \
#  sudo tee /etc/apt/sources.list.d/kubernetes.list
#
## Install
#sudo apt-get update
#sudo apt-get install -y kubelet kubeadm kubectl
#
## Hold versions to prevent auto upgrade
#sudo apt-mark hold kubelet kubeadm kubectl
#
## Verify versions
#kubeadm version
#kubectl version --client
#kubelet --version
#
#
## Get your IP address
#MY_IP=$(ip addr show | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 | head -1)
#echo "My IP: $MY_IP"
#
## Initialize cluster
#sudo kubeadm init \
#  --pod-network-cidr=10.244.0.0/16 \
#  --apiserver-advertise-address=$MY_IP \
#  --node-name=$(hostname) \
#  2>&1 | tee kubeadm-init.log
#
## Check init was successful
#echo "Exit code: $?"

mkdir -p $HOME/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $USER:$USER $HOME/.kube/config

# Verify
kubectl get nodes
kubectl cluster-info

# Install flannel
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml

# Create subnet.env (fixes common flannel issue)
sudo mkdir -p /run/flannel/
sudo tee /run/flannel/subnet.env <<EOF
FLANNEL_NETWORK=10.244.0.0/16
FLANNEL_SUBNET=10.244.0.1/24
FLANNEL_MTU=1450
FLANNEL_IPMASQ=true
EOF

# Verify flannel pods
kubectl get pods -n kube-flannel

# Install flannel
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml

# Create subnet.env (fixes common flannel issue)
sudo mkdir -p /run/flannel/
sudo tee /run/flannel/subnet.env <<EOF
FLANNEL_NETWORK=10.244.0.0/16
FLANNEL_SUBNET=10.244.0.1/24
FLANNEL_MTU=1450
FLANNEL_IPMASQ=true
EOF

# Verify flannel pods
kubectl get pods -n kube-flannel

# Remove taint so pods can run on master
kubectl taint nodes --all node-role.kubernetes.io/control-plane-

# Verify taint removed
kubectl describe node $(hostname) | grep Taint
# Should show: <none>

# Debian/Ubuntu
sudo apt-get install -y kubernetes-cni

# OR manually download (replace with latest version)
CNI_VERSION="v1.4.0"
sudo mkdir -p /opt/cni/bin
curl -L "https://github.com/containernetworking/plugins/releases/download/${CNI_VERSION}/cni-plugins-linux-amd64-${CNI_VERSION}.tgz" \
  | sudo tar -C /opt/cni/bin -xz
