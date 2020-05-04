from simpleStorageR import storeAList
import re
import subprocess
from multiprocessing import Pool, freeze_support
from endmark import windowEndMarkEx as wex


def parallel(x,v,z):
  with Pool(processes=x) as pool:
    return pool.map(v, z)


def run_and_get(cmd):
    p = subprocess.Popen(cmd, shell=True)
  ## But do not wait till netstat finish, start displaying output immediately ##
    im=""
    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            return None
            break
        if out != '':
            im += out
    return im


def getOutput(cmd):
    print(cmd)
    try:
        # return subprocess.check_output([cmd], shell=True, executable="C:\\WINDOWS\\System32\\cmd.exe")
        return run_and_get(cmd)
    except:
        return None


if __name__=="__main__":
    with open ("piplist.log") as f:
        g=f.read()
        h=g.split("\n")[2:]
        j={}
        i=[]
        for x in h:
            try:
                y=re.findall(r"^[a-zA-Z0-9\._\-]+",x)[0]
#            print(y)
                i.append(y)
            except:
                pass
#        print(i,len(i))
        l=[]
        for x in i:
            if len(x)>1:
                l.append("pip36 show "+x)
        l=wex(l,10)
    freeze_support()
    for msg in l:
        # print("\n".join(msg))
        x0=parallel(len(msg),getOutput,msg)
        x0=[(msg[x],x0[x]) for x in range(len(msg))]
        for x, x1 in x0:
            ms = re.findall(r"[a-zA-Z0-9\._\-]+$", x)[0]
            if x1!=None:
                j.update({ms:x1.decode()})
                # print("processed: {}".format(x))
                # print(x1.decode())
    storeAList(j)
    print("brief stored.")
