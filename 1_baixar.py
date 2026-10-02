from dotenv import load_dotenv
import os
import requests
import pandas as pd
import json

# 1. carrega a chave do .env
load_dotenv()
CHAVE = os.getenv("YOUTUBE_API_KEY")


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

    lista_comentarios = []
    for item in dados["items"]:
        snippet_comentario = item["snippet"]["topLevelComment"]["snippet"]
    
        lista_comentarios.append({
            "texto": snippet_comentario["textDisplay"],
            "autor": snippet_comentario["authorDisplayName"],
            "data": snippet_comentario["publishedAt"],
        })
    return lista_comentarios
   #REPITO A MESMA COISA NO EXEMPLO COMENTADO DE BAIXO 
    
#  passo 1: pega o valor de fora
# texto_do_comentario = snippet_comentario["textDisplay"]

# # passo 2: monta um dicionário com esse valor
# comentario_individual = {
#     "texto": texto_do_comentario,
#     "autor": snippet_comentario["authorDisplayName"],
# }

# # passo 3: coloca o dicionário na lista
# comentarios.append(comentario_individual)
    
    
    # print("Total de comentários:", len(lista_comentarios))
    # return lista_comentarios

# ==== quando roda como script ====
if __name__ == "__main__":
    comentarios = baixar_comentarios("9uadMPZfZc4")
    print("Total:", len(comentarios))

    tabela = pd.DataFrame(comentarios)
    tabela.to_csv("dados/comentarios.csv", index=False)
    print("Salvei", len(tabela), "comentários em dados/comentarios.csv")

#tabela = pd.DataFrame(comentarios)
#tabela.to_csv("dados/comentarios.csv", index=False)
#print("Salvei", len(tabela), "comentários em dados/comentarios.csv")