import random
from classes.personagens.inimigos.boss import Boss

class Boss_Acido(Boss):
    def realizar_ataque(self):
        movimento = random.randint(1,2)

        if movimento == 1:

            Dano_Total = self.dano * 1.5        
            
            print(f"\O {self.nome} lançou O Ataque Chuva de Toxina! Ele ataca em área, causando {Dano_Total} de dano!")
            return Dano_Total
                
        elif movimento == 2:

            Dano_Total = self.dano * 1.5        
            
            print(f"\O {self.nome} lançou O Ataque de Cuspe Corrosivo! Ele ataca com sua toxina do corpo, causando {Dano_Total} de dano!")
            return Dano_Total
        
        
        '''elif movimento == 3:        ---->Implementar mecânica de cura

            Dano_Total = self.dano * 2.0 
            
            print(f" O {self.nome} utiliza o Caldeirão Ambulante! Ele utiliza os fluídos ácido ao redor e se cura! Causou {Dano_Total} de dano!")
            return Dano_Total'''