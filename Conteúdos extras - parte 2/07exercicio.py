# 7ª Peça um número e retorne a tabuada.

# Obter um número
print('Informe um número')
numero = int(input())

# Laço FOR
for indice in range(11):
    mensagem = '{} X {} = {}'
    print(mensagem.format(str(numero), str(indice), str(numero*indice)))