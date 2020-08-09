# coding:utf-8
import sqlite3
import json
import traceback
import time
import random
import json
# just use a different database.


def dum():
    r = random.random()*0.1
    time.sleep(r)


# import jieba
# wtf?
# these people always concern about safety, which leads to nothing.
# think about that brainfuck thing!


def createMain():
    conn = sqlite3.connect('Monitor2.db', timeout=45)
    c = conn.cursor()  # zoom_level,corresponding_text.
    # you may miss the spot!
    sql = """CREATE TABLE IF NOT EXISTS projects (
    iterator integer NOT NULL,
    iterator_x integer NOT NULL,
    iterator_y integer NOT NULL,
    shift integer NOT NULL,
	content json,
    CONSTRAINT unq UNIQUE (iterator,iterator_x,iterator_y,shift)
);"""
# four kinds of shift: 0: no shift,1: right shift,2: down shift,3: right and down shift ( merge four )
# when want to create shift, first check avaliability.
# and there are rules to get the thing.
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
    # conn = sqlite3.connect('Monitor2.db', timeout=45)
    conn = sqlite3.connect('Monitor2.db', timeout=45)
    c = conn.cursor()
    # sql = "SELECT name FROM "+_table+";"
    # at most two.
    def sql(t, x, y, z, s): return c.execute("INSERT INTO " + t +
                                             " (iterator,iterator_x,iterator_y,shift) VALUES(?,?,?,?);", (x, y, z, s))
    # f = []
    # hell is the formatter.
    # for row in c.execute(sql):
    #     f.append(row)
    for x, y, z, s in _t:
        # print(x, y, z)
        # this thing must be done after every execute.
        sql(_table, x, y, z, s)
    # return f
    conn.commit()
    conn.close()


def regcheck(_table):
    conn = sqlite3.connect('Monitor2.db', timeout=45)
    c = conn.cursor()
    sql = "SELECT iterator,iterator_x,iterator_y,shift FROM " + \
        _table+" WHERE content IS NULL;"
    f = []
    for row in c.execute(sql):
        f.append(row)
    conn.close()
    return f
# batch commit? then there is no need for filesystem.


def inf(_table, _t):
    # _id = str(_id) if type(_id) != str else _id
    conn = sqlite3.connect('Monitor2.db', timeout=45)
    c = conn.cursor()

    def sql(x, y, z, a, s):
        c.execute("UPDATE "+_table +
                  " SET content = ? WHERE iterator = ? AND iterator_x = ? AND iterator_y = ? AND shift = ?", (json.dumps(x if x != None else []), y, z, a, s))
        # c.execute("UPDATE "+_table +
        #   " SET iterator = 1 WHERE filelink = ?", (y,))
        return
        # return True
        # finally!
    for x, y, z, a, s in _t:
        # y0 = random.choice(range(len(x)-5))
        # sb = x[y0:y0+5]
        if x is not None:
            # patience = 3
            patience = 5
            while patience > 0:
                try:
                    sql(x, y, z, a, s)
                    print("INSERTED!", y, z, a, s)
                    break
                except:
                    e = traceback.format_exc()
                    print(e)
                    # mainly because database is locked. but might have other reasons.
                    print("FAILED! CHANCE: {}".format(patience), y, z, a, s)
                    patience -= 1
                    dum()
            if patience == 0:
                print("SERIOUS PROBLEM ENCOUNTERED", y, z, a, s)
        else:
            print("GOT EMPTY FOR", y, z, a, s)
        #     sql = "INSERT INTO "+_table+" (id,pass) VALUES("+idx+","+_pass+");"
        #     # print(sql)
        #     # will it be too damn slow?
        # do not want some python None objects.
        #     try:
        #         c.execute(sql)
        #     except:
        #         print("duplicate", idx)
    # this thing must be done after every execute.
    conn.commit()
    conn.close()


def show(_table):
    conn = sqlite3.connect('Monitor2.db', timeout=45)
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
    conn = sqlite3.connect('Monitor2.db', timeout=45)
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
    conn = sqlite3.connect('Monitor2.db', timeout=45)
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
    conn = sqlite3.connect('Monitor2.db', timeout=45)
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
