Cluster Maintainance

kubectl get deployment
kubectl get pods -o wide
kubectl drain node01 --ignore-daemonsets #Remove node for maintainance an pod will be died
kubectl get pods -o wide
kubectl uncordon node01 #Pod can be scheduled again
kubectl describe node controlplane
kubectl cordon node03 #unschedule pod 

ETCD and core dns have different versions #kube api server controller etc have same version
1.20.2

kube-apiserver always higher than other components
but kubectl can be same or higher or lower version of kube-apiserver

Always upgrade only one minor version

Always first upgrade master/controlplane then upgrade worker nodes

Note: Always start one minor version by other minor version instead of jumping to higher version directly


for Worker node upgrade process
please execute commands on the controlplane
kubectl drain node01 --ignore-daemonsets
kubectl uncordon node01 --ignore-daemonsets


controlplane $ kubectl describe node controlplane|grep -i taint
Taints:             <none>
controlplane $ kubectl describe node node01|grep -i taint
Taints:             <none>

If taints are none we can have nodes scheduled

kubectl describe node controlplane|grep -i taint
kubectl describe node node01|grep -i taint
kubectl get deployment -o wide
kubectl get pods -o wide
kubeadm upgrade plan
kubectl drain controlplane --ignore-daemonsets
kubectl get nodes

apt update -y && apt-get upgrade kubelet -y 
apt install kubelet=1.19.0
apt upgrade kubelet -y

kubectl logs etcd-controlplane -n kube-system
kubectl describe pod etcd-controlplane -n kube-system
kubectl describe pod etcd-controlplane -n kube-system |grep "\--listen-client-urls"

backup
ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 \
--cacert=/etc/kubernetes/pki/etcd/ca.crt \
--cert=/etc/kubernetes/pki/etcd/server.crt \
--key=/etc/kubernetes/pki/etcd/server.key \
snapshot save /opt/snapshot-pre-boot.db


restore

ETCDCTL_API=3 etcdctl  --data-dir /var/lib/etcd-from-backup \
snapshot restore /opt/snapshot-pre-boot.db

