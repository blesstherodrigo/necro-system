# data/fases/hospital.py
from data.zumbis.infectados import zumbi_infectado_1, zumbi_infectada_2, boss_infectado

fase_hospital = {
    "numero": 1,
    "nome": "Hospital",
    "descricao": "Corredores escuros, macas quebradas e gritos ao longe.",
    "inimigos": [
        zumbi_infectado_1,
        zumbi_infectada_2,
        boss_infectado
    ]
}