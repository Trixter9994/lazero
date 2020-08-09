from getFromPickleR import returnListR
import copy

def processor(a, b):
  for b0 in b:
    if a in b0:
      if a == b0[0]:
        return b0, 1
      else:
        return b0, -1
  return None

def globalCounter(a, b):
  fl=range(len(a))
  b0 = {x: 0 for x in b}
  b1=[]
  for lf in fl:
    af = processor(a[lf], b)
    if af != None:
      b0[af[0]] += af[1]
    bs=copy.copy(b0)
    b1.append(bs)
  return b1

def globalSpliter(a, b):
  g, g0, g1, g2, g3 = globalCounter(a, b), [], "", None, range(len(a))
  b0 = [x for y in b for x in y]
  # print(b0)
  for a0 in g3:
    if g2 == None or g2 == g[a0]:
      if a[a0] not in b0:
        g1 += a[a0]
      if g2 == None:
        g2 = g[a0]
    else:
      fx = None
      g0.append([g2, g1])
      if a[a0] not in b0:
        g1 = a[a0]
      else:
        g1=""
      g2=g[a0]
  if g1 != "":
    g0.append([g2,g1])
  # g0[0]=wrapper(g0[0],True)
  # g0[1]=wrapper(g0[1],False)
  return g0

def checkMate(dest):
  r = returnListR()
  r0 = [y for z in [r[x] for x in r.keys()] for y in z]
  # dest = "hello everyone(where is the syntax tree(get words out))"  # detect the level of things.
  g = globalSpliter(dest, r0)
  return g