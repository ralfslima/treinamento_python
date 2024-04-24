# 3ª Pedir uma média e retornar a situação, se a média for maior ou igual a 7, o aluno estará aprovado, caso contrário estará reprovado.

# Pedir a média
print('Informe a média')
media = float(input())

# Condicional
#if media >= 7:
#    print('Aprovado(a)')
#else:
#    print('Reprovado(a)')

# Operador ternário
print('Aprovado' if media >= 7 else 'Reprovado')