import sqlite3


dbfile  = 'data.db'

conn = sqlite3.connect(dbfile)

cursor = conn.cursor()

querry = """
SELECT *FROM albums 
WHERE Title LIKE '%Live%' AND LENGTH(TItle)> 10
"""""

cursor.execute(querry)

row = cursor.fetchall()
print(row)
print(type(row))

for r1 in row:
   for a,b,c in row:
       m,n,o = a,b,c
       print(m,n,o)

conn.close()