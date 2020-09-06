from niche import Method2
from matrixPro import Linkage, bashBunny, reform

def getEssence(a,b):
  return [[[y[0],b[y[1][0]:y[1][1]]]for y in x] for x in a]

t0 = "由事件a推出“天鹅是白的”这个概念，由事件b也推出“天鹅是白的”，以至于集合x内所以事件都推出“天鹅是白的”，所以归纳出“天鹅是白的”"
t1 = Method2(t0, t0)
# print(t1.tolist())
# print(Linkage(t1))
t2 = Linkage(t1)
tx = reform(t2)[1:]
# remove first column.
# that was a strange experience.
t3 = bashBunny(tx)
# print(t3)
t4 = getEssence(t3, t0)
# print(t4)
t5 = [x for y in t4 for x in y]
t6 = [x for x in t5 if x[0]]
print(t6)