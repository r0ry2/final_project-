DevOps
Installation & Setup

___

1. DevOps( Development Operation): 
is a workflow approach that combines software development and IT operations, with the goal of delivering software faster, more reliably, and more consistently through automation. 

Automation is about making everything work with minimal human interaction in these types of processes:
- testing
- deployment
- monitoring
- code integration.

🔹 The basic idea of ​​DevOps:
It is to remove barriers between the development team and the operations team so that they work as one team.

We use tools that help us integrate, such as:
- Docker 🐳
- Kubernetes 
- Jenkins 
- Git 


2. Docker 
## 🐳 What is Docker?

Docker is an open source platform that helps you run any application inside a lightweight, isolated box called a container.
It's a tool that allows you to run programs or databases within containers.

🔹 The idea:
Instead of installing software (database, libraries, tools) directly on your device and encountering problems (for example, some libraries work for you but not for me), Docker puts everything ready and integrated inside its own container.

That means:
No more "works on my machine" issues.
You can run the same environment anywhere.

🎯 Why we use Docker?

Solve compatibility issues: The application works the same way for everyone.

- Portability: Run applications on any device.
The container itself runs on Windows, Mac, or Linux.

- Speed: Containers are lightweight and launch in seconds.

- Isolation: Each application is isolated from the others.

- Scalability: You can easily run thousands of containers.

- Efficiency: Your machine can handle up to 50 containers.

## Project work steps :

## Step 1:Preparing the work environment
🐳 Steps to Install Docker 

1. Download Docker Desktop from Docker website.
## Live Demo
[Visit the website here](https://www.docker.com/products/docker-desktop/)

After downloading,we ran the installation file.
2. Verify that Docker is Download
We opened Terminal and typed:

docker --version

If you see the Docker version : the installation was successful.

3. Run Docker Desktop
After installation, we opened the Docker Desktop application.
If everything is fine, you'll see a running whale icon 🐳 .
4. Test the first container
We typed:

docker run hello-world


What happened:
- Docker communicated with the Server.
- Downloaded an image named hello-world from Docker Hub.
- Run a small container and printed a message:



![hello_docker](images/hello-docker.png)

Now you have a ready-made environment to run any database or application within Docker.
___
## container
3. 📦 What is a container?

After they understand Docker, move on to explain the concept of a Container.

A container is a lightweight, isolated environment in which an application runs with everything it needs (code, libraries).
The container uses the underlying kernel but remains isolated from other containers.

You can think of it as a small box containing all the libraries, tools, and applications.
It's different from a Virtual Machine (lighter, faster, uses the same kernel).

🎯The main goal of Container is to learn how to run a small web application inside a container without having to install any server on your machine


## docker compose 

4. What is Docker Compose?

Docker Compose is a tool that allows you to run multiple containers simultaneously using a single file called docker-compose.yaml.
Instead of running each database or service with lengthy commands, you write them all in a single YAML file(docker-compose.yaml):

Benefit: I don't need to manually operate each database.
Docker Compose = container management.


(System Components)

simulation of a Trading System consists of multiple services:
- Zookeeper: A core program that Kafka needs to run (it manages the brokers).
- Docker Compose → The foundation, which is the container in which we run everything.
- Kafka → A streaming system Responsible for receiving data .
- Anaconda → A Python programming environment (which can be used inside a container).

Each is independent and serves a different type of data: 

- Cassandra (SQL) → A distributed powerful NoSQL database for storage.
- PostgreSQL → A traditional SQL database.
- InfluxDB Time-Series database for storing real-time data (e.g., currency prices every second).


🔗relationships between th server :
![services](images/digram.jpg)

![services](images/Diagram.jpg)


The image depicts a trading system consisting of several services. Each service runs within its own container.

Services:

- Kafka ← Depends on ← Zookeeper
Kafka needs Zookeeper to organize brokers.
Kafka → Databases: Kafka streams incoming data into Databases (Cassandra, Postgres, InfluxDB)

Anaconda ↔ Kafka & Databases
anaconda Connects to all databases (Cassandra + Postgres + InfluxDB) and uses Kafka for Streaming Data.
It is the interface through which we write code and analyze data.


## Step 2: Create a Project Folder
##  Create the docker-compose.yml Filed
![dockerfile-compose](images/docker-compose.png)

What did i do?
i wrote a file named docker-compose.yaml containing definitions for three databases:
- PostgreSQL
- Cassandra
- InfluxDB
In addition. 
- Zookeeper 
- Kafka

Inside the file, we wrote for each database:
- The container name
- The port (so we could access it from outside)
- The username and password (to secure the connection)
___
## Step 3:Verify Everything is Running

witre the comende :

docker-compose up -d
![Running](images/Running.jpg)

Docker will:
- Download images (ready-made software) from the internet.
- Create containers for each tool.
- Connect them together (like a small network between them).
- Open ports for you so you can access them from your device.

docker pc : Displays only containers that are currently running.
![docker_ps](images/docker_ps.jpg)




## Step 4: Access Each Service


![docker-Desktop](images/Docker.jpg)


kafka: docker exec -it trading-tools-docker-kafka-1 bash
![postgresDB](images/postgresDB.jpg)

postgresDB: docker exec -it trading-tools-docker-postgres-1 psql -U admin
![postgresDB](images/postgresDB.jpg)

cassandra: docker exec -it trading-tools-docker-cassandra-1 cqlsh
![postgresDB](images/postgresDB.jpg)

nfluxDB: Open your browser at http://localhost:8086 Login: admin / passeword :rema2002
![Setup](images/Setup.jpg)

![InfluxDB_interface](images/InfluxDB.jpg)


Anaconda / Jupyter :Anaconda is running as a Jupyter server on port :http://localhost:8888
![jupyter](images/jupyter.jpg)
![token](images/token.jpg)
![jupyter_interfase](images/jupyter_interfase.jpg)


## Step 5: How database connect with Anconda 

![Anaconda](images/Anaconda.jpg)

Activate the virtual environment
conda activate cassandra_env

Install the library to communicate with :
- psycopg2
- cassandra-driver
- influxdb-client

![postgres](images/check.jpg)
![postgres](images/postgres.jpg)

postgres:
![postgres](images/postgres.jpg)
cassandra:
![cassandra](images/cassandra.jpg)
Influx:
From inside Anaconda (Python code)
![Influx](images/InfluxDBClient.jpg)
![Influx](images/API_token.jpg)
 
## Step 6: Volumes
In Docker, when you stop a container (the temporary application running Docker), all the data inside it is erased unless you store it somewhere permanent.

That's why we use something called Volumes, which is persistent storage that persists even if the container is stopped or deleted.
![volume](images/volume.jpg)

docker volume ls
This command displays all volumes currently present in the system.

![jupyter_interfase](images/docker_volume.jpg)


