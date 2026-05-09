from data.inimigos.infectados.paciente import paciente_infectado
from data.inimigos.infectados.enfermeira import enfermeira_infectada
from data.inimigos.infectados.doutor import doutor_infectado

fases = {
    {
        "nome": "Hospital",
        "inimigos": [paciente_infectado, enfermeira_infectada, doutor_infectado],
        "descricao": "",
    },
    {
        "nome": "Estação de Energia",
        "inimigos": ["zumbi_eletrico", "tecnico_energizado", "gerador_vivo"],
        "descricao": "",
    },
    {
        "nome": "Laboratório",
        "inimigos": ["zumbi_acido", "cobaia_derretida", "experimento_corrosivo"],
        "descricao": "",
    },
    {
        "nome": "Usina Nuclear",
        "inimigos": ["zumbi_radioativo", "operario_do_reator", "nucleo_infectado"],
        "descricao": "",
    }
}