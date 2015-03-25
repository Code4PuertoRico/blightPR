import csv

with open('inventario.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print row[2]
