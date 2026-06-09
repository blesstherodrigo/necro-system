# instancias/zumbis/eletricos.py
from classes.personagens.inimigos.zumbi import Zumbi
from classes.personagens.inimigos.boss import Boss

zumbi_eletrico_1 = Zumbi(
    "Auxiliar Elétrica",
    27, 27, 10,
    "zumbi_eletrico_1.txt",
    "Ataque Elétrico 1",
    "Cobre", "Chumbo"
)

zumbi_eletrico_2 = Zumbi(
    "Técnico Elétrico",
    30, 30, 12.5,
    "zumbi_eletrico_2.txt",
    "Ataque Elétrico 2",
    "Cobre", "Chumbo"
)

boss_eletrico = Boss(
    "Engenheiro Elétrico",
    65, 65, 20,
    "boss_eletrico.txt",
    ["Ataque Elétrico 3", "Defesa Elétrica", "Cura Elétrica", "Concentração Elétrica"],
    "Cobre", "Chumbo"
)

eletricos = [zumbi_eletrico_1, zumbi_eletrico_2, boss_eletrico]