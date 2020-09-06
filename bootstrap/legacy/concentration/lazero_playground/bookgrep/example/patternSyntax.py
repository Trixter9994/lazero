from getFromPickleR import returnList
import unicode_charnames as uc
import uniprop as up
import hashlib
from simpleStorageR import storeListR

def hash(a):
  b = []
  for b0 in a:
    if b0 not in b:
      b.append(b0)
  return b

def hashString(a):
    return sum([ord(x) for x in a])**(1/(len(a)+0.1))
# no fucking division by zero!
def sorter(a):
    # not avaliable for every unicode char.
    # hashFunc collision
    f=(len(list(set(list(map(hashString,a)))))== len(a))
    if f:
        return tuple(sorted(a,key=hashString))
    else:
        # no double check?
        return tuple(sorted(a,key=lambda x:int("0x"+hashlib.sha1(x.encode("utf-8")).hexdigest(),0)))

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
  l,l0=len(a0),len(b0)
  if l==l0:
    for x in range(l):
      if a0[x]!=b0[x]:
        return [a0[x],b0[x]]
    else:
      return None
  else:
    return None

r = returnList()
# r4=[[x,r[x]] for x in r.keys()]
# a dictionary
rf=[[x, r[x][0]]for x in r.keys() if len(r[x]) == 1]
r0 = [pairFinder(*list(map(uc.charname, x))) for x in rf]
r0 = list(map(sorter, r0))
r1 = hash(r0)
# r1={x:r0.count(x) for x in hash(r0)}
# print(r1)
r2 = list(reversed(sorted(r1, key=lambda x:r0.count(x))))[:2]
# print(r2)
r3 = {x: hash(list(map(sorter,[rf[index] for index, content in enumerate(r0) if content == x]))) for x in r2}
print(r3)

# time to purify this.
storeListR(r3)
# so what? sort them.