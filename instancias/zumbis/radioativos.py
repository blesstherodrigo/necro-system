# instancias/zumbis/radioativos.py
from classes.personagens.inimigos.zumbi import Zumbi
from classes.personagens.inimigos.boss import Boss

zumbi_radioativo_1 = Zumbi(
    "Operario Radioativo",
    10, 10, 5,
    "zumbi_radioativo_1.txt",
    "Ataque Radioativo 1",
    "Chumbo", "Titânio"
)

zumbi_radioativo_2 = Zumbi(
    "Administrador Radioativo",
    10, 10, 5,
    "zumbi_radioativo_2.txt",
    "Ataque Radioativo 2",
    "Chumbo", "Titânio"
)

boss_radioativo = Boss(
    "Segurança Radioativo",
    20, 20, 10,
    "boss_radioativo.txt",
    ["Ataque Radioativo 3", "Defesa Radioativa", "Cura Radioativa", "Concentração Radioativa"],
    "Chumbo", "Titânio"
)

radioativos = [zumbi_radioativo_1, zumbi_radioativo_2, boss_radioativo]