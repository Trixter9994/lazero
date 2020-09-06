i=open("README","r")
fulltext=list(filter((lambda x: x!=""),i.read().split("\n")))
for x in range(len(fulltext)):
    fulltext[x]=list(filter((lambda x:x!=""),[pos for pos in fulltext[x].split(".")]))
    for y in range(len(fulltext[x])):
        fulltext[x][y]=list(filter((lambda x:x!=""),[pos for pos in fulltext[x][y].split(",")]))
        for z in range(len(fulltext[x][y])):
            fulltext[x][y][z]=list(filter((lambda x:x!=""),[pos for pos in fulltext[x][y][z].split(" ")]))
print(fulltext)

i.close()

