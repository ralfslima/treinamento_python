# Criar uma lista contendo 5 nomes e exibir utilizando um laço de repetição.

# Lista
nomes = ['Ralf', 'Luisa', 'Ana', 'Jaison', 'Isabela']

# Exibir os nomes
#for n in nomes:
#    print(n)

indice = 0
while indice < 5:
    print(str(indice+1)+' '+nomes[indice])
    indice+=1