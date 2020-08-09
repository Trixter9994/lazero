from getFromPickle import returnAList
from term1 import executeCode, closeConnection
from conPro import sqlMaker
masochist=list(map((lambda x:x[0]),returnAList()))
print(masochist)
# this is a fucking list.
for k in masochist:
    print("-- spliter for "+k+" --")
    superMan=executeCode(sqlMaker(k))
    for superMania in superMan:
        print(superMania)
    print("-- spliter for "+k+" --")
closeConnection()
