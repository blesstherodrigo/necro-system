import random
from classes.personagens.inimigos.zumbi import Zumbi

class Zumbi_Radioativo(Zumbi):
    def realizar_ataque(self):
        
        movimento = random.randint(1,2)

        if movimento == 1:

            Dano_Total = self.dano * 1.5        
        
            print(f"O {self.nome} lançou um Ataque Mordida Radioativa! Causando {Dano_Total} de dano!")
            return Dano_Total

        elif movimento == 2:

            Dano_Total = self.dano * 2.0 
        
            print(f" O {self.nome} ataca com uma Chute! Casuou {Dano_Total} de dano!")
            return Dano_Total