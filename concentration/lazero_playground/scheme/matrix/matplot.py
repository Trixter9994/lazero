import random
import numpy as np

def getnum(a,b):
    return random.randrange(a,b)

def randomMatrix(a,b,c):
    return np.matrix([[getnum(a,b)+getnum(a,b)*1J for x in range(c)] for x in range(c)])

#r=randomMatrix(-10,10,10)
#print(r)
