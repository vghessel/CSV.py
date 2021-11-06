import csv

with open('/home/vinicius/Documentos/Pokemon1.csv', 'wt') as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames = ["Number", "Name", "Type", "HP"])
    writer.writeheader()