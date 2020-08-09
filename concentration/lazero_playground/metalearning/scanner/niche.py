import numpy as np

def Method2(a, b):
    group1, group2= np.meshgrid([*a],[*b])
<<<<<<< HEAD
#    print(group1)
#    print(group2)
#    print(type(group1))
#    print(dir(group1))
    return group1 == group2

#v=Method2("group","groupChar")
#print(type(v))
#$print(v and v)
=======
    print(group1)
    print(group2)
    print(type(group1))
    print(dir(group1))
    return group1 == group2

v=Method2("group","groupChar")
print(type(v))
$print(v and v)
>>>>>>> 82f1d86cc9810194c8951262d2377a020d4e3a47
