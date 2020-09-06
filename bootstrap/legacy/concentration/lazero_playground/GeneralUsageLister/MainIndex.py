def anal0(p):
    b=open("MainIndex/zero/"+p,"w+")
    b.write("#!/bin/bash\n")
    b.write(p+" &> ../zero-log/"+p+".log")
    b.write('\n')
    b.close()

def anal1(p):
    b=open("MainIndex/one/"+p,"w+")
    b.write("#!/bin/bash\n")
    b.write(p+" -h &> ../one-log/"+p+".log")
    b.write('\n')
    b.close()

def anal2(p):
    b=open("MainIndex/two/"+p,"w+")
    b.write("#!/bin/bash\n")
    b.write(p+" --help &> ../two-log/"+p+".log")
    b.write('\n')
    b.close()

import re
a=open("MainIndexWithIdenticalKeywords.txt","r")
i=0
p1=[]
while i!=1:
    p=a.readline()
    if p!="":
        p=re.findall(r'[^, ]+',p)
#        print (p)
        for p0 in p:
            if len(p0)<35:
                p1.append(p0[:-1])
    else:
        i=1
        break
a.close()

p2=set(p1)

for p3 in p2:
    anal0(p3)
    anal1(p3)
    anal2(p3)
