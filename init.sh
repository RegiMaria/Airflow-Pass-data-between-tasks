#!/bin/bash
set -e

# Atualiza o banco do Airflow
airflow db upgrade

# Cria usuário admin (ignora se já existir)
airflow users create \
    --username airflow \
    --password airflow \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com || true

# Remove conexão antiga caso exista
airflow connections delete postgres_default || true

# Adiciona a conexão default do Postgres
airflow connections add postgres_default \
    --conn-type postgres \
    --conn-login airflow \
    --conn-password airflow \
    --conn-host postgres \
    --conn-port 5432 \
    --conn-schema airflow || true

echo "Conexão postgres_default criada com sucesso!"
