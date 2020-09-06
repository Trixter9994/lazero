import networkx as nx
from simpleStorageR import storeList
# man graph theory sucks.
G = nx.read_gpickle("randomFuck.gpickle")
g = list(nx.cycle_basis(G))
storeList(g) # not fucking cycles.
# mother fucker.
# again. for another shit.
# how the fuck can we use this shit?
# for g0 in g:
#   print(g0)
# what is this loop?
# g=nx.all_simple_paths(G,source="，",target="，")
# print(g)
# this is not simple path.