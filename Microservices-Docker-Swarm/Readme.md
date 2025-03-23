# Microservices with Docker Swarm 🚀

This project demonstrates how to deploy microservices using Docker Swarm, enabling high availability, scalability, and load balancing.

Project Overview

This setup includes multiple microservices running as Docker containers within a Swarm cluster. It ensures efficient container orchestration, making services resilient and distributed.

# Tech Stack

Docker & Docker Swarm 🐳

Python (Flask) for microservices

Docker Compose for service definitions

PostgreSQL/MySQL (Optional) for data persistence

NGINX (Optional) as a reverse proxy

# Setup & Deployment

1️⃣ Prerequisites

Ensure you have the following installed:

Docker & Docker Compose

Docker Swarm initialized (docker swarm init)

2️⃣ Build & Push Docker Images

Before deploying, build the images for each microservice:

docker build -t microservice1 ./microservice1

docker build -t microservice2 ./microservice2

(Optional: Push to Docker Hub if needed)

docker tag microservice1 <your-dockerhub-username>/microservice1

docker push <your-dockerhub-username>/microservice1

3️⃣ Deploy the Stack

docker stack deploy -c docker-compose.yml microservices

4️⃣ Check Running Services

docker service ls

5️⃣ View Logs

docker service logs microservices_microservice1

# Project Structure

📂 Microservices-Docker-Swarm
│── 📂 microservice1/  
│   ├── app.py  
│   ├── requirements.txt  
│   ├── Dockerfile  
│── 📂 microservice2/  
│   ├── app.py  
│   ├── requirements.txt  
│   ├── Dockerfile  
│── docker-compose.yml  
│── README.md  

# Common Issues & Fixes

failed to create service: invalid repository/tag	Ensure the image name in docker-compose.yml is correct (use just microservice1:latest, not ./microservice1:latest).

no such file or directory: requirements.txt	Ensure requirements.txt exists in the correct directory and is copied inside the Dockerfile.

fatal: Unable to read current working directory	Run cd ~/My-Docker-Projects/Microservices-Docker-Swarm before pushing to GitHub.
