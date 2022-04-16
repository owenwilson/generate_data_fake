import csv
import random

#headers
fieldnames = ['Años de Experiencia', 'Salario']

#data csv random
data = []

def aniosExperiencia(inicio, fin):
    return random.randrange(inicio,fin)/10

def salarioAleatorio(montoInicial, limite):
    return random.randrange(montoInicial, limite)/100

with open('output_salarios.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    #Generate random data
    for x in range(1,10):
        data.append({'Años de Experiencia': aniosExperiencia(10,120),'Salario': salarioAleatorio(10000,120000)})
        print(data)
    
    writer.writerows(data)

