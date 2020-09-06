import re
# maybe we shouldn't go further than __a__ funcs
# use globals() locals() dictionaries.
# no kwargs.
def parseDir(objectName,gloss):
    return list(map((lambda x: objectName+"."+x),eval("dir({})".format(objectName),gloss)))

def parseType(objectList,gloss):
    return list(map((lambda x: eval("type({})".format(x),gloss).__name__), objectList))

def recurDir(objectStruct,former,gloss):
    joke=[list(filter((lambda x:len(re.findall(r'__.+__',x.split('.')[-1]))==0),obj)) for obj in objectStruct]
#    print(joke)
    if sum([len(joker) for joker in joke])==0:
        return (objectStruct+former)
    else:
        a=[]
        for obj in joke:
            for obj0 in obj:
                a.append(parseDir(obj0,gloss))
        return recurDir(a,former+objectStruct,gloss)

def depthType(ls,gloss):
    return list(map((lambda x: parseType(x,gloss)), ls))

def monad(m,gloss):
    ml=recurDir([parseDir(m,gloss)],[],gloss)
#    print(ml)
    return (ml,depthType(ml,gloss))
# That was intense.
