import random
import math

def checkin(a,b,c=0):
    if a<=b:
        return c
    else:
        return checkin(a*0.5,b,c+1)

def checkout(a,b,theta):
    z=checkin(a,b)
    #print("z",z)
    disk=1-theta/b
    #print("disk",disk)
    epsilon=-math.log2(disk)
    phi=int(z/epsilon)
    print(epsilon,phi)
    return epsilon, phi

def finite(a,epsilon,phi):
#    c=int(a/b)
    d=epsilon*random.randint(0,phi)
    return a*(0.5**d)

def distribute(a,b,theta,c):
    epsilon, phi= checkout(a,b,theta)
    d=[finite(a,epsilon, phi) for x in range(c)]
    return d

d=distribute(100,1,0.01,300)
print(d)
