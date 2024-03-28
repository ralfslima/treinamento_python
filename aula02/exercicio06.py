# 6ª Utilizando como base o mês de março de 2024, 
# peça uma data entre 1 a 31, retorne o dia da semana, exemplos:

# a) 1: Deverá retornar segunda-feira

# b) 12: Deverá retornar sexta-feira

# c) 32: Deverá retornar que o número informado não existe

# Obter o dia
print('Informe um dia do mês de março')
dia = int(input())

# Resto da divisão
resto = (dia-1) % 7

# Estrutura de escolha
match resto:
    case 0:
        print('Sexta-feira')
    case 1:
        print('Sábado')
    case 2:
        print('Domingo')
    case 3:
        print('Segunda-feira')
    case 4:
        print('Terça-feira')
    case 5:
        print('Quarta-feira')
    case 6:
        print('Quinta-feira')
    case _:
        print('Dia inválido')

# Condicionais
#if dia == 1 or dia == 8 or dia == 15 or dia == 22 or dia == 29:
#    print('Sexta-feira')
#elif dia == 2 or dia == 9 or dia == 16 or dia == 23 or dia == 30:
#    print('Sábado')
#elif dia == 3 or dia == 10 or dia == 17 or dia == 24 or dia == 31:
#    print('Domingo')
#elif dia == 4 or dia == 11 or dia == 18 or dia == 25:
#    print('Segunda-feira')
#elif dia == 5 or dia == 12 or dia == 19 or dia == 26:
#    print('Terça-fera')
#elif dia == 6 or dia == 13 or dia == 20 or dia == 27:
#    print('Quarta-fera')
#elif dia == 7 or dia == 14 or dia == 21 or dia == 28:
#    print('Quinta-fera')
#else:
#    print('Dia inválido')