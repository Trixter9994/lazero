# what we need is a code snippet collector.
# import unicode
# https://github.com/goto456/stopwords
import unicode_charnames
import uniprop
from simpleStorageR import storeAList
# shall we concern the predefined groups?
# is there any missing alphabet or components?
# hidden candidate everywhere.
# split -> filter
# dir()
def hash(a):
  b = []
  for b0 in a:
    if b0 not in b:
      b.append(b0)
  return b
drm=list(set(["　"," ","\b","\n","\t"]))
fg=["中文停用词表.txt","哈工大停用词表.txt","四川大学机器智能实验室停用词库.txt","百度停用词表.txt"]
fgx=""
def getShit(a):
  with open(a, "r") as f:
    return f.read().split("\n")
def probe(a):
  for b in a:
    if "CJK" not in b:
      return False
  return True
def latin(a):
  b0,b1=len(a),0
  for b in a:
    if "LATIN" in b and "FULLWIDTH" not in b:
      b1 += 1
  return 0.7<(b1/b0+0.1)

u0=lambda y:[unicode_charnames.charname(x) for x in y]
drx = {"control": [], "stopword": []}
for gf in range(len(fg)):
  u=getShit(fg[gf])
  for u1 in u:
    ux=u0(u1)
    if probe(ux) or latin(ux):
      # drx["stopword"].append(u1)
      drx["stopword"].append(u1)
    else:
      for y in u1:
        drx["control"].append(y)
drx["stopword"] = hash(drx["stopword"])
drx["control"] = hash(drx["control"] + drm)
storeAList(drx)
print(drx)
  # all blank chars to space?
    # print(u1)
    # just how the fuck can we do this?