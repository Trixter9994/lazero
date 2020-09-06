# run me first.
import sqlite3
# there is nothing special here.
# decentralized design.
command='''CREATE TABLE subdir
 (uuid TEXT NOT NULL,
 word TEXT    NOT NULL,
 pos TEXT NOT NULL,
 pi  TINYINT     NOT NULL,
 si TINYINT NOT NULL,
 ssi TINYINT NOT NULL,
 wi TINYINT NOT NULL,

CONSTRAINT rule  UNIQUE (uuid ASC, pi  ASC  ,si ASC, ssi ASC, wi ASC  )
 );'''

sql = ("CREATE INDEX index0 ON subdir (pos);")

sql0 = ("CREATE INDEX index1 ON subdir (uuid);")

#sql1 = ("CREATE INDEX index2 ON subdir (depth);")

conn=sqlite3.connect("fuckyou.db")
conn.execute(command)
conn.execute(sql0)
conn.execute(sql)
# you could use another identifier instead of POS symbols, but that's another story.

# rape people off and get paid for it.
conn.commit()
conn.close()
# check if the rule works.
# export the uuid in case of forgotten.
#font=open("hello.log","w+")
# this will not be the problem, isn't it?
#struct=a0+"\n"+a+"\n"
#font.write(struct)
#font.close()
