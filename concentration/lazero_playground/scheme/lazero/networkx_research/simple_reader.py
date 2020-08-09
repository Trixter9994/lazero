# must start with some sentence.
# get the init number?
# add one simple node as standalone mark.
from buildAGraph import Graph
# hashtagger?
with open("networkx_reference.txt", "r") as f:
    h = f.read().split("\n")
G = Graph(None, "networkx_readings")
mark = G.getMark("bookmark-7429x")
# it is my work, my hard work.
# sort of.
if mark is None:
    mark = 0
# if receive the signal, we will save.
# char: ENDGAME_SAVE
b = None
while True:
    try:
        m = h[mark]
        print(m)
        p = input(">>>write comment here. type '__EDSA__' to save.<<<\n")
        if b != None:
            G.addEdge((("sentence", b), ("sentence", m)))
        if p == "__EDSA__":
            break
        if p!="\n":
            G.addEdge((("sentence", m), ("comment", p)))
        b = m
        mark += 1
    except:
        print(">>>end of work.<<<")
        break
G.addMark("bookmark-7429x", mark)
G.save_graph("networkx_readings")
print(">>>graph saved. program will exit.<<<")
# try to check the graph?
# you really have to read it line by line?
# make it roar!
# what about next?