# data/zumbis/radioativos.py
from classes.personagens.zumbi import Zumbi
from classes.personagens.boss import Boss

operario_radioativo = Zumbi(
    "Operario Radioativo",
    10, 10, 5,
    [
        "Imagem"
    ]
)

administrador_radioativo = Zumbi(
    "Administrador Radioativo",
    10, 10, 5,
    [
        "Imagem"
    ]
)

seguranca_radioativo = Boss(
    "Segurança Radioativo",
    20, 20, 10,
    [
        "Imagem"
    ]
)