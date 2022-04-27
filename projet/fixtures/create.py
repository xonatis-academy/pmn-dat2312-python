import sqlite3

con = sqlite3.connect('inventory.db')

cur = con.cursor()
cur.execute('CREATE TABLE person (firstname text, lastname text)')
cur.execute("INSERT INTO person VALUES ('Vincent', 'Time')")
cur.execute("INSERT INTO person VALUES ('Annie', 'Versaire')")
cur.execute("INSERT INTO person VALUES ('Jean', 'Aimarre')")
con.commit()

cur.execute('CREATE TABLE company (name text)')
cur.execute("INSERT INTO company VALUES ('Google')")
cur.execute("INSERT INTO company VALUES ('Microsoft')")
cur.execute("INSERT INTO company VALUES ('Apple')")
con.commit()

con.close()