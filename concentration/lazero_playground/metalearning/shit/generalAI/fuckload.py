from getFromPickle import returnList

def writeShit(a,b):
    with open(a,"w+") as fuck:
        for f in b:
            fuck.write(f+"\n")
#    return f

d=list(set([d for d in returnList()]))

writeShit("fuckLord.log",d)
