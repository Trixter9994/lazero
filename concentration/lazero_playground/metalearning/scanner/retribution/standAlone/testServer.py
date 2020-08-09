def groupMe(a,b):
    # this is linear version of the game. -> recursive grouping -> recursive sorting?
    # b is the lambda function which can determine each fucking shit.
    r=[[],[]]
    for x in a:
        r[int(not b(x))].append(x)
    if len(r[0])>0 and len(r[1])>0:
        return r
    else:
        return a

d=[1,2,3,4,5,6,7]
d0=groupMe(d,(lambda x: x<4))
print(d0)