# 2ª Peça dois números inteiros, em seguida exiba os
# números informados e os valores dos seus respectivos intervalos
# Exemplo: 2 8 = 2 3 4 5 6 7 8

# Obter dois números
print('Informe um número')
numero1 = int(input())

print('Informe outro número')
numero2 = int(input())

# Condicional para verificar o menor número
if numero1 < numero2:
    # Laço de repetição
    while numero1 <= numero2:
        print(numero1)
        numero1+=1
else:
    # Laço de repetição
    while numero1 >= numero2:
        print(numero1)
        numero1-=1