# instancias/zumbis/acidos.py
from classes.personagens.inimigos.zumbi import Zumbi
from classes.personagens.inimigos.boss import Boss

zumbi_acido_1 = Zumbi(
    "Cobaia Ácida",
    10, 10, 5,
    [
        "Imagem"
    ], "Titânio", "Ferro"
)

zumbi_acido_2 = Zumbi(
    "Analista Ácido",
    10, 10, 5,
    [
        "Imagem"
    ], "Titânio", "Ferro"
)

boss_acido = Boss(
    "Cientista Ácido",
    20, 20, 10,
    [
        "Imagem"
    ], "Titânio", "Ferro"
)

acidos = [zumbi_acido_1, zumbi_acido_2, boss_acido]