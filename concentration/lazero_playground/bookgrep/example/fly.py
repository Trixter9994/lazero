from getFromPickleR import returnFuck
def distance(a, b):
    with open(a, "a+", newline="") as f:
        # for d in b:
        #   f.write(d+"\n")
        for r in b:
          f.write(r+"\n")
        # c = csv.writer(f)
        # for d in range(len(b) - 1):
        #     c.writerow([b[d], b[d + 1]])
r=returnFuck()
r0="all\\push\\"
r1=[x for x in r.keys()]
for x in r1:
    distance(r0+x+".csv",list(map(lambda x: x[0],r[x])))