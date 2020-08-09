# 14165
from getFromPickleR import returnAList
prefix="../../multilingual/rockstar/"
lister=returnAList()
limbo=(lambda x:reversed(x[:-1]+["unicode-table-data"]))
lamb=(lambda x:"/".join(x))
#for x in lister:
def fuckMe(x):
    limp=list(limbo(lister[x]))
    return prefix+lamb(limp),limp
