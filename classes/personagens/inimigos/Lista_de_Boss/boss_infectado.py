import random
from classes.personagens.inimigos.boss import Boss

class Boss_Infectado(Boss):
    def realizar_ataque(self):
        
        movimento = random.randint(1,3)

        if movimento == 1:

            Dano_Total = self.dano * 1.5        
        
            print(f"\O {self.nome} lançou um Ataque Triagem Cruel: Ele utiliza uma seringa gigante e desfere o golpe, causando {Dano_Total} de dano!")
            return Dano_Total

        elif movimento == 2:

            Dano_Total = self.dano * 2.0 
        
            print(f"\O {self.nome} ataca Sinfonia do Sangue: ele consome bolsa de sangue e triplica o dano! Causou {Dano_Total} de dano!")
            return Dano_Total
        
        elif movimento == 3:
            Dano_Total = self.dano * 3.0

            print(f"\O {self.nome} ataca com Tratamento de Choque: ele pega desfribilador quebrado e junta os cabos para te atacar, causa {Dano_Total} de dano!")
            return Dano_Total