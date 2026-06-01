# instancias/zumbis/eletricos.py
from classes.personagens.inimigos.Lista_de_Zumbis.zumbi_eletrico import Zumbi_Eletrico
from classes.personagens.inimigos.Lista_de_Boss.boss_eletrico import Boss_Eletrico

zumbi_eletrico_1 = Zumbi_Eletrico(
    "Auxiliar Elétrico",
    10, 10, 5,
    "imagem", "Cobre", "Chumbo"
)

zumbi_eletrico_2 = Zumbi_Eletrico(
    "Técnico Elétrico",
    10, 10, 5,
    "imagem", "Cobre", "Chumbo"
)

boss_eletrico = Boss_Eletrico(
    "Engenheiro Elétrico",
    20, 20, 10,
    "imagem", "Cobre", "Chumbo"
)

eletricos = [zumbi_eletrico_1, zumbi_eletrico_2, boss_eletrico]


''' MOVIMENTOS
Zumbi Comum

    Mordida letal: causa 12 de dano
    

====================
Boss:
    Curto-Circuito: Ataque que Causa dano e impede de usar um medicamento na próxima rodada

    Tempestade de Ìons: Causa 15 de dano

    Choque Estático: Ataque físico básico. Tem 30% de chance de aplicar Paralisia (o jogador perde o próximo turno) ou Lentidão (joga por último no próximo turno).

'''