from simpleStorageR import storeAList
import re
import subprocess
from multiprocessing import Pool, freeze_support
from endmark import windowEndMarkEx as wex


def parallel(x, v, z):
    with Pool(processes=x) as pool:
        return pool.map(v, z)


def getOutput(cmd):
    return subprocess.check_output([cmd], shell=True, executable='/data/data/com.termux/files/usr/bin/zsh')
# ??

if __name__ == "__main__":
    with open("piplist.log") as f:
        g = f.read()
        h = g.split("\n")[2:]
        j = {}
        i = []
        for x in h:
            try:
                y = re.findall(r"^[a-zA-Z0-9\._\-]+", x)[0]
#            print(y)
                i.append(y)
            except:
                pass
#        print(i,len(i))
        l = []
        for x in i:
            if len(x) > 1:
                l.append("pip3 show "+x)
        l = wex(l, 10)
    freeze_support()
    for msg in l:
        print("\n".join(msg))
        x0 = parallel(len(msg), getOutput, msg)
        x0 = [(msg[x], x0[x]) for x in range(len(msg))]
        for x, x1 in x0:
            ms = re.findall(r"[a-zA-Z0-9\._\-]+$", x)[0]
            j.update({ms: x1.decode()})
            print("processed: {}".format(x))
            print(x1.decode())
    storeAList(j)
    print("brief stored.")
