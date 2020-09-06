from getStandard import fuckMe
# 14139 max index
# 2,6
from simpleStorageR import storeList
from fuckMe import secondTest
prefix="../../multilingual/rockstar/"
f0=[[],[],[]]
for x in range(14166):
    f=fuckMe(x)
    p=secondTest(prefix+f[1])
    if p[0]==True:
        f0[0].append(f[0])
    elif p[1]==True:
        f0[1].append(f[0])
    else:
        f0[2].append(f[0])
storeList(f0)
