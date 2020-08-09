# This is called the metaProgramming and basically any fucking prog lang can do this fuck!
import re
from simpleStorageR import storeAList
def cockShock(fuckMe):
    with open(fuckMe,"r") as s:
        rk=s.read().replace('\n',' ')
#    print(rk)
        so=re.findall(r"'''CREATE TABLE[^']+",rk,re.MULTILINE)[0][3+6+7:]
#        print(so)
        sd=re.match(r'^\w+',so).group(0)
#        print(sd)
        rn=so.replace(sd,'')
#        print(rn)
        sv=re.findall(r'^.+CONSTRAINT',rn)[0].replace("CONSTRAINT","")
#        print(sv)
        svd=list(filter((lambda x : x!=""),sv.split(',')))
        lamb=(lambda x: re.findall(r"\w+",x)[0])
        lambs=(lambda x: re.findall(r"\w+",x) !=[])
#        print(svd)
        svg=list(map((lambda x: lamb(x)),list(filter((lambda x:lambs(x)),svd))))
#        print(svg)
    return [sd,svg]
    # sample of metacoding
    # I need transformation now!
dickHead=['makeDB0.py']
a=cockShock(dickHead[0])
'''b=cockShock(dickHead[1])
c=cockShock(dickHead[2])
d=cockShock(dickHead[3])'''
'''print(a)
print("--spliter--")
print(b)'''
storeAList([a])
