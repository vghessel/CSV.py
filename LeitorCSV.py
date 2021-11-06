import csv

arquivo = '/home/vinicius/Documentos/Pokemon1.csv'
arquivo_aberto = open(arquivo, 'rt')
reader = csv.reader(arquivo_aberto, delimiter=',')

for row in reader:
    print(row)













