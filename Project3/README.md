# Project 3: Kubernetes Deployment of Stock Portfolio Management

This project focuses on deploying the stock portfolio management system on Kubernetes (k8s). It builds on the previous projects by containerizing the application and orchestrating its deployment using Kubernetes. The goal is to achieve scalability, high availability, and fault tolerance in a cloud-native environment.

## Features

- **Kubernetes Orchestration:** Deploy and manage the application using Kubernetes for scalability and resilience.  
- **Scalability:** Automatically scale the stock services based on demand using Kubernetes Horizontal Pod Autoscaler (HPA).  
- **High Availability:** Ensure the application remains available even if individual pods or nodes fail.  
- **Persistent Storage:** Use Kubernetes Persistent Volumes (PV) and Persistent Volume Claims (PVC) to store data persistently.  
- **Load Balancing:** Kubernetes Services provide built-in load balancing for incoming requests.  
- **Configuration Management:** Use Kubernetes ConfigMaps and Secrets to manage environment variables and sensitive data.  

## Architecture

The application is deployed as a set of microservices in a Kubernetes cluster, with the following components:  

1. **Stocks Service:** Manages the stock portfolio, with multiple replicas for high availability.  
2. **Capital Gains Service:** Calculates capital gains or losses for the portfolio.  
3. **Database Service:** MongoDB is used for persistent storage of stock data.  
4. **NGINX Ingress Controller:** Acts as a reverse proxy and load balancer for routing external traffic to the appropriate services.  
5. **Kubernetes Services:** Provide internal and external access to the application components.  

## Technologies Used

- **Programming Language:** Python (Flask)  
- **Containerization:** Docker  
- **Orchestration:** Kubernetes (k8s)  
- **Database:** MongoDB  
- **Reverse Proxy and Load Balancing:** NGINX
  

## Setup and Usage

### Prerequisites

1. **Kubernetes Cluster:** Set up a Kubernetes cluster using tools like Kind.  
2. **kubectl:** Install the Kubernetes command-line tool, `kubectl`.  
3. **Docker:** Ensure Docker is installed for building and pushing container images.  

### Steps to Deploy

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yanivNaor92/cloud-computing-k8s-assignment
   cd cloud-computing-k8s-assignment
2. **Create a KIND cluster**   
   ```bash
   kind create cluster --config kind-config.yaml
3. **Applay the namespace:**  
   Apply the Kubernetes manifests to deploy the application.  
   ```bash
   kubectl apply -f namespace.yaml
4. **Build the Docker Images for each Service and Load them Into the Cluster**    
   ```bash
   docker build -t <image-name> -f <path-to-dockerfile> .
   kind load docker-image <image-name>
5. **Deploy the Resources in the Cluster**    
   ```bash
   kubectl apply -f deployment.yaml
6. **Check the System's Behavior**    
   ```bash
   kubectl get pods -n <namespace>
7. **The output should be like this:**
   ```bash
   NAME                             READY   STATUS    RESTARTS   AGE
    stocks-6d967d75cb-72xrw          1/1     Running   0          11h
    stocks-6d967d75cb-ug84r          1/1     Running   0          11h
    capital-gains-1d947a758b-g7bjj   1/1     Running   0          11h
    nginx-5er68d65c9-tnsst           1/1     Running   0          11h
    mongo-2q93yd1514-tbasyn          1/1     Running   0          11h  

## Acknowledgments
This project was part of a cloud computing course at Reichman University. Special thanks to Dr. Daniel Yellin for his guidance and resources.

---
