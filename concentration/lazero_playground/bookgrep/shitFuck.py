import networkx as nx
from simpleStorageR import storeListR
# man graph theory sucks.
G = nx.read_gpickle("randomVomit.gpickle")
g = list(nx.simple_cycles(G)) # fuck this is too damn fucking long.
# maybe more fucking rigid?
# won't work.
storeListR(g)
# this will not work. try it in server.
# what the fuck is going on?
# mother fucker.
# again. for another shit.
# how the fuck can we use this shit?
# for g0 in g:
#   print(g0)
# what is this loop?
# g=nx.all_simple_paths(G,source="，",target="，")
# print(g)
# this is not simple path.
"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""