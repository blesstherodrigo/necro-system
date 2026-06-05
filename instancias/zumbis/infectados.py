# instancias/zumbis/infectados.py
from classes.personagens.inimigos.zumbi import Zumbi

zumbi_infectado_1 = Zumbi(
    "Paciente Infectado",
    10, 10, 5,
    "zumbi_infectado_1.txt",
    "Ataque Infectado 1",
    "Ferro", "Cobre"
)

zumbi_infectado_2 = Zumbi(
    "Enfermeira Infectada",
    10, 10, 5,
    "zumbi_infectado_2.txt",
    "Ataque Infectado 2",
    "Ferro", "Cobre"
)

infectados = [zumbi_infectado_1, zumbi_infectado_2]