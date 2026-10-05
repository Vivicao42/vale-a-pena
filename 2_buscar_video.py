from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import json

# 1. carrega a chave do .env
load_dotenv()
CHAVE = os.getenv("YOUTUBE_API_KEY")

def buscar_video(termo) -> dict:
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": termo,
        "type": "video",
        "key": CHAVE,
        "maxResults": 10,
        "relevanceLanguage": "pt",
        "regionCode": "BR",
    }
    resposta = requests.get(url, params=params)
    dados = resposta.json()
    
    return dados
    
def extrair_ids(dados) -> list:
    lista_ids = []
    for item in dados["items"]:
        lista_ids.append(item["id"]["videoId"])
    
    return lista_ids

def salvar_json(dados: dict, caminho: str) -> None:
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    conteudo = json.dumps(dados, indent=2, ensure_ascii=False)
    caminho.write_text(conteudo, encoding="utf-8")
        
def buscar_varios_termos(termos):
    todos_ids = []
    for termo in termos:
        dados = buscar_video(termo)
        nome_arquivo = termo.replace("#", "").replace(" ", "_")
        salvar_json(dados, f"dados/raw/busca_{termo}.json")
        ids = extrair_ids(dados)
        todos_ids.extend(ids)
    
    
    return list(set(todos_ids))

def salvar_ids(ids: list, caminho: str) -> None:
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text("\n".join(ids), encoding="utf-8")


if __name__ == "__main__":
    TERMOS = ["base maquiagem", "resenha base", "#base"]
    ids_unicos = buscar_varios_termos(TERMOS)
  
    salvar_ids(ids_unicos, "dados/id_video.txt")
    print("Total de IDs:", len(ids_unicos))
    print("Salvei em dados/id_videos.txt")