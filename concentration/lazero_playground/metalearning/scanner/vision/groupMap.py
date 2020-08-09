from itertools import combinations as combination
import numpy as np
import random
import copy
import math

def cluster(a, b):
  if a >= b:
    return (a + 0.1) / (b + 0.1)
  else:
    return cluster(b, a)

def checker(a, b):
  c = cluster(a, b)
  # print(c)
  return c < 10

def mapGroup(a):
  # print(a)
  m = list(a.keys())
  m0 = combination(m, 2)
  # print(m0)
  m1 = {x: checker(a[x[0]],a[x[1]]) for x in m0}
  return m1

def mapCluster(a):
  m,m0= mapGroup(a),[]
  for x in m.keys():
    if m[x]:
      if m0 == []:
        m0.append(list(x))
      else:
        for y in range(len(m0)):
          for z in x:
            if z in m0[y]:
              m0[y] = list(set(m0[y] + list(x)))
              break
  return m0

def coorGet(a):
  # print(a)
  return np.array(a).transpose(1, 0)

def calcDis(a,b):
  return np.linalg.norm(a - b, ord=np.inf)

def calcMulti(a, b, c=3):
  # segmentation -> 3
  return [x for x in b if x is not a and calcDis(a, x)<c]
# better use replacement -> generate number around it.
def checkContinual(a):
  b, e = copy.copy(a), []
  f = lambda x: [y for z in x for y in z]
  while b != []:
    c = random.choice(b)
    # print(c)
    d = calcMulti(c, b)
    # print(d)
    e.append([c] + d)
    f0 = f(e)
    # print(f0)
    b = [x for x in b if not (x == f0).any()]
    # print(b)
  return e

def mapBlank(a):
  b = list(a.items())
  c = list(sorted(b, key=lambda x: x[1]))
  return list(map(lambda x: x[0], c[:-1]))

def centralDots(a):
  return [sum(x) / len(x) for x in a]

# def normal_equation(X,y):
#   a = np.dot(X.transpose(), X)
#   b = np.dot(X.transpose(), y)
#   return np.dot(np.linalg.inv(a), b)

def subLine(a,θ):
  X_new = np.array([[a[0]],[a[1]]])
  X_new_b = np.c_[np.ones((2, 1)), X_new]
  # print("xn",X_new_b)
  y = X_new_b.dot(θ)
  return [y[0][0],y[1][0]]

def getDis(pointX, pointY, lineX1, lineY1, lineX2, lineY2):
    a = lineY2 - lineY1
    b = lineX1 - lineX2
    c = lineX2 * lineY1 - lineX1 * lineY2
    dis = (math.fabs(a * pointX + b * pointY + c)) / (math.pow(a * a + b * b, 0.5))
    return dis

def getBatchDistance(a, b):
  b0 = lambda x: [z for y in x for z in y]
  b1 = b0(b)
  r = [getDis(*x, *b1) for x in a]
  # return max(r) < 7
  return r
  # use continual approach sooner or later.

def getLine(a):
  cf = lambda c0: np.array(c0).transpose(1, 0)
  c0 = centralDots(a)
  # print(c2)
  c = cf(c0)
  c1 = c[0]
  c2 = [min(c1), max(c1)]
  d = lambda x: np.array([[y] for y in x])
  X, y = d(c[0]), d(c[1])
  X_b = np.c_[np.ones((len(c0), 1)), X]
  t = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
  # t = normal_equation(X, y)
  # print(t)
  t0 = subLine(c2, t)
  return cf([c2, t0])


  # print("yp",y_predict)
# def ordLine(a):
  # c=centralDots(a)