# data/fases.py
from data.zumbis.infectados import zumbi_infectado_1, zumbi_infectada_2, boss_infectado

fase_1 = {
    "numero": 1,
    "nome": "Hospital",
    "descricao": "Corredores escuros, macas quebradas e gritos ao longe.",
    "inimigos": [
        zumbi_infectado_1,
        zumbi_infectada_2,
        boss_infectado
    ]
}

from data.zumbis.eletricos import zumbi_eletrico_1, zumbi_eletrico_2, boss_eletrico

fase_2 = {
    "numero": 2,
    "nome": "Estação de Energia",
    "descricao": "",
    "inimigos": [
        zumbi_eletrico_1,
        zumbi_eletrico_2,
        boss_eletrico
    ]
}

from data.zumbis.acidos import zumbi_acido_1, zumbi_acido_2, boss_acido

fase_3 = {
    "numero": 3,
    "nome": "Laboratório",
    "descricao": "",
    "inimigos": [
        zumbi_acido_1,
        zumbi_acido_2,
        boss_acido
    ]
}

from data.zumbis.radioativos import zumbi_radioativo_1, zumbi_radioativo_2, boss_radioativo

fase_4 = {
    "numero": 4,
    "nome": "Usina Nuclear",
    "descricao": "",
    "inimigos": [
        zumbi_radioativo_1,
        zumbi_radioativo_2,
        boss_radioativo
    ]
}