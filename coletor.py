import os
import json
from pathlib import Path

import requests
import pandas as pd
from dotenv import load_dotenv


# 1. carrega a chave do .env
load_dotenv()
CHAVE = os.getenv("YOUTUBE_API_KEY")

def salvar_json(dados: dict, caminho: str) -> None:
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    conteudo = json.dumps(dados, indent=2, ensure_ascii=False)
    caminho.write_text(conteudo, encoding="utf-8")
  

def baixar_comentarios(id_video):
    # 3. monta a URL e os parâmetros
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
    "part": "snippet",
    "videoId": id_video,
    "key": CHAVE,
    "maxResults": 100,
    }
    # 4. faz o pedido
    resposta = requests.get(url, params=params)
    #print(resposta.status_code)
    dados = resposta.json()
    #print(json.dumps(dados, indent=2)[:2000]) 
    #"Pega o dicionário dados, transforma numa string JSON formatada com 2 espaços de recuo por nível, 
    # e imprime só os primeiros 2000 caracteres."
    
  
    salvar_json(dados, f"dados/raw/comentarios_{id_video}.json")

    lista_comentarios = []
    for item in dados["items"]:
        snippet_comentario = item["snippet"]["topLevelComment"]["snippet"]
    
        lista_comentarios.append({
            "texto": snippet_comentario["textDisplay"],
            "autor": snippet_comentario["authorDisplayName"],
            "data": snippet_comentario["publishedAt"],
        })
    return lista_comentarios


# ==== quando roda como script ====
if __name__ == "__main__":
    comentarios = baixar_comentarios("9uadMPZfZc4")
    print("Total:", len(comentarios))

    tabela = pd.DataFrame(comentarios)
    tabela.to_csv("dados/comentarios.csv", index=False)
    print("Salvei", len(tabela), "comentários em dados/comentarios.csv")
