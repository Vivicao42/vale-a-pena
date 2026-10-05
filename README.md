# Vale a Pena? — Pipeline de reviews de maquiagem

Pipeline de dados que unifica reviews de maquiagem de diversas fontes para ajudar as consumidoras a decidir se um produto vale a pena comprar.

## O problema

Este projeto surgiu da necessidade de unificar todos as avaliaçoes de produtos de maquiagem em um so lugar. Se eu quiser saber se a base hidra glow da niina secrets é boa, eu preciso acessar o tiktok, o instagram, o yt, sites de venda de maquiagem, etc. So nessa busca eu ja perdi a vontade de saber se aquele produto vale ou nao a pena comprar.

## Como funciona

1. Busca vídeos de resenha no YouTube por palavra-chave e hashtag
2. Coleta os comentários de cada vídeo

## Estrutura
vale-a-pena/
├── 1_baixar.py
├── 2_buscar_video.py
├── dados/
│ ├── id_videos.txt
│ └── comentarios.csv
├── .env.example
└── README.md


## Como rodar

(ainda em construção)

## Decisões técnicas

- **YouTube API em vez de scraping:** APIs oficiais evitam violação de termos de uso.
- **Busca por palavra-chave + hashtag:** diversifica youtubers e reduz viés de amostragem.
- **Deduplicação com `set()`:** o mesmo vídeo pode aparecer em mais de um termo de busca.

## Status

- [x] Coleta de comentários
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


