# instancias/municoes.py
from classes.itens.municao import Municao

# Bronze dano comum para todos os zumbis
municao_bronze = Municao("Bronze", 5,5,5)

# Ferro (Melhor contra Infectado | Pior contra Ácido)
municao_ferro = Municao("Ferro", 8,11,10)

# Cobre (Melhor contra Elétrico | Pior contra Infectado)
municao_cobre = Municao("Cobre", 8,11, 10)

# Titânio (Melhor contra Ácido | Pior contra Radioativo)
municao_titanio = Municao("Titânio", 8,11, 10)

# Chumbo (Melhor contra Radioativo | Pior contra Elétrico)
municao_chumbo = Municao("Chumbo", 8,11, 10)

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