from stackMe import queue

def checkUnique(a):
    x0=[]
    for x in a:
        if x not in x0:
            x0.append(x)
            print(x)
        else:
            pass
    return x0

def fixedQueue(a,b):
    assert type(b)==int and b>=3
    x0=queue(b)
    x1=""
    for x in a:
        if x not in x0.dump():
            x0.queue(x)
            x1+=x
        else:
            pass
    return x1
