import networkx as nx
import matplotlib.pyplot as plt
# G = nx.Graph()
# G.add_node("a")
# G.add_nodes_from(["b","c"])
G=nx.path_graph(4)
# G.add_edge(1,2) # not about "a" and "c"
# edge = ("d", "e")
# G.add_edge(*edge)
# edge = ("a", "b") # it concerns about the name.
# G.add_edge(*edge)
# G.add_node("a")
# # a list of nodes:
# G.add_nodes_from(["b","c"])
# cities = {0:"Toronto",1:"London",2:"Berlin",3:"New York"}
H = nx.Graph()
# H.add_nodes_from(G) # only arbitrary nodes. no edges.
H.add_edges_from(G.edges())
G.clear()
# H.add_node(G) # hypernode!
# None shall never be used as nodes.
# H=nx.relabel_nodes(G,cities)
nx.draw(H)
plt.show() # this is useless.
print("Nodes of graph: ")
print(H.adj)
print("Edges of graph: ")
print(H.degree)# are they lists?
# print(G.nodes())
# print(G.edges())

# print(type(G.nodes()))
# print(type(G.edges()))