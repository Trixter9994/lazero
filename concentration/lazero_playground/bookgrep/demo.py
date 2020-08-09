import unicode_charnames
# shall we concern the predefined groups?
# is there any missing alphabet or components?
# hidden candidate everywhere.
def getShit(a):
  with open(a, "r") as f:
    return f.read()
u=getShit("example\\0.log")
u0=[unicode_charnames.charname(x) for x in u]
for u1 in u0:
    print(u1)
    # just how the fuck can we do this?