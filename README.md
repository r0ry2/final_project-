DevOps
Installation & Setup
___
1. Docker 
🐳 What is Docker?
Docker is an open source platform that helps you run any application inside a lightweight, isolated box called a container.

🔹 The idea:
Instead of installing software (database, libraries, tools) directly on your device and encountering problems (for example, some libraries work for you but not for me), Docker puts everything ready and integrated inside its own container.

📦 What is a container?
A container is a lightweight, isolated environment in which an application runs with everything it needs (code, libraries).
The container uses the underlying kernel but remains isolated from other containers.
You can think of it as a small box containing your application and all its tools.

🎯The main goal of Container is to learn how to run a small web application inside a container without having to install any server on your machine.

🎯 Why we use Docker?
Solving compatibility issues: The application works the same way for everyone.
1- Portability: The same container runs on Windows, Mac, or Linux.
2- Speed: Containers are lightweight and launch in seconds.
3- Isolation: Each application is isolated from the others.
4- Scalability: You can easily run thousands of containers.


2. Docker Compose & YAML
What is Docker Compose?
🔹 Docker Compose is a tool that lets you easily manage multiple containers at the same time.
🔹 Instead of running each container with lengthy commands in the terminal, you write a single YAML file that specifies:
- Which images to use.
- Container names.
- Ports.
- Passwords.
- The network between them.
📌 Result:
Turns everyone on with one command:
docker-compose up -d

What is the docker-compose.yaml file?
🔹 It's a YAML file (space-delimited, no parentheses).
🔹 It defines each container and its details.
📌 Example: If you have three databases (Postgres, MySQL, MongoDB), you would write them in a single file.

![Docker Hello World](images/hello-docker.png)

## Steps
1. Install Docker
2. Run Hello World
3. Run PostgreSQL container
4. Run Cassandra container
5. Run MongoDB container
6. Connect databases with Jupyter
7. Document everything on GitHub

What is required of us in the project is to install the tools (Kafka, Cassandra, PostgreSQL, Anaconda, Docker, InfluxDB) inside Docker and make sure that they work together (Installation & Setup) only, not to build a complete system or programming 

Our goels :
Install and run each tool provided by the doctor inside a Docker container.
Ensure that the containers are running and accessible.
You may need to connect them to each other using a simple network inside Docker.
Main Objective: To understand the basic tools commonly used in Algorithmic Trading projects.

Tools
Docker → Foundation, which is the container in which we run everything.
Apache Kafka → Streaming system.
Apache Cassandra (SQL) → Distributed database.
PostgreSQL → Traditional SQL database.
Anaconda → Python programming environment (can be used inside a container).
InfluxDB → Time-series database (suitable for financial data).
Algorithmic Trading → You won't actually build it, just install a basic environment to support it.

Project work steps :
1- Preparing the work environment
- Download Docker Desktop (docker --version)
- (Optional but important) Download Docker Compose, it makes it easier to run more than one tool together. (docker-compose )

* NOTE : Docker Compose installation steps:
No download required: When you download Docker Desktop, Docker Compose comes with it automatically.

2- Create a folder for the project.
mkdir trading-tools-docker
cd trading-tools-docker

3-  Create docker-compose.yml file(Docker Compose)
This file combines all the tools (Kafka, Cassandra, PostgreSQL, Anaconda, InfluxDB).

When you run the command:
(docker-compose up -d)

Docker will:
- Download images (ready-made software) from the internet.
- Create containers for each tool.
- Connect them together (like a small network between them).
- Open ports for you so you can access them from your device.


4-Operate the tools
docker-compose up -d

5- Check that it is working.
- To make sure Docker Desktop is running
- Ensure that Kafka runs inside Docker.
- Open the Terminal Type the command: (docker ps)
- Cassandra: Connect to the container via cqlsh.
- PostgreSQL: Try logging in with user/password (admin/admin).
- InfluxDB: Open http://localhost:8086 in a browser.
- Anaconda: Enter the terminal → docker exec -it <container_id> bash and try conda --version.



![Database](images/postgres.jpg)
