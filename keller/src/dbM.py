# coding:utf-8
import sqlite3
import json
import traceback
import jieba

def createMain():
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS projects (
	id integer NOT NULL,
    page integer NOT NULL,
	name text NOT NULL,
	metadata json
);"""
# never mind.
# it is timestamp!
    # print(sql)
    # will it be too damn slow?
    c.execute(sql)
    conn.commit()
    # this thing must be done after every execute.
    conn.close()


def initial(_table):
    # conn = sqlite3.connect('Monitor.db', timeout=45)
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    sql = "SELECT name FROM "+_table+";"
    f = []
    for row in c.execute(sql):
        f.append(row)
    # this thing must be done after every execute.
    return f
    conn.close()


def inf(_table, _id, _pass):
    _id = str(_id) if type(_id) != str else _id
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    for idx in _id:
        sql = "INSERT INTO "+_table+" (id,pass) VALUES("+idx+","+_pass+");"
        # print(sql)
        # will it be too damn slow?
        try:
            c.execute(sql)
        except:
            print("duplicate", idx)
    conn.commit()
    # this thing must be done after every execute.
    conn.close()


def show(_table):
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    sql = "SELECT * FROM "+_table+";"
    f = []
    for row in c.execute(sql):
        f.append(row)
    # conn.commit()
    # this thing must be done after every execute.
    conn.close()
    return f
    # tuple.


def up(_id, _p, _name, _pass):
    _id = int(_id) if type(_id) == str else _id
    _p = int(_p) if type(_p) == str else _p
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    try:
        # dict to string.
        #    unix="UPDATE "+_table+" SET metadata = {}".format(json.dumps(_pass))+" WHERE id = "+_id+";"
        #    print(unix)
        c.execute("INSERT INTO projects (id,name,page,metadata) VALUES (?,?,?,?)",
                  (_id, _name, _p, json.dumps(_pass)))
        # unix="UPDATE projects SET checked = 1 WHERE id = "+str(_id)+";"
#    print(unix)
        # c.execute(unix)
        print("json imported", _id)
    except:
        e = traceback.format_exc()
        print(e)
        print("failed to import", _id)
    conn.commit()
    conn.close()


def showX(_table, _id):
    _id = str(_id) if type(_id) != str else _id
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    sql = "SELECT id,name FROM "+_table+" WHERE checked ="+_id+";"
    f = []
    for row in c.execute(sql):
        f.append(row)
    # conn.commit()
    # this thing must be done after every execute.
    conn.close()
    return f
    # tuple.


def showId(_table, _id):
    _id = str(_id) if type(_id) != str else _id
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    sql = "SELECT * FROM "+_table+" WHERE id ="+_id+";"
    f = []
    for row in c.execute(sql):
        f.append(row)
    # conn.commit()
    # this thing must be done after every execute.
    conn.close()
    if len(f) == 1:
        return f[0]
    else:
        return None
    # tuple.
    # manage your way in. all possible way to get in.
