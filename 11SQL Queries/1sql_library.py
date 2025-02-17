import sqlite3

dbfile = 'data.db'

# 1 create a connection
conn = sqlite3.connect(dbfile)

# 2 create a cursor
cursor = conn.cursor()

# 3 build an querry
querry = """
SELECT *FROM albums 
WHERE Title LIKE '%Live%' AND LENGTH(TItle)> 10
"""""

# 4 execute the querry
cursor.execute(querry)


row = cursor.fetchall()


for r in row:
    print(r[0],r[1])


conn.close()
