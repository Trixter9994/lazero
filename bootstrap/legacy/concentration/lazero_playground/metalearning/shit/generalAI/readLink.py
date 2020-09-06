vlan="https://github.com/search?"
wlan=len(vlan)
def constructLinks(a):
    c,d=a
    f=[vlan+"p="]
    g=[]
#    if d[wlan]=="p":
    f.append(d[d.index("&"):])
    if not d[wlan]=="p":
        f[1]+=("&"+d[len(vlan):d.index("&")])
    for e in range(int(c)):
        g.append(str(e+1).join(f))
    return g

def readLinks():
    g=[]
    with open("links.log","r") as fuck:
        g=list(filter((lambda x:x!="" and x!= "\n"),fuck.read().split("\n")))
    return g

prt=list(map((lambda x: x.split(" ")),readLinks()))
#print(prt)
grt=list(map((lambda y:constructLinks(y)),prt))
#print(grt)
k0=0
for k in grt:
    with open("buster"+str(k0)+".sh","w+") as buster:
        buster.write("#!/bin/bash\n")
        k2=0
        for k1 in k:
            buster.write("wget '"+k1+"' -O "+str(k0)+"_"+str(k2)+".log\n")
            k2+=1
    k0+=1
