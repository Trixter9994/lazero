# coding:utf-8
import sqlite3
import json
import traceback
import jieba
# these people always concern about safety, which leads to nothing.
# think about that brainfuck thing!


def createMain():
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS projects (
    dnsprovider text NOT NULL,
	filename text NOT NULL,
    filelink text UNIQUE NOT NULL,
    iterator integer NOT NULL,
	content blob
);"""
# never mind.
# yes we will store some binary data.
# use curl?
# it is timestamp!
# do it later?
    # print(sql)
    # will it be too damn slow?
    c.execute(sql)
    conn.commit()
    # this thing must be done after every execute.
    conn.close()


def initial(_table, _t):
    # conn = sqlite3.connect('Monitor.db', timeout=45)
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    # sql = "SELECT name FROM "+_table+";"
    # at most two.
    def sql(t, x, y, z): return c.execute("INSERT INTO "+t +
                                          " (dnsprovider,filename,filelink,iterator) VALUES(?,?,?,0);", (x, y, z))
    # f = []
    # hell is the formatter.
    # for row in c.execute(sql):
    #     f.append(row)
    for x, y, z in _t:
        # print(x, y, z)
        # this thing must be done after every execute.
        sql(_table, x, y, z)
    # return f
    conn.commit()
    conn.close()


def regcheck(_table):
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    sql = "SELECT filelink FROM "+_table+" WHERE iterator == 0;"
    f = []
    for row in c.execute(sql):
        f.append(row)
    conn.close()
    return f

# batch commit? then there is no need for filesystem.


def inf(_table, _t):
    # _id = str(_id) if type(_id) != str else _id
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    def sql(x, y):
        c.execute("UPDATE "+_table +
                  " SET content = ? WHERE filelink = ?", (x, y))
        c.execute("UPDATE "+_table +
                  " SET iterator = 1 WHERE filelink = ?", (y,))
        return
        # finally!
    for x, y in _t:
        if x is not None:
            try:
                sql(x, y)
                print("INSERTED!",y)
            except:
                e= traceback.format_exc()
                print(e)
                print("FAILED!",y)
        else:
            print("GOT EMPTY FOR",y)
        #     sql = "INSERT INTO "+_table+" (id,pass) VALUES("+idx+","+_pass+");"
        #     # print(sql)
        #     # will it be too damn slow?
        # do not want some python None objects.
        #     try:
        #         c.execute(sql)
        #     except:
        #         print("duplicate", idx)
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
        # this is the right way.
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
