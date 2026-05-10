# data/zumbis/eletricos.py
from classes.personagens.zumbi import Zumbi
from classes.personagens.boss import Boss

auxiliar_eletrico = Zumbi(
    "Auxiliar Eletrico",
    10, 10, 5,
    [
        "imagem"
    ]
)

tecnico_eletrico = Zumbi(
    "Técnico Elétrico",
    10, 10, 5,
    [
        "imagem"
    ]
)

engenheiro_eletrico = Boss(
    "Engenheiro Elétrico",
    20, 20, 10,
    [
        "imagem"
    ]
)