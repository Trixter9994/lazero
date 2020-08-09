# 14165 max index
import os
from simpleStorageR import storeList
prefix="../../../multilingual/rockstar/unicode-standard/retribution"
#lister=returnAList()
limbo=os.listdir(prefix)
prt=(lambda x:list(filter((lambda x: x[0]=='U' and x[-3:]=='txt'),x)))(limbo)
storeList(prt)
#for x in lister:
