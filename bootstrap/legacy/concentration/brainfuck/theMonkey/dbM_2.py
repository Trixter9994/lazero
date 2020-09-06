# coding: utf-8
import sqlite3
import time
# import random
import traceback
import random
import json


def dum():
    r = random.random()*0.1
    time.sleep(r)
# how about start another process?

# import jieba
# wtf?
# these people always concern about safety, which leads to nothing.
# think about that brainfuck thing!
# what about concurrent things? database might be locked?


def createMain():
    conn = sqlite3.connect('Monitor.db', timeout=45)
    conn.text_factory = str
    c = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS projects ( \
    ts float NOT NULL, \
    op_code text NOT NULL, \
    op_output json NOT NULL \
);"
    c.execute(sql)
    conn.commit()
    # this thing must be done after every execute.
    conn.close()

# fucking shit.


def initial(_table, _t):
    #  is it good for me to get connection with python3?
    # conn = sqlite3.connect('Monitor.db', timeout=45)
    conn = sqlite3.connect('Monitor.db', timeout=45)
    conn.text_factory = str
    c = conn.cursor()
    # sql = "SELECT name FROM "+_table+";"
    # at most two.
    # still not fast enough.
    def sql(t, x, y, z): return c.execute("INSERT INTO " + t +
                                          " (ts,op_code,op_output) VALUES(?,?,?);", (x, y, json.dumps(z)))
    # f = []
    # hell is the formatter.
    # for row in c.execute(sql):
    #     f.append(row)
    for x, y, z in _t:
        # print(x, y, z)
        # z=str(z)
        if x is not None and y is not None and z is not None:
            # patience = 3
            patience = 5
            while patience > 0:
                try:
                    sql(_table, x, y, z)
                    conn.commit()
                    print("INSERTED!", y, z)
                    break
                except:
                    e = traceback.format_exc()
                    print(e)
                    # mainly because database is locked. but might have other reasons.
                    print("FAILED! CHANCE: {}".format(patience), y, z)
                    patience -= 1
                    dum()
            if patience == 0:
                print("SERIOUS PROBLEM ENCOUNTERED", y, z)
        else:
            print("GOT EMPTY FOR", y, z)
        # codec problem.
        # # this thing must be done after every execute.
        # # while True:
        # try:
        #     sql(_table, x, y, z)
        #     # break
        # except:
        #     # just do this??
        #     e= traceback.format_exc()
        #     print(e)
        #     # raise Exception("NOT AGAIN!")
        #         # break
    # return f
    conn.commit()
    conn.close()
