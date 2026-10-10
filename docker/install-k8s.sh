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
#sudo kubeadm init --pod-network-cidr=10.244.0.0/16   --apiserver-advertise-address=$MY_IP --node-name=$(hostname) 2>&1 | tee kubeadm-init.log
#
## Check init was successful
#echo "Exit code: $?"

sudo apt-get update
# apt-transport-https may be a dummy package; if so, you can skip that package
sudo apt-get install -y apt-transport-https ca-certificates curl gpg
# If the directory `/etc/apt/keyrings` does not exist, it should be created before the curl command, read the note below.
# sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.37/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.37/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl

sudo systemctl enable --now kubelet

sudo kubeadm init --pod-network-cidr=10.244.0.0/16   --apiserver-advertise-address=192.168.0.149 --node-name=$(hostname) 2>&1 | tee kubeadm-init.log

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl get nodes
kubectl get pods -A
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
