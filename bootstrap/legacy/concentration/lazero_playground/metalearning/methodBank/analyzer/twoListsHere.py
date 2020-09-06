from defTester import notch, checkFunctor
from niche import wroteAHaskell
functorNames=[]
# parse indentation first.
nicetry="sample_strip",".py"
pm=[]
with open("".join(nicetry),"r") as j:
    i1=0
    for fuck in j.readlines():
        i=0
        for i0 in range(len(fuck)):
            if fuck[i0] in [" ","\t"]:
                i+=1
            else:
                break
        iFuck=fuck if fuck[-1]!="\n" else fuck[:-1]
        pm.append((i,fuck[i:],notch(iFuck),checkFunctor(iFuck),i1))
        i1+=1
#        pm.append((i,fuck,notch(iFuck),checkFunctor(iFuck)))

print(pm)
bitch="_fix".join(nicetry)
print(bitch)
wroteAHaskell(bitch,pm)
