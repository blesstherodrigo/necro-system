# data/fases/usinaNuclear.py
from data.zumbis.radioativos import operario_radioativo, administrador_radioativo, seguranca_radioativo

zumbi_1 = operario_radioativo
zumbi_2 = administrador_radioativo
boss = seguranca_radioativo

fase_usina_nuclear = {
    "numero": 4,
    "nome": "Usina Nuclear",
    "descricao": "",
    "inimigos": [
        zumbi_1,
        zumbi_2,
        boss
    ]
}