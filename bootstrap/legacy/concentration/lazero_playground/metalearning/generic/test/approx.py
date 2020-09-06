log=[2.71828,0.71828]
def approx(a):
    a0=(lambda x:(float)(1+1/x)**x)
    return (log[1]-abs(a0(a)-log[0]))/log[1]
