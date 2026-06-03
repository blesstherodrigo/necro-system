# classes/personagens/inimigos/boss.py
import random
from classes.personagens.inimigos.inimigo import Inimigo

class Boss(Inimigo):
    def __init__(self, nome, vida, vida_max, dano, imagem, fraqueza=None, imune=None):
        super().__init__(nome, vida, vida_max, dano, imagem, fraqueza, imune)

    def realizar_ataque(self):
        movimento = random.randint(1, 3)

        if movimento == 1:
            dano_total = self.dano * 1.5
            print(f"\n{self.nome} usou movimento 1, causando {dano_total} de dano!")
            return dano_total

        elif movimento == 2:
            dano_total = self.dano * 2.0
            print(f"\n{self.nome} usou movimento 2, causando {dano_total} de dano!")
            return dano_total

        elif movimento == 3:
            dano_total = self.dano * 2.5
            print(f"\n{self.nome} usou movimento 3, causando {dano_total} de dano!")
            return dano_total

# Boss_Acido
# print(f"\O {self.nome} lançou O Ataque Chuva de Toxina! Ele ataca em área, causando {Dano_Total} de dano!")
# print(f"\O {self.nome} lançou O Ataque de Cuspe Corrosivo! Ele ataca com sua toxina do corpo, causando {Dano_Total} de dano!")
# print(f" O {self.nome} utiliza o Caldeirão Ambulante! Ele utiliza os fluídos ácido ao redor e se cura! Causou {Dano_Total} de dano!")
#
# Boss_Infectado
# print(f"\O {self.nome} lançou um Ataque Triagem Cruel: Ele utiliza uma seringa gigante e desfere o golpe, causando {Dano_Total} de dano!")
# print(f"\O {self.nome} ataca Sinfonia do Sangue: ele consome bolsa de sangue e triplica o dano! Causou {Dano_Total} de dano!")
# print(f"\O {self.nome} ataca com Tratamento de Choque: ele pega desfribilador quebrado e junta os cabos para te atacar, causa {Dano_Total} de dano!")
#
# Boss_Radioativo
# print(f"\O {self.nome} lançou o Ataque 'Alerta Vermelho'! Joga uma bomba causando {Dano_Total} de dano!")
# print(f"\O {self.nome} lançou o Ataque Tiro Radioativo! Ele saca uma espingarda e atira, causando {Dano_Total} de dano!")
# print(f"\O {self.nome} usa a Recuperação química! Ele absorve a radiação do ambiente e regenera {Dano_Total} de dano!")
#
# Boss_Eletrico
# print(f"\O {self.nome} lançou o Ataque de Curto-Circuito! Ele ataca com correntes elétricas, causando {Dano_Total} de dano!")
# print(f"\ O {self.nome} fez o ataque da Tempestade de Íons! Canalizando a eletrecidade do poste e lança em você! Causou {Dano_Total} de dano!")
# print(f"\O {self.nome} lançou o Ataque de Choque Estático! Ele ataca jogando água em você em seguida te eletrifica pelo chão, causando {Dano_Total} de dano!")