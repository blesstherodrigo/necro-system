# instancias/zumbis/infectados.py
from classes.personagens.inimigos.Lista_de_Zumbis.zumbi_infectado import Zumbi_Infectado

zumbi_infectado_1 = Zumbi_Infectado(
    "Paciente Infectado",
    10, 10, 5,
    "zumbi_infectado_1.txt", "Ferro", "Cobre"
)

zumbi_infectado_2 = Zumbi_Infectado(
    "Enfermeira Infectada",
    10, 10, 5,
    "zumbi_infectado_2.txt", "Ferro", "Cobre"
)

infectados = [zumbi_infectado_1, zumbi_infectado_2]

''' MOVIMENTOS
Zumbi Comum

    Mordida infecciosa: causa 12 de dano
    Garras Necróticas: causa 23 de dano
====================

Boss:

    Triagem Cruel: Ataca com uma Seringa Gigante causando 30 de dano

    Tratamento de Choque: Ele ataca com um desfribilador quebrado juntando cabos, causa dano mas ele tambem perde sua vida
'''