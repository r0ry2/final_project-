DevOps
Installation & Setup
___
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

