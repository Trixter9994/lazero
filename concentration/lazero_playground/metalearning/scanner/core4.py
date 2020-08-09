# coding: utf-8 -*-
from py2neo import Graph
# import re
from simpleStorageR import storeAList
# Node,Relationship,NodeMatcher
graph = Graph("http://localhost:7474", username="neo4j", password="parrot")

#graph.run("create index on :key(name)")
#graph.run("create index on :dictionary(name)")

#graph.run("USING PERIODIC COMMIT LOAD CSV FROM 'file:///root/lazer-ubuntu/metalearning/net/keyboardMap/fuck.csv' AS line WITH line MERGE (a:key{name:line[0]}) WITH a,line MATCH (b:key{name:line[1]}) WITH a,b MERGE (a)-[:nextTo]-(b);")

#graph.run("USING PERIODIC COMMIT  LOAD CSV FROM 'file:///root/lazer-ubuntu/metalearning/net/gamma.csv' AS line MATCH  (a:english) WHERE a.name=line[0] WITH a,line MATCH ;")

#a=open("beta.csv","r")
#for b in a.readlines():
#    c=re.sub("\n","",b).split(",")
#    graph.run("MATCH (a:english) where a.name=\""+c[0]+"\" with a match (b:english) where b.name=\""+c[1]+"\" create (a)<-[:lemma]-(b)")
#a.close()
# graph.run("MATCH (a:lemma),(b:derived) CREATE (a)<-[:lemma]-(b)")
# this is slow as hell
# graph.run("USING PERIODIC COMMIT  LOAD CSV FROM 'file:///root/lazer-ubuntu/metalearning/net/beta.csv' AS line MERGE (a:dictionary:english:derived {name:line[0]}) WITH line MERGE  (b:dictionary:english:lemma {name:line[1]}) ;")

#matcher=NodeMatcher(graph)
#test_node_1 = Node(label = "Person",name = "test_node_1")
#test_node_2 = Node(label = "Person",name = "test_node_2")

#graph.create(test_node_1)
#graph.create(test_node_2)

"""分别建立了test_node_1指向test_node_2和test_node_2指向test_node_1两条关系，
关系的类型为"CALL"，两条关系都有属性count，且值为1。"""
#node_1_call_node_2 = Relationship(test_node_1,'CALL',test_node_2)
#node_1_call_node_2['count'] = 1
#node_2_call_node_1 = Relationship(test_node_2,'CALL',test_node_1)
#node_2_call_node_1['count'] = 1
#graph.create(node_1_call_node_2)
#graph.create(node_2_call_node_1)


"""节点和关系的属性初始赋值在前面节点和关系的建立
的时候已经有了相应的代码，在这里主要讲述一下怎么更新一个节点/关系的属性值。"""

#node_1_call_node_2['count']+=1
#graph.push(node_1_call_node_2)

"""通过find和find_one函数，可以根据类型和属性、属性值来查找节点和关系。"""

"""find和find_one的区别在于：
find_one的返回结果是一个具体的节点/关系，可以直接查看它的属性和值。如果没有这个节点/关系，返回None。
find查找的结果是一个游标，可以通过循环取到所找到的所有节点/关系。"""

#find_code_1 = graph.match(label="key",property_key="name",property_value="k")
# print(find_code_1['name'])

#find_code_3 = graph.match_one(  label="Person",  property_key="name", # property_value="test_node_2")

"""如果已经确定了一个节点或者关系，想找到和它相关的关系和节点，
就可以使用match和match_one"""
#
# find_relationship = graph.match_one(start_node=find_code_1,end_node=find_code_3,bidirectional=False)
# print(find_relationship)

def matchNeighbor():
    k0=[]
    match_relation =graph.run("""MATCH (a:directory) WHERE NOT ()-->(a) WITH a MATCH p=(a)-[*]->(b) WHERE b.id=1 RETURN p""")
            #graph.run("""MATCH (n:key{name:'"""+k+"""'})<--(r) RETURN r;""")]
#    for m in match_relation:
    for i in list(match_relation):
#         print(i)
#     print(dir(i))
#     print(type(i))
        k0.append(list(map((lambda x: x["name"]),i[0].nodes)))
    return k0
#     i['count']+=1
#     graph.push(i)

storeAList(matchNeighbor())
# print("1111111111111111")
# # print(graph)
# print(test_node_1)
# print(test_node_2)
# print(node_2_call_node_1)
# print(node_1_call_node_2)
