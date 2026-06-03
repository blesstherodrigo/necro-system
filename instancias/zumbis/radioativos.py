# instancias/zumbis/radioativos.py
from classes.personagens.inimigos.Lista_de_Zumbis.zumbi_radioativo import Zumbi_Radioativo
from classes.personagens.inimigos.Lista_de_Boss.boss_radioativo import Boss_Radioativo

zumbi_radioativo_1 = Zumbi_Radioativo(
    "Operario Radioativo",
    10, 10, 5,
    "zumbi_radioativo_1.txt", "Chumbo", "Titânio"
)

zumbi_radioativo_2 = Zumbi_Radioativo(
    "Administrador Radioativo",
    10, 10, 5,
    "zumbi_radioativo_2.txt", "Chumbo", "Titânio"
)

boss_radioativo = Boss_Radioativo(
    "Segurança Radioativo",
    20, 20, 10,
    "boss_radioativo.txt", "Chumbo", "Titânio"
)

radioativos = [zumbi_radioativo_1, zumbi_radioativo_2, boss_radioativo]


''' MOVIMENTOS

Zumbi Comum:


Boss:

    Alerta Vermelho: Detonação! : Planta uma bomba no oponente que ao final de 3 turnos ele explode causando 40 de dano

    Tiro radioativo: Acerta uma bala com uma pistola causando dano e tirando efeito de defesa

    Protocolo de confinamento: o zumbi joga o cassetete no chão, e reforça sua armadura aumentando a defesa 

    Recuperação química: o boss absorve a radiação do ambiente e regenera sua vida


'''