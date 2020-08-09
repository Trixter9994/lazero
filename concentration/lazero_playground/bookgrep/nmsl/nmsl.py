from getFromPickleR import returnWTF
from simpleStorageR import storeAList
import uniprop
def fuckYou(a):
  try:
    e=eval(a)
    return e,type(e)
  except:
    return None
r,r0,r1,r2= returnWTF(),"a",{},{}
for x in r:
  r1.update({x: fuckYou("uniprop." + x + "('" + r0 + "')")})
  r2.update({x: eval("type(uniprop." + x + ")")})
storeAList([r1,r2]) # two fucking distinct dicks
# print(r1)
# print("________________________________________________________________")
# # one hot encoder?
# print(r2)
# what a loopy function.
# how to deal with other shits?
# I mean get the girth of text.
# how about rake?
# how about use unsupervised learning?
# without marker?