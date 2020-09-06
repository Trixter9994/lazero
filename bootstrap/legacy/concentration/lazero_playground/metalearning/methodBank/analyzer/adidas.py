#from returnSameVar import retrieve_name

def schema(name,*args):
    # b is a lambda.
    # a[1] IS A TUPLE.
    print("--Function "+name+"--")
    print(args)
    print([type(a0) for a0 in args])
    # what if object doesn't match?
    # pass global and local params!

def scheme(a,b):
    # b is a lambda.
    # a[1] IS A TUPLE.
    print("--Function "+str(a[0])+"--")
    print(a[1])
    print([type(a0) for a0 in a[1]])
    # what if object doesn't match?
    # pass global and local params!
    return b(*a[1])

def chaos(sb,sc):
    return scheme([sb[0],sc],sb[1])

"""superLamb=(lambda x,y: x+y)

print(chaos(["superLamb",superLamb],(1,2)))"""
