def testCube(_list):
    v=sorted(list)
    for i in range(len(_list)-1):
        if abs(v[i]-v[i+1])==1:
            return True
        else:
            pass
    return False
    
def semen(sortedList,unsortedList):
    l=len(sortedList)/2
    l0,l1=sortedList[:l-1],sortedList[l:]
    if (testTube(l0) or testTube(l1)):
        return sortedList
    else:
        v0,v1=unsortedList[:l-1],unsortedList[l:]
        v2=[]
        for k in len(v0):
            v2.append(v0[k])
            v2.append(v1[k])
        return v2
    
