def scheme(a,b):
    # b is a lambda.
    # a[1] IS A TUPLE.
    print("--Function "+a[0]+"--")
    print([type(a0) for a0 in eval(a[1])])
    return eval("b"+a[1])

superLamb=(lambda x,y: x+y)
shit=1,2
# this expands the tuple
print(superLamb(*shit))
#print(scheme(["superLamb","(1,2)"],superLamb))
