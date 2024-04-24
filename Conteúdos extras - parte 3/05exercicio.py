# 5ª Informe um cargo, valide se o cargo existe na empresa ou não.
# A validação ocorrerá através de uma tupla contendo três cargos.

# Tupla
cargos = ('Desenvolvedor', 'Analista', 'Gerente')

# Pedir um cargo
print('Informe um cargo')
cargo = input()

# Laço
existeCargo = False

for c in cargos:
    if c == cargo:
        print('O cargo existe!')
        existeCargo = True

# Caso o cargo não seja encontrado
if existeCargo == False:
    print('O cargo informado não existe!')