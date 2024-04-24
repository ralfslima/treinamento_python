# 10ª Peça um dia do mês de abril e retorne o dia da semana.
# Valide caso o dia não exista.

# Obter o dia
print('Informe um dia do mês de abril')
dia = int(input())

# Verificação
if dia == 7 or dia == 14 or dia == 21 or dia == 28:
    print('Domingo')
elif dia == 1 or dia == 8 or dia == 15 or dia == 22 or dia == 29:
    print('Segunda-feira')
elif dia == 2 or dia == 9 or dia == 16 or dia == 23 or dia == 30:
    print('Terça-feira')
elif dia == 3 or dia == 10 or dia == 17 or dia == 24:
    print('Quarta-feira')
elif dia == 4 or dia == 11 or dia == 18 or dia == 25:
    print('Quinta-feira')
elif dia == 5 or dia == 12 or dia == 19 or dia == 26:
    print('Sexta-feira')
elif dia == 6 or dia == 13 or dia == 20 or dia == 27:
    print('Sábado')
else:
    print('Data não encontrada!')