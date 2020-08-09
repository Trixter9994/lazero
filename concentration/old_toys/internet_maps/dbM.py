# coding:utf-8
import sqlite3
import json
import traceback
import time
import random


def dum():
    r = random.random()*0.1
    time.sleep(r)


# import jieba
# wtf?
# these people always concern about safety, which leads to nothing.
# think about that brainfuck thing!


def createMain():
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS projects (
    iterator integer NOT NULL,
    iterator_x integer NOT NULL,
    iterator_y integer NOT NULL,
	content blob,
    CONSTRAINT unq UNIQUE (iterator,iterator_x,iterator_y)
);"""
# get that thing over another place.
# never mind.
# constrains?
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
                                          " (iterator,iterator_x,iterator_y) VALUES(?,?,?);", (x, y, z))
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
    sql = "SELECT iterator,iterator_x,iterator_y FROM " + \
        _table+" WHERE content IS NULL;"
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

    def sql(x, y, z, a):
        c.execute("UPDATE "+_table +
                  " SET content = ? WHERE iterator = ? AND iterator_x = ? AND iterator_y = ?", (x, y, z, a))
        # c.execute("UPDATE "+_table +
        #   " SET iterator = 1 WHERE filelink = ?", (y,))
        return
        # return True
        # finally!
    for x, y, z, a in _t:
        if x is not None:
            # patience = 3
            patience = 5
            while patience > 0:
                try:
                    sql(x, y, z, a)
                    conn.commit()
                    print("INSERTED!", y, z, a)
                    break
                except:
                    e = traceback.format_exc()
                    print(e)
                    # mainly because database is locked. but might have other reasons.
                    print("FAILED! CHANCE: {}".format(patience), y, z, a)
                    patience -= 1
                    dum()
            if patience == 0:
                print("SERIOUS PROBLEM ENCOUNTERED", y, z, a)
        else:
            print("GOT EMPTY FOR", y, z, a)
        #     sql = "INSERT INTO "+_table+" (id,pass) VALUES("+idx+","+_pass+");"
        #     # print(sql)
        #     # will it be too damn slow?
        # do not want some python None objects.
        #     try:
        #         c.execute(sql)
        #     except:
        #         print("duplicate", idx)
    # this thing must be done after every execute.
    conn.close()


def show(_table,_s):
    conn = sqlite3.connect('Monitor.db', timeout=45)
    c = conn.cursor()
    sql = "SELECT content FROM "+_table+" WHERE iterator = ? AND iterator_x = ? AND iterator_y = ? ;"
    f = []
    for s in _s:
        for row in c.execute(sql,s):
            f.append(row[0])
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
