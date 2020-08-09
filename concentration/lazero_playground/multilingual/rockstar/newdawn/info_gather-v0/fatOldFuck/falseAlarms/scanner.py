# fully trustworthy partial trustworthy complete nonsense
# return a list instead.

import re
literal="2 3 42 3 451 2 3 4 5 62 3 45 2 3 45"
anus0="2 3 4"

#def testStone(major,minor,jerkOff):


def testTube(nb,anus):
#    fuck=re.findall(r'[0-9]{}?[0-9]|?[0-9]{}[0-9]'.format(anus,anus,anus),nb)
    fuck=[m.start() for m in re.finditer(anus,nb)]
    fuckme=[len(nb),len(anus)]
    bitch=[]
    for wifu in fuck:
        if wifu==0:
            if nb[wifu+fuckme[1]]==" ":
                bitch.append(wifu)
            else:
                pass
        elif wifu+fuckme[1]==fuckme[0]:
            if nb[wifu-1]==" ":
                bitch.append(wifu)
            else:
                pass
        else:
            if nb[wifu+fuckme[1]]==" " and nb[wifu-1]==" ":
                bitch.append(wifu)
            else:
                pass
    return bitch
    #print(fuck)

print(literal)
print("--spliter--")
print(testTube(literal,anus0))
