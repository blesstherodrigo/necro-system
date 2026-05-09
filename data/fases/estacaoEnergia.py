# data/fases/estacaoEnergia.py

from data.zumbis.eletricos import auxiliar, tecnico, engenheiro

zumbi_1 = auxiliar.auxiliar_eletrico
zumbi_2 = tecnico.tecnico_eletrico
boss = engenheiro.engenheiro_eletrico

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