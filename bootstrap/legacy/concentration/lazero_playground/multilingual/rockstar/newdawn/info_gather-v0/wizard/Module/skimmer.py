from simpleStorage import storeAList
with open("base.log","r") as f:
    storeAList(list(filter((lambda x: x!="" and ('.' not in x ) and ord(x[0])>=97),f.read().split("\n"))))
#    print(road)
