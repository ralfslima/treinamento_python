# Set/Sets estrutura de agrupamento, onde
# não é possível ALTERAR os dados.
# Porém é possível cadastrar e remover registros.

# Criar Set
cores = {'vermelho', 'azul', 'verde', 'rosa'}

# Adicionar uma nova cor
cores.add('amarelo')

# Remover uma cor
cores.remove('azul')

# Listar cores
for c in cores:
    print(c)