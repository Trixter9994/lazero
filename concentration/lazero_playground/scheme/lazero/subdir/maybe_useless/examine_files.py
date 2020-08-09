from getFromPickleR import returnListV

def checkDuplicate(a):
    b=a.split(".")
    b0=set(b)
    return len(b)>len(b0)

def getMeDone(a):
    r=returnListV(a)
    r=list(map(lambda x:{y:x[y] for y in x.keys() if not checkDuplicate(y)},r))
    return r

