from py2neo import Graph
graph = Graph("http://localhost:7474", username="neo4j", password="parrot")
graph.run("create index on :黑客(name)")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/push/relationships.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客:relationships{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/push/tags.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客:tags{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-22.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"22"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-d1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-f1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-f1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-f1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-f1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-g1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-g1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-g1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-g1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-g1-iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-h1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-h1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-h1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-hN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-hN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-hN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-hN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-i1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-a1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"a1-i1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-g1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-g1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-g1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-g1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN1-g1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN1-g1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-aN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"aN2-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"b1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"b1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"b1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"b1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"b1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"b2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"b2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-b2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"b2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-c1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-c1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-c1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"c1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"d1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"d1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"d1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"d1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"d1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"d1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"d1-h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-d1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"d1-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-dN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-dN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-dN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"dN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-dN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-dN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-dN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"dN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-dN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-dN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-dN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"dN1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"f1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"f1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"f1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"f1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"f1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"f1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-f1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"f1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-22"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-h2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-h2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-h2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-hN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-hN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-hN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-hN1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-hN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-hN1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-iN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-k1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-k1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-g1-k1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"g1-k1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-gN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-gN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-gN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"gN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-gN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-gN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-gN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"gN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-gN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-gN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-gN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"gN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-22"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-i1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-j2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-j2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-j2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-j2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-j2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-j2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h1-j2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h1-j2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-h2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"h2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-i1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN1-i1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN2-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN2-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN2-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN2-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN2-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN3-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN3-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN3-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN3-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-hN3-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"hN3-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i1-22"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i2-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i2-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-i3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"i3-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN3-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-iN4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"iN4-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-k1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-k1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-k1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"k1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"kN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"kN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"kN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/cross-kN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:cross{name:"kN1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:""}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"a1-d1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-f1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-f1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-f1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"a1-f1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-g1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-g1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-g1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"a1-g1-iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"a1-g1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"a1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"a1-hN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-hN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-hN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-hN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"a1-hN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"a1-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-a1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"a1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-aN1-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-aN1-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-aN1-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"aN1-g1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-aN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-aN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-aN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"aN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-aN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-aN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-aN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"aN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-b1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-b1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-b1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"b1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-b2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-b2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-b2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"b2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-bN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-bN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-bN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"bN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-d1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-d1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-d1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"d1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-d1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-d1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-d1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"d1-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"d1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-dN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-dN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-dN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"dN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-f1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-f1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-f1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"f1-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-f1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-f1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-f1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"f1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"g1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-h2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-h2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-h2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"g1-h2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"g1-hN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"g1-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"g1-iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"g1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"h1-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"h1-iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"h1-iN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-h2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"h2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"hN1-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"hN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN2-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN2-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN2-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"hN2-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"hN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN3-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN3-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN3-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"hN3-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN3.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"hN3"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-hN4.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"hN4"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"i2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-i3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-i3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-i3.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"i3"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"iN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN3.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"iN3"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-iN4.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"iN4"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-j1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-j1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-j1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"j1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-j2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-j2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:黑客{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/all/normal-j2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:黑客{name:line[0]})
MATCH (b:黑客{name:line[1]})
MERGE (a)-[:normal{name:"j2"}]->(b);""")
