from getFromPickleR import returnAList
import continuality
from simpleStorageR import storeList
# r = returnFuck()
# for x in r:
#   print(x)
# so what?
r, rx = returnAList(), []
# onehot model?
# iterate over dics?
# -> (None,"str")?
# better get the core of things.
for x in r:
  f = [y for y in x]
  f0 = continuality.Faith([x[z] for z in f]).set()
  rx.append({z: [r0 for r0 in f if x[r0] == z] for z in f0}) # abstraction needed.
storeList(rx)
  # print(f1)
  # print("________________________________________________________________")
  # we have a translator.