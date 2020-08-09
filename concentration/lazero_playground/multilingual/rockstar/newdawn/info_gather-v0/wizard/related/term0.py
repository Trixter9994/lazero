import sqlite3
# initial shits

def executeCode(sql):
    conn=sqlite3.connect("fuckyou.db")
    conn.execute(sql)
    conn.commit()
    conn.close()
'''
def closeConnection():
	conn.close()'''
