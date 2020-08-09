import pickle

# use some global shits.
#import sqlite3

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
                    if word[1] in union[0]:
                        print("--word: ",enumerator[3]," pronoun: ",word)
                    elif word[1] in union[1]:
                        print("word: ",enumerator[3]," determiner: ",word)
                    else:
                        pass

with open("scavenger.pickle","rb") as _file:
    papi=pickle.load(_file)
#    print(papi)
    nothing(papi)
# to make the thing stored into a database.
# i don't want to fuck with it no more.
"""with open("scavenger.json","r") as _file:
    # in json the tuple is the same as list.
    # some kind of minor loss.
    # neglible.
    papi=json.load(_file)
    print(papi)"""
