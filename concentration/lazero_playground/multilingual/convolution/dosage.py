from hashFunc import fuckYou
# there must be major and monir inside.
# we could use big prime number to do this.
# here comes the rsa package!
# no it won't do.
# figure it out yourself.
# i mean the highlighter. very important.
def testIfIn(a):
    if a == "<":
        return 1
    elif a == ">":
        return -1 
    else:
        return 0

def cannabis(a):
    a1 = [0,0]
    a4 = []
    for a0 in a:
#        print(a0)
        a3=[testIfIn(a2) for a2 in a0]
        oreo=a1[len(a1)-1]
#        print(a3)
        pie=(0 if len(a3)==0 else sum(a3))
#        print(pie)
        els=pie+oreo
#        print(els)
        a1.append(els)
        a4.append(1 if (sum(a3)==0 and (1 in a3)) else 0)
    return [1 if not a4[r]==0 else a1[r+2] for r in range(len(a))]

def drug(a):
    c=cannabis(a)
    b=[fuckYou(r) for r in a]
    for r in range(len(a)):
        if c[r]==1:
            b[r][0]=1
    return b
