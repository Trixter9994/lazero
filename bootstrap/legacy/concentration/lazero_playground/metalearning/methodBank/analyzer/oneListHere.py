from defTester import notch, checkFunctor
functorNames=[]

# parse indentation first.

with open("sample_strip.py","r") as j:
    i1=0
    for fuck in j.readlines():
        i=0
        for i0 in range(len(fuck)):
            if fuck[i0] in [" ","\t"]:
                i+=1
            else:
                break
        iFuck=fuck if fuck[-1]!="\n" else fuck[:-1]
        print(i,fuck[i:],notch(iFuck),checkFunctor(iFuck),i1)
        i1+=1
