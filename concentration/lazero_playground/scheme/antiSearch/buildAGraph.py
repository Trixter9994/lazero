# the code is not certain.
# what is valid?
import networkx as nx
# from getFromPickleR import returnFuckMe, returnWTF
# how to insert things? just how?
# f2048 = [x for y in returnFuckMe() for x in y]
# find the size
# i still have something!
# GraphMLReader?
class Graph:
    def __init__(self, graph=None, load=None):
        if graph is None:
            if load is None:
                self.G = nx.Graph()
            else:
                try:
                    self.G = nx.read_gpickle(load+".gpickle" if ".gpickle" != load[-len(".gpickle"):] else load)
                except:
                    self.G = nx.Graph()
                    # first time.
                    # nx.write_gpickle(self.G,load)
        else:
            self.G = graph

    def addMark(self,a,rl):
        self.G.add_node(a,readline=rl)

    def getNode(self,a):
        return a in self.G.nodes()

    def addNode(self,a):
        self.G.add_node(a)

    def getMark(self,a):
        try:
            return [x for x in self.G.nodes(data=True) if x[0]==a][0][1]['readline']
        except:
            return
# just blindly read on and record? no other stuff?
# we can pass it to another class. calm down.
    def getEdge(self,a):
        return a in self.G.edges()

    # def addNode(self,a):
    #     self.G.add_node(a)
    def addEdge(self, a):
        assert type(a) in [list, tuple]
        assert len(a) == 2
        self.G.add_edge(*a)
        # without attribute?
        # that is not good.
# my keyboard is fucked.
# this got to be fucking good.
    def dump_graph(self):
        return self.G
# what format will you use?
# doesn't matter. just get it done.
    def save_graph(self, load):
        nx.write_gpickle(self.G, load+".gpickle" if ".gpickle" != load[-len(".gpickle"):] else load)
        # build a graph instead of db this time?
        # all we need is this.
# ask for help?
# enterprise.
# EMPIRE.
# it is not just about click into the link.
# it is about whether you can remember or not.
# FOR EXAMPLE, THE TREE PARSER, THE HIGHLIGHTER.
# what about that thing? the novel?
# you can do it, but it is in chinese!
# NVM.

    # are they related?
    # what about attr?
# inference.
# all possible moves?
# write crap -> try to compensate -> write crap
# def insert_node(a)
# form matching?
# HAVE SOMETHING TO DO WITH THE THING.
# we just initialize the whole shit.
# create_edge? what is it?
# find the code here.
# i want to write code.
# I want answers.
# cloud delivered solution?
