# Peça três notas, em seguida realize a média
# Exiba a média e a situação, em seguida
# contabilize a situação do aluno
# por fim, pergunte se deseja continuar
# caso não queira continuar, exiba a quantidade
# de alunos aprovados, em exame e reprovados

# Aprovados 7 >
# Em exame >= 5 e < 7
# Reprovado < 5

# Contadores
aprovado = 0
exame = 0
reprovado = 0

# Continuar laço
continuar = 0

# Laço de repetição
while continuar != 2:

    # Obter notas
    print('Informe a primeira nota')
    nota1 = float(input())
    
    print('Informe a segunda nota')
    nota2 = float(input())

    print('Informe a terceira nota')
    nota3 = float(input())

    # Realizar a média
    media = (nota1+nota2+nota3)/3

    # Condicional
    if media > 7:
        aprovado += 1
        print('Aprovado com média ' + str(media))
    elif media >= 5:
        exame += 1
        print('Em exame com média: ' + str(media))
    else:
        reprovado += 1
        print('Reprovado com média ' + str(media))

    # Verifica se quer continuar no laço de repetição
    print('Deseja cadastrar mais um aluno?')
    print('1 - SIM')
    print('2 - NÃO')
    continuar = int(input())

# Exibir contadores
print('Aprovados: ' + str(aprovado))
print('Exame: ' + str(exame))
print('Reprovados: ' + str(reprovado))