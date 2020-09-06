import numpy as np

def Method2(a, b):
    group1, group2= np.meshgrid([*a],[*b])
    return group1 == group2

def Method0(a,b):
    # fuck you bitch get me here. you fucking bitch ass fucker cocksucker.
    return [[a0==b0 for a0 in a] for b0 in b]