# ---- IMPORTAÇÕES ----
from airflow import DAG
from airflow.decorators import dag, task
from datetime import datetime
import pandas as pd
import os

# ----- CONFIGURAÇÕES INICIAIS -----
FONTE_DADOS = "/opt/airflow/data" # Onde nossos dados serão salvos
INPUT_CSV = "/opt/airflow/datasets/movie.csv" # Nosso arquivo de entrada


# ------ DAG OBJECT -----
@dag(
    dag_id="movies_etl_aula01",
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
        output_path = os.path.join (FONTE_DADOS, "movies_extracted_aula01.csv")
        df.to_csv(output_path, index=False)
        return output_path  # Retorna caminho, não so dados em si como dicionário

    # ------ TRANSFORMAÇÃO ------
    @task
    def transform(input_path: str):
        df = pd.read_csv(input_path)
        df = df.rename(columns={
            "Series_Title":"Título",
            "Released_Year": "Ano_Lançamento",
            "Director":"Diretor"
        })
        output_path = os.path.join(FONTE_DADOS, "movies_transformed_aula01.csv")
        df.to_csv(output_path, index=False)
        return output_path # Apenas o caminho
        
    # ----- CARREGAMENTO -----
    @task
    def load(input_path: str):
        df = pd.read_csv(input_path)
        final_path = os.path.join(FONTE_DADOS,"movies_loaded_aula01.csv")
        df.to_csv(final_path, index=False)
        print("Dados carregados com sucesso!")
       
    # ----- DEFINIR DEPENDÊNCIAS -----
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)

# Instancia a DAG
dag = movies_etl()

