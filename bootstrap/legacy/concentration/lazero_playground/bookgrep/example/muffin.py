from getFromPickleR import returnFuck, returnFuckMe,returnListR
import unicode_charnames as uc
from getter import pairFinder
from simpleStorageR import storeListR

def hash(a):
  b = []
  for b0 in a:
    if b0 not in b:
      b.append(b0)
  return b

def setter(a):
  for b in a:
    b0,b1=uc.charname(b),0.001
    b2=len(a)+b1*2
    if "CJK" not in b0 and "LETTER" not in b0:
      b1+=1
    return (b1/b2)>0.8

def minimal(a):
  return min(a)/max(a)

def funcHot(a):
  r0=[]
  for r in range(len(a)-1):
    fx=[a[r][0],a[r+1][0]]
    if list(map(len,fx))==[1,1]:
      if pairFinder(*fx) and minimal([a[r][1],a[r+1][1]]):
        r0.append(fx)
  return r0

def alcSort(a):
  return list(map(lambda a0:list(sorted(a0,key=ord)),a))

def alt(a):
  b1=[0,0]
  for b in a:
    b0=uc.charname(b)
    if "LEFT" in b0:
      b1[0]=1
    elif "RIGHT" in b0:
      b1[1]=1
    else:
      pass
  return b1==[1,1]

r,r0=returnFuck(),returnFuckMe()
k=lambda x: [y for z in x for y in z]
r1,r2=k([r[x] for x in r.keys()]),k([r0[x] for x in r0.keys()])
k0=lambda x: list(filter(lambda y:setter(y[0]),x))
r3,r4=k0(r1),k0(r2)
r5,r6=funcHot(r3),funcHot(r4)
# print(r5,r6)
r7,r8=alcSort(r5),alcSort(r6)
r9,r10=list(filter(alt,r7)),list(filter(alt,r8))
# print(r9,r10)
r11=returnListR()
rkn=hash(r11[("RIGHT","LEFT")]+list(map(tuple,r9+r10)))
r11[("RIGHT","LEFT")]=rkn
print(r11)
storeListR(r11)