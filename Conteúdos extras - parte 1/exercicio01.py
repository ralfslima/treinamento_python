#1ª Pedir um nome e concatenar em uma frase.

# Obter o nome
print('Informe seu nome')
nome = input()

# Concatenar boa noite com a variável nome #1
#print('Boa noite ' + nome)

# Concatenar boa noite com a variável nome #2
texto = 'Boa noite {}'
print(texto.format(nome))