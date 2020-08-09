from matplot import randomMatrix
import numpy as np

def closest(a,b):
#    print(a,b)
    m=[abs(sum(sum(np.array((a-x).flatten(order='C'))))) for x in b]
#    print(m)
    n=min(m)
    return {m[x]:x for x in range(len(m))}[n]

c="""python: can't open file 'matrix.py': [Errno 2] No such file or directory"""
c0=[(randomMatrix(-10,10,10),x) for x in set(c)]
#c1={x[0]:x[1] for x in c0}
c2={x[1]:x[0] for x in c0}
c3=[x[0] for x in c0]
c5=[x[1] for x in c0]
#print(c3,c5)
c4=""
#for x in c:
y=0
while True:
    x=c[y]
    c7=""
    g=c2[x]
    try:
        c7=c4[-1]
        c2[x]=c2[c7]*g
    except:
        pass
    c6=closest(g,c3)
#    print(c6,len(c5))
    c7=c5[c6]
    if c7==x:
        c4+=c7
        y+=1
        print("letter #%d  learned." % (y,))
        if y>=len(c):
            break
    else:
        c2[x]=c2[c7]*randomMatrix(-10,10,10)*0.1
print("output below:")
print(c4)
