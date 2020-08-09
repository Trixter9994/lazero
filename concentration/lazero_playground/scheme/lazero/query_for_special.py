from getFromPickleR import returnAList

r = returnAList()
r0 = list(r.keys())
# print(r0)
for x in r0:
    r1=r[x].lower()
    if "character" in r1 or "unicode" in r1:
          print(x)
          # print(r[x])
