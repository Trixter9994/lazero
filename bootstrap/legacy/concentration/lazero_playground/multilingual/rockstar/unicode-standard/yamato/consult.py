import os

def openShit(a):
    with open(a, 'r') as f:
        return list(filter((lambda x: len(x)>1),f.read().split("\n")))

# def manipulate(a):
#     return list(map((lambda x:x[:-4]),a))
# pdftoppm -png -rx 300 -ry 300 document.pdf
def writeShit(a,b):
    with open(a, 'w+') as f:
        # c=manipulate(b)
        f.write("#!/bin/bash\n")
        for d in range(len(b)):
      #      f.write("mutool convert -o yamato/fuckYou/"+c[d]+".txt "+c[d]+".pdf\n")
             f.write("python3 fuckYou.py "+b[d]+"\n")

writeShit("ML.sh",openShit("format.log"))
os.popen("chmod +x ML.sh")
# i mean, are we done?
# use the optical scanner!