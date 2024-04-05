# Dictionary/Dictionaries
# Objeto, é uma variável que possui atributos/características

# Criar objeto
pessoa = {
    'nome':'Ana',
    'idade':20,
    'cpf':78998767812,
    'cidade':'Rio de Janeiro'
}

# Exibir o objeto pessoa
print(pessoa)

# Exibir o nome da pessoa
txt = 'O nome da pessoa é {}.'
print(txt.format(pessoa['nome']))
