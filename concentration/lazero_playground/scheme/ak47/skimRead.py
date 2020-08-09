def sk(a,t):
    a0 = len(a)
    a1 = [a[t0: t0 + t] for t0 in range(a0 - t)]
    return a1
    # is this real?