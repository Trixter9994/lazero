import re
stickGlue=(lambda x: "".join(list(filter((lambda y:y not in [" ","\t"]),x))))
# this is for those without semicolons.
# i will do another semi parser.
# or just code formatter.
def checkFunctor(s):
    # along with the calling.
    rape=list(map((lambda x:stickGlue(x[:-1])),re.findall(r"[a-zA-Z0-9_]*[ \t]*\(",s)))
    return rape
def notch(k):
    k0=stickGlue(k)
    e=k0.split("=",1)
    try:    
        if "def" == k0[:3]:
            return 1, k0.split("(",1)[1].split(":",1)[0][:-1]+","
        elif "lambda" == e[1][1:7]:
            return 0,e[0]
        else:
            return 2,""
    except:
        return 2,""
def smoke(fuck):
    a=fuck if fuck[-1]!="\n" else fuck[:-1]
    b=stickGlue(a).split(":",1)[0][7:]
    return (fuck,b,"("+b+",)")
