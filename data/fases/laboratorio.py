# data/fases/laboratorio.py

from data.zumbis.acidos import cobaia, analista, cientista

zumbi_1 = cobaia.cobaia_acida
zumbi_2 = analista.analista_acido
boss = cientista.cientista_acido

fase_laboratorio = {
    "numero": 3,
    "nome": "Laboratório",
    "descricao": "",
    "inimigos": [
        zumbi_1,
        zumbi_2,
        boss
    ]
}