#!/bin/bash
echo "=== Resetting kubeadm ==="
sudo kubeadm reset -f

echo "=== Removing packages ==="
sudo apt-get purge -y kubeadm kubectl kubelet kubernetes-cni
sudo apt-get autoremove -y
sudo apt-get clean

echo "=== Removing files ==="
sudo rm -rf /etc/kubernetes/
sudo rm -rf /var/lib/kubernetes/
sudo rm -rf /var/lib/kubelet/
sudo rm -rf /var/lib/etcd/
sudo rm -rf $HOME/.kube/
sudo rm -rf /root/.kube/
sudo rm -rf /etc/cni/
sudo rm -rf /var/lib/cni/
sudo rm -rf /opt/cni/
sudo rm -rf /run/flannel/

echo "=== Removing repo ==="
sudo rm -f /etc/apt/sources.list.d/kubernetes.list
sudo rm -f /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo "=== Cleaning network ==="
sudo iptables -F && sudo iptables -X
sudo iptables -t nat -F && sudo iptables -t nat -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo ip link delete cni0 2>/dev/null
sudo ip link delete flannel.1 2>/dev/null

echo "=== Restarting network ==="
sudo systemctl restart NetworkManager

echo "=== Done! Rebooting in 5 seconds ==="
sleep 5
sudo reboot
