# Contar caracteres
frase = 'Aprendendo Python na Yto Nihon'

# Exibir a quantidade de letras
print(frase.count(''))

# Variável para contar vogais
vogais = 0

# Laço de repetição
for f in frase.lower():
    if f == 'a' or f == 'e' or f == 'i' or f == 'o' or f == 'u':
        vogais+=1

# Exibir a quantidade de vogais
txt = 'A quantidade de vogais é {}'
print(txt.format(vogais))