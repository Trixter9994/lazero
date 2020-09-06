import networkx as nx
import random
# my fucking brain fried.
# shall we hse directed graph or error control?
# what if there is an isolated node?
def getNext(a, b):
  x=random.choice(a)
  return x,list(b.neighbors(x))
# def recursiveGet(a, b, c,d):
#   if
"""
s=nx.read_sparse6("randomFuck.s6")"""
s=nx.read_gpickle("reFuck.gpickle")
# print(s.nodes())
# print(s.edges())
p = list(s.nodes())
# is it a multigraph?
# shall we find loops?
# print(p)
# this is node.
# the total nodes
# shall we hse a directed graph?
x1 = ""
# man this sucks.
for x in range(100):
  # print(p)
  x0, p = getNext(p, s)
  x1+=x0
  # print(p,x0)
# print(p)
print(x1)
# mother fucker what the fuck is this?
# p1=random.choice()
# for p0 in p:
#   p1 = list(s.neighbors(p0))
# you will never know fuck.
# how to use that shit?
  # print(p0,p1)
  # randomly select successors.