import os
def getFile(a):
    with open("script.sh","w+") as f:
        f.write("#!/bin/bash\n")
        f.write("\n".join(a))
def genCode():
    d=[]
    for x in range(1,71):
        d.append("curl 'https://github.com/google?page="+str(x)+"&tab=repositories' > "+str(x)+".log")
    return d
getFile(genCode())
os.popen('chmod +x script.sh')
