def readLinks():
    g=[]
    with open("links.log","r") as fuck:
        g=list(filter((lambda x:x!="" and x!= "\n"),fuck.read().split("\n")))
    return g

prt=readLinks()
#print(prt)
#grt=list(map((lambda y:constructLinks(y)),prt))
#print(grt)
#k0=0
with open("buster.sh","w+") as buster:
    buster.write("#!/bin/bash\n")
    k2=0
    for k1 in prt:
        buster.write("wget '"+k1+"' -O "+str(k2)+"_.log\n")
        k2+=1
#    k0+=1
