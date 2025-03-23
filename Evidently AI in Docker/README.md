# Evidently AI in Docker 🚀

This project containerizes an Evidently AI application using Docker. Evidently AI is an open-source tool for monitoring and analyzing machine learning models in production.

# 📌 Features

Dockerized setup for easy deployment

Uses Python 3.9

Includes a requirements.txt for dependency management

Runs on port 5000

📂 Project Structure

Evidently AI in Docker/
│── Dockerfile
│── app.py
│── requirements.txt
│── README.md
Dockerfile → Defines the container setup

app.py → Python script for the app

requirements.txt → Lists dependencies

README.md → You're reading it! 📖

# 🔧 Setup & Run

1️⃣ Clone the repository

git clone https://github.com/alveerraa/My-Docker-Projects.git
cd "My-Docker-Projects/Evidently AI in Docker"

2️⃣ Build the Docker image

docker build -t evidently-ai .

3️⃣ Run the container

docker run -p 5000:5000 evidently-ai

4️⃣ Open in browser

Go to http://localhost:5000

🐞 Troubleshooting

Port 5000 already in use?

Run:

lsof -i :5000  # Find the process using port 5000
kill -9 <PID>  # Replace <PID> with the process ID

Then rerun the container.

