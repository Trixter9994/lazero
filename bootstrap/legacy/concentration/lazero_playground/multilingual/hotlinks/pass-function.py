# very fucking important while using python3
from functools import reduce
def hello():
    print ("hello")
    return 1

def k(m):
    s=m()
    print(s)

k(hello)
# this is as easy as fuck.
s=list(map((lambda x:x**2),[2]))
print (s)
se=[1,2,3]
sm=list(map((lambda x:x**2),se))
print (sm)
sd=list(map((lambda v,vo:v*vo+hello()),se,sm))*3
# this is adding combining multiple copies of the same list as one
# you had better pass lambda to filter and map?
# i saw map in process before.
#sd=list(filter(hello,se))
print(sd)
# return true and that item survives
# filter out those false things
sd=list(map((lambda v,v0,v1:v*v0*v1),se,sm,sd))
print(sd)
vk=reduce(lambda x,y:x+y,sd)
print(vk)
# i don't know how to accomplish this.
vm=reduce(lambda x,y:x if x>y else y,sd)
print(vm)
skr=lambda d,f:d*f
print(skr(3,4))
# lambda can only have one expression
# when the list is called, the lambda function will be evaluated.
# what if we do not pass lambda to it?
