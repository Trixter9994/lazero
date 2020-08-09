import pickle
import uuid
struct=uuid.uuid4().hex
# this is a string which should be put into some place.
font=open("frog.log","w+")
font.write(struct+"\n")
font.close()
# what the fuck is going on?
# use some global shits.
import sqlite3

connection=sqlite3.connect("fuckyou.db")

anion=open("SOB.log","r")
onion=list(filter((lambda x: x!=""),anion.read().split("\n")))
# two lines.
union=[]
for x in range(len(onion)):
    union.append(list(filter((lambda x: x!=""),onion[x].split(" "))))
# actually two groups.
anion.close()

#wtf you want to do here?
# unpack the thing?
# how about use a function?

def nothing(bear):
    enumerator=[0,0,0,0]
    for paragraph in bear:
        enumerator[0]+=1
        print("-----paragraph: ",enumerator[0])
        for sentence in paragraph:
            enumerator[1]+=1
            print("----sentence: ",enumerator[1])
            for subsentence in sentence:
                enumerator[2]+=1
                print("---subsentence: ",enumerator[2])
                for word in subsentence:
                    enumerator[3]+=1
                    # this is good.
                    command="INSERT INTO subdir (uuid,word,pos,pi,si,ssi,wi)  VALUES ('{}','{}','{}',{},{},{},{});".format(struct,word[0],word[1],enumerator[0],enumerator[1],enumerator[2],enumerator[3])
                    connection.execute(command)
                    connection.commit()
                    # manually close the connection outside the function.
with open("scavenger.pickle","rb") as _file:
    papi=pickle.load(_file)
#    print(papi)
    nothing(papi)
    connection.close()
# to make the thing stored into a database.
# use memory in exchange of time.
# i don't want to fuck with it no more.
"""with open("scavenger.json","r") as _file:
    # in json the tuple is the same as list.
    # some kind of minor loss.
    # neglible.
    papi=json.load(_file)
    print(papi)"""
