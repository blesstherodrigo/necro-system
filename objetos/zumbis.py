# objetos/zumbis.py

from classes.personagens.zumbi import Zumbi
from classes.personagens.boss import Boss


def criar_fases():
    return [
        {
            "numero": 1,
            "nome": "Hospital Abandonado",
            "descricao": "Corredores escuros, macas quebradas e gritos ao longe.",
            "inimigos": [
                Zumbi("Médica Infectada", 120, 120, 12),
                Zumbi("Paciente Zumbi", 140, 140, 14),
            ],
        },
        {
            "numero": 2,
            "nome": "Rua Destruída",
            "descricao": "Carros queimados bloqueiam o caminho enquanto zumbis cercam a avenida.",
            "inimigos": [
                Zumbi("Zumbi Corredor", 160, 160, 16),
                Zumbi("Zumbi Policial", 180, 180, 18),
                Boss("Brutamontes da Rua", 260, 260, 24),
            ],
        },
        {
            "numero": 3,
            "nome": "Laboratório Secreto",
            "descricao": "Tanques quebrados e experimentos falhos revelam a origem da infecção.",
            "inimigos": [
                Zumbi("Cientista Infectado", 200, 200, 20),
                Zumbi("Segurança Mutante", 220, 220, 22),
                Boss("Experimento Alfa", 340, 340, 30),
            ],
        },
        {
            "numero": 4,
            "nome": "Centro de Controle",
            "descricao": "O último sistema ainda funciona, mas o maior perigo está protegendo a saída.",
            "inimigos": [
                Zumbi("Operador Infectado", 240, 240, 24),
                Zumbi("Soldado Zumbi", 260, 260, 26),
                Boss("NecroBoss", 450, 450, 38),
            ],
        },
    ]
