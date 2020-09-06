def testCube(_list):
    v=sorted(_list)
    vk=0
    v2=int(len(_list)/2)
    for i in range(len(_list)-1):
        if abs(v[i][1]-v[i+1][1])==1:
            vk+=1
            if vk>v2:
                return True
            else:
                pass
        else:
            pass
    return False
    
def semen(sortedList,unsortedList):
    l=int(len(unsortedList)/2)
    l0,l1=sortedList[0],sortedList[1]
    jam=testCube(l0) or testCube(l1)
    print("-- LIB STD --")
    print(jam)
    print("-- LIB STD --")
    if jam:
        return sortedList
    else:
        if l*2==len(unsortedList):
            v0,v1=unsortedList[:l-1],unsortedList[l:]
            # need for hard code.
#        v2=[]
#        for k in len(v0):
#            v2.append(v0[k])
#            v2.append(v1[k])
            return semen([v0,v1],unsortedList[:-1])
        else:
            print("FUCKING FUCKED\nFUCKING FUCKED")
            return [[],[]]
    
