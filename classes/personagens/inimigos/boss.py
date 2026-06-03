# classes/personagens/inimigos/boss.py
import random
from classes.personagens.inimigos.inimigo import Inimigo
from textos.tela import enter_continuar

class Boss(Inimigo):
    def __init__(self, nome, vida, vida_max, dano, imagem, fraqueza=None, imune=None):
        super().__init__(nome, vida, vida_max, dano, imagem, fraqueza, imune)
        self.buff_ativo = False
        self.buff_multiplicador = 1.5
        self.acao_anterior = "atacar"
        self.defendendo = False
        self.transicoes = {
            "atacar": {
                "atacar": 0.35,
                "defender": 0.25,
                "curar": 0.15,
                "concentrar": 0.25
            },
            "defender": {
                "atacar": 0.45,
                "defender": 0.10,
                "curar": 0.20,
                "concentrar": 0.25
            },
            "curar": {
                "atacar": 0.50,
                "defender": 0.20,
                "curar": 0.05,
                "concentrar": 0.25
            },
            "concentrar": {
                "atacar": 0.85,
                "defender": 0.05,
                "curar": 0.10,
                "concentrar": 0
            }
        }

    def escolher_acao(self):
        vida_percentual = self.vida / self.vida_max

        if self.buff_ativo:
            probabilidades = {
                "atacar": 0.85,
                "defender": 0.05,
                "curar": 0.10,
                "concentrar": 0
            }

            if vida_percentual <= 0.2:
                probabilidades["curar"] += 0.25
                probabilidades["atacar"] -= 0.25

        else:
            probabilidades = self.transicoes[self.acao_anterior].copy()

            # Se estiver com pouca vida, aumenta chance de curar
            if vida_percentual <= 0.3:
                probabilidades["curar"] += 0.45
                probabilidades["atacar"] -= 0.20
                probabilidades["defender"] -= 0.15
                probabilidades["concentrar"] -= 0.10

            # Se estiver com vida cheia/quase cheia, evita curar e fica mais agressivo
            elif vida_percentual >= 0.75:
                probabilidades["atacar"] += 0.15
                probabilidades["concentrar"] += 0.15
                probabilidades["curar"] -= 0.20
                probabilidades["defender"] -= 0.10

            # Se já está com vida cheia, não faz sentido curar
            if self.vida >= self.vida_max:
                probabilidades["curar"] = 0
                probabilidades["atacar"] += 0.10
                probabilidades["concentrar"] += 0.10

        for acao in probabilidades:
            probabilidades[acao] = max(0, probabilidades[acao])

        # Normaliza para a soma voltar a ser 1
        total = sum(probabilidades.values())

        for acao in probabilidades:
            probabilidades[acao] /= total

        acoes = list(probabilidades.keys())
        pesos = list(probabilidades.values())

        acao_escolhida = random.choices(acoes, weights=pesos, k=1)[0]

        self.acao_anterior = acao_escolhida

        return acao_escolhida

    def realizar_ataque(self):
        acao = self.escolher_acao()

        if acao == "atacar":
            self.defendendo = False

            multiplicador = random.choice([1.5, 2.0, 2.5])
            dano_total = self.dano * multiplicador

            if self.buff_ativo:
                dano_total *= self.buff_multiplicador
                self.buff_ativo = False
                print(f"\n{self.nome} usa sua concentração para desferir um ataque poderoso!") # mudar texto

            print(f"\n{self.nome} atacou, causando {dano_total} de dano!")
            enter_continuar()
            return dano_total

        elif acao == "defender":
            self.defendendo = True

            print(f"\n{self.nome} se defendeu!")
            enter_continuar()
            return 0

        elif acao == "curar":
            self.defendendo = False

            quantidade_cura = int(self.vida_max * 0.25)
            self.curar(quantidade_cura)

            print(f"\n{self.nome} se curou em {quantidade_cura} de vida!")
            enter_continuar()
            return 0

        elif acao == "concentrar":
            self.defendendo = False

            self.buff_ativo = True
            self.buff_multiplicador = 1.5

            print(f"\n{self.nome} fecha os olhos e se concentra.") # mudar texto
            print(f"{self.nome} causará mais dano na próxima rodada!") # mudar texto
            enter_continuar()
            return 0

    def curar(self, quantidade):
        self.vida += quantidade

        if self.vida > self.vida_max:
            self.vida = self.vida_max

    def receber_dano(self, dano):
        if self.defendendo:
            dano = dano * 0.5
            self.defendendo = False

        return super().receber_dano(dano)

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