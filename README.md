## Study Project with Apache Airflow:Passing Data Between Tasks ##
[Para acessar o vídeo dessa tarefa clique aqui](https://www.youtube.com/watch?v=AGbUmwZVTY4)

This repository has a set of simple ETL DAGs made to learn the basic concepts of Apache Airflow.

The goal is to show step by step how to create DAGs, read data from a CSV, make transformations, and save the results in different layers (raw/bronze, silver, gold).


 ## Project Goals ##

By studying this repository, you will learn:

🌟 What a DAG is and how Airflow organizes pipelines.

🌟 How to use TaskFlow API (@dag and @task) to write tasks.

🌟 The difference between passing data directly (with XCom) and using file paths.

🌟 How to build a simple layered architecture (Bronze → Silver → Gold).

🌟 How the Extract → Transform → Load (ETL) flow works in practice.


## Estrutura do Repositório ##

.
├── dags/
│   ├── etl_pipeline_aula.py        # DAG 1 - Versão simples (retorno em dicionário)
│   ├── etl_pipeline_aula01.py      # DAG 2 - Versão usando caminhos de arquivos
│   ├── etl_pipeline_aula02.py      # DAG 3 - Versão com camadas Bronze/Silver/Gold
├── datasets/
│   └── movie.csv                 # Arquivo de entrada
├── data/
│   ├── bronze/                   # Dados brutos (extraídos)
│   ├── silver/                   # Dados transformados
│   └── gold/                     # Dados carregados
│── docker-compose.yml            # Setup infraestrutura
│
│── init.sh                       # SETUP Airflow
│── requirements.txt
└── README.md                     # Este guia

## Requirements ##

Create an environment with the following dependencies:

``` apache-airflow==2.7.1 pandas ```

🔶 If you are running with Docker + docker-compose, you don’t need to install it manually.

## How to Run ##

Clone this repository:

```git clone https://github.com/your-username/airflow-etl-classes.git ```

```cd airflow-etl-classes ```


Start Airflow with Docker (if using docker-compose.yml):

``` docker-compose up -d ``` 


Open the Airflow web interface:
🌟 http://localhost:8080

Enable and run the DAGs:

``` etl_pipeline_aula.py ``` - simplest version (to_dict).

``` etl_pipeline_aula01.py ``` -  version using file paths.

``` etl_pipeline_aula02.py ``` - version with Bronze/Silver/Gold layers.


## Study DAGs ##

🔶 DAG 1 – etl_pipeline_aula

Extracts data from CSV.

Transforms column names.

Loads into a single transformed file.

🧚🏾‍♀️Learning: Pass data between tasks using XCom (returning a dictionary).

🔶 DAG 2 – etl_pipeline_aula01

Extracts and saves data to a file.

Transforms by reading the previous file.

Loads into a final file.

🧚🏾Learning: Pass only file paths between tasks (more efficient than XCom for large data).

🔶 DAG 3 – etl_pipeline_aula02

Extracts and saves to Bronze.

Transforms and saves to Silver.

Loads and saves to Gold.

🧚🏾‍♀️Learning: Medallion architecture (Bronze → Silver → Gold).

## To Learn More ##

[Official Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html)

[TaskFlow API](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html)

[Medallion Architecture concept(Databricks)](https://www.databricks.com/br/glossary/medallion-architecture)

[Pass data between tasks (Astronomer)](https://www.astronomer.io/docs/learn/airflow-passing-data-between-tasks)

## Next Steps ##

Create DAGs with dynamic parameters (using Airflow macros).

Schedule DAGs with different schedule_interval.

Add data quality checks (nulls, duplicates).

Test DAGs locally with airflow tasks test.

## ✨ Contribution ##

This project is educational. If you want to contribute:

Add new example DAGs.

Suggest improvements for the README.

Share questions and discussions.


### Prerequisites ###

[Docker](https://docs.docker.com/desktop/setup/install/windows-install/)
[Docker Compose](https://docs.docker.com/compose/)
[Arquivo docker-compose.yaml](https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml)

**Check if the following are installed:**

``` docker --version ```

``` docker compose version ```


### How to Run the Project ###

1. Extract the Project

Unzip the project into any folder on your computer.

Make sure Docker and Docker Compose are installed.

Ensure ports 8080 (Airflow), 5432 (Postgres), and 6379 (Redis) are free, or change them in docker-compose.yml.


2. Start the Containers 

``` docker compose up -d ```


3. This will start:

Postgres (metadata database + ETL data)

Redis (task queue for CeleryExecutor)

Airflow (webserver, scheduler, worker, triggerer)

Access the Airflow Web Interface

Open in your browser:

🌟 http://localhost:8080

Default login: 

User: airflow

Password: airflow

## How Initialization Works ##

The airflow-init service runs ``` init.sh. ```

Executes migrations on the Airflow database.

Creates the default user airflow / airflow.

Creates **postgres_default** connection pointing to the project’s Postgres.

After that, the other services (webserver, scheduler, worker, triggerer) start automatically.

## About the Files ##

**DAGs:** ./dags/

**Datasets (CSV):** ./datasets/

**Local Data Lake:** ./data/

## Stop the Containers ##
``` docker compose down ```

## Reset Everything (including database) ##

```docker compose down -v ```


**-v:** removes persistent volumes (database, logs)

**--remove-orphans:** removes old containers not listed in docker-compose.yml

## Common Errors ##

Port 8080 occupied: change in docker-compose.yml or free the port

Port 5432 occupied: change Postgres port in docker-compose.yml

Locked volumes: use docker compose down -v --remove-orphans

## Reproducibility ##

Portable environment: works on Linux, Mac, and Windows.

Uses Docker images with fixed versions.

Airflow configuration is automated via ``` init.sh. ```

Database always starts with the same schema (credsimples.sql).

## Improvements ##
1. Logging and Monitoring

Create detailed ETL logs: number of rows processed, errors, alerts.

Save inconsistent data reports for review (data quality table).

Ensure traceability: which transaction came from which file/source.

## Feedbacks? contact me: ##

🫂 [Regilene Mariano](https://www.linkedin.com/in/regilene-mariano-a973722a4/)

📩 **regimaria015@gmail.com**

