# Microservices Orchestration with Minikube & Kubernetes 🚀

This project demonstrates how to orchestrate microservices using Minikube and Kubernetes. It includes setting up a local Kubernetes cluster, deploying multiple microservices, and managing them efficiently.

# 📌 Features

Uses Minikube for local Kubernetes cluster

Deploys multiple microservices using Kubernetes manifests

Includes Service, Deployment, and Ingress configurations

Demonstrates scalability and load balancing

📂 Project Structure

Microservices-Orchestration/
│── microservice1/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   ├── deployment.yaml
│   ├── service.yaml
│── microservice2/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   ├── deployment.yaml
│   ├── service.yaml
│── ingress.yaml
│── README.md
microservice1/ & microservice2/ → Independent microservices

deployment.yaml → Defines how each microservice is deployed

service.yaml → Exposes the microservices

ingress.yaml → Handles routing to different services

README.md → You're reading it! 📖

# 🔧 Setup & Run

1️⃣ Start Minikube

minikube start

2️⃣ Build and Load Docker Images into Minikube

eval $(minikube docker-env)  # Point Docker CLI to Minikube

docker build -t microservice1 ./microservice1

docker build -t microservice2 ./microservice2

3️⃣ Apply Kubernetes Manifests

kubectl apply -f microservice1/deployment.yaml
kubectl apply -f microservice1/service.yaml
kubectl apply -f microservice2/deployment.yaml
kubectl apply -f microservice2/service.yaml
kubectl apply -f ingress.yaml

4️⃣ Enable Ingress Controller

minikube addons enable ingress

5️⃣ Get Minikube IP and Access Services

minikube ip

Use the Minikube IP in your browser or test using curl.

