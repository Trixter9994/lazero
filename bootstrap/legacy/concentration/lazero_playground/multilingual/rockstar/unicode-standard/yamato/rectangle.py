def returnFuck(a,b):
    x,y,h,w=b
    b0=[]
    # b -> [x,y,h,w]
    # if width not satisfied, then return the longest shit.
    for x0 in range(h):
        try:
            x1=a[x0+x]
            l=len(x1)
            if y+w<=l:
                b0.append(x1[y:y+w])
            elif y<l:
                b0.append(x1[y:])
            else:
                b0.append("")
        except:
            b0.append(None) # it has to exist first.
    return b0
# fuck you!
# how to get that dynamic spliter?