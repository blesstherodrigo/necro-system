# data/zumbis/radioativos.py
from classes.personagens.zumbi import Zumbi
from classes.personagens.boss import Boss

zumbi_radioativo_1 = Zumbi(
    "Operario Radioativo",
    10, 10, 5,
    [
        "Imagem"
    ]
)

zumbi_radioativo_2 = Zumbi(
    "Administrador Radioativo",
    10, 10, 5,
    [
        "Imagem"
    ]
)

boss_radioativo = Boss(
    "Segurança Radioativo",
    20, 20, 10,
    [
        "Imagem"
    ]
)