# 🚀Containerized MySQL

In this project, you'll set up MySQL inside a Docker container, allowing you to run a database without installing MySQL directly on your system. This is useful for database management in local development environments and production setups.

🛠️ Step 1: Create the Project Directory

Navigate to your My-Docker-Projects folder and create a new directory:

cd ~/My-Docker-Projects

mkdir Containerized-MySQL

cd Containerized-MySQL

📄 Step 2: Create a docker-compose.yml File

Instead of manually running MySQL inside Docker, we'll use Docker Compose to simplify the process.

Create a docker-compose.yml file:

touch docker-compose.yml

Now open it in a text editor and add the following content:

version: '3.8'

services:
  mysql:
    image: mysql:latest
    container_name: mysql_container
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: testdb
      MYSQL_USER: user
      MYSQL_PASSWORD: userpassword
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
Explanation of the above file:

image: mysql:latest → Uses the latest MySQL Docker image.

container_name: mysql_container → Names the container.

restart: always → Ensures MySQL restarts if it crashes.

environment: → Defines environment variables for the database.

MYSQL_ROOT_PASSWORD → Root user password.

MYSQL_DATABASE → Name of the default database.

MYSQL_USER → Custom user.

MYSQL_PASSWORD → Password for the custom user.

ports: → Maps port 3306 (MySQL default) from the container to the host.

volumes: → Ensures persistent storage of database data.


🐳 Step 3: Run MySQL in Docker

Now, start the MySQL container using Docker Compose:

docker-compose up -d

What happens?

The MySQL container starts in the background (-d means detached mode).

It creates a persistent volume so data isn't lost when restarting.

✅ Step 4: Check Running Containers

Run this command to see if MySQL is running:

docker ps
You should see an output like this:

CONTAINER ID   IMAGE         STATUS         PORTS                   NAMES
abc123456789   mysql:latest  Up 5 minutes   0.0.0.0:3306->3306/tcp  mysql_container

🖥️ Step 5: Access MySQL from the Terminal

To enter the MySQL container and log in:

docker exec -it mysql_container mysql -u root -p

Then, enter the root password (rootpassword in this case).

To list databases:

SHOW DATABASES;

To connect to the testdb database:

USE testdb;

To create a new table:

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

To insert data:

INSERT INTO users (name, email) VALUES ('Alveera', 'alv@example.com');

To retrieve data:

SELECT * FROM users;

🚀 Step 6: Stop and Restart MySQL

To stop MySQL:

docker-compose down

To restart MySQL:

docker-compose up -d

📌 Step 7: Push to GitHub

# 📂 Project Structure
Containerized-MySQL/ │── docker-compose.yml # Docker Compose configuration │── README.md # Documentation

✅ Done! 🎉
