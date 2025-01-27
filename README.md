# Cloud Computing Projects

This repository features my cloud computing projects, showcasing key concepts such as RESTful APIs, containerization, microservices, and orchestration. Each project demonstrates practical implementations of robust, scalable, and fault-tolerant cloud-based systems.

---

## Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [Project 1: Stock Portfolio Management](./Project1/README.md)
  - [Project 2: High Availability and Robust Applications](./Project2/README.md)
  - [Project 3: Kubernetes Deployment](./Project3/README.md)
- [Technologies Used](#technologies-used)
- [Setup and Prerequisites](#setup-and-prerequisites)
- [Acknowledgments](#acknowledgments)

---

## Overview

This repository contains three projects, each building upon the previous to explore advanced cloud computing techniques:
1. **Project 1: Stock Portfolio Management** - A RESTful API for managing stock portfolios, containerized with Docker.
2. **Project 2: High Availability and Robust Applications** - An extension introducing persistence, fault tolerance, and load balancing with Docker Compose.
3. **Project 3: Kubernetes Deployment** - Deployment of microservices to a Kubernetes cluster, showcasing scalability and orchestration.

Each project is contained in its dedicated folder with a comprehensive README that explains its functionality and usage.

---

## Projects

- **[Project 1: Stock Portfolio Management](./Project1/README.md):**  
  A Dockerized RESTful application that allows users to manage stock portfolios. Features include retrieving stock prices via an external API, calculating portfolio values dynamically, and providing a clean and efficient JSON-based interface for CRUD operations.

- **[Project 2: High Availability and Robust Applications](./Project2/README.md):**  
  This project enhances the previous implementation by introducing a microservices architecture using Docker Compose. It features:
  - Persistent data storage using MongoDB.
  - Fault tolerance and automatic service recovery.
  - Load balancing with NGINX to distribute requests across multiple service instances.
  - Reverse proxy using NGINX.

- **[Project 3: Kubernetes Deployment](./Project3/README.md):**  
  This project brings the microservices to a Kubernetes cluster, demonstrating:
  - Deployment of replicas for scalability and resilience.
  - Service discovery and networking with Kubernetes.
  - Advanced configurations like health checks and resource monitoring.

---

## Technologies Used

- **Languages:** Python
- **Containerization:** Docker, Docker Compose
- **Orchestration:** Kubernetes
- **APIs:** [API Ninjas Stock Price API](https://api-ninjas.com/api/stockprice)
- **Database:** MongoDB
- **Proxy:** NGINX

---

## Setup and Prerequisites

To explore these projects, you will need:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Kubernetes (kubectl)](https://kubernetes.io/docs/tasks/tools/)
- An API key for [API Ninjas Stock Price API](https://api-ninjas.com/).

Detailed setup instructions are included in the README of each project folder.

---

## Acknowledgments

These projects were developed as part of a cloud computing course at Reichman University, led by Dr. Daniel Yellin. Special thanks for the valuable resources and guidance provided.

---

For questions or issues, feel free to open an issue or contact me via GitHub.
