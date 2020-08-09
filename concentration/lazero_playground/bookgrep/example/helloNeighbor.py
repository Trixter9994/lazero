from py2neo import Graph
# it will be exhausting if done without metaprogramming.
graph = Graph("http://localhost:7474", username="neo4j", password="parrot")
graph.run("create index on :三体(name)")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/push/relationships.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体:relationships{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/push/tags.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体:tags{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-22.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"22"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-b1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-b1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-b1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-b1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-g1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-g1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-g1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-g1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-g1-h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-gN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-gN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-gN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-gN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-gN1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-gN1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-gN1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-gN1-h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-gN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-gN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-gN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-gN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-h4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-h4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-h4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-h4-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-kN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-kN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-kN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-kN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-kN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-kN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-kN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-kN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-kN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-kN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-a1-kN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"a1-kN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-aN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-aN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-aN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"aN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b1-d1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b1-h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b1-h1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b1-h1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b1-h1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b1-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b1-h1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-b2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"b2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"bN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"bN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"bN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"bN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-bN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"bN1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-c1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-c1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-c1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"c1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"d1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"d1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"d1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-22.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"d1-22"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-d1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"d1-h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-eN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-eN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-eN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"eN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"f1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"f1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"f1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"f1-h1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-f1-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"f1-h1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"fN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"fN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"fN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"fN1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-fN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"fN1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-h1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-h2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-h2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-hN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-hN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-hN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-hN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-hN3-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-iN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-iN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g1-iN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g1-iN1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-g2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"g2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-gN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-gN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-gN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"gN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-i1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-i2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h1-iN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h1-iN3-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h2-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h2-iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-iN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-iN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-iN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h2-iN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-iN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-iN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h2-iN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h2-iN1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h3-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h3-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h3-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h3-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h3-iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h4-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h5-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h5-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-h5-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"h5-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-i1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-i1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-i2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-iN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-iN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-iN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-iN2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN1-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN1-iN2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN10-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN10-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN10-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN10-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-iN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-iN2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-iN2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-iN2-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-iN2-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN2-iN2-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN2-iN2-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-02.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-02.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-02"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-20.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-20.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-20"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-iN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-iN2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-iN2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-iN2-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN3-iN2-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN3-iN2-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN4-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN4-iN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-iN2-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN4-iN2-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN4-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN4-iN2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN5-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN5-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN5-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN5-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN5-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN5-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN5-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN5-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN5-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN5-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN5-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN5-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN6-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN6-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN6-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN6-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN6-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN6-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN6-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN6-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN6-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN6-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-hN6-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"hN6-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"i1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"i1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"i1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-i2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"i2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"iN1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-01.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"iN1-01"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"iN1-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"iN1-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-12.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"iN1-12"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN1-21.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"iN1-21"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN2-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"iN2-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN2-10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"iN2-10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-iN2-11.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"iN2-11"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-k1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-k1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/cross-k1-00.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:cross{name:"k1-00"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:""}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-b1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-b1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-b1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1-b1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1-g1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-gN1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-gN1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-gN1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1-gN1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-gN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-gN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-gN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1-gN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-gN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-gN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-gN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1-gN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-h4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-h4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-h4.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1-h4"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-h5.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-h5.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-h5.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1-h5"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-kN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-kN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1-kN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1-kN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a2-h4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a2-h4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-a2-h4.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"a2-h4"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-aN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-aN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-aN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"aN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"b1-d1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1-gN1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1-gN1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1-gN1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"b1-gN1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"b1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"b1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-b2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"b2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-bN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-bN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-bN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"bN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-c1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-c1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-c1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"c1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-d1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-d1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-d1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"d1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-d1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"d1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-eN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-eN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-eN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"eN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-f1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-f1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-f1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"f1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-f1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-f1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-f1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"f1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-fN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-fN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-fN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"fN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"g1-h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"g1-hN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1-hN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1-hN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1-hN3.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"g1-hN3"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"g1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"g2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g3.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"g3"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g4.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"g4"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g5.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g5.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-g5.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"g5"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-gN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-gN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-gN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"gN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h1-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h1-i2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h1-iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h1-iN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN3.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h1-iN3"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN4.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h1-iN4"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN6.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN6.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1-iN6.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h1-iN6"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h2-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h2-iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h2-iN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h3-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h3-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h3-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h3-iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h3.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h3"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h4.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h4"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h5.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h5.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-h5.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"h5"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN1-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN1-i2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN1-iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN1-iN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN10.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN10.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN10"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN2-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN2-iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN2-iN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN3-i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN3-iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN3-iN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN3.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN3"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN4-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN4-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN4-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN4-iN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN4.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN4.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN4"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN5.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN5.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN5.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN5"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN6.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN6.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-hN6.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"hN6"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-i1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"i1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-i2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"i2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-iN1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"iN1"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-iN2.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"iN2"}]->(b);""")
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-k1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[0]});''')
graph.run('''USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-k1.csv' AS line FIELDTERMINATOR ','
WITH line
MERGE (a:三体{name:line[1]});''')
graph.run("""USING PERIODIC COMMIT 1000
LOAD CSV FROM 'file:///E:/AGI/lazero/bookgrep/example/santi/normal-k1.csv' AS line FIELDTERMINATOR ','
WITH line
MATCH (a:三体{name:line[0]})
MATCH (b:三体{name:line[1]})
MERGE (a)-[:normal{name:"k1"}]->(b);""")
