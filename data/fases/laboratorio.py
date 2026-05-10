# data/fases/laboratorio.py
from data.zumbis.acidos import cobaia_acida, analista_acido, cientista_acido

zumbi_1 = cobaia_acida
zumbi_2 = analista_acido
boss = cientista_acido

fase_laboratorio = {
    "numero": 3,
    "nome": "Laboratório",
    "descricao": "",
    "inimigos": [
        zumbi_1,
        zumbi_2,
        boss
    ]
}