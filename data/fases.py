# data/fases.py
from classes.fase import Fase

from data.zumbis.infectados import zumbi_infectado_1, zumbi_infectada_2, boss_infectado
from data.zumbis.eletricos import zumbi_eletrico_1, zumbi_eletrico_2, boss_eletrico
from data.zumbis.acidos import zumbi_acido_1, zumbi_acido_2, boss_acido
from data.zumbis.radioativos import zumbi_radioativo_1, zumbi_radioativo_2, boss_radioativo

fase_1 = Fase(
    1,
    "Hospital",
    "Corredores escuros, macas quebradas e gritos ao longe.",
    10,
    [
        zumbi_infectado_1,
        zumbi_infectada_2,
        boss_infectado
    ]
)

fase_2 = Fase(
    2,
    "Estação de Energia",
    "colocar uma descrição",
    10,
    [
        zumbi_eletrico_1,
        zumbi_eletrico_2,
        boss_eletrico
    ]
)

fase_3 = Fase(
    3,
    "Laboratório",
    "colocar uma descrição",
    10,
    [
        zumbi_acido_1,
        zumbi_acido_2,
        boss_acido
    ]
)

fase_4 = Fase(
    4,
    "Usina Nuclear",
    "colocar uma descrição",
    10,
    [
        zumbi_radioativo_1,
        zumbi_radioativo_2,
        boss_radioativo
    ]
)