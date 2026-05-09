
from data.zumbis.infectados import paciente, enfermeira, doutor

hospital_zumbi_1 = paciente.paciente_infectado
hospital_zumbi_2 = enfermeira.enfermeira_infectada
hospital_boss = doutor.doutor_infectado

fases = {
    {
        "numero": 1,
        "nome": "Hospital",
        "descricao": "",
        "inimigos": [
            "paciente",
            "enfermeira",
            "doutor"
        ]
    },
    {
        "numero": 2,
        "nome": "Estação de Energia",
        "descricao": "",
        "inimigos": [
            "zumbi_eletrico",
            "tecnico_energizado",
            "gerador_vivo"
        ]
    },
    {
        "numero": 3,
        "nome": "Laboratório",
        "descricao": "",
        "inimigos": [
            "zumbi_acido",
            "cobaia_derretida",
            "experimento_corrosivo"
        ]
    },
    {
        "numero": 4,
        "nome": "Usina Nuclear",
        "descricao": "",
        "inimigos": [
            "zumbi_radioativo",
            "operario_do_reator",
            "nucleo_infectado"
        ]
    }
}