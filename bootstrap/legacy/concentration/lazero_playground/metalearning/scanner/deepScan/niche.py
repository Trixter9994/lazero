import numpy as np

def Method2(a, b):
    group1, group2= np.meshgrid([*a],[*b])
    return group1 == group2
