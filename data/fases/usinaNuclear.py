# data/fases/usinaNuclear.py

from data.zumbis.radioativos import operario, administrador, seguranca

zumbi_1 = operario.operario_radioativo
zumbi_2 = administrador.administrador_radioativo
boss = seguranca.operario_radioativo

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