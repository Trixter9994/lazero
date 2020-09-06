import difflib
def intake(x,y):
    # return a function.
    # True for a -> b, False for b -> a.
    # how to get commons?
    d=lambda a,b:difflib.Differ().compare(a,b)
    return lambda a: d(x,y) if a else d(y,x)
# ready for more?
# predefined types.
# make sure there is only one. either prefix or suffix. never other things.
# [whatever] -> [whatever]+[something]
def genetic(a):
  if a == " ":
    return None
  else:
    return a == "+"

def parser(a):
  return [(genetic(x[0]), x[2:]) for x in a]

def grouper(a):
  g0,g1,g2=[],"",-1
  for a0 in range(len(a)):
    if g2 == -1 or g2 == a[a0][0]:
      g1 += a[a0][1]
      if g2 == -1:
        g2 = a[a0][0]
    else:
      g0.append([g2,g1])
      g1=a[a0][1]
      g2=a[a0][0]
  if g1 != "":
    # if not checkMe(g1):
    g0.append([g2,g1])
  # g0[0]=wrapper(g0[0],True)
  # g0[1]=wrapper(g0[1],False)
  return g0

def retribution(a, b, c=True):
  i = intake(a, b)
  k = list(i(c))
  j = grouper(parser(k))
  return j
  # None and False items are arglist.
  # ask for arg num?
  # ask for the function?
  # ask for example of input?
def proquo(a, b):
  b0,b1 = 0,""
  for x in b:
    if x[0] in [None, False]:
      x0 = len(x[1])
      a1 = a[b0:x0]
      assert a1 == x[1]
      if x[0] == None:
        b1 += a1
      b0 += x0
    else:
      b1 += x[1]
  return b1

def metapro(a, b):
  b0, b1 = [x for x in b if x[0] in [None, False]], ""
  if len(b0) == len(a):
    for x in b:
      if x[0] in [None, False]:
        if x[0] == None:
          b1 += a.pop(0)
        else:
          a.pop(0)
      else:
        b1 += x[1]
    return b1
  else:
    return None
    
def metaproII(a, b):
  b0, b1 = [x for x in b if x[0] in [True]], ""
  if len(b0) == len(a):
    for x in b:
      if x[0]==True:
          b1 += a.pop(0)
        # else:
        #   a.pop(0)
      elif x[0]==None:
        b1 += x[1]
      else:
        pass
    return b1
  else:
    return None
