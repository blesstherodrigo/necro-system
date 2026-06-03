# instancias/zumbis/acidos.py
from classes.personagens.inimigos.Lista_de_Zumbis.zumbi_acido import Zumbi_Acido
from classes.personagens.inimigos.Lista_de_Boss.boss_acido import Boss_Acido

zumbi_acido_1 = Zumbi_Acido(
    "Cobaia Ácida",
    10, 10, 5,
    "cobaia_acida.txt", "Titânio", "Ferro"
)

zumbi_acido_2 = Zumbi_Acido(
    "Analista Ácido",
    10, 10, 5,
    "analista_acido.txt", "Titânio", "Ferro"
)

boss_acido = Boss_Acido(
    "Cientista Ácida",
    20, 20, 10,
    "cientista_acida.txt", "Titânio", "Ferro"
)

acidos = [zumbi_acido_1, zumbi_acido_2, boss_acido]

'''MOVIMENTOS

Zumbi Comum
    ataque basico:
    
    Baba Ácida: 6 de dano (usarei o multiplicador de dano por enquanto)

    Mordida Letal: 20 de dano

================================================
Zumbi Boss:
    
    Chuva de Toxina: ataque em area de 5 de dano, se o escudo estiver reduzido causa dobro de dano 10

    O caldeirão ambulante: Ele absorve os fluídos ácidos ao redor dele e se cura 

    Cuspe Corrosivo: 6 de dano (usarei o multiplicador de dano por enquanto)


    '''