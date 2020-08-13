# string first.
def blackwhite(a,b,c=True):
    assert type(a)==str
    assert type(b)==str
    assert type(c)==bool
    buf=""
    cb=[]
    for x in a:
        if c:
            if x in b:
                buf+=x
            elif buf!="":
                cb.append(buf)
                buf=""
        else:
            if x not in b:
                buf+=x
            elif buf!="":
                cb.append(buf)
                buf=""
    if buf!="":
        cb.append(buf)
    return cb
