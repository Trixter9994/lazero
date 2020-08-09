import random
import copy
def readLines(a):
    with open(a, "r") as f:
        return f.read().split("\n")

def filt(a):
    assert type(a)==str
    if len(a) > 0:
        return a[0] != "#"
    else:
        return False

def selectCandidates(b):
    a=copy.copy(b)
    return [x for x in range(len(a)) if filt(a[x])]
# missing one whole line!
# that is too rude.
# is it? for one might not know things?
# fuzzy logic switch?
def rComment(a):
    b = readLines(a)
    b0 = selectCandidates(b)
    if not len(b0) > 0:
        return None
    else:
        r = random.choice(b0)
        b[r] = "# " + b[r]
    return b