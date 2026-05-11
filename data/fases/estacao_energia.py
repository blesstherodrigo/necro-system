# data/fases/estacao_energia.py
from data.zumbis.eletricos import zumbi_eletrico_1, zumbi_eletrico_2, boss_eletrico

fase_estacao_de_energia = {
    "numero": 2,
    "nome": "Estação de Energia",
    "descricao": "",
    "inimigos": [
        zumbi_eletrico_1,
        zumbi_eletrico_2,
        boss_eletrico
    ]
}