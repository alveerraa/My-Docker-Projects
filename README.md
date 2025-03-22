Docker Bridge Network Project 🐳

📌 Overview
This project demonstrates network isolation using Docker bridge networks. It shows how containers within the same custom bridge network can communicate, while containers on different networks remain isolated.

🛠️ Steps to Run the Experiment

1️⃣ Create a Custom Bridge Network

docker network create my_bridge

2️⃣ Run Two Containers in the Same Network

docker run -dit --name container1 --network my_bridge alpine sh
docker run -dit --name container2 --network my_bridge alpine sh

3️⃣ Verify Communication Between Containers

Enter container1 and ping container2:

docker exec -it container1 sh

ping container2 -c 4

💡 Expected Output: The ping should be successful.

4️⃣ Run a Third Isolated Container

docker run -dit --name isolated_container alpine sh

docker exec -it isolated_container sh

ping container1 -c 4

💡 Expected Output: The ping should fail because this container is not in the same network.

🔬 Key Learnings
✅ Containers in the same bridge network can communicate

✅ Containers in different networks remain isolated

✅ Understanding network segmentation in Docker is crucial for security

📂 Project Structure

Docker-Bridge/
│── Dockerfile
│── README.md

Now, add this to your repository:

nano README.md  

git add README.md

git commit -m "Added README for Docker Bridge Network project"

git push origin main

