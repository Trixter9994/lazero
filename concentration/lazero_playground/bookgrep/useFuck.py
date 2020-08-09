import networkx as nx
# import random
# shall we hse directed graph or error control?
# what if there is an isolated node?
# man this fucking sucks.
def getNext(a, b):
  x=random.choice(a)
  return x,list(b.neighbors(x))
# def recursiveGet(a, b, c,d):
#   if
"""
s=nx.read_sparse6("randomFuck.s6")"""
s = nx.read_gpickle("randomFuck.gpickle")
# graph theory will save our fucking ass.
# print(s.nodes())
# print(s.edges())
# p = s.edges()
# how about let's get directed graph?
# play around with this shit. Never expect anything fucking useful.
# May use multigraph?
# print(type(p))
# this is node.
# the total nodes.
# p1=random.choice()
# man what the fuck is this?
# get edges?
# this will not work.
# for p0 in p:
#   print(p0)
  # randomly select successors.
# graph theory is exhausitive and unpredictable.