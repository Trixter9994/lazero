import re
stringSet=["set:",["[","]"]]
#standAlone=(lambda x: list(filter((lambda y: y!=""), list(map((lambda z: z[1] if len(z) <=3 else re.match(r"\d+").group(0)),x)) )))
standAlone1=(lambda x: list(filter((lambda y:y!=""),x.split(", "))))
standAlone0=(lambda x: list(filter((lambda y:y!=""),x.split(", "))))
standAlone=(lambda x: standAlone1(x) if standAlone1(x).count(sorted(set(standAlone1(x)),key=(lambda y: standAlone1(x).count(y)))[0]) <3 else standAlone0(x))
wrapper=(lambda xy: [xy,ord(xy)])
wrapper0=(lambda xy: [chr(xy),xy])
with open("alphabets.txt","r") as rockstar:
#    mandarin=0
    for kn in rockstar.readlines():
        if stringSet[0] in kn:
            print("set only")
            print(kn)
#            ks=re.findall(r" .(,?)| \&#\d*;(,?)", kn[5:])
            prt=standAlone(kn[5:-1])
            prt[0]=prt[0][1:]
#            print(prt)
            if len(prt)>1:
                try:
                    pat=list(map((lambda z: wrapper(z) if len(z)==1 else wrapper0(int(re.findall(r"\d+",z)[0]))),prt))
                    print(pat)
                except:
                    print("FUCKED UP\nFUCKED UP")
            else:
                print("TOO YOUNG TOO NAIVE\nTOO YOUNG TOO NAIVE")
#            print(kn[-1])
#            print(ks)
#            print(standAlone(ks))
        else:
            if (stringSet[1][0] in kn and stringSet[1][1] in kn):
                print("name only")
                print(kn)
#        elif mandarin==1:
            else:
                print("empty line")
                print(kn)
#        mandarin+=1
#        if mandarin==3:
#            mandarin=0
