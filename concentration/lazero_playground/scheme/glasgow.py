def ransome(a, b):
    # return a+b
    print("%s and %s are about to interact!" % (a, b))
    return


def getter(a):
    if not a:
        return " not "
    else:
        return " "

# ransome("hello", "world")


def controller(a, b, c, d, e, f):
    # e is for direction.
    # c for negation of a.
    # d for negation of b.
    # if not e:
    # formula=
    # these things form a distribution all the fucking time.
    # return controller(b, a, d, c, not e)
    # else:
    return getter(e)+"know"+getter(c)+a + " ->" + getter(f)+"know" + getter(d)+b
    # never mind?
    # get the sequence.
# it is interesting.
# the world is playing tricks on us.

def getSequence(a, b, c=[]):
  # c is the target thing.
   # a is for choice.
   # b is for length.
    if b > 0:
        b0 = b-1
        if c == []:
            c0 = [[x] for x in a]
            # flattern?
        else:
            c0 = [[y + [x] for x in a] for y in c]
            c0 = [x for y in c0 for x in y]
        return getSequence(a, b0, c0)
    elif b == 0:
        return c
    else:
        raise Exception


    # return [True,False,True,False]
    # make it recursive?
# you always get shit.
# 2^3=8
getPerm = getSequence([True, False], 4)
# print(getPerm)
for g in getPerm:
    g0 = controller("hello", "world", *g)
    print(g0)
# to finite the possibility.
# that is interesting.
# not enough.
# get the unknown?
# well, you can change this.
# teach that thing how to fucking fix bugs.
# we do not know how to do this shit so far.
# who the hell knows that?
# do whatever, launch whatever, get whatever.
# all we need is a connector.
# do that mbti stuff.
