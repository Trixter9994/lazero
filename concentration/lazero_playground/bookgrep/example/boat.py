#coding: "utf-8"
import os
from nameParser import getX,getAll
token="三体" #the encoding really makes me a hard-on.
def distance(a, b):
    with open(a, "a+", newline="") as f:
        # for d in b:
        #   f.write(d+"\n")
        for r in b:
          f.write(r+"\n")
path,px="santi\\push",[]
for files in os.listdir(path):
    if os.path.isfile(os.path.join(path, files)):
        px.append(files)
# generate code for batch import?
# coding: utf-8 -*-
fl=["""from py2neo import Graph"""]
# import re
# from simpleStorageR import storeAList
# Node,Relationship,NodeMatcher
fl.append("""graph = Graph("http://localhost:7474", username="neo4j", password="parrot")""")

fl0=lambda x: """graph.run("create index on :{}(name)")""".format(x)
#graph.run("create index on :dictionary(name)")
fl.append(fl0(token))
# graph.run("USING PERIODIC COMMIT 1000 LOAD CSV FROM 'file:///E:/AGI/everything/0.csv' AS line WITH line MERGE (a:fileKey{name:line[0]}) WITH a,line MERGE (b:fileKey{name:line[1]}) WITH a,b MERGE (a)-[:r0]->(b);")
# graph.run("USING PERIODIC COMMIT 1000 LOAD CSV FROM 'file:///E:/AGI/everything/1.csv' AS line WITH line MERGE (a:fileKey{name:line[0]}) WITH a,line MERGE (b:fileKey{name:line[1]}) WITH a,b MERGE (a)-[:r1]->(b);")
fl1 = lambda x, y, z: """graph.run('''USING PERIODIC COMMIT 1000\nLOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/{}' AS line FIELDTERMINATOR ','\nWITH line\nMERGE (a:{}""".format(x, z) + "{name:line[" + y+"]});''')"

for x in px:
    fl.append(fl1(path.replace("\\","/")+"/"+x,"0",":".join([token,getAll(x)[0]])))

path,px="santi",[]
for files in os.listdir(path):
    if os.path.isfile(os.path.join(path, files)):
        px.append(files)
fl2 = lambda x, y, z, a: '''graph.run("""USING PERIODIC COMMIT 1000\nLOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/{}' AS line FIELDTERMINATOR ','\nWITH line\nMATCH (a:{}'''.format(x, z) + "{name:line[0]})\nMATCH " + "(b:{}".format(z) + "{name:line[1]})\nMERGE " + '''(a)-[:''' + y + '''{name:"''' + a + '''"}]->(b);""")'''
for x in px:
    fl.append(fl1("/".join([path, x]), "0", token))
    fl.append(fl1("/".join([path, x]), "1", token))
    f=getAll(x)
    fl.append(fl2("/".join([path, x]), f[0], token,'-'.join(f[1:-1])))

distance("helloNeighbor.py",fl)