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
        nothing[hotspot.index(k)].append(r)

    # the r is the index.

# to illustrate this:
for r,k in enumerate(nothing):
    print(r,k)
