# Running a Streamlit App in Docker on AWS EC2 🚀

We'll deploy a Streamlit app inside a Docker container and run it on an AWS EC2 instance.

1️⃣ Setup AWS EC2 Instance

🔹 Step 1: Launch an EC2 Instance

Go to AWS EC2 Console

Click Launch Instance

Choose an Ubuntu 22.04 or Amazon Linux 2 AMI

Select instance type (t2.micro for free tier)

Configure Security Group:

Add rule: Allow HTTP (Port 80)

Add rule: Allow Custom TCP (Port 8501) for Streamlit

Add rule: Allow SSH (Port 22, Your IP)

Launch and Download Key Pair (.pem file)

2️⃣ Connect to EC2 via SSH

🔹 Step 2: SSH into the instance

Replace your-key.pem and your-ec2-public-ip accordingly:


chmod 400 your-key.pem  # Set correct permissions

ssh -i your-key.pem ubuntu@your-ec2-public-ip

3️⃣ Install Docker on EC2

🔹 Step 3: Install Docker

Run the following commands:

sudo apt update -y

sudo apt install docker.io -y

sudo systemctl start docker

sudo systemctl enable docker

4️⃣ Build & Run Streamlit App in Docker

🔹 Step 4: Create a Simple Streamlit App

Inside the EC2 instance, create a project folder:

mkdir streamlit-app && cd streamlit-app

Create a app.py file:

nano app.py

Add the following Streamlit code:

import streamlit as st

st.title("Streamlit in Docker on AWS 🚀")

st.write("Hello, this is a test deployment of a Streamlit app running inside Docker on AWS EC2!")

Save (CTRL+X, then Y, then ENTER).

5️⃣ Create a Dockerfile

🔹 Step 5: Create Dockerfile

nano Dockerfile

Add the following:

FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

Save (CTRL+X, then Y, then ENTER).

6️⃣ Build & Run Docker Container

🔹 Step 6: Build the Docker Image

sudo docker build -t streamlit-app .

🔹 Step 7: Run the Container

sudo docker run -d -p 8501:8501 streamlit-app

7️⃣ Access the Streamlit App

🔹 Step 8: Open in Browser
Go to:

http://your-ec2-public-ip:8501

You should see your Streamlit app running! 🎉

8️⃣ (Optional) Push to Docker Hub

🔹 Step 9: Push Image to Docker Hub

Login to Docker Hub:

docker login

Tag the image:

docker tag streamlit-app your-dockerhub-username/streamlit-app

Push to Docker Hub:

docker push your-dockerhub-username/streamlit-app

9️⃣ Clean Up (Optional)

To Stop & Remove Everything:

sudo docker stop $(sudo docker ps -q)

sudo docker rm $(sudo docker ps -aq)

sudo docker rmi streamlit-app

To Terminate EC2 Instance:

Go to AWS EC2 Console → Select your instance → Terminate

Done! 🎉
