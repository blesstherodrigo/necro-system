# data/fases/estacaoEnergia.py
from data.zumbis.eletricos import auxiliar_eletrico, tecnico_eletrico, engenheiro_eletrico

zumbi_1 = auxiliar_eletrico
zumbi_2 = tecnico_eletrico
boss = engenheiro_eletrico

fase_estacao_de_energia = {
    "numero": 2,
    "nome": "Estação de Energia",
    "descricao": "",
    "inimigos": [
        zumbi_1,
        zumbi_2,
        boss
    ]
}