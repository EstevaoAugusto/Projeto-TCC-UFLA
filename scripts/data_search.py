import requests
import pandas as pd                 # Biblioteca para manipulação e análise de dados
import sys                          # Biblioteca para acessar variaveis e funções que interagem fortemente com o interpretador
from pathlib import Path            # Biblioteca para a manipulação de caminhos do sistema a nivel orientado a objetos
import time
import os

ROOT_DIRECTORY_PATH = Path("__file__").resolve().parent
PARENT_DIRECTORY_PATH = ROOT_DIRECTORY_PATH.parent

if str(PARENT_DIRECTORY_PATH) not in sys.path:
    sys.path.append(str(PARENT_DIRECTORY_PATH))

from config_path import *

if __name__ == "__main__":
    raise RuntimeError("O script 'data_search.py' não pode ser executado diretamente!")

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0"}

def web_scrapping(df_link : pd.DataFrame):
    print(f"{'='*60}")
    alt_text_coluna = [] # Lista que terá EXATAMENTE o mesmo tamanho do df_link
    
    quant_registros = len(df_link)
    
    print(f"Processando {quant_registros} requisições de download de imagens.\n")
    
    for i in range(0, quant_registros):
        try:
            registro_atual = df_link.iloc[i]
            id_img = registro_atual['id_img']
            url_img_alvo = registro_atual['link_fonte_imagem_selecionada']
            output = Path(IMAGES_DIRECTORY_PATH) / f"{id_img}.jpg"

            print(f"Requisição {i+1}/{quant_registros}: {id_img}.jpg")
            if output.exists():
                print(f"Arquivo existe: {output}")
                pass

            req_img = requests.get(url_img_alvo, headers=HEADERS, timeout=15)
            output.write_bytes(req_img.content)
            
            time.sleep(3)
        except Exception as e:
            print(f"Erro no índice {i}: {e}")
            alt_text_coluna.append("ERRO_CONEXAO") # Mantém o alinhamento mesmo no erro

    print(f"\n{'='*60}")
    
    print("Web Scrapping Finalizado")
        
    print(f"Arquivo salvo: {PROCESSED_DATA_DIRECTORY_PATH}/dados_processados.csv")
    print(f"{'='*60}\n")