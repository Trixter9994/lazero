import re
import os
from getCorrectList import letIt
from shallowCopy import mover
def open_to_return(file_name):
    hardcore=[]
    with open(file_name,"r") as fuck:
        hardcore=list(filter((lambda x: x!=""),fuck.read().split('\n')))
    return hardcore

def parse_file(flist):
    lamb=[(lambda v: list(map((lambda x:True if x!=[] else False),v))),(lambda x: list(map((lambda y: re.findall(r'^(import|from)',y)),x))),(lambda x,y:list(filter((lambda g: g!=""),list(map((lambda v: re.findall(r'[^ ]+',v[0])[1] if v[1] == True else "" ),[[x[r],y[r]]for r in range(len(x))])))))]
#    print(flist)
    cold=lamb[1](flist)
#    print(cold)
    bless=lamb[0](cold)
#    print(bless)
    angle=lamb[2](flist,bless)
#    print(angle)
    return angle

def toyProject(file_name):
    return parse_file(open_to_return(file_name))

def superAddress(listOfFame):
    # better not to make things loopy.
    # loop detection is needed.
    return list(map((lambda x: x+'.py'),listOfFame))

def seekOn(nextTargets,HallOfFame,corr):
    # scan until nothing left?
    # it is like parsing a directory tree.
    # in fact it is not.
    # HallOfFame is a list
    if nextTargets!=[]:
        wantedTo=[]
        for nextTarget in nextTargets:
            wantedTo+=superAddress(toyProject(nextTarget))
        wantedTo=[pos for pos in wantedTo if pos in corr]
        HallOfFame+=wantedTo
        return seekOn(list(set(wantedTo)),list(set(HallOfFame)),corr)
    else:
        return HallOfFame

def seekAWrapper(initialFactor):
    correction=letIt()
    # maybe need another fix if wanted to parse file under subdirectory
    return seekOn([initialFactor],[],correction)

"""print(toyProject("exampleLinear.py"))
print("--popular shot--")
print(toyProject("sampleIntermediate.py"))
print("--blowjob--")"""
fuckingTerm="extractLinear.py"
Monad='/data/data/com.termux/files/home/lazer/metalearning/methodBank/analyzer/decrypter'
fuckMe=seekAWrapper(fuckingTerm)+[fuckingTerm]
print(fuckMe)
mover(fuckMe,Monad)
os.system('chmod +x shallowCopy.sh')
