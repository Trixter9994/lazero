def panasonic(a,b):
#    for c in b:
    if (len(b)==0 or len(a)==0):
        return a
    else:
#        d=[]
#        for c in a:
#        print(b)
#        e=list(filter((lambda x:(x>=b[0][0] and x<= b[0][1])),a))
#        c+=e
        return panasonic(list(filter((lambda x:(x<b[0][0] or x>b[0][1])),a)),b[1:])

def aka(m,s,e):
    geek=list(filter((lambda v: v not in e),panasonic(m,s)))
    return [list(filter((lambda y: y not in geek),m)),geek]

test=[1,2,4,5,6,7]
best=[[1,2],[6,9]]
exception=[4]
print(test)
print(best)
print(exception)
print(aka(test,best,exception))
