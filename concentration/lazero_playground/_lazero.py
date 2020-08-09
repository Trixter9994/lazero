import subprocess
#import random
from storeADill import storeAList

#def reader(f):
#    with open(f,"r") as f0:
#        return f0.read()

cmd = "ls **/*.py"
ms = subprocess.check_output([cmd],shell=True,executable='/data/data/com.termux/files/usr/bin/zsh')
#print(ms)
ms=ms.decode().split("\n")[:-1]
#print(ms)
ms0=storeAList(ms)
