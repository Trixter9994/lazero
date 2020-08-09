import os

def exist(a):
    return os.path.exists(a)

def returnDir(a):
    return os.listdir(a)

def firstTest(a):
    return os.path.isabs(a)

def secondTest(a):
    return os.path.isdir(a), os.path.isfile(a)

def thirdTest(a):
    return os.path.islink(a), os.path.ismount(a)

def absList(a):
    def getReal(a):
        return os.path.realpath(a)
    def merge(a,b):
        if a[-1]=="/":
            return a+b
        else:
            return "/".join([a,b])
    # only for internal use.
    fma=(lambda b:list(map((lambda x: merge(b,x)),returnDir(b))))
    if not firstTest(a):
        return fma(getReal(a))
    else:
        return fma(a)

def stdTest(x):
    return [[y,*secondTest(y)] for y in absList(x)]
