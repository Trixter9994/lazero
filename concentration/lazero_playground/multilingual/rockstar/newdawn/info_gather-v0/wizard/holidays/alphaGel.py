# first, pattern.
# second, utilize.
# sorted or not
import os
import statistics
from keepMeSatisfied import same_fuck

similar=(lambda x,y: True if (x/y > 1/4 and x/y < 4) else False)

def sucker(m):
    s=""
    for k in m:
        s+=(str(k)+" ")
    return s[:-1]

def ash(bitchEternity):
    init="lua geniusWalk.lua"
    for fuckall in bitchEternity:
        init+=" "+str(fuckall)
    myCmd0 = os.popen(init)
    myCmd=list(filter((lambda xn:xn!=""),myCmd0.read().split("\n")))
   # kill=(lambda k:list(map((lambda x:int(x)),k)))
#    dickHead=kill(list(filter((lambda x:x!=""),myCmd[1].split(" "))))
    myCmd0.close()
    return myCmd[1]
#    ksn=dickhead.count(statistics.mode(dickhead))
#    ksd=len(dickhead)
    #return [similar(ksn,ksd),similar(ksn,ksd//2)]

shit=(lambda x0: list(filter((lambda x:x!=""),x0.split(" "))))

def amplifier(c):
    a,b=c[0],c[1]
    if a==True:
        return True
    elif b==True:
        return True
    else:
        return False

# derive=(lambda f,g: int(g/(2+(f*(1/(1-g//2))))))
derive=(lambda f,g: int(g/(2+(f*(1/(1-g/2))))) if f%2==1 else int(g//f)*f)
takeTwo=(lambda v:list(map((lambda f: abs(int(f))),v)))
def verizon0(mode,dutch,count):
    duck=dutch[0]
    rubber=dutch[1]
    if mode == True:
        # sorted.
        a,b=rubber[0]
        a0,b0=len(shit(a)),len(b)
        pushUp=similar(count[0]/2,a0)
        if count[1]==True and b0==2:
            return [pushUp,True]
        else:
            return [pushUp,False]
    if mode == False:
        # not sorted.
        if statistics.mean(list(map((lambda x:statistics.mean(takeTwo(shit(x)))),[ducky[0] for ducky in duck])))>5:
            ver2=verizon0(True,dutch,count)[0]
            a=[int(similar(len(shit(deutsch[0]))*len(deutsch[1]),derive(len(shit(deutsch[0])),count[0]))) for deutsch in duck]
            b=0
            for a0 in a:
                b+=a0
            if similar(b,len(duck)):
                return [True,ver2]
            else:
                return [False,ver2]
        else:
            return [False,False]

def verizon1(ducky,count):
    similar0=(lambda x,y: True if (x/y > 1/4 and x/y < 4) else False)
    # only work in sorted mode.
    bang=ducky[0]
    shaky=list(map((lambda x: x[1]-x[0]),bang))
    fuckMe=ducky[1]
    if fuckMe!=[]:
        if similar0(len(fuckme),count[0]):
            watchMe=same_fuck(ash(fuckme))
            return verizon0(True,watchMe,[len(watchMe),True if len(watchMe)%2==0 else False])
        else:
            pass
    else:
        print(shaky)
        suckMeUp=sucker(shaky)
        print(suckMeUp)
        watchMe=same_fuck(suckMeUp)
        print(watchMe)
        # use try catch.
#        if watchMe[0]!=[] and watchMe[1]!=[]:
        return verizon0(True,watchMe,[len(watchMe),True if len(watchMe)%2==0 else False])
#        else:
#            print("FUCKING HELL!\nFUCKING HELL!")
#            return [False,False,False]

def utilize(result,ab,cd):
    if result == True:
        if ab == True:
            return [[cd[a] for a in range(len(cd)) if a%2==0],[cd[a] for a in range(len(cd)) if a%2==1]]
        else:
            print("-- DUPLICATES FOUND --\n-- MIGRATE TO ICU --")
            return [[],[]]
    else:
        print("-- I FUCKED UP --\n-- NO FUCKS GIVEN --")
        return [[],[]]
