from getFromPickleR import returnList
from simpleStorageR import storeListR
r=returnList()[1]
#print(r)
r0=[]
for x in range(5):
    r0.append([])
for x in r:
    r0[len(x)-2].append(x)
storeListR(r0)
