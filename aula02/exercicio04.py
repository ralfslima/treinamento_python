# 4ª Crie um sistema para conversão de horas. 
# Informe a hora atual e a cidade que deseja saber o horário, exemplos:

#a) 14 - Tóquio, deverá retornar 2, pois Tóquio são +12 horas

#b) 17 - Lisboa, deverá retornar 20, pois Lisboa são +3 horas

#c) 19 - Cidade do México, deverá retornar 16, pois Cidade do México são -3 horas

# Obter a hora de Brasília
print('Informe a hora de Brasília')
horaBrasilia = int(input())

# Obter a cidade
print('Informe a cidade que deseja saber o horário')
print('1 - Tóquio')
print('2 - Lisboa')
print('3 - Cidade do México')
cidade = int(input())

# Estrutura de escolha (Versão 3.10 ou superior do Python)
novaHora = -1
match cidade:
    case 1:
        novaHora = horaBrasilia + 12
    case 2:
        novaHora = horaBrasilia + 3
    case 3:
        novaHora = horaBrasilia - 3
    case _:
        print('Opção inválida')


#if cidade == 1:
#    novaHora = horaBrasilia + 12
#elif cidade == 2:
#    novaHora = horaBrasilia + 3
#elif cidade == 3:
#    novaHora = horaBrasilia - 3
#else:
#    print('Opção inválida')

# Retorno
if novaHora != -1:
    if novaHora > 23:
        print(str(novaHora - 24))
    else:
        print(str(novaHora))