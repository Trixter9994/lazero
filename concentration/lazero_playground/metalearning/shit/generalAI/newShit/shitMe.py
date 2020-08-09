# exclude the 'binrapt/ail' through search engine interface
# it is an empty repo. should figure that out in log file if exists
from niche import Method2
#from simpleStorage import storeAList
def tabNine(x0):
    v=[[],[]]
    with open(x0,"r") as fuck:
        fucked=fuck.read()
        v=[list(map((lambda x:x.split('/')[1]),list(filter((lambda x: x!=""),fucked.split('\n'))))),list(filter((lambda x: x!=""),fucked.split('\n')))]
    return [v[0],list(map((lambda x: x.lower()),v[0])),v[1]]
m=list(map((lambda x:tabNine(x)),['shitLord.log','fuckLord.log']))
#print(m[1][2])
m0=m[0][1]+[m[1][1][v0] for v0 in range(len(m[1][1])) if m[1][0][v0] not in m[0][0]]
m1=m[0][2]+[m[1][2][v0] for v0 in range(len(m[1][1])) if m[1][0][v0] not in m[0][0]]
Grid=Method2(m0,m0)
# now we can mark these things.
# we must have same elements, unique elements.
# the matrix.
Grid=list(filter((lambda x: sum(x)>1),list(map((lambda x: list(map((lambda x: int(x)),x))),Grid))))
Grid=[[i0 for i0, x0 in enumerate(g) if x0 == 1] for g in Grid]
#print(Grid)
# you need to rehash.
Grid1=list(set([Grid.index(x) for x in Grid]))
#print(Grid1)
Grid0=list(map((lambda x:list(map((lambda x:m1[x]),x))),[Grid[x] for x in Grid1]))
for GridX in Grid0:
    print(GridX,len(GridX))
#storeAList(Grid0)
