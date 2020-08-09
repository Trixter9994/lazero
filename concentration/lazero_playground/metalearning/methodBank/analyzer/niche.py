import uuid
from defTester import smoke
# to create random stuff.
def wroteAHaskell(name,turtle):
    holyIndent="\t"
    with open(name,"w+") as fuck:
        jerkMeUp=str(uuid.uuid4())[:8]
        suckMeUp=str(uuid.uuid4())[:8]
        mess=[0 in list(map((lambda x:x[2][0]),turtle)),1 in list(map((lambda x:x[2][0]),turtle))]
        messUp=list(sorted(list(set(list(map((lambda x:x[0]),turtle))))))
        if mess[0]==True:
            fuck.write("from adidas import chaos as chaos"+jerkMeUp+"\n")
        if mess[1]==True:
            fuck.write("from adidas import schema as schema"+suckMeUp+"\n")
        # read, and then generate prank list.
        prankLamb=[tur[4] for tur in turtle if tur[2][0]==0]
        hashDog=[str(uuid.uuid4())[:8] for r in range(len(prankLamb))]
#        prankQuote=[]
# reserved for in place debugging without def
        prankDef=[tur[4] for tur in turtle if tur[2][0]==1]
        devil=[]
        for i in range(1+turtle[-1][-1]):
            if i in prankLamb:
                airPods=turtle[i][2][1]+hashDog[prankLamb.index(i)]
                f=smoke(turtle[i][1].split("=",1)[1])
                devil.append(holyIndent*messUp.index(turtle[i][0])+turtle[i][2][1]+hashDog[prankLamb.index(i)]+"="+f[0])
                devil.append(holyIndent*messUp.index(turtle[i][0])+turtle[i][2][1]+"=(lambda "+f[1]+":chaos"+jerkMeUp+"([\""+turtle[i][2][1]+"\","+airPods+"],"+f[2]+"))\n")
            else:
                devil.append(holyIndent*messUp.index(turtle[i][0])+turtle[i][1])
                if i in prankDef:
                    devil.append(holyIndent*(messUp.index(turtle[i][0])+1)+"schema"+suckMeUp+"(\""+turtle[i][-2][0]+"\","+turtle[i][-3][1]+")\n")
        for pm in devil:
            fuck.write(pm)
