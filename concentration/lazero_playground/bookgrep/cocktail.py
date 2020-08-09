import unicode_charnames as uc
import copy
import os


def getFuck(a, b):
    with open(a, "a+") as f:
        for d in b:
            f.write(d + "\n")


def getShit(a):
    with open(a, "r") as f:
        return f.read()


def revEnv(a):
    f = list(reversed(copy.copy(a)))
    #    print(f)
    try:
        for x in range(len(f)):
            if "LATIN" in uc.charname(f[x]):
                break
            f.pop(x)
        return "".join(list(reversed(f)))
    except:
        return


# get useful things?
d, d0 = getShit("rgHelp.log").split("\n"), []
for x in d:
    d0 += list(
        filter(lambda x: x[0] == "-", list(filter(lambda x: len(x) > 0, x.split(" "))))
    )
fg, gkd = ["!/bin/bash"], "rgScript.sh"
for y in list(set(map(revEnv, d0))):
    if y != None:
        fg.append("rg " + y)

getFuck(gkd, fg)
os.popen("chmod +x " + gkd)
