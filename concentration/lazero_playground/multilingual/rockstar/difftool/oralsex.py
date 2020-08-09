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
    fuck=fuckall([pos for pos, char in enumerate(superstring) if char == " "])
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
        analsex[x]=[anus,gnu.count(anus)]
#    print(analsex)
    return [analsex,gnu]
shit="hell yeah i am back. oh yeah i am kidding . just kkkk   k "
print(same_fuck(shit))
