from pathlib import Path
from coletor import baixar_comentarios
from datetime import datetime
import pandas as pd

caminho_ids = Path('dados/id_video.txt')
linhas = caminho_ids.read_text(encoding='utf-8').splitlines()

todos_caminhos = []
for id in linhas: 
    todos_caminhos.extend(baixar_comentarios(id))

tabela = pd.DataFrame(todos_caminhos)

agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
caminho_saida = Path(f'dados/comentarios_{agora}.csv')

caminho_saida.parent.mkdir(parents=True, exist_ok=True)
tabela.to_csv(caminho_saida, index=False)
