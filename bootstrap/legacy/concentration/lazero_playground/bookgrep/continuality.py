# add tolerance to overall function.
# use inertia mechanism.
# not a package.
# from approx import approx
# WTF is this shit?
# for subgap processing.
#from stackMe import queue
import backTrans
#import flattern, flatternII

class Faith:
    def __init__(self, a):
        self.a = a

    def set(self):
        v = []
        for a0 in self.a:
            if a0 not in v:
                v = v + [a0]
        return v


def indices(a, x0):
    return [i for i, x in enumerate(a) if x == x0]

def lazer(a, b):
    c = [[] for x in range(len(b))]
    for i, x in enumerate(a):
        if x in b:
            c[b.index(x)].append(i)
    return c

def selected(a, b):
    l = len(a) - 1
    # b is tolerance.
    r = [0] + backTrans.flatternII(
        list(
            map((lambda x: [x, x + 1]),
                indices([int((a[v + 1] - a[v]) > b)
                         for v in range(l)], 1)))) + [l]
    #    print(a)
    # much better.
    #    print(r)
    return [[a[r[2 * k]], a[r[2 * k + 1]]] for k in range(int(len(r) / 2))]


def moveOnII(g, b, c, d, e):
    a = [d(z) for z in g]
    # subpattern finder.
    # b for scale, c for tolerance.
    # export non-standard matricies.
    l = len(a)
    xvn = [a[m:m + b] for m in range(l - b + 1)]
    # print(xvn)
    m = list(filter((lambda x: backTrans.flatternIII(x)), xvn))
    # what is this flattern function?
    # print(m)
    candidate = Faith(m).set()
    # print(candidate)
    # important! 0 for 0 tolerance. must be next to each other.
    return list(
        map((lambda z: list(filter((lambda y: y[1] - y[0] > e), z))),
            list(map((lambda x: selected(x, c + b)), lazer(xvn, candidate)))))


def moveOn(a, b, c):
    # subpattern finder.
    # b for scale, c for tolerance.
    # export non-standard matricies.
    l = len(a)
    xvn = [a[m:m + b] for m in range(l - b + 1)]
    # print(xvn)
    m = list(filter((lambda x: backTrans.flattern(x)), xvn))
    # what is this flattern function?
    # print(m)
    candidate = Faith(m).set()
    # print(candidate)
    # important! 0 for 0 tolerance. must be next to each other.
    return list(map((lambda x: selected(x, c + b)), lazer(xvn, candidate)))
    # now check the shit.
    # WTF?

#    cn=[indices(xvn,c) for c in candidate]
# extract the shit.
#    org=set(candidate)
# encapsule the objects.
# tolerace shall be processed along with the subgap. More tolerance, more subgaps.
# is this the total tolerance?
# shall we not using flattern func?
# this is for linear scanning.
# double spliter?
# this shall be better.
# use the dump func.
