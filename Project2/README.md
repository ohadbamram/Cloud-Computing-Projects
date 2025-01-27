# Project 2: High Availability and Robust Applications

This project extends the functionality of the stock portfolio management system by introducing high availability, persistence, and fault tolerance. Using Docker Compose, the application is redesigned as a microservices architecture with multiple services working together seamlessly.

## Features

- **Persistence:** Data is stored in a MongoDB database, ensuring it is retained even after container restarts.  
- **High Availability:** Multiple instances of the stock service are deployed to handle load and ensure reliability.  
- **Fault Tolerance:** Services automatically restart after a failure using Docker Compose restart policies.  
- **Load Balancing:** Requests to the stock services are distributed using NGINX, with weighted round-robin load balancing.  
- **Reverse Proxy:** NGINX is used as a reverse proxy to route requests to the appropriate service.  

## Microservices Architecture

The application consists of the following services:  
1. **Stocks Service:** Two instances (`stocks1` and `stocks2`) of the stock portfolio service handle different portfolios.  
2. **Capital Gains Service:** Provides information about the capital gains or losses for the portfolios.  
3. **Database Service:** MongoDB is used to persist data for the stock services.  
4. **Reverse Proxy Service:** NGINX acts as a reverse proxy and load balancer for routing requests.  

## Technologies Used

- **Programming Language:** Python (Flask)  
- **Containerization:** Docker, Docker Compose  
- **Database:** MongoDB  
- **Proxy and Load Balancing:** NGINX  

## Setup and Usage

1. **Prerequisites:**  
   - Install [Docker](https://www.docker.com/).  
   - Install [Docker Compose](https://docs.docker.com/compose/).  

2. **Clone the Repository:**  
   ```bash
   git clone https://github.com/ohadbamram/Cloud-Computing-Projects
   cd Project2
3. **Run the Application with Docker Compose:**
    ```bash
   docker-compose up --build
4. **Access the Application:**

The stock services and capital gains service are available through the NGINX reverse proxy at http://localhost.
Host Ports:
stocks1: Available at http://localhost/stocks1.
stocks2: Available at http://localhost/stocks2.
capital-gains: Available at http://localhost/capital-gains.

## Example Request and Response
Retrieving Capital Gains (GET /capital-gains)
Request:

GET /capital-gains?portfolio=stocks1

Response:

{
  "total capital gain": 1200.50
}

Load Balancing Example

Requests to http://localhost/stocks1 are distributed between the two instances of the stocks1 service using a weighted round-robin policy. The first instance receives three requests for every one request received by the second instance.

## Acknowledgments
This project was part of a cloud computing course at Reichman University. Special thanks to Dr. Daniel Yellin for his guidance and resources.

---
