# Kubernetes in a Nutshell

## Docker Architecture

### Anatomy of a container

Namespaces is a linux kernel feature that provide different "views" of the system.

| Name| Description |
| :---: | :--- |
| USERNS | User lists |
| MOUNT | Access to file systems |
| NET | Network communication |
| IPC | Interprocess communication |
| TIME | The ability to change time (not supported by Docker) |
| PID | Process ID Management |
| CGROUP | Create control groups |
| UTC | Create host/domain names |

Control groups are another Linux kernel feature to control access to resources:

1. Monitor and restrict CPU Usage
2. Monitor and restrict network and disk bandwidth
3. Monitor and restrict memory consumption
4. Assign disk quotas (not supported by Docker)

### Dockerfile

A Docker-File is a plain text file with step by step instructions on how to build an image. It includes the code, the configuration and the environment where the image will run.

```
FROM alpine:latest

RUN mkdir /tmp/mDir

COPY ./myScript /tmp/forme

USER someuser

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["myCmd"]
```

### Trusted Base Image

Use a trustworthy (golden) base image as first layer (i.e. FROM alpine:latest).

### Networking

#### Network over Bridge

Is the default option and allows containers to communicate with each other on the same host. 

```
$ docker network create --driver bridge <net-name>

$ docker run --network <net-name> <image-name>
```

#### Closed Container

Has only a loopback interface and cannot communicate with other containers.

```
$ docker run --network none <image-name>
```

#### Shared

The container share the host's network interface.

```
$ docker run --network host <image-name>
```

#### Underlay networks

Container communication by leveraging underlying physical interface (i.e. macvlan, ipvlan). 

#### Overlay networks

Also leveraging a virtual network but taking a different approach. The virtual network sits above host networks (i.e. vxlan).

#### Routing

Containers are not directly routable from outside their cluster. You have to map host port to target container port.

```
$ docker run -p 8088:8080/tcp
```

With the above command the container's port is bound to the host's IP address of 0.0.0.0. It is better to limit connections on a specific interface with:

```
$ docker run -p <ip>:<port-in>:<port-to> <image-name>
```

### Docker Socket

A process with access to the socket file (/var/run/docker.sock) can send any command to the docker deamon. Therefore you should not mount the socket as a volume inside a container.

## Working with docker

### Docker CLI

| Term | Description |
| :---: | :--- |
| docker --help | Show docker CLI help |
| docker container create [OPTIONS] IMAGE [:Tag] |
| docker container start [--attach] <CONTAINER-ID> | Start a container. Attach the containers output to the current terminal with the flag --attach | 
| docker exec CONTAINERID COMMAND | Executes a command in the container |
| docker exec --interactive --tty CONTAINERID bash | Starts an interactive shell in the container |
| docker images | Show the images on the Docker Server |
| docker kill | Stop the container |
| docker logs <CONTAINER-ID> | Show logs for container |
| docker ps [--all] | Show the containers which are actively running [or all known] | 
| docker run [-d] IMAGENAME | Builds and starts the container from the Image. -d means the container will not attach to the current console window |
| docker rm CONTAINERID | Remove container from Docker Server's Containerlist |
| docker rmi IMAGENAME | Remove container from Docker Servers Repository |
| docker stop CONTAINERID | Stops the container with the given ID |

### Creating and starting a docker container

To compile an image into an container, give the Image to the docker CLI tool. Usually the tool downloads the image file from Docker hub.

For an example we're creating a container with the hello-world image from Docker Hub by issuing the following command:

```
$ docker container create hello-world
$ docker container start <CONTAINER-ID>
$ docker container attach <CONTAINER-ID>
```

The docker container command creates containers but do not start them. Every container created by docker gets an ID. The shorter version of above steps is:

```
$ docker run <IMAGE-NAME>
```

### Create a Docker container from Dockerfiles

Create a dockerfile, that reflects your application, customization and starting point.

Run the following command:

```
$ docker build -t <buildname> --file <name of the dockerfile>
```

Or the more advanced BuildKit Imagebuilder-Command:

```
$ docker buildx build -t first-container --load .
```

### Binding ports to the container

Start the container with the following command to bind ports:

```
$ docker run -d --name CONTAINERNAME -p HOSTPORT:CONTAINERPORT IMAGENAME
```

### Binding Mappings to the container

Start the container with the following command mount a part of the filesystem:

```
$ docker run --rm --entrypoint sh -v /tmp/container:/tmp ubuntu -c "echo 'Hello there.' > /tmp/file && cat /tmp/file
```