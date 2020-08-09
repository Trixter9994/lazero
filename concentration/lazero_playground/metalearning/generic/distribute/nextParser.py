from reader import retribution,metapro,metaproII,grouper
# from type theory to set theory
def meaningList(a, b):
  return [[x in a, x] for x in b]
def meaningGrouper(a, b):
  return grouper(meaningList(a, b))
# the inverse function?
txt = open("bookShelf", encoding="utf-8").read()
t0 = txt.split("\n")
print(t0)