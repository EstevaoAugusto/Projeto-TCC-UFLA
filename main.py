import scripts.data_search as data_search   #
import os                                   #
import pandas as pd                         # Biblioteca de tratamento e manipulação de dados
from config_path import *                   #
import csv

# Criando os caminhos de pastas necessários
# Os objetos 'Path' abaixo criam a pasta quando ela não existe, incluindo seus parentes.
MODELS_DIRECTORY_PATH.mkdir(exist_ok=True, parents=True)
METRIC_DIRECTORY_PATH.mkdir(exist_ok=True, parents=True)
REPORTS_DIRECTORY_PATH.mkdir(exist_ok=True, parents=True)
SCRIPTS_DIRECTORY_PATH.mkdir(exist_ok=True, parents=True)
IMAGES_DIRECTORY_PATH.mkdir(exist_ok=True, parents=True)
RAW_DATA_DIRECTORY_PATH.mkdir(exist_ok=True, parents=True)
PROCESSED_DATA_DIRECTORY_PATH.mkdir(exist_ok=True, parents=True)

def main():
    if not os.path.exists(f"{RAW_DATA_DIRECTORY_PATH}/links_noticiarios.csv"):
        raise RuntimeError("Arquivo 'links_noticiarios.csv' não foi encontrado")
    
    df_links_raw = pd.read_csv(f"{RAW_DATA_DIRECTORY_PATH}/links_noticiarios.csv", sep=",", quotechar='"')
    df_links_raw = df_links_raw.dropna(axis=0).reset_index(drop=True)
    
    df_links_raw.to_csv("teste.csv", index=False)
    
    df_links_raw.to_csv(
        f"{PROCESSED_DATA_DIRECTORY_PATH}/link_noticiarios_novo.csv",
        sep=';',
        index=False,
        quoting=csv.QUOTE_ALL,
        encoding='utf-8'
    )
    
    df_link_processed = pd.read_csv(f"{PROCESSED_DATA_DIRECTORY_PATH}/link_noticiarios_novo.csv", sep=';', quotechar='"')
    
    print("Iniciando Script")
    
    data_search.web_scrapping(df_link_processed)
    
    print("Script Finalizado")
    
if __name__ == "__main__":
    main()