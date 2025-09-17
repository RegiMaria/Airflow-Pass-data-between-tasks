# ---- IMPORTAÇÕES ----
from airflow import DAG
from airflow.decorators import dag, task
from datetime import datetime
import pandas as pd
import os

# ----- CONFIGURAÇÕES INICIAIS -----
FONTE_DADOS = "/opt/airflow/data" # Onde nossos dados serão salvos
INPUT_CSV = "/opt/airflow/datasets/movie.csv" # Nosso arquivo de entrada


BRONZE_PATH = os.path.join(FONTE_DADOS, "bronze") 
SILVER_PATH = os.path.join(FONTE_DADOS, "silver")
GOLD_PATH = os.path.join (FONTE_DADOS, "gold")

# ----- CRIAR PASTAS ------
os.makedirs(BRONZE_PATH, exist_ok=True)
os.makedirs(SILVER_PATH, exist_ok=True)
os.makedirs(GOLD_PATH, exist_ok=True)

# ------ DAG OBJECT -----
@dag(
    dag_id="movies_etl_aula02",
    start_date=datetime(2025,9,15),
    schedule_interval="@daily",
    catchup=False,
    description="ETL bronze -- > silver --> gold em data"

)
def movies_etl():
    # ----- EXTRAÇÃO -----
    @task
    def extract():
        """EXTRAI DADOS DA ONTE E SALVA EM BRONZE"""
        df= pd.read_csv(INPUT_CSV, usecols= ["Series_Title", "Released_Year", "Director"])
        output_path = os.path.join (BRONZE_PATH, "movies_extracted_bronze_aula01.csv")
        df.to_csv(output_path, index=False)
        return output_path  # Retorna caminho do arquivo

    # ------ TRANSFORMAÇÃO ------
    @task
    def transform(input_path: str):
        """TRANSFORMA DADOS E SALVA NA CAMADA SILVER"""
        df = pd.read_csv(input_path)
        df = df.rename(columns={
            "Series_Title":"Título",
            "Released_Year": "Ano_Lançamento",
            "Director":"Diretor"
        })
        output_path = os.path.join(SILVER_PATH, "movies_transformed_silver_aula01.csv")
        df.to_csv(output_path, index=False)
        return output_path # Apenas o caminho
        
    # ----- CARREGAMENTO -----
    @task
    def load(input_path: str):
        """CARREGA DADOS DA SILVER E SALVA NA CAMADA GOLD"""
        df = pd.read_csv(input_path)
        final_path = os.path.join(GOLD_PATH,"movies_loaded_gold_aula01.csv")
        df.to_csv(final_path, index=False)
        print("Dados carregados com sucesso em {final_path}!")
        return final_path
       
    # ----- DEFINIR DEPENDÊNCIAS -----
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)

# Instancia a DAG
dag = movies_etl()

