from dbM import showE
import json
from simpleStorageR import storeWTF
s=showE("projects",1)
u={}
for x in s:
    p=json.loads(x[1])
    # print(x[0])
    try:
        u.update({x[0]:(p['info']['description'])})
    except:
        pass
storeWTF(u)
# this is bad. only for output, preprocessing.
# all technical stuff.