import re
import os


# def openfinder(a):
#     with open(a, "r") as f:
#         return re.findall(r'[a-zA-Z0-9\-\_]+', str(f.read()))


def openfinder(a):
    with open(a, "r") as f:
        y0 = []
        def d(x): return [z for y in x for z in y]
        for x in f.read().split("\n"):
            if len(x) > 1:
                if x[0] != "#":
                    y0.append(x)
        return re.findall(r'[a-zA-Z0-9\-\_]+', " ".join(y0))

# it does not have metainfo. we have to relocate them.
# do not think you can save time. it is really stupid.

def getList():
    return os.listdir(".")


def getPy(a):
    return list(filter(lambda x: x[-3:] == ".py", list(filter(lambda x: len(x) > 3, (a)))))


def pyList(a):
    return {x: openfinder(x) for x in a}


def findBase(a, b):
    return [x for x in a if x in b]


def findCommon(a):
    b = list(a.keys())
    c = {b[x]: b[x+1:] for x in range(len(b)-1)}
    d = {x: {y: findBase(a[x], a[y]) for y in c[x]} for x in c.keys()}
    return d


def findRelational(a):
    b = {x: {y: a[x][y] for y in a[x].keys() if len(a[x][y]) > 0}
         for x in a.keys()}
    c = {(x, y): a[x][y] for x in a.keys() for y in a[x].keys()}
    return c


def differ(a, b):
    return list(set([x for x in a if x not in b]))


def findDistinct(a):
    def f(x): return [y for z in x for y in z]
    b = [x for x in a.keys()]
    c = [[x for x in b if x != b[y]] for y in range(len(b))]
    d = {b[y]: list(set(f([a[x] for x in c[y]]))) for y in range(len(c))}
    e = {x: differ(a[x], d[x]) for x in a.keys()}
    return e


g = getList()
e = getPy(g)
p = pyList(e)
f = findCommon(p)
r = findRelational(f)
s = findDistinct(r)
print(s)
# print(r)
