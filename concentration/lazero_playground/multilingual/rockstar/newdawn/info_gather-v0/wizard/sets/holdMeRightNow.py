import sqlite3
conn=sqlite3.connect("fuckyou.db")
# R U SURE IT IS GOOD TO HAVE SUCH A JOB?
# FUCK IT.
def insertOneItem(a,b):
    try:
        sql="INSERT INTO groupAllChars (mainId,charGroup) VALUES ({},'{}');".format(a,b)
        conn.execute(sql)
    except:
        print("DATABASE CONSTRAINT ERROR OR ELSE")
#    return
def insertOneRelation(a,b,c,d,e):
    try:
        sql="INSERT INTO subdue (startId,startType,endId,endType,relationType) VALUES ({},'{}',{},'{}','{}');".format(a,b,c,d,e)
        conn.execute(sql)
    except:
        print("DATABASE CONSTRAINT ERROR OR ELSE")
#    return

def cleanUp():
    try:
        conn.commit()
    except:
        print("COMMIT FAILED")
    conn.close()
# you have to let some intermediate things going through before putting the data into the fucking graph database.
# alphabetical order, case relationship are all one-directional.
# the lables can have relationships too.
# but what is the difference here? shall we check something as not usable?
# just by putting all labels into an array? shall we distinguish them?
# i mean at least wee have the alphabetical order.
# insert random stuff first? or just make sure the relationship is kept?