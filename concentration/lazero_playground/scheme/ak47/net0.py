import networkx as nx


g0='''def g0(x): return x*10'''


g1='''def g1(x, y): return x + y'''

# oh shit?
# cannot be lambda?
# who knows?
# dump and draw it?
G = nx.Graph()
G.add_edge(g0, g1)
nx.write_gpickle(G, "text_regressor0\\random.gpickle")
# shall we do it in a separate directory?
# cannot pickle function?
