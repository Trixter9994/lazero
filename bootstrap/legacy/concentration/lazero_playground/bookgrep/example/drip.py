from pureTest import grouper
from wrap import checkMate
from getFromPickleR import returnFuck
import csv
def transformer(a):
  b = list(map(chr, list(range(ord("a"), ord("z")+1))))
  b0,b1= list(a.keys()),"normal"
  for x in range(len(b0)):
    fx=a[b0[x]]
    if fx != 0:
      if fx >0:
          b1 += ("-" + b[x] + str(fx))
      else:
          b1 += ("-" + b[x] + "N" + str(-1 * fx))
  return b1
def writer(a, b, c):
  with open(c + "\\" + a + ".csv ", "a+", newline="") as f:
    # for d in b:
    #   f.write(d+"\n")
    c = csv.writer(f)
    for d in b:
      c.writerow(d)
    # f.write("\b")
txt = open("santi.txt", encoding="utf-8").read().split("\n")
for t in txt:
  t0=grouper(t)
  t1 = checkMate(t0)
  for t2 in t1:
    t3, t4 = t2[0], list(map(lambda x: [str(x[0]),x[1]], t2[1]))
    writer(transformer(t3), t4, "santi")
  # print(t1)