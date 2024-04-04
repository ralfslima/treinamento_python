# Tabela para extrair dados do datetime: https://www.w3schools.com/python/python_datetime.asp

# Importar uma biblioteca de data
import datetime

# Variável de tempo
tempo = datetime.datetime.now()

# Exibir data formatada
print(tempo.strftime('%d-%m-%Y'))