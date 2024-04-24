# 5ª Informe três notas e retorne a média e a situação.
# Após informada a média e a situação, pergunte se deseja continuar.
# Caso positivo pergunte três notas e retorne a média e a 
# situação, caso contrário, retorne a quantidade de 
# alunos: aprovados, em exame e reprovado.

# Contadores de situação
aprovados = 0
exame = 0
reprovados = 0

# Variável lógica de loop
continuar = True

# Laço
while continuar:

    # Pedir as três notas
    print('Informe a primeira nota')
    nota1 = float(input())

    print('Informe a segunda nota')
    nota2 = float(input())
    
    print('Informe a terceira nota')
    nota3 = float(input())

    # Realizar a média
    media = (nota1+nota2+nota3)/3

    # Verificar situação
    if media >= 7:
        situacao = 'aprovado(a)'
        aprovados+=1
    elif media >= 5:
        situacao = 'em exame'
        exame+=1
    else:
        situacao = 'reprovado(a)'
        reprovados+=1

    # Retornar média e situação
    mensagem = 'A situação é {} com média {}.'
    print(mensagem.format(situacao, str(media)))

    # Deseja continuar?
    print('Deseja continuar? 1-SIM e 2-NÃO')
    validaContinuar = int(input())

    if validaContinuar == 2:
        continuar = False

# Exibir a quantidade de alunos por situação
print('Aprovados(as): ' + str(aprovados))
print('Em exame: ' + str(exame))
print('Reprovado(as): ' + str(reprovados))