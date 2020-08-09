<<<<<<< HEAD
# 14165 max index
from getFromPickleR import returnAList
lister=returnAList()
lamb=(lambda x:list(reversed(x[:-1]+["unicode-table-data"])))
limbo=(lambda x:"/".join(x))
#for x in lister:
#    print(prefix+limbo(x))
def fuckMe(x):
    l=lamb(lister[x])
    return l,limbo(l)
=======
# 14165
from getFromPickleR import returnAList
prefix="../../multilingual/rockstar/"
lister=returnAList()
limbo=(lambda x:"/".join(reversed(x[:-1]+["unicode-table-data"])))
#for x in lister:
def fuckMe(x):
    return prefix+limbo(lister[x])
>>>>>>> 82f1d86cc9810194c8951262d2377a020d4e3a47
