# oh shit what the fuck is this shit?
# i need to parse the new shit right now!
import networkx as nx
from itertools import tee
# I have found vulnarbilities in Baidu!
# one can only bookmark the page to get the real fucking link!
# import matplotlib.pyplot as plt
# have weighted graph but never fucking mind.
def pairwise(_iterable):
  "s -> (s0,s1), (s1,s2), (s2, s3), ..."
  a, b = tee(_iterable)
  next(b, None)
  return zip(a, b)
# def fuckMe(a):
#   return [x for x in pairwise(a)]
def getShit(a):
  with open(a, "r") as f:
    return f.read()
def shatter(a):
  return [x for x in a]
def getFucked(a, b):
  for x, y in pairwise(a):
    b.add_edge(x, y)
  return b
G = nx.MultiDiGraph() # just fuck.
s = getShit("example\\0.log")
s0 = shatter(s)
s1 = getFucked(s0, G)
# this is real shit.
# ['write_adjlist', 'write_edgelist', 'write_gexf', 'write_gml', 'write_gpickle', 'write_graph6', 'write_graphml', 'write_graphml_lxml', 'write_graphml_xml', 'write_multiline_adjlist', 'write_pajek', 'write_shp', 'write_sparse6', 'write_weighted_edgelist', 'write_yaml']
nx.write_gpickle(s1, "neverVomit.gpickle")
# nx.write_shp(s1, "randomFuck.shp")
# what the fuck is this?
# nx.draw(s1)
# plt.show()
# # fucking awesome!
# print("Nodes of graph: ")
# print(s1.nodes())
# print("Edges of graph: ")
# print(s1.edges())
# you had better use random package to determine the thing.
# store this graph somehow.
# I hate this fucking world.
# predefined rules all over my fucking head.