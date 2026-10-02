Onde eu parei:

2_buscar_videos.py tá funcionando, mas deu erro list indices must be integers or slices, not str

Provavelmente é confusão entre devolver dicionário ou lista na buscar_video

Próximo passo: rodar print(type(resultado)) pra descobrir o que é

O que ainda falta no Tijolo 2:

✅ Decidir o return da buscar_video (dicionário ou lista)

✅✅✅✅✅✅✅✅

Testar termos diferentes pra ver quantos resultados voltam

Loop em várias palavras-chave

Deduplicar

Salvar os IDs num arquivo

Projeto: Vale a pena? - Pipeline de reviews de maquiagem
Pipeline de dados que unifica reviews de maquiagem de diversas fontes para ajudar as consumidoras a decidir se um produto vale a pena comprar.

Coletar reviews de maquiagem dos comentarios dos videos do youtube.
Este projeto surgiu da necessidade de unificar todos as avaliaçoes de produtos de maquiagem em um so lugar. Se eu quiser saber se a base hidra glow da niina secrets é boa, eu preciso acessar o tiktok, o instagram, o yt, sites de venda de maquiagem, etc. So nessa busca eu ja perdi a vontade de saber se aquele produto vale ou nao a pena comprar.

Comecei criando uma funçao que faz downloads de comentarios de videos com ids especificas.



# Vale a Pena? — Pipeline de reviews de maquiagem
Pipeline de dados que unifica reviews de maquiagem de diversas fontes para ajudar as consumidoras a decidir se um produto vale a pena comprar.
(descrição curta)

## O problema
(seu texto revisado)
Este projeto surgiu da necessidade de unificar todos as avaliaçoes de produtos de maquiagem em um so lugar. Se eu quiser saber se a base hidra glow da niina secrets é boa, eu preciso acessar o tiktok, o instagram, o yt, sites de venda de maquiagem, etc. So nessa busca eu ja perdi a vontade de saber se aquele produto vale ou nao a pena comprar.
## Como funciona
(5 passos do fluxo)

## Estrutura
(árvore de arquivos)
\`\`\`
vale-a-pena/
├── coletor.py
├── 2_buscar_videos.py
├── dados/
│   ├── videos.txt
│   └── raw/
├── .env.example
└── README.md
\`\`\`

## Como rodar
(ainda em construção — deixa placeholder)
1. Clone o repositório
2. Crie o arquivo `.env` a partir do `.env.example`
3. Coloque sua chave da YouTube API no `.env`
4. Instale as dependências: `pip install -r requirements.txt`
5. Rode: `python 2_buscar_videos.py`

## Decisões técnicas
- **YouTube API em vez de scraping:** APIs oficiais evitam
  violação de termos de uso.
- **Busca por palavra-chave + hashtag:** diversifica youtubers
  e reduz viés de amostragem.
- **Deduplicação com `set()`:** o mesmo vídeo pode aparecer em
  mais de um termo de busca.

## Status
- [ ] Coleta de comentários
- [x] Busca de vídeos
- [ ] Limpeza
- [ ] Sentimento
- [ ] Dashboard

## Tecnologias
- Python
- requests, python-dotenv, pathlib
- YouTube Data API v3

## Autor
Viviane Sousa de Melo