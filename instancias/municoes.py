# instancias/municoes.py
from classes.itens.municao import Municao

# Bronze dano comum para todos os zumbis
municao_bronze = Municao("Bronze", 15,15,5, "Nenhuma")

# Ferro (Melhor contra Infectado | Pior contra Ácido)
municao_ferro = Municao("Ferro", 20,35,10, "Infecção")

# Cobre (Melhor contra Elétrico | Pior contra Infectado)
municao_cobre = Municao("Cobre", 20,35, 10, "Eletricidade")

# Titânio (Melhor contra Ácido | Pior contra Radioativo)
municao_titanio = Municao("Titânio", 20,35, 10, "Acidez")

# Chumbo (Melhor contra Radioativo | Pior contra Elétrico)
municao_chumbo = Municao("Chumbo", 20,35, 10, "Radioatividade")

municoes = [
    municao_bronze,
    municao_ferro,
    municao_cobre,
    municao_titanio,
    municao_chumbo
]

# | Categoria    | Melhor metal | Pior metal |
# | -------------| ------------ | -----------|
# | Infecção     | Ferro        | Cobre      |
# | Eletricidade | Cobre        | Chumbo     |
# | Ácido        | Titânio      | Ferro      |
# | Radiação     | Chumbo       | Titânio    |