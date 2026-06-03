# instancias/zumbis/eletricos.py
from classes.personagens.inimigos.zumbi import Zumbi
from classes.personagens.inimigos.boss import Boss

zumbi_eletrico_1 = Zumbi(
    "Auxiliar Elétrica",
    10, 10, 5,
    "zumbi_eletrico_1.txt", "Cobre", "Chumbo"
)

zumbi_eletrico_2 = Zumbi(
    "Técnico Elétrico",
    10, 10, 5,
    "zumbi_eletrico_2.txt", "Cobre", "Chumbo"
)

boss_eletrico = Boss(
    "Engenheiro Elétrico",
    20, 20, 10,
    "boss_eletrico.txt", "Cobre", "Chumbo"
)

eletricos = [zumbi_eletrico_1, zumbi_eletrico_2, boss_eletrico]