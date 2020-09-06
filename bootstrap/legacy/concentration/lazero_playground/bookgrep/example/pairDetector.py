from getFromPickleR import returnAList
from simpleStorageR import storeList
import unicode_charnames as uc
# get all words.

def getBatch(a):
  return [uc.charname(x) for x in a]

def checker(a):
  if "LATIN" in a and "LETTER" in a:
    return True
  else:
    return False

def grouper(a):
  g,g0,g1,g2=list(map(checker,getBatch(a))),[],"",None
  for a0 in range(len(a)):
    if g2 == None or g2 == g[a0]:
      g1 += a[a0]
      if g2 == None:
        g2 = g[a0]
    else:
      fx = None
      g0.append([g2,g1])
      g1=a[a0]
      g2=g[a0]
  if g1 != "":
    g0.append([g2,g1])
  # g0[0]=wrapper(g0[0],True)
  # g0[1]=wrapper(g0[1],False)
  return g0

def pairFinder(a,b):
  # nope. remove these things.
  fi=lambda x: list(map(lambda z:z[1],list(filter(lambda y: y[0],grouper(x)))))
  a0,b0=fi(a),fi(b)
  # print(a0,b0)
  l,l0,l1=len(a0),len(b0),0
  if l==l0:
    for x in range(l):
      if a0[x]!=b0[x]:
        l1+=1
    if l1==1:
      return True
    else:
      return False
  else:
    return False
r=returnAList()["control"]
# sequential finder. -1
r0=getBatch(r)
# print(r0)
# have name directly.
r1={x:[y for y in r if pairFinder(r0[r.index(x)],r0[r.index(y)])] for x in r}
storeList(r1)
print(r1)