from getFromPickle import returnAList
from term1 import executeCode, closeConnection
from conPro import sqlMaker
masochist=list(map((lambda x:x[0]),returnAList()))
print(masochist)
# this is a fucking list.
countOn=0
for k in masochist:
    print("-- spliter for "+k+" --")
    superMan=executeCode(sqlMaker(k))
    for superMania in superMan:
        if countOn!=0:
            print(superMania)
        else:
            # check the fucking shit.
            print(superMania[0],chr(superMania[0]),superMania[1],superMania[2],chr(superMania[2]),superMania[4])
    print("-- spliter for "+k+" --")
    countOn+=1
closeConnection()
