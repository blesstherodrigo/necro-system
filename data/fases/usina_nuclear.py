# data/fases/usina_nuclear.py
from data.zumbis.radioativos import zumbi_radioativo_1, zumbi_radioativo_2, boss_radioativo

fase_usina_nuclear = {
    "numero": 4,
    "nome": "Usina Nuclear",
    "descricao": "",
    "inimigos": [
        zumbi_radioativo_1,
        zumbi_radioativo_2,
        boss_radioativo
    ]
}