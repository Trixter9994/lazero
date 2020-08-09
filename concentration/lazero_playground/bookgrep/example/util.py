import wordninja as wj
# import uniprop as up
import unicode_charnames as uc
import random
import jieba
import pandas as pd
import csv
# import pickle
# from simpleStorageR import storeAList
def writer(a, b):
  with open(a+".csv", "a+",newline="") as f:
    c = csv.writer(f)
    for d in b:
      c.writerow(d)
    # f.write("\b")

def getBatch(a):
  return [uc.charname(x) for x in a]

def splitMe(a):
  return a[3:].split("\\")

def randomGet(a,b):
  a0=a[:-1]
  if len(a0)>b:
    return random.sample(a0,b)+[a[-1]]
  else:
    return a

def checker(a):
  if "LATIN" in a and "LETTER" in a:
    return 1
  elif "CJK" in a:
    return 0
  else:
    return 2

def wrapper(a,b):
  # j=lambda x: [z for y in x for z in y]
  if b==True:
    return list(jieba.cut(a))
  else:
    return wj.split(a)

def grouper(a):
  g,g0,g1,g2=list(map(checker,getBatch(a))),[],"",None
  for a0 in range(len(a)):
    if g2 == None or g2 == g[a0]:
      g1 += a[a0]
      if g2 == None:
        g2 = g[a0]
    else:
      fx = None
      if g2 in [0,1]:
        if g2==0:
          fx=wrapper(g1,True)
        elif g2==1:
          fx = wrapper(g1, False)
        for xf in fx:
          g0.append([g2,xf.replace("\b\n","").replace("\n","")])
      else:
        g0.append([g2,g1.replace("\b\n","").replace("\n","")])
      g1=a[a0]
      g2=g[a0]
  if g1 != "":
    if g2 in [0,1]:
      if g2==0:
        fx=wrapper(g1,True)
      elif g2==1:
        fx = wrapper(g1, False)
      for xf in fx:
        g0.append([g2,xf.replace("\b\n","").replace("\n","")])
    else:
      g0.append([g2,g1.replace("\b\n","").replace("\n","")])
  # g0[0]=wrapper(g0[0],True)
  # g0[1]=wrapper(g0[1],False)
  return g0

p=pd.read_csv("cve.csv",usecols = ['Filename'])
# p0=list(p['Filename'])
# three level of abstraction: directorial, categorical, sequential (DCS)
# xn=[]
# for x in p0:
for index, rows in p.iterrows():
  x=rows.Filename.replace("\b\n","").replace("\n","")
    # Create list for the current ro
  # print(x)
  if type(x)==str and len(x)>3:
    w=randomGet(splitMe(x),3)
    if len(w)>1:
      w0=list(map(grouper, w))
      w1={x:[] for x in range(5)}
      w2=[[w0[x][-1][1],w0[x+1][0][1]] for x in range(len(w0)-1)]
      for y in w0:
        if len(y)>1:
          for z in range(len(y) - 1):
            if (y[z][0],y[z+1][0]) not in [(0,2),(2,0)]:
              wx = y[z][0] + y[z + 1][0]
            else:
              wx=4
            w1[wx].append([y[z][1],y[z+1][1]])
      w1.update({"directorial": w2})
      wf = w1.keys()
      for wx in wf:
        writer(str(wx) if type(wx)!=str else wx,w1[wx])
      # write in append mode.
      # xn.append(w1)
# storeAList(xn)
