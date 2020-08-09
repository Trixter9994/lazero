import re
def Magisk(erectile):
    stringSet=["set:",["[","]"]]
#standAlone=(lambda x: list(filter((lambda y: y!=""), list(map((lambda z: z[1] if len(z) <=3 else re.match(r"\d+").group(0)),x)) )))
#ky0=(lambda k:k if k[-1]!=" " else k[:-1])
#ky=(lambda k:ky0(k) if k[0]!=" " else k[1:])
    wrap=(lambda x: [ord(x0) for x0 in list(x)])
    standAlone1=(lambda x: list(filter((lambda y:y!=""),x.split(","))))
    def standAlone2(a,b):
        b0=b
#        print("FUCK\nFUCK")
#        print(a)
        for a0 in a:
            if a0!="":
                b0=b0.replace(a0,chr(int(re.findall(r"\d+",a0)[0])))
            else:
                pass
#        print("SHIT\nSHIT")
#        print(b0)
        return b0
    standAlone=(lambda y: standAlone1(standAlone2(re.findall(r"{}\d+;?".format(re.escape("&#")),y),y)))
#standAlone0=(lambda x: list(filter((lambda y:y!=""),x.split(", "))))
#standAlone=(lambda x: standAlone1(x) if standAlone1(x).count(sorted(set(standAlone1(x)),key=(lambda y: standAlone1(x).count(y)))[0]) <3 else standAlone0(x))
    wrapper=(lambda xy: ord(xy))
#wrapper0=(lambda xy: xy)
#    with open("alphabets.txt","r") as rockstar:
#    mandarin=0
# simply another workaround?
        #for kn in rockstar.readlines():
    kn=erectile
    if stringSet[0] in kn:
#            print("set only")
#            print(kn)
#            ks=re.findall(r" .(,?)| \&#\d*;(,?)", kn[5:])
        prt=standAlone(kn[5:-1])
#            print(prt)
        if len(prt)>1:
            try:
#                    print(list(map((lambda x: [x,len(x),wrap(x)]),prt)))
                pat=list(map((lambda z: wrapper(re.findall(r"[^ ]",z)[0])),prt))
#                    print(pat)
                return pat
            except:
#                    print("FUCKED UP\nFUCKED UP")
                return []
        else:
            return []
#                print("TOO YOUNG TOO NAIVE\nTOO YOUNG TOO NAIVE")
#            print(kn[-1])
#            print(ks)
#            print(standAlone(ks))
    else:
        return []
"""            if (stringSet[1][0] in kn and stringSet[1][1] in kn):
                print("name only")
                print(kn)
#        elif mandarin==1:
            else:
                print("empty line")
                print(kn)"""
#        mandarin+=1
#        if mandarin==3:
#            mandarin=0
