import networkx as nx
# import pickle
from simpleStorageR import storeAList
# import random
# shall we hse directed graph or error control?
# what if there is an isolated node?
# man this fucking sucks.
# how about check it in directed graph?
# or regraph the whole thing?
# what the fuck are you thinking?
def getNext(a, b):
  x=random.choice(a)
  return x,list(b.neighbors(x))
# def recursiveGet(a, b, c,d):
#   if
"""
s=nx.read_sparse6("randomFuck.s6")"""
s=nx.read_gpickle("randomFuck.gpickle")
# print(s.nodes())
# print(s.edges())
p, p1 = list(s.nodes()),[]
# print(type(p))
# this is node.
# the total nodes.
# p1=random.choice()
# man what the fuck is this?
# get edges?
for p0 in p:
  p2 = list(s.neighbors(p0))
  p1.append([p0, p2])
p1 = list(sorted(p1, key=(lambda x: - len(x[1]))))
storeAList(p1)
# for x in p1:
#   print("________________________________________________________________")
#   print(x)
#   # randomly select successors.