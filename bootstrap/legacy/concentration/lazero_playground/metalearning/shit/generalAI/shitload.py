from getFromPickle import returnAList

def writeShit(a,b):
    with open(a,"w+") as fuck:
        for f in b:
            fuck.write(f+"\n")
#    return f

d=list(set([d for b in returnAList() for c in b for d in c]))

writeShit("shitLord.log",d)

