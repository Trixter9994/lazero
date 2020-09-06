import sqlite3
conn=sqlite3.connect("fuckyou.db")
# R U SURE IT IS GOOD TO HAVE SUCH A JOB?
# FUCK IT.
sql='''CREATE TABLE chainer (startId INT NOT NULL,
endId INT NOT NULL, groupName TEXT NOT NULL,
CONSTRAINT rule UNIQUE (startId ASC, endId ASC, groupName ASC)
 );'''
conn.execute(sql)
conn.commit()
conn.close()
# you have to let some intermediate things going through before putting the data into the fucking graph database.
# alphabetical order, case relationship are all one-directional.
# the lables can have relationships too.
# but what is the difference here? shall we check something as not usable?
# just by putting all labels into an array? shall we distinguish them?
# i mean at least wee have the alphabetical order.
# insert random stuff first? or just make sure the relationship is kept?
