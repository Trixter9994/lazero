def SM(x):
    return {a[0]:a[1] for a in x}
# import random module?
def getApprox(a):
    a0=[]
    for xm in a:
        x0=list(xm('span'))
        if len(xm.text)>2:
            a0.append((lambda y:int(SM(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),y.attrs["style"].split(";"))))))["top"][:-2]))(xm))
    return list(sorted(list(set(a0))))

def cleanUp(a):
    a0=[]
    for x in getApprox(a):
        if a0!=[]:
            if abs(x-a0[-1])>7:
                a0.append(x)
        else:
            a0.append(x)
    return a0
# multiple bold -> combine
def subFix(a):
    a0=[]
    for x in a:
        if a0!=[]:
            if abs(x-a0[-1])>6:
                a0.append(x)
        else:
            a0.append(x)
    return a0
# greater than seven.
# warning there is possibility to have problems in CJK section.
def programApprox(a,b,c=3):
    # this is fucking amazing!
    if a in b:
        # print("AMANDA!",a)
        return a
    else:
        for y in range(1,c):
            for x in [-1,1]:
                ocho=a+y*x
                if ocho in b:
                    # print("I AM HERE!",ocho)
                    return ocho
        # print("THERE!",a)
        return a