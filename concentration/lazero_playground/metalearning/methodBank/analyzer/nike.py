from returnSameVar import retrieve_name
def scheme(a,b):
    # b is a lambda.
    # a[1] IS A TUPLE.
    print("--Function "+str(a[0])+"--")
    print([type(a0) for a0 in a[1]])
    # what if object doesn't match?
    # pass global and local params!
    return b(*a[1])

def chaos(sb):
    return scheme([retrieve_name(sb),(1,2)],sb)

superLamb=(lambda x,y: x+y)

print(chaos(superLamb))
