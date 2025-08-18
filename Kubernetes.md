# Kubernetes Learning

Kubernetes is also called K8s. Is written in Go for a planet-scale deployment.


## Container Technologies

* Docker
* podman
* Containerd
* rkt
* LXD

### YAML

* Acronym for YAML ain't Markup Language
* Files can have the endings .yml and .yaml
* One file can contain multiple documents seperated by a startin '---'.
* Comments are placed with a '#'
* Consists of 'key: value' pairs
* Indentations are used as lists like indentated key:value-Pairs or Arrays of strings with '-' in front.
* YAML-Files can be validated by [YAML Checker](https://yamlchecker.com)

## Lab

### Minikube

| Command | Description |
| :---: | :--- |
| minikube dashboard | Shows the minikube Dashboard |
| minikube start | Start the minicube cluster |
| kubectl cluster-info | Get status of the cluster |
| kubectl apply -f <file> | Create stuff out of YAML-Files. I.e. namespaces out of namespace.yaml or deployments via deployment.yaml. |
| kubectl delete -f <file> | Delete stuff out of YAML-Files. I.e. namespaces out of namespace.yaml |
| kubectl delete pod <podname> -n <namespace> | Delete a specific pod from a namespace. |
| kubectl describe pod <podname> -n <namespace> | Watch Pod infos with errors included. |
| kubectl exec -it <podname> -- <shell> | Execute a function in the interactive terminal like /bin/sh on a busybox pod. |
| kubectl get deployments -n <namespace> | Control the existence of deployment. |
| kubectl get namespaces | Isolate and manages applications. Shortened by get ns. |
| kubectl get nodes | Get Node infos |
| kubectl get pods -A | Shows the Pods in every namespace (-A) |
| kubectl get pods -n <namespace> | Show the Pods in a specific namespace. |
| kubectl get pods -n <namespace> -o wide | Show the Pods in a specific namespace with additional info like IP-Adresses. |
| kubectl get services | Shows the Services running in the cluster |
| kubectl logs <podname> -n <namespace> | View the logs of a pod |





### Docker

How do I create a testing environment with maximum privileges?

### Procedure to install an application

1. Create a name space - kubectl apply -f namespace.yaml
2. Have an image available
3. Have a descriptive deployment.yaml file to copy the image to the namespace
4. Deploy the image - kubectl apply -f deployment.yaml
5. Check the deployment - kubectl get deployment -n development
6. Spin up a busybox pod - kubectl apply -f busybox.yaml
7. Get origin pod's IP - kubectl get pods -n <namespace> -o wide
8. Connect to the pod - kubectl exec -it <bbpodbane> -- /bin/sh
9. Connect via the busybox shell and wget. Look at the deployment.yaml for the pods Port


## Terms

| Term | Description |
| :---: | :--- |
| Cloud-native | Open-Source projects designed to let technologists use cloud computing services to automatically deploy and scale applications. |
| Container | A technology that bundles the code for an application, and the configuration required to run the code itself in one unit. |
| Container Image | A file with executable code that can be run as a container. |
| Container Registry | A database that stores container images. Examples: Docker Hub, Quay, Google Container Registry. |


