from jit_char_render import getJson
from storeADill import storeXList
def openFile(a):
	with open(a,"r") as f:
		return f.read()

f=openFile("transgender.log")
f0={}
f1=set(f)
for x in f1:
	x0=getJson(x)
	f0.update(x0)
	# print(x0)
    # i ain't no lady!
storeXList(f0,"trench")
# better check them.