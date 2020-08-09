import sqlite3
import pandas as pd

def toxic(jerk):
    return [[jerk[1][a],jerk[2][a]] for a in range(len(jerk[1]))]

def to_tables(cer):
    db = sqlite3.connect(cer)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    cursor.close()
    db.close()
    return tables

def to_columns(per,cer):
    db=sqlite3.connect(cer)
    db.text_factory = str
    cur = db.cursor()
    der=[]
    for jer in per:
        result = cur.execute("PRAGMA table_info('%s')" % jer).fetchall()
        her=toxic(list(zip(*result)))
        der.append(her)
    cur.close()
    db.close()
    return der

def to_sample(cer):
    db = sqlite3.connect(cer)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        table = pd.read_sql_query("SELECT * FROM %s LIMIT 1" % table_name, db)
        print(table)
#        table.to_csv(dir0+"/"+table_name + '.csv', index_label='index')
    cursor.close()
    db.close()
