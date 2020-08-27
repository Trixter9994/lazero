def writeFile(a,b):
    with open(a,"w+") as f:
        f.write(b)
se="this xml"
sn="not xml"
sf=se
for x in range(100000):
    sf+="\n"+se
writeFile("file0",sf)
sf=se
for x in range(100000):
    if x!=2000:
        sf+="\n"+se
    else:
        sf+="\n"+sn
writeFile("file1",sf)
