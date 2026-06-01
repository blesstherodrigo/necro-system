import random
from classes.personagens.inimigos.boss import Boss

class Boss_Eletrico(Boss):
    def realizar_ataque(self):
        
        movimento = random.randint(1,3)

        if movimento == 1:

            Dano_Total = self.dano * 1.5        
        
            print(f"\O {self.nome} lançou o Ataque de Curto-Circuito! Ele ataca com correntes elétricas, causando {Dano_Total} de dano!")
            return Dano_Total

        elif movimento == 2:

            Dano_Total = self.dano * 2.0 
        
            print(f"\ O {self.nome} fez o ataque da Tempestade de Íons! Canalizando a eletrecidade do poste e lança em você! Causou {Dano_Total} de dano!")
            return Dano_Total
        
        elif movimento == 3:

            Dano_Total = self.dano * 1.5        
        
            print(f"\O {self.nome} lançou o Ataque de Choque Estático! Ele ataca jogando água em você em seguida te eletrifica pelo chão, causando {Dano_Total} de dano!")
            return Dano_Total