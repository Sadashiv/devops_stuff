Containers Everywhere=New
Dcoker container command don't have feature to scale up/down

By using the swarm we can achieve it

Swarm mode build in orachestration
-Swarm mode is clustering solution built inside docker

By default the docker swarm is inactive
you can make it acitve by command

$sudo docker init
 Root signing ceritificate created for our own
 Ceritficate issued for first manager
 Join tokens are created
 In background raft database created to store CA, config and secrets

$sudo docker node ls
 Only one leader at time
 ID                            HOSTNAME                 STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
 huu78rhltkz9q4dgkrxq7vo6x *   sadashiv-ThinkPad-E480   Ready               Active              Leader              19.03.3

$sudo docker serivce ls
$sudo docker container ls

[sadashiv@sadashiv-ThinkPad-E480 docker (master )]$ sd service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
3ci600stgkx4        cocky_swartz        replicated          1/1                 apache:latest
od692nddop49        hopeful_raman       replicated          1/1                 apache:1.1
38q56z7m5wjh        vibrant_lamarr      replicated          1/1                 centos:latest
[sadashiv@sadashiv-ThinkPad-E480 docker (master )]$ sudo docker service update 3ci600stgkx4 --replicas 3


[sadashiv@sadashiv-ThinkPad-E480 docker (master )]$ sd service rm cocky_swartz hopeful_raman vibrant_lamarr
cocky_swartz
hopeful_raman
vibrant_lamarr

[sadashiv@sadashiv-ThinkPad-E480 docker (master )]$ sd service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS

[sadashiv@sadashiv-ThinkPad-E480 docker (master )]$ sd container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

That's how the orchestration works and it brins up container if any continer goes down


K8 vs swarm
k8 installation varies os to os
swarm come with default docker just make "docker swarm init" to start

k8 support logging(kibana/ELK) and Grafana fro monitoring
Swarm supported inly with third party applications

Kubernetes is more of an all-in-one framework for distributed systems.
Docker Swarm can deploy containers faster; this allows fast reaction times to scale on demand.

Benefits & drawbacks of Kubernetes

Benefits of Kubernetes:
Kubernetes is backed by the Cloud Native Computing Foundation (CNCF).
Kubernetes have an impressively huge community among container orchestration tools. Over 50,000 commits and 1200 contributors.
Kubernetes is an open source and modular tool that works with any OS.
Kubernetes provides easy service organization with pods

Drawbacks of Kubernetes
When doing it yourself, Kubernetes installation can be quite complex with steep learning curve. An option to solve this issue is to opt for a managed Kubernetes-as-a-service such as ours.
In Kubernetes, it is required to have a separate set of tools for management, including kubectl CLI.
It is Incompatible with existing Docker CLI and Compose tools

Benefits & drawbacks of Docker Swarm

Benefits of Docker Swarm
Docker Swarm is easy to install with a fast setup
Docker Swarm is a lightweight installation. It is simpler to deploy and Swarm mode is included in the Docker engine.
Docker Swarm has an easier learning curve.
Docker Swarm smoothly integrates with Docker Compose and Docker CLI. That’s because these are native Docker tools. Most of the Docker CLI commands will work with Swarm.

Drawbacks of Docker Swarm
Docker Swarm provides limited functionality.
Docker Swarm has limited fault tolerance.
Docker Swarm have smaller community and project as compared to Kubernetes community
In Docker Swarm, services can be scaled manually.



