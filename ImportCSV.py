import csv, sqlite3

adress = '/home/vinicius/Pokemons.db'
con = sqlite3.connect(adress)
cur = con.cursor()
cur.execute("CREATE TABLE Pok1 (Number, Name, Type, HP);")

with open('/home/vinicius/Documentos/Pokemon1.csv','rt') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Number'], i['Name'], i['Type'], i['HP']) for i in dr]

cur.executemany("INSERT INTO Pok1 (Number, Name, Type, HP) VALUES (?, ?, ?, ?);", to_db)
con.commit()
con.close()
