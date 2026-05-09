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
                Zumbi("Médica Infectada", 12, 12, 12, "imagem"),
                Zumbi("Paciente Zumbi", 14, 14, 14, "imagem"),
            ],
        },
        {
            "numero": 2,
            "nome": "Rua Destruída",
            "descricao": "Carros queimados bloqueiam o caminho enquanto zumbis cercam a avenida.",
            "inimigos": [
                Zumbi("Zumbi Corredor", 16, 16, 16, "imagem"),
                Zumbi("Zumbi Policial", 18, 18, 18, "imagem"),
                Boss("Brutamontes da Rua", 26, 26, 24, "imagem"),
            ],
        },
        {
            "numero": 3,
            "nome": "Laboratório Secreto",
            "descricao": "Tanques quebrados e experimentos falhos revelam a origem da infecção.",
            "inimigos": [
                Zumbi("Cientista Infectado", 20, 20, 20, "imagem"),
                Zumbi("Segurança Mutante", 22, 22, 22, "imagem"),
                Boss("Experimento Alfa", 34, 34, 30, "imagem"),
            ],
        },
        {
            "numero": 4,
            "nome": "Centro de Controle",
            "descricao": "O último sistema ainda funciona, mas o maior perigo está protegendo a saída.",
            "inimigos": [
                Zumbi("Operador Infectado", 24, 24, 24, "imagem"),
                Zumbi("Soldado Zumbi", 26, 26, 26, "imagem"),
                Boss("NecroBoss", 45, 45, 38, "imagem"),
            ],
        },
    ]
