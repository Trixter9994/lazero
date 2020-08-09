import numpy as np

def Linkage(a0):
  if type(a0) != list:
    a = a0.tolist()
  else:
    a = a0
  b,c=len(a),len(a[0])
  # be the first. extract identity matrix and its length.
  # repetation can be visualized as multiple identity matrices mixed together.
  # add tolerance for omition
  # you can switch the major direction.
  # -l, l-1 avaliable.
  return [a[f][f%c:c]+a[f][-c:-c+f%c] for f in range(b)]

def reform(a):
  return np.array(a).transpose(1,0).tolist()

def ReverseLink(a):
  b,c=len(a),len(a[0])
  return [a[f][(-f)%c:c]+a[f][-c:-c+(-f)%c] for f in range(b)]
          # begin the matrix transformation.

def binGrouper(a):
  # only internal use.
  g0,g1,g2=[],0,-1
  for a0 in range(len(a)):
    if g2 == -1 or g2 == a[a0]:
      g1 += 1
      if g2 == -1:
        g2 = a[a0]
    else:
      g0.append([g2,g1])
      g1 = 1
      g2=a[a0]
  if g1 != 0:
    # if not checkMe(g1):
    g0.append([g2,g1])
  # g0[0]=wrapper(g0[0],True)
  # g0[1]=wrapper(g0[1],False)
  return g0

def mapper(a, b):
  return [a,a+b]

def transcriber(a):
  f, f1, f2 = binGrouper(a), [], 0
  for f0 in f:
    fx=f0[1]
    f1.append([f0[0], mapper(f2, fx)])
    f2 += fx
  return f1

def bashBunny(a):
  return [transcriber(x) for x in a]