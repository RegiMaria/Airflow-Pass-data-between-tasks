# ---- IMPORTAÇÕES ----
from airflow import DAG
from airflow.decorators import dag, task
from datetime import datetime
import pandas as pd

# ----- CONFIGURAÇÕES INICIAIS -----
FONTE_DADOS = "/opt/airflow/data" # Onde nossos dados serão salvos
INPUT_CSV = "/opt/airflow/datasets/movie.csv" # Nosso arquivo de entrada


# ------ DAG OBJECT -----
@dag(
    dag_id="movies_etl",
    start_date=datetime(2025,9,15),
    schedule_interval="@daily",
    catchup=False,
    description="ETL simples, extrair, transformar e salvar movies.csv em data"

)
def movies_etl():
    # ----- EXTRAÇÃO -----
    @task
    def extract():
        df= pd.read_csv(INPUT_CSV, usecols= ["Series_Title", "Released_Year", "Director"])
        return df.to_dict(orient="records")  # Convert pra dicionário

    # ------ TRANSFORMAÇÃO ------
    @task
    def transform(data):
        df = pd.DataFrame(data)
        df = df.rename(columns={
            "Series_Title":"Título",
            "Released_Year": "Ano_Lançamento",
            "Director":"Diretor"
        })
        return df.to_dict(orient="records")
        
    # ----- CARREGAMENTO -----
    @task
    def load(data):
        df = pd.DataFrame(data)
        df.to_csv(f"{FONTE_DADOS}/movies_transformes.csv", index=False)
        print("Dados carregados com sucesso!")
       
    # ----- DEFINIR DEPENDÊNCIAS -----
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)

# Instancia a DAG
dag = movies_etl()

