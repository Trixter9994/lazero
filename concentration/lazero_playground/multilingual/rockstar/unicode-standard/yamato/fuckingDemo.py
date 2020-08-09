from rectangle import returnFuck
f0=""
with open("layout_improved/U1C90.txt","r") as f:
    f0=f.read().split("\n")
r=returnFuck(f0,[52,64,20,600])
# print(r)
for r0 in r:
    print(r0)
    # do not rebuild shit.
    # simply use the power of old database.