What is container

A container is a standard unit of software that packages up code and all its dependencies so the application
runs quickly and reliably from one computing environment to another. Available for both Linux and Windows-based applications,
containerized software will always run the same, regardless of the infrastructure.


Find ipaddress of Docker container
docker inspect -f "{{ .NetworkSettings.IPAddress }}" 656d4c48a0d2
