import numpy as np
# strange. i even have to create some complex numbers?
n=1+10j
n0=np.sin(n)
print(n0)
n1=np.matrix([[n,n0],[n0,n]])
n2=np.cos(n1)
print(n2)
