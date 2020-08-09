import talib, numpy
def wrap(_list):
    close = numpy.array(list(map((lambda x : float(x)),_list)))
    return close
hotpot={}
mississippi=""
with open("README","r") as fortnight:
    mississippi=fortnight.read()
    hotpot=set(mississippi)
print(hotpot)
# use ascii values!
# this is one of our main purpose here!
# i may vomit.
# fuck me! just get the fucking research out!
# not inside those common patterns.
hotspot=list(filter((lambda x:not ((ord(x)>=97 and ord(x)<=122 )or (ord(x)>=65 and ord(x)<=90)) ),hotpot ) )
# derandom
print(hotspot)
# you didn't add numbers to it.
# i need my spliter!
# you can also consider the lone-wolf filter.
# filter out those things that shall always appear in a group.
# this can be achieved by adding some attributes to each letter.
# LOCAL! LOCAL! LOCAL!

# the second step is to get the basic information: linear index.
# create the thing?
#nothing=list(enumerate(hotspot))
# you must be a list.
#print(nothing)
nothing=[]
for k in range(len(hotspot)):
    nothing.append([])

superagent=list(mississippi)
for k in range(len(nothing)):
    nothing[k]=list(map((lambda x: int(x == hotspot[k])),superagent))
# the r is the index.

# to illustrate this:
nothing0=[]
for r,k in enumerate(nothing):
    print(r,k)
    print("-----[",r,"]-----")
    vm=wrap(k)
    # you could use hex representation.
    # also the prime multiply notation.
    sob=talib.SUM(vm,timeperiod=30)
    print(sob)
    nothing0.append(sob)
    print(list(talib.MINMAXINDEX(vm, timeperiod=30)))
    print(list(talib.MINMAX(vm, timeperiod=30)))
print("--finalshow--")
nothing2=[]
for tape in range(len(nothing0)-1):
    nude=talib.MULT(nothing0[tape],nothing0[tape+1])
    nothing2.append(nude)
    print(list(nude))
    print("--blitz--")
for cake in range(len(nothing2)-1):
    nuke=talib.SUB(nothing2[cake],nothing2[cake+1])
    print(list(nuke))
    print("--freak--")
