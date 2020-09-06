import sqlite3
conn=sqlite3.connect("shitItUp.db")
# initial shits

def executeCode(sql):
    values=[]
    with conn:
        cur=conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for element in rows:
            values.append(element)
    return values

def closeConnection():
    conn.commit()
    conn.close()
