# instancias/zumbis/acidos.py
from classes.personagens.inimigos.zumbi import Zumbi
from classes.personagens.inimigos.boss import Boss

zumbi_acido_1 = Zumbi(
    "Cobaia Ácida",
    37, 37, 12.5,
    "zumbi_acido_1.txt",
    "Ataque Ácido 1",
    "Titânio", "Ferro"
)

zumbi_acido_2 = Zumbi(
    "Analista Ácido",
    40, 40, 15,
    "zumbi_acido_2.txt",
    "Ataque Ácido 2",
    "Titânio", "Ferro"
)

boss_acido = Boss(
    "Cientista Ácida",
    80, 80, 24,
    "boss_acido.txt",
    ["Ataque Ácido 3", "Defesa Ácida", "Cura Ácida", "Concentração Ácida"],
    "Titânio", "Ferro"
)

acidos = [zumbi_acido_1, zumbi_acido_2, boss_acido]