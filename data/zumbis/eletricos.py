# data/zumbis/eletricos.py
from classes.personagens.inimigos.zumbi import Zumbi
from classes.personagens.inimigos.boss import Boss

zumbi_eletrico_1 = Zumbi(
    "Auxiliar Elétrico",
    10, 10, 5,
    [
        "imagem"
    ], "Cobre", "Chumbo"
)

zumbi_eletrico_2 = Zumbi(
    "Técnico Elétrico",
    10, 10, 5,
    [
        "imagem"
    ], "Cobre", "Chumbo"
)

boss_eletrico = Boss(
    "Engenheiro Elétrico",
    20, 20, 10,
    [
        "imagem"
    ], "Cobre", "Chumbo"
)

eletricos = [zumbi_eletrico_1, zumbi_eletrico_2, boss_eletrico]