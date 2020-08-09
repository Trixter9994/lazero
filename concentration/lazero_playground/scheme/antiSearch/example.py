# use graph? tell apart what is the known thing inside the char, what is unknown.
# for example: how old are you? the old is unknown. other things are known.
# understand natural language operands?
# have word -> do not store -> look neighbors
# not have word -> store -> look neighbors.
# replace current graph (approach it) using regex
# two mode: single mode or chain mode.
# chain mode needs to follow the pattern.
# single mode only check existance.
# what exactly do you learn? tell me.
from buildAGraph import Graph
import traceback

G=Graph(None,"simple_graph")
while True:
    i=input("Which mode? S/C/E: Single, Chain, Exit\n")
    try:
        assert type(i)==str and i in ["S","C","E"]
        if i == "S":
            i=input("type the text you want to query:\n")
            e=G.getNode(i)
            if e:
                print("have this node!")
            else:
                print("not have this node! inserting!")
                G.addNode(i)
        elif i == "C":
            i0=input("type first text you want to query:\n")
            i0=(i0,input("type second text you want to query:\n"))
            e=G.getEdge(i0)
            if e:
                print("have this edge!")
            else:
                print("not have this edge! inserting!")
                G.addEdge(i0)
        else:
            print("exiting!")
            break
    except:
        print("Wrong choice!")
        e0 = traceback.format_exc()
        print(e0)
        continue
G.save_graph("simple_graph")
print("graph saved!")