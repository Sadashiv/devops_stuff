Docker Concepts:
https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index
https://docs.docker.com/compose/compose-file/
https://docs.docker.com/develop/dev-best-practices/
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
https://docs.docker.com/engine/reference/builder/


What is Docker?
Docker is an open platform for developing, shipping, and running applications.
Docker is a platform for developers and sysadmins to develop, deploy, and run applications with containers.
The use of Linux containers to deploy applications is called containerization.
Containers are not new, but their use for easily deploying applications is.

The Docker platform
Docker provides the ability to package and run an application in a loosely isolated environment called a container.
The isolation and security let you run many containers simultaneously on a given host. 
Containers are lightweight and contain everything needed to run the application, so you don't need to rely on what's installed on the host.

What is a Docker Image?
A Docker image is an immutable (unchangeable) file that contains the source code, libraries, dependencies, tools, 
and other files needed for an application to run.
Docker image template/read-only/snapshots

Docker architecture
Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building,
running, and distributing your Docker containers. The Docker client and daemon can run on the same system,
or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API,
over UNIX sockets or a network interface. Another Docker client is Docker Compose, that lets you work with applications consisting of a set of containers.

The Docker daemon
The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes.
A daemon can also communicate with other daemons to manage Docker services.

The Docker client
The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run,
the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.

Docker objects
When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects. This section is a brief overview of some of those objects.


Unlike virtual machines (VMs) where virtualization happens at the hardware level, containers virtualize at the app layer.
They can utilize one machine, share its kernel, and virtualize the operating system to run isolated processes.
This makes containers extremely lightweight, allowing you to retain valuable resources.

Minikube installation
URL: https://minikube.sigs.k8s.io/docs/start/
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb

Containerization is increasingly popular because containers are:

Flexible: Even the most complex applications can be containerized.
Lightweight: Containers leverage and share the host kernel.
Interchangeable: You can deploy updates and upgrades on-the-fly.
Portable: You can build locally, deploy to the cloud, and run anywhere.
Scalable: You can increase and automatically distribute container replicas.
Stackable: You can stack services vertically and on-the-fly.

Docker server also called engine
docker version -> verified cli can task to engine
docker info ->Most config values of engine

Old and new way of running docker commands
docker container run - new way of run
docker run - Old way of run

Images and containers
A container is launched by running an image. An image is an executable package that includes everything
needed to run an application the code, a runtime, libraries, environment variables, and configuration files.

A container is a runtime instance of an image --what the image becomes in memory when executed
(that is, an image with state, or a user process). You can see a list of your running containers with the command,
docker ps, just as you would in Linux.

Image vs Container
Image contains binaries, libraries and source code all make to run application
Container is instance of that image running as process
Docker default image registry is called docker hub(hub.docker.com)

Containers and virtual machines
A container runs natively on Linux and shares the kernel of the host machine with other containers.
It runs a discrete process, taking no more memory than any other executable, making it lightweight.

By contrast, a virtual machine (VM) runs a full-blown “guest” operating system with virtual access to host
resources through a hypervisor. In general, VMs provide an environment with more resources than most applications need.

Install Docker on Ubutnu
Uninstall
sudo rm -f /etc/apt/sources.list.d/docker.list
sudo rm -f /etc/apt/keyrings/docker.gpg
sudo apt-get remove -y docker docker-engine docker.io docker-ce docker-ce-cli containerd containerd.io runc
sudo apt-get purge -y docker.io containerd.io containerd
sudo apt-get autoremove -y

Install

sudo apt-get update
sudo apt-get install -y docker.io containerd docker-buildx
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
newgrp docker
sudo docker run hello-world

sudo curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
docker compose version

docker run -it linux_user_mgmt:0.3 bash
apt update && apt install -y nodejs
docker container commit -m "Added nodejs" 2d071a3d77a8(container id)  sadashiv (new image name)
docker image history sadashiv
docker run sadashiv node -e "console.log('Hello again')"

$ docker image ls<br/>

Recap and cheat sheet
## List Docker CLI commands
docker container --help

## Display Docker version and info
docker --version<br/>
docker version<br/>
docker info

## List Docker containers (running, all, all in quiet mode)
docker container ls<br/>
docker container ls --all<br/>
docker container ls -aq<br/>

Build Image
docker build -t apache:v1.5 -f Dockerfile_apache .<br/>
docker image build -t apache:v1.5 -f Dockerfile_apache . --no-cache=true<br/>

Create tag in local<br/>
docker tag <image_name> username/repository:<tag_version>
docker tag lum:1.0 lum:latest

Push image to public<br/>
docker push username/repository:t<ag_version>

# Set proxy server, replace host:port with values for your servers
ENV http_proxy host:port<br/>
ENV https_proxy host:port<br/>

DNS Settings<br/>
/etc/docker/daemon.json with the dns key, as following:

{
  "dns": ["your_dns_address", "8.8.8.8"]
}

--> Always create docker container then start and attach to enter into the container
Run in the background
docker run -d -p 4000:80 centos

Stop container with ID
docker container stop <containerid>

A registry is a collection of repositories, and a repository is a collection of images—sort of like a GitHub repository,
except the code is already built. An account on a registry can create many repositories. 
The docker CLI uses Docker’s public registry by default.

set environment and memory details command line
docker run -e POSTGRES_PASSWORD=secret --memory="512m" --cpus="0.5" postgres

Run docker container<br/>
docker run -p 5000:80 9538253250/testing:latest

Get the ipaddress of docker container<br/>
docker inspect  2c8f59c4cd14 | grep IPAddress

docker run --name containername -it  centos /bin/bash<br/>
docker run --name portal -it portal:v0.0.1 /bin/bash


$ vim docker-compose.yaml<br/>
$ docker stack deploy -c docker-compose.yaml getwebapp<br/>
Creating network getwebapp_webnet<br/>
Creating service getwebapp_web<br/>

$ docker service ls<br/>
ID                  NAME                MODE                REPLICAS            IMAGE                       PORTS<br/>
1kv11tg86qtm        getwebapp_web       replicated          5/5                 9538253250/testing:latest   *:4000->80/tcp<br/>

$ docker stack services getwebapp
ID                  NAME                MODE                REPLICAS            IMAGE                       PORTS<br/>
1kv11tg86qtm        getwebapp_web       replicated          5/5                 9538253250/testing:latest   *:4000->80/tcp<br/>

$ docker service ps getwebapp_web<br/>

docker stack is used to deploy and manage multi-container applications on a Docker Swarm cluster using a docker-compose.yml file

docker stack ls                                            # List stacks or apps<br/>
docker stack deploy -c <composefile> <appname>  # Run the specified Compose file<br/>
docker service ls                 # List running services associated with an app<br/>
docker service ps <service>                  # List tasks associated with an app<br/>
docker inspect <task or container>                   # Inspect task or container<br/>
docker container ls -q                                      # List container IDs<br/>
docker stack rm <appname>                             # Tear down an application<br/>
docker swarm leave --force      # Take down a single node swarm from the manager

Docker Registry (Docker Trusted Registry – DTR) is an enterprise-grade storage solution for Docker images.<br/>
In other words, it’s an image storage service. Think about GitHub, but for Docker Images.

Docker Repository is a collection of Docker images with the same name and different tags.<br/>
For example, the repository we’ve used several times so far, microsoft/aspnetcore has a bunch<br/>
of images with different tags in it. We can choose which one you want to pull by typing docker<br/>
pull image-name:tag. Something similar to GitHub repo and commits. We can go back to whichever<br/>
commit we want and pull it to the local machine.

curl -fsSL get.docker.com -o get-docker-ce.sh<br/>
RHEL EE need docker EE<br/>
docker doesn't support normal sudo user to run command

## Build docker image
sudo docker image build -t apache:1.1 . -f Dockerfile_apache

## Run container using the above image built
sudo docker container run -p 8009:80 -d --name apache apache:1.1<br/>
sudo docker container rm --force apache<br/>

--publish 80:80<br/>
first 80 port to access(expose port) in browser and second one is container port.<br/>
docker container run --publish 80:80 nginx -> fg<br/>
docker container run --publish 80:80 --detach nginx - Service/Daemon<br/>
sudo docker create --name centos_7 centos<br/>
sudo docker container start centos_7<br/>
docker container stop <containerid><br/>
docker container ls - List running container<br/>
docker container ls -a - List all container stop/start<br/>

Into the container<br/>
$ sudo docker container attach 3e3e141c722a<br/>
or<br/>
$ sudo docker exec -it dff9974acdf0  /bin/bash

docker container run --publish 80:80 --detach nginx - Service<br/>
docker container run --publish 80:80 --detach nginx --name <name_of_container>(should be unique)<br/>
docker container rm <container_id><br/>
docker container stop <container_id>(-f forcefully)

docker top <image_name> - List running process in specific container<br/>
docker container logs <container_id><br/>
docker container inspect <container_name> - Give the json data<br/>
docker container stats <container_id>/<container_name><br/>
docker container stats - All container stats<br/>

docker container run -it --name xyz ubuntu - Start new container interactively<br/>
docker container exec -it ubuntu - Run additional command in existing container<br/>
docker container start -ai ubuntu<br/>
docker container exec -it 9e0153426878 bash<br/>

When you start docker container in the background connecting to particular docker network and by default bridge network
Each network routes through NAT firewall on host IP

docker container port <container_id>
docker continaer ipaddress

Find IPAddress of container
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 9e0153426878

docker network ls
docker network inspect bridge
docker network create <create_custome_network>
docker network ls
docker cotainer connect <network_id> <container_id>
docker container exec -it <frst_cotainer_id_nginx> ping <second_container_id_nginx>
Always create custom network

docker history centos
docker image inspect centos - metadata(data about data)

#Volume attach -v.
#VOLUME /var/run/mmeysql
docker container run -d --name nginx -p 80:80 -v $(pwd):/usr/share/nginx/html nginx

Above all called the layers of image to build

Container lifetime and Persitent data
Two way : Data volumes and Bind mounts
Volumes: make special location outside of container UFS
Bind Mounts: link container path to host path
Volumes are used for persistent data mounting database related containers database stuff to host machine
bind mount are suitable for developers to make config file changes in the host machine and get affected in container

sudo docker container run --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysql

sudo docker container run -d --name mysql1 -e MYSQL_ALLOW_EMPTY_PASSSWORD=True -v /var/lib/mysql mysql
sudo docker container run -d --name mysql2 -e MYSQL_ALLOW_EMPTY_PASSSWORD=True -v mysql-db:/var/lib/mysql mysql - named volume(-v mysql-db:/var/lib/m#

Bind mount
maps host file or directory to container file or directory
Docker_nginx and build and start container
sudo docker build -t custom_nginx -f Dockerfile_nginx .
sudo docker container run  -d  --name nginx -p 8075:80 -v $(pwd):/usr/share/nginx/html custom_nginx
Change in the host file is going to take precdence

docker run --mount type=bind,source=/HOST/PATH,target=/CONTAINER/PATH,readonly nginx
docker run -v HOST-DIRECTORY:/CONTAINER-DIRECTORY:rw nginx


Docker compose
Comprised of two seperate but related things
 1. YAML-formatted file that describes our solution option for
    * continers
    * networks
    * Volumes

 2. A CLI Tool docker-compose used for local dev/test automation with those YAML files.

Docker compose is talking to the docker API in the background on behalf of docker CLI, is kind of replacement for CLI.

COPY and ADD are both Dockerfile instructions that serve similar purposes.
They let you copy files from a specific location into a Docker image.

COPY takes in a src and destination. It only lets you copy in a local file or directory
from your host (the machine building the Docker image) into the Docker image itself.

ADD lets you do that too, but it also supports 2 other sources.
First, you can use a URL instead of a local file / directory.
Secondly, you can extract a tar file from the source directly into the destination.
add python27.tar.gx /app

RUN executes command(s) in a new layer and creates a new image. E.g., it is often used for installing software packages.
CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.
ENTRYPOINT configures a container that will run as an executable.
ENTRYPOINT ab 
With the ENTRYPOINT instruction, it is not possible to override the instruction during
the docker run command execution like we are with CMD. This highlights another usage of ENTRYPOINT,
as a method of ensuring that a specific command is executed when the container in question is started
regardless of attempts to override the ENTRYPOINT.

$sudo docker container run -i -t --rm -p 80:80 nginx #Run foreground and remove container once it stops

FROM ubuntu
ENTRYPOINT ["top", "-b"] #Append with command
CMD ["-c"]

$sd container run -it --rm --name test11 ubuntu top -H

VOLUME
VOLUME ["/data"]


USER
USER <user>[:<group>] or
USER <UID>[:<GID>]

WORKDIR
WORKDIR /path/to/workdir

WORKDIR /a
WORKDIR b
WORKDIR c
RUN pwd
The output of the final pwd command in this Dockerfile would be /a/b/c.
ENV APP_PORT=8000 -> -e APP_PORT=8090 Can't override run time, runtime container yes,
ARG name=sadashiv -> --build-args ARGS override at build time, run time container no,
ARG 
ARG
ARG <name>[=<default value>]
The ARG instruction defines a variable that users can pass at build-time to the builder with the
docker build command using the --build-arg <varname>=<value> flag. If a user specifies a build
argument that was not defined in the Dockerfile, the build outputs a warning.

Login or configure custom docker registery
docker login [server]

docker swarm init<br/>
docker swarm leave<br/>
docker swarm leave --force<br/>
docker swarm join --token SWMTKN-1-4i4knr4xnbz7ti8tgw8utc1243r13kbd8ui1tb7vmapr7njdw0-der121xbosee0fg0x6bn7ce5n 192.168.0.7:2377<br/>
docker swarm join-token manager

Multi-stage builds

Dockerfile
FROM eclipse-temurin:21.0.8_9-jdk-jammy AS builder
WORKDIR /opt/app
COPY .mvn/ .mvn
COPY mvnw pom.xml ./
RUN ./mvnw dependency:go-offline
COPY ./src ./src
RUN ./mvnw clean install

FROM eclipse-temurin:21.0.8_9-jre-jammy AS final
WORKDIR /opt/app
EXPOSE 8080
COPY --from=builder /opt/app/target/*.jar /opt/app/*.jar
ENTRYPOINT ["java", "-jar", "/opt/app/*.jar"]


docker network create app-network

docker run -d --name mysql-db --network  app-network -e MYSQL_ROOT_PASSWORD=root  -e MYSQL_DATABASE=linux_mgmt  \
-e MYSQL_USER=sadashiv   -e MYSQL_PASSWORD=Sadashiv@123   -v mysql_data:/var/lib/mysql   mysql:8.0

docker run  --name django-app --network app-network -p 8000:8000 lmt:2.1
