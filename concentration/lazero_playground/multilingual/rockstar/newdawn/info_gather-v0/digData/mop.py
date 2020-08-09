import pickle
import difflib, re
from mapper import souviet 
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
    fuck0=fuckall([pos for pos, char in enumerate(superstring) if char == "\n"])
    #print(fuck0)
    # this ain't right.
    if len(fuck0)>9:
        select=int(len(fuck0)-2)//5
        fuck=[]
        for mk in range(5):
            fuck.append(fuck0[int(select*(mk+0.5))])
    #    print(fuck)
    else:
        fuck=fuck0
    #fuck=filter(lambda x:fuck.index)
    # you could make something overlappy.
    # no dude you are kidding me.
    # swipe off the corner!
    # this might be the source of the efficiency problem.
    for k in fuck:
        a, b = superstring[k+2::],superstring[:k]
#        print([a,b])
        thug=[a[i:i+n] for i, _, n in difflib.SequenceMatcher(None, a, b).get_matching_blocks() if n]
        gnu+=thug
    bsd=list(set(gnu))
    cp=len(bsd)
    mop=[[]]*cp
    for x in range(cp):
        ruby=bsd[x]
        mop[x]=[ruby,gnu.count(ruby)]
    #print(mop)
    #print("-----spliter-----")
    return mop

#shit="hell yeah i am back. oh yeah i am kidding . just kkkk   k "
nope=""
with open("core.log","r") as tits:
    nope=tits.read()
#print(nope)
joker=(lambda nope0:nope0[:-1] if nope0[-1]=="\n" else nope0)
with open(joker(nope)+"alphabets.txt","r") as dickhead:
    shit=dickhead.read()
    #print(shit)
    #print("-----spliter-----")
    joke=list(reversed(sorted(same_fuck(shit),key=(lambda x:x[1]))))
    #print(joke)
    std=joke[0][1]
    numkill=list(filter((lambda x:(std-x[1])/std<0.2),joke))
    #print(numkill)
    with open('scavenger.pickle', 'wb') as filehandle:
        pickle.dump(numkill, filehandle)
    geeks=[]
    for geek in numkill:
        geeks+=geek[0].split("\n")
    with open('scavenger0.pickle', 'wb') as filehandle:
        pickle.dump(geeks, filehandle)
    gnome=[]
    for geek in numkill:
        gnome.append(souviet(geek[0]))
    with open('scavenger1.pickle', 'wb') as filehandle:
        pickle.dump(gnome, filehandle)

#    geeks
    #fuck
    #if at the beginning or the ending, you shall say it.
