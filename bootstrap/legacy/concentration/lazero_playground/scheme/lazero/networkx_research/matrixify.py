import numpy as np

def courage(x):
    x0=list(map(len,x))
    x1=max(x0)
    x2=[x1-y for y in x0]
    return np.matrix([[z for z in x[y]]+["" for z in range(x2[y])] for y in range(len(x))])
