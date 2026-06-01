import random
from classes.personagens.inimigos.boss import Boss

class Boss_Radioativo(Boss):
    def realizar_ataque(self):
        
        movimento = random.randint(1,2)

        if movimento == 1:

            Dano_Total = self.dano * 1.5        
        
            print(f"\O {self.nome} lançou o Ataque 'Alerta Vermelho'! Joga uma bomba causando {Dano_Total} de dano!")
            return Dano_Total
        
        if movimento == 2:

            Dano_Total = self.dano * 1.5        
        
            print(f"\O {self.nome} lançou o Ataque Tiro Radioativo! Ele saca uma espingarda e atira, causando {Dano_Total} de dano!")
            return Dano_Total
        
        '''elif movimento == 3:         --------> Implementar mecânica de cura

            Dano_Total = self.dano * 2.0 
        
            print(f"\O {self.nome} usa a Recuperação química! Ele absorve a radiação do ambiente e regenera {Dano_Total} de dano!")
            return Dano_Total'''
        