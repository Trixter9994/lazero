import sqlite3
# remember that similar objects could be detected.
# you can use different UUIDs to identify objects and create relations.
# you can also makr UUID shorter.
# something that needed to be searched separately, independent from contents (usually repeated content or something general like menu or index)
#sql = ("CREATE INDEX index0 ON subdir (pos);")

#sql0 = ("CREATE INDEX index1 ON subdir (uuid);")

#sql1 = ("CREATE INDEX index2 ON subdir (depth);")

conn=sqlite3.connect("wtf.db")

#conn.execute(sql0)
#conn.execute(sql)
# the constraints works well.

# you could use another identifier instead of POS symbols, but that's another story.
cursor=conn.execute("SELECT * FROM subdir;")

for a in cursor:
    print("-----separator-----")
    print(a)
    # it is actually a tuple.
    for b in a:
        print(b)

# rape people off and get paid for it.
conn.commit()
conn.close()
# fuck them.
# check if the rule works.
# export the uuid in case of forgotten.
#font=open("hello.log","w+")
# this will not be the problem, isn't it?
#struct=a0+"\n"+a+"\n"
#font.write(struct)
#font.close()
