# data/zumbiss.py

from classes.personagens.zumbi import Zumbi
from classes.personagens.boss import Boss

def criar_fases():
    return [
        {
            "numero": 1,
            "nome": "Hospital Abandonado",
            "descricao": "Corredores escuros, macas quebradas e gritos ao longe.",
            "inimigos": [
                Zumbi("Médica Infectada", 120, 120, 12, "imagem"),
                Zumbi("Paciente Zumbi", 140, 140, 14, "imagem"),
            ],
        },
        {
            "numero": 2,
            "nome": "Rua Destruída",
            "descricao": "Carros queimados bloqueiam o caminho enquanto zumbis cercam a avenida.",
            "inimigos": [
                Zumbi("Zumbi Corredor", 160, 160, 16, "imagem"),
                Zumbi("Zumbi Policial", 180, 180, 18, "imagem"),
                Boss("Brutamontes da Rua", 260, 260, 24, "imagem"),
            ],
        },
        {
            "numero": 3,
            "nome": "Laboratório Secreto",
            "descricao": "Tanques quebrados e experimentos falhos revelam a origem da infecção.",
            "inimigos": [
                Zumbi("Cientista Infectado", 200, 200, 20, "imagem"),
                Zumbi("Segurança Mutante", 220, 220, 22, "imagem"),
                Boss("Experimento Alfa", 340, 340, 30, "imagem"),
            ],
        },
        {
            "numero": 4,
            "nome": "Centro de Controle",
            "descricao": "O último sistema ainda funciona, mas o maior perigo está protegendo a saída.",
            "inimigos": [
                Zumbi("Operador Infectado", 240, 240, 24, "imagem"),
                Zumbi("Soldado Zumbi", 260, 260, 26, "imagem"),
                Boss("NecroBoss", 450, 450, 38, "imagem"),
            ],
        },
    ]
