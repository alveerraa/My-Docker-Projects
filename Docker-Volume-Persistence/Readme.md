# 🚀Docker Volume Persistence - Bind Mounts with Linux Containers

This project focuses on using Docker volumes to persist data across container restarts using bind mounts.

# 🚀 Steps to Set Up Docker Volume Persistence with Bind Mounts

1️⃣ Create a Project Directory

First, navigate to your main project directory and create a new folder for this project:

cd ~/My-Docker-Projects

mkdir Docker-Volume-Persistence

cd Docker-Volume-Persistence

2️⃣ Create a Simple Web App (Optional)

If you're working with a simple app (e.g., a Python/Flask app), create app.py:

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is a persistent volume test!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    
3️⃣ Create a Dockerfile

Inside Docker-Volume-Persistence/, create a file named Dockerfile:

FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]

4️⃣ Set Up a Bind Mount Volume

Instead of using Docker-managed volumes, we'll use a bind mount to map a local directory to the container.

Create a local directory for persistent data:

mkdir ~/My-Docker-Projects/Docker-Volume-Persistence/data

Run the container with a bind mount:

docker run -d -p 5000:5000 -v ~/My-Docker-Projects/Docker-Volume-Persistence/data:/app/data --name my_volume_test volume-test

🔹 This binds the data/ folder on your host machine to /app/data inside the container.

5️⃣ Verify Volume Persistence

Check if the data directory exists inside the container:

docker exec -it my_volume_test ls /app/data

If the directory is successfully mounted, you'll see the contents.

Stop and remove the container:

docker stop my_volume_test
docker rm my_volume_test

Check if the files still exist on your host machine:

ls ~/My-Docker-Projects/Docker-Volume-Persistence/data

If they are still there, your volume persistence is working!

6️⃣ Commit and Push to GitHub
Now, add the project to your GitHub repository:

cd ~/My-Docker-Projects
git add Docker-Volume-Persistence
git commit -m "Added Docker Volume Persistence project"
git push origin main
