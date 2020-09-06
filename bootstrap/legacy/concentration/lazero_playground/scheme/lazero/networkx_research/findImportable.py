import os
# import re
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def checkFront(b, a):
    i = len(b)
    if len(a) <= i:
        return False
    else:
        if a[:i] == b:
            return True
    return False


def getFinal(b, a):
    # first bracket.
    c = a[len(b):]
    d = ""
    e = [" ", "(", ":"]
    # hook in.
    for x in c:
        if x in e:
            if d == "":
                pass
            else:
                return d
        else:
            d += x


def getParsed(a):
    with open(a, "r") as f:
        f0 = f.read().split("\n")
        x0 = []
        for x in f0:
            if checkFront("class", x):
                g = getFinal("class", x)
                x0.append(g)
            elif checkFront("def", x):
                g = getFinal("def", x)
                x0.append(g)
            else:
                pass
        return x0

# is it a class or definition?
# anyway it is not worthwhile.
# generate networkx code!
# def getName(a):
#     try:
#         exec("import " + a)
#         e = eval("dir({})".format(a))
#         e0 = list(filter(lambda x: len(x) > 4, e))
#         e1 = list(filter(lambda x: x[0:2] != "__" and x[-2:] != "__", e0))
#         return e1
#     except:
#         return []


def corrector(a, b):
    c = {similar(x, a): x for x in b}
    d = max(list(c.keys()))
    e = c[d]
    return e
    # one word
    # likelyhood?


fullList = os.listdir(".")
queryScript = list(filter(lambda x: len(x) > 3, fullList))
queryName = list(filter(lambda x: x[-3:] == ".py", queryScript))
queryScript = list(map(lambda x: x[:-3], queryName))
query = {x: getParsed(corrector(x, queryName)) for x in queryScript}
# have unknown things.
# do not import them. just parse them.
print(query)
