import sqlite3

db = sqlite3.connect('dict.db')
cursor = db.cursor()

limit = " where serial<50"
cursor.execute("select * from english")
edata = cursor.fetchall()

cursor.execute("select * from bengali")
bdata = cursor.fetchall()

cursor.execute("drop table if exists db")
cursor.execute("create table db(en TEXT, bn TEXT)")

l = min(len(edata), len(bdata))
print(l, len(bdata))
for a in range(l):
    #print(edata[a][1], bdata[a][0])
    cursor.execute("insert into db values(?,?)",(edata[a][1], bdata[a][1]))

db.commit()