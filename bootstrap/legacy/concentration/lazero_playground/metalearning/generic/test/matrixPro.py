def Linkage(a):
    b,c=len(a),len(a[0])
    # be the first. extract identity matrix and its length.
    # repetation can be visualized as multiple identity matrices mixed together.
    # add tolerance for omition
    # you can switch the major direction.
    # -l, l-1 avaliable.
    return [a[f][f%c:c]+a[f][-c:-c+f%c] for f in range(b)]

def ReverseLink(a):
    b,c=len(a),len(a[0])
    return [a[f][(-f)%c:c]+a[f][-c:-c+(-f)%c] for f in range(b)]
            # begin the matrix transformation.
