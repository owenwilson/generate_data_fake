import csv
import random

#header
fieldnames = ['YearsExperience', 'Salary']

#data csv random
data = []

def yearsExperiences(initialNumber, endNumber):
    return random.randrange(initialNumber,endNumber)/10

def salaries(initialSalarie, endSalarie):
    return random.randrange(initialSalarie,endSalarie)/100

with open('output_salaries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    #Generate random data
    for x in range(1,10):
        data.append({'YearsExperience': yearsExperiences(10,120),'Salary': salaries(10000,120000)})
        print(data)
    
    writer.writerows(data)
