import sqlite3
conn=sqlite3.connect("fuckyou.db")
# initial shits

def executeCode(sql):
	conn.execute(sql)
	conn.commit()

def closeConnection():
	conn.close()
