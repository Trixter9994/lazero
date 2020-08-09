# this analsex is extremely fast.
# just sayin'
import difflib

import re
"""
a, b = "same order words", "not same but order words matched"
thug=[a[i:i+n] for i, _, n in difflib.SequenceMatcher(None, a, b).get_matching_blocks() if n]
print(thug)"""
# i don't give a shit about time complexity.
def fuckall(list0):
    asshole=list0[:-1]
    bitch=[]
    for dick in range(len(list0)-1):
        jerk=list0[dick]
        if asshole[dick]!=(jerk+1):
            bitch.append(jerk)
        else:
            pass
    marker=list0[-1]
    #print(bitch)
    if marker!=(bitch[-1]+1):
        bitch.append(marker)
    else:
        pass
#    for x in range(2):
        #masochist=bitch[-(2-x)]
    for x in range(2):
        # loop it twice
        if not bitch[-1]<len(list0):
#            if x==0:
                del bitch[-1]
        else:
            pass
    if (bitch[-2]+1)==bitch[-1]:
        del bitch[-1]
    else:
        pass
    return bitch

def same_fuck(superstring):
    gnu=[]
    # standard spliter here is the space char.
    try:
        fuck=fuckall([pos for pos, char in enumerate(superstring) if char == " "])
    except:
        fuck=[pos for pos, char in enumerate(superstring) if char == " "]
#    print(fuck)
    # you could make something overlappy.
    # no dude you are kidding me.
    # swipe off the corner!
    # this might be the source of the efficiency problem.
    for k in fuck:
        a, b = superstring[k+1:],superstring[:k]
#        print([a,b])
        thug=list(filter((lambda x:x!=' '),[a[i:i+n] for i, _, n in difflib.SequenceMatcher(None, a, b).get_matching_blocks() if n]))
        gnu+=list(map((lambda x: re.sub("^ ","",re.sub(" $","",x))),thug))
    bsd=list(set(gnu))
    cp=len(bsd)
    analsex=[[]]*cp
    for x in range(cp):
        anus=bsd[x]
        analsex[x]=anus
#    print(analsex)
    return [analsex,gnu]

ok=open("POS.log")      
shit=list(filter((lambda x:x!=""),ok.read().split("\n")))
ok.close()

scortum=[]
for x in range(len(shit)-1):
    # the item which you append here is not for fun.
    # you shall check manuals on how to build a fucking complier.
    # i believe there are some commondities between natural language and code.
    # two items, one counting list, the other is pure list.
    scortum.append(same_fuck(shit[x]+shit[x+1]))
#print(scortum)
cockshock=[]
#groin={}
ovary=[]
for testicle in scortum:
    ball=testicle[0]
    ovary+=testicle[1]
    # this is a tuple list.
    cockshock+=ball
    # we should do it all in once.
#for semen in cockshock:
"""venum=[]
for k in range(len(cockshock)):
    venum.append(cockshock[k][0])"""
semen=set(cockshock)
#print(semen)

blowjob=[]
for groin in semen:
    blowjob.append([groin,ovary.count(groin)])

blowjob=sorted(list(filter((lambda x:len(x[0])>3),blowjob)),key=(lambda x: x[1]),reverse=True)

print(blowjob)

#print(ovary)

    # abandon the second shit.

#    balloon=testicle[1]

