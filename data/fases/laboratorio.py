# data/fases/laboratorio.py
from data.zumbis.acidos import zumbi_acido_1, zumbi_acido_2, boss_acido

fase_laboratorio = {
    "numero": 3,
    "nome": "Laboratório",
    "descricao": "",
    "inimigos": [
        zumbi_acido_1,
        zumbi_acido_2,
        boss_acido
    ]
}