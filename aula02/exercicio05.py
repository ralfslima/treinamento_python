# 5ª Precisamos descobrir qual o tipo do triângulo, 
# peça três valores, sendo eles
# - Lado Direito
# - Lado Esquerdo
# - Lado Inferior

# Dependendo dos valores informados, retorne o tipo de triângulo, que pode ser:
# - Isósceles: Dois lados possuem a mesma medida e um lado diferente das demais 
# - Escaleno: Os três lados possuem medidas distintas
# - Equilatero: Os três lados possuem as mesmas medidas

# Obter dados
print('Informe o lado direito')
ladoDireito = int(input())

print('Informe o lado esquerdo')
ladoEsquerdo = int(input())

print('Informe o lado inferior')
ladoInferior = int(input())

# Condicional
if ladoDireito == ladoInferior and ladoInferior == ladoEsquerdo and ladoEsquerdo == ladoDireito:
    print('Equilatero')
elif ladoDireito != ladoInferior and ladoInferior != ladoEsquerdo and ladoEsquerdo != ladoDireito:
    print('Escaleno')
else:
    print('Isósceles')