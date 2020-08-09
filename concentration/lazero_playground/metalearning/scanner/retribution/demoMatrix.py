from matrixPro import prep
import numpy
n=numpy.array([[1,0],[0,1]])
# detect the start column and length.
"""s=Linkage(n)
print(s)
r=numpy.array(s).transpose((1,0))
print(r)"""
s=prep(n,0)
print(s)
"""for a in s:
    print(a)
    print(a[1:1])"""
#    for s0 in a:
#        print(s0)