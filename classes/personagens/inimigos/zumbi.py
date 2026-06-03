# classes/personagens/inimigos/zumbi.py
from classes.personagens.inimigos.inimigo import Inimigo

class Zumbi(Inimigo):
    def __init__(self, nome, vida, vida_max, dano, imagem, fraqueza=None, imune=None):
        super().__init__(nome, vida, vida_max, dano, imagem, fraqueza, imune)
        
    def realizar_ataque(self):
        print(f"\n{self.nome} arranhou e causou {self.dano} de dano!")
        return self.dano

# Zumbi_Acido
# print(f"O {self.nome} lançou um Ataque de Baba Ácida! Causando {Dano_Total} de dano!")
# print(f" O {self.nome} ataca com uma Mordida Letal! Casuou {Dano_Total} de dano!")
#
# Zumbi_Eletrico
# print(f"O {self.nome} lançou um Ataque Abraço Elétrico! Causando {Dano_Total} de dano!")
# print(f" O {self.nome} ataca com uma Mordida Letal! Casuou {Dano_Total} de dano!")
#
# Zumbi_Infectado
# print(f"O {self.nome} lançou um Ataque de Mordida Infecciosa! Causando {Dano_Total} de dano!")
# print(f" O {self.nome} ataca com uma Garras Necróticas! Causou {Dano_Total} de dano!")
#
# Zumbi_Radioativo
# print(f"O {self.nome} lançou um Ataque Mordida Radioativa! Causando {Dano_Total} de dano!")
# print(f" O {self.nome} ataca com uma Chute! Casuou {Dano_Total} de dano!")