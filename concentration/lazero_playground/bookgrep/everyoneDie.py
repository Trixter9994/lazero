from getFromPickleR import returnFuckMe, returnWTF
from simpleStorageR import storeFuckYou
import random
r,r1=returnFuckMe(),returnWTF()
def halfOut(a,b,c):
  x,y=len(a),len(b)
  a0,a1=[int(a[z] in c) for z in range(x)],[int(b[z] in c) for z in range(y)]
  return sum(a0)*sum(a1)>=(1/8)
# shall we do it again?
# how the fuck can we group these things?
# man this is crazy.
def crazy(r,r1):
  rx,rz=[],[]
  for x in range(100):
    r0=random.choice(r)
    # print(r0)
    # rz=[]
    for y in range(100):
      rk=random.choice(r1)
      if halfOut(*r0,random.choice(rk)):
        # print(rk)
        rz.append(rk)
    if rz!=[]:
      rx.append(rz)
      rz=[]
  return rx
  # print("_____THESE ARE SHITS_____")
  # get category from multiple variables.
  # do they have the same shit?
  # how to build the fuck?
  # common pattern getter.
  # how the fuck can we use networks?
  # excuse me how do we get shits from these?
cxk=[]
for x in range(100):
#  print(">>>TAKING HEAD ANIME<<<")
  c=crazy(r,r1) # why the same?
  #print(c)
  # maybe the print function helps out?
  cxk.append(c)
storeFuckYou(cxk)
#  for z in c:
#    print(z)
#    print("_____THESE ARE SHITS_____")
  # you will never know shit.