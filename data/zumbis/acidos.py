# data/zumbis/acidos.py
from classes.personagens.zumbi import Zumbi
from classes.personagens.boss import Boss

cobaia_acida = Zumbi(
    "Cobaia Ácida",
    10, 10, 5,
    [
        "Imagem"
    ]
)

analista_acido = Zumbi(
    "Analista Ácido",
    10, 10, 5,
    [
        "Imagem"
    ]
)

cientista_acido = Boss(
    "Cientista Ácido",
    20, 20, 10,
    [
        "Imagem"
    ]
)