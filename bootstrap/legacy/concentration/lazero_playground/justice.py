from storeADill import storeXList

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

def mindBlocks(a):
    with open("layer_"+str(a)+".log","r") as f:
        return list(filter(lambda x: len(x)>1,f.read().split("\n")))

fx=lambda x: [z for y in x for z in y]
m0=[mindBlocks(x) for x in range(9)]
m0 = fx(m0)
m1={}
for x in m0:
    m1.update({x: getParsed(x)})

storeXList(m1, "functors_and_classes")
# all we need is the search.