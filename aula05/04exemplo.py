nome = 'Letícia'
idade = 22

# Concatenção 1
# print('Boa noite ' + nome + ' você tem ' + str(idade) + ' anos.')

# Concatenção 2
frase = 'Olá {} você tem {} anos.'
print(frase.format(nome, idade))