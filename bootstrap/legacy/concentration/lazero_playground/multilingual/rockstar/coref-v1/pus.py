import sqlite3
# fuck.
# only works out a linear list.
# if wanna do the same thing, then download code from other place.

# this is authority.

# remember that similar objects could be detected.
# you can use different UUIDs to identify objects and create relations.
# you can also makr UUID shorter.
# something that needed to be searched separately, independent from contents (usually repeated content or something general like menu or index)
#sql = ("CREATE INDEX index0 ON subdir (pos);")

#sql0 = ("CREATE INDEX index1 ON subdir (uuid);")

#sql1 = ("CREATE INDEX index2 ON subdir (depth);")

conn=sqlite3.connect("fuckyou.db")

#conn.execute(sql0)
#conn.execute(sql)
# the constraints works well.

# you could use another identifier instead of POS symbols, but that's another story.
cursor=conn.execute("SELECT * FROM subdir;")

blitz=[]

for a in cursor:
    print("-----separator-----")
    print(a)
    blitz.append(a[1:])
    # this will filter out the uuids.
    # uuid name pos pi si ssi wi
    # it is actually a tuple.
"""    for b in a:
        print(b)"""

# rape people off and get paid for it.
conn.commit()
conn.close()

blitz0=set( [blitz[i][2] for i in range(len(blitz))  ] )
print(blitz0)

blitz1=set( [blitz[i][1] for i in range(len(blitz))  ] )
print(blitz1)

blitz2=set( [blitz[i][3] for i in range(len(blitz))  ] )
print(blitz2)

blitz3=set( [blitz[i][4] for i in range(len(blitz))  ] )
print(blitz3)

blitz4=set( [blitz[i][5] for i in range(len(blitz))  ] )
print(blitz4)

#for things in blitz1:
# you shall consider a sorting algorithm.

# Hitler As A Programmer
# Launching Blitz Over The Entire Internet

hitler=list(sorted(blitz,key=(lambda x:x[1])))
print(hitler)

# fuck them.
# check if the rule works.
# export the uuid in case of forgotten.
#font=open("hello.log","w+")
# this will not be the problem, isn't it?
#struct=a0+"\n"+a+"\n"
#font.write(struct)
#font.close()
