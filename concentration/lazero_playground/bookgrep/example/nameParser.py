import unicode_charnames as uc

def getBatch(a):
  return [uc.charname(x) for x in a]

def checkMe(a):
  if len(a)>6:
    if len(list(set(a)))==1:
      return True
  return False

def checker(a):
  if "DIGIT" in a or "LATIN" in a:
    return 1
  else:
    return 0

# def wrapper(a,b):
#   # j=lambda x: [z for y in x for z in y]
#   if b==True:
#     return list(jieba.cut(a))
#   else:
#     return wj.split(a)

def grouper(a):
  g,g0,g1,g2=list(map(checker,getBatch(a))),[],"",None
  for a0 in range(len(a)):
    if g2 == None or g2 == g[a0]:
      g1 += a[a0]
      if g2 == None:
        g2 = g[a0]
    else:
      fx = None
      if g2 == 1:
        # if g2==0:
        #   fx=wrapper(g1,True)
        # elif g2==1:
        #   fx = wrapper(g1, False)
        # for xf in fx:
        if not checkMe(g1):
          g0.append([g2,g1.replace("\b\n","").replace("\n","")])
      g1=a[a0]
      g2=g[a0]
  if g1 != "":
    if g2 == 1:
      if not checkMe(g1):
        g0.append([g2,g1.replace("\b\n","").replace("\n","")])
  # g0[0]=wrapper(g0[0],True)
  # g0[1]=wrapper(g0[1],False)
  return g0

def getX(a):
  return list(map(lambda x: x[1], grouper(a)))[1:-1]

def getAll(a):
  return list(map(lambda x: x[1], grouper(a)))