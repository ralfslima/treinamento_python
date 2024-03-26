# Obter a média
print('Informe sua média')
media = float(input())

# Condicional
if media > 10:
    print('Média inválida, a média não pode ser superior a 10')
elif media >= 7:
    print('Aprovado(a)')
elif media >= 5:
    print('Em exame')
elif media >= 0:
    print('Reprovado(a)')
else:
    print('Média inválida, a média não pode ser inferior a 0')