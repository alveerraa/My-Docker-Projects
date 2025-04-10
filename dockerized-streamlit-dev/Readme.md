# 🚀 Dockerized Streamlit Development Environment

# Live demo: https://my-docker-projects-99u7fv8h8ai79qbuyxgal5.streamlit.app/

This project sets up a Streamlit development environment inside a Docker container to ensure consistency and portability.

📌 Prerequisites

Docker installed → Download Docker

Git installed → Download Git

# 🛠️ Steps to Set Up the Environment

1️⃣ Clone the Repository

git clone https://github.com/alveerraa/My-Docker-Projects.git

cd "My-Docker-Projects/Dockerized Streamlit Development Environment"

2️⃣ Create a Dockerfile

Inside your project folder, create a file named Dockerfile and add the following content:

FROM python:3.9  

WORKDIR /app  

COPY . .  

RUN pip install -r requirements.txt  

EXPOSE 8501  

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

3️⃣ Create requirements.txt

Create a requirements.txt file with the following dependencies:

streamlit

4️⃣ Create a Simple Streamlit App

Create a Python file named app.py and add this sample code:

import streamlit as st

st.title("🚀 Dockerized Streamlit App")

st.write("This Streamlit app is running inside a Docker container!")

5️⃣ Build the Docker Image

Run the following command to build your Docker image:

docker build -t streamlit-dev .

6️⃣ Run the Streamlit App in Docker

Now, start the container and expose it to port 8501:

docker run -p 8501:8501 streamlit-dev

7️⃣ Open the App in Browser

Go to http://localhost:8501 in your web browser. You should see your Streamlit app running inside Docker!

🎯 Expected Output
The Streamlit app should run inside a Docker container.

You can access it via http://localhost:8501

🛠 Stopping & Removing the Container

To stop the running container:

docker ps

docker stop <container_id>

To remove the container:

docker rm <container_id>

To remove the image:

docker rmi streamlit-dev

🎉 That’s It!

Your Dockerized Streamlit Development Environment is now set up and ready to use! 🚀
