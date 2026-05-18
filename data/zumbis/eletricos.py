# data/zumbis/eletricos.py
from classes.personagens.zumbi import Zumbi
from classes.personagens.boss import Boss

zumbi_eletrico_1 = Zumbi(
    "Auxiliar Elétrico",
    10, 10, 5,
    [
        "imagem"
    ], "Incendiária", []
)

zumbi_eletrico_2 = Zumbi(
    "Técnico Elétrico",
    10, 10, 5,
    [
        "imagem"
    ], "Incendiária", []
)

boss_eletrico = Boss(
    "Engenheiro Elétrico",
    20, 20, 10,
    [
        "imagem"
    ], "Incendiária", []
)