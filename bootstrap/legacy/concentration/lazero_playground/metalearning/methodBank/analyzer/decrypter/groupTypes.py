from tokenize import *
fuck=dir()
shit=[(h,eval(h)) for h in fuck if type(eval(h)).__name__ == "int"]
#print(shit)
jerk=list(sorted(shit,key=(lambda x:x[1])))
# very important! do it afterwards.
from simpleStorage import storeAList
storeAList(jerk)
