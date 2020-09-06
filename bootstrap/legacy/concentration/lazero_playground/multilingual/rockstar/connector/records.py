import os, re, sqlite3
#import pandas as pd
#import sqlite3
# to trace back and forth, using the full path if you want to.
# if it is absolute path, we use origin as "" or something like that.
# if it is relative, we make a header for the topmost, marked as origin.
#startpath="/data/data/com.termux/files/home/lazer/multilingual/rockstar/superdir"
startpath="/data/data/com.termux/files/home/lazer/multilingual/rockstar/unicode-table-data"

def superskimmer(path):
    path0=list(filter((lambda x:x!=""),path.split("/")))[:-1]
    p0=""
    for p in path0:
        p0+=("/"+p)
    return p0

porn=list(os.walk(startpath))
#print(porn)
# I still prefer the full path.
# give it a try.
base=os.path.basename(startpath)
#_id=0
shit=[[base,0,startpath.count("/")-1,"",superskimmer(startpath)]]
for fuck in porn:
    pussy=fuck[0]
    for bitch in fuck[1]:
#        _id+=1
        shit.append([bitch,0,pussy.count("/"),os.path.basename(pussy),pussy])
    for jerk in fuck[2]:
#        _id+=1
        shit.append([jerk,1,pussy.count("/"),os.path.basename(pussy),pussy])

#print(shit)

conn = sqlite3.connect('tits.db')             
# you shall not execute it every time.  

conn.execute('''CREATE TABLE subdir 
 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 name           TEXT    NOT NULL,
 type         TINYINT     NOT NULL,
 depth TINYINT NOT NULL,
 parent TEXT ,
 miscellaneous TEXT NOT NULL,
CONSTRAINT rule  UNIQUE (name ASC, miscellaneous ASC )
 );''')

sql = ("CREATE INDEX index0 ON subdir (name);")  

# sql0 = ("CREATE INDEX index1 ON subdir (id);")  

sql1 = ("CREATE INDEX index2 ON subdir (depth);") 

conn.execute(sql)

conn.execute(sql1)


for a,b,c,d,e in shit:                  
    if e!="": 
#        print([a,b,c,d,e])
        conn.execute("INSERT INTO subdir (name,type,depth,parent,miscellaneous)  VALUES ( '{}',{},{},'{}','{}');".format(a,b,c,d,e))            
    else: 
#        print([a,b,c,d,e])
        conn.execute("INSERT INTO subdir (name,type,depth,miscellaneous)  VALUES ( '{}',{},{},'{}');".format(a,b,c,e))
conn.commit()
conn.close()
