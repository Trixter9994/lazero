#coding:utf-8
import sqlite3
import json

def createMain():
    conn=sqlite3.connect('Monitor.db',timeout=45)
    c=conn.cursor()
    sql="""CREATE TABLE IF NOT EXISTS projects (
	id integer PRIMARY KEY,
	name text NOT NULL,
	metadata json,
        checked integer NOT NULL
);"""

    # print(sql)
    # will it be too damn slow?
    c.execute(sql)
    conn.commit()
    #this thing must be done after every execute.
    conn.close()


def initial(_table,passme):
    conn=sqlite3.connect('Monitor.db',timeout=45)
    c=conn.cursor()
    _id=0
    for _pass in passme:
        sql="INSERT INTO "+_table+" (id,name,checked) VALUES("+str(_id)+",'"+_pass+"',0);"
    # print(sql)
        _id+=1
    # will it be too damn slow?
        c.execute(sql)
    conn.commit()
    #this thing must be done after every execute.
    conn.close()


def inf(_table,_id,_pass):
    _id = str(_id) if type(_id)!=str else _id
    conn=sqlite3.connect('Monitor.db',timeout=45)
    c=conn.cursor()
    for idx in _id:
      sql="INSERT INTO "+_table+" (id,pass) VALUES("+idx+","+_pass+");"
      # print(sql)
      # will it be too damn slow?
      try:
        c.execute(sql)
      except:
        print("duplicate",idx)
    conn.commit()
    #this thing must be done after every execute.
    conn.close()


def show(_table):
    conn=sqlite3.connect('Monitor.db',timeout=45)
    c=conn.cursor()
    sql="SELECT * FROM "+_table+";"
    f=[]
    for row in c.execute(sql):
      f.append(row)
    # conn.commit()
    #this thing must be done after every execute.
    conn.close()
    return f
    # tuple.


def up(_id,_pass):
    _id = int(_id) if type(_id)==str else _id
    conn=sqlite3.connect('Monitor.db',timeout=45)
    c=conn.cursor()
    try:
#    unix="UPDATE "+_table+" SET metadata = {}".format(json.dumps(_pass))+" WHERE id = "+_id+";"
    #    print(unix)
        c.execute("UPDATE projects SET metadata = ?  WHERE id = ?;",(json.dumps(_pass),_id))
        unix="UPDATE projects SET checked = 1 WHERE id = "+str(_id)+";"
#    print(unix)
        c.execute(unix)
        print("json imported",_id)
    except:
        print("failed to import",_id)
    conn.commit()
    conn.close()


def showX(_table,_id):
    _id = str(_id) if type(_id)!=str else _id
    conn=sqlite3.connect('Monitor.db',timeout=45)
    c=conn.cursor()
    sql="SELECT id,name FROM "+_table+" WHERE checked ="+_id+";"
    f=[]
    for row in c.execute(sql):
      f.append(row)
    # conn.commit()
    #this thing must be done after every execute.
    conn.close()
    return f
    # tuple.


def showId(_table,_id):
    _id = str(_id) if type(_id)!=str else _id
    conn=sqlite3.connect('Monitor.db',timeout=45)
    c=conn.cursor()
    sql="SELECT * FROM "+_table+" WHERE id ="+_id+";"
    f=[]
    for row in c.execute(sql):
      f.append(row)
    # conn.commit()
    #this thing must be done after every execute.
    conn.close()
    if len(f)==1:
        return f[0]
    else:
        return None

def showN(_table,_id):
    # _id = str(_id) if type(_id)!=str else _id
    conn=sqlite3.connect('Monitor.db',timeout=45)
    c=conn.cursor()
    sql="SELECT * FROM "+_table+" WHERE name ='"+_id+"';"
    f=[]
    for row in c.execute(sql):
      f.append(row)
    # conn.commit()
    #this thing must be done after every execute.
    conn.close()
    if len(f)==1:
        return f[0]
    else:
        return None
    # tuple.
    # manage your way in. all possible way to get in.

def showE(_table,_id):
    _id = str(_id) if type(_id)!=str else _id
    conn=sqlite3.connect('Monitor.db',timeout=45)
    c=conn.cursor()
    sql="SELECT name,metadata FROM "+_table+" WHERE checked ="+_id+";"
    f=[]
    for row in c.execute(sql):
      f.append(row)
    # conn.commit()
    #this thing must be done after every execute.
    conn.close()
    return f
    # tuple.
