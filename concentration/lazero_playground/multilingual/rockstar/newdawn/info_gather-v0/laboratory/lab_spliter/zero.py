hotpot={}
with open("README","r") as fortnight:
    hotpot=set(fortnight.read())
print(hotpot)
# use ascii values!
# this is one of our main purpose here!
# i may vomit.
# fuck me! just get the fucking research out!
# not inside those common patterns.
hotspot=list(filter((lambda x:not ((ord(x)>=97 and ord(x)<=122 )or (ord(x)>=65 and ord(x)<=90)) ),hotpot ) )
# derandom
print(hotspot)
# you can also consider the lone-wolf filter.
# filter out those things that shall always appear in a group.
# this can be achieved by adding some attributes to each letter.
# LOCAL! LOCAL! LOCAL!
