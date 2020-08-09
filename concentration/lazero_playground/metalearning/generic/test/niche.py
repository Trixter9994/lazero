import numpy as np

def Method2(a, b):
    group1, group2= np.meshgrid([*a],[*b])
    print(group1)
    print(group2)
    return group1 == group2

v=Method2("group","groupChar")
print(type(v))
#print(v and v)
