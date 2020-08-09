import talib, numpy
def wrap(_list):
    close = numpy.array(list(map((lambda x : float(x)),_list)))
    return close
def sexy(k):
    if len(k)>3:
        vm=wrap(k)
        print("--talib--")
        print(list(talib.HT_DCPERIOD(vm)))
        print(list(talib.HT_DCPHASE(vm)))
        print(list(talib.HT_PHASOR(vm)))
        print(list(talib.HT_SINE(vm)))
        print(list(talib.HT_TRENDMODE(vm)))
        print("--talib--")
    else:
        pass

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

for r,k in enumerate(list(mississippi)):
    if k in hotspot:
#        print (r,k)
        # and append the shit.
        # consider some linear algorithm?
        # you want to use finance method to do this task? perfect. MACD, PSY, KDJ and more.
        #starts from zero.
        nothing[hotspot.index(k)].append(r)

    # the r is the index.

# to illustrate this:
vim=[]
for k in range(len(nothing)):
    anything=[]
    if nothing[k][-1]!=(len(mississippi)-1):
        nothing[k].append(len(mississippi)-1)
    if nothing[k][0]!=0:
        nothing[k].insert(0,0)
    for m in range(len(nothing[k])-1):
        anything.append(nothing[k][m+1]-nothing[k][m])
    vim.append(anything)

derivative=(lambda k0: [(k0[m+1]-k0[m]) for m in range(len(k0)-1)])

for r,k in enumerate(vim):
    print("---the original---")
    print(r,k)
#    print("--spliter--")
    geek0=derivative(k)
    print("--spliter--")
    print(geek0)
    sexy(geek0)
    print("--spliter--")
    geek=derivative(geek0)
#    print(nothing[r])
    print(geek)
    sexy(geek)

