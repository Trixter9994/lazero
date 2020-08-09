from storeADill import storeXList
def flat(x):
    return [z for y in x for z in y]

def returnIp(a,b=""):
    assert a>=0
    if b=="":
        assert a>0
        return returnIp(a-1,[str(x) for x in range(256)])
    elif a>0:
        return returnIp(a-1,list(map(lambda x:".".join(x),flat([[[str(y),z] for z in b] for y in range(256)]))))
    else:
        return b

b=returnIp(2)
storeXList(b,"ipv4_list_0")
storeXList(b,"ipv4_list_1")
