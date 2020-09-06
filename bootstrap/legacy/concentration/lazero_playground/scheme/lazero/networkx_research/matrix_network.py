from matrixify import courage
#from getFromPickleR import returnList
from simpleStorageR import storeListR

with open("networkx_reference.txt","r") as f:
    c=courage(f.read().split("\n"))
    storeListR(c)
