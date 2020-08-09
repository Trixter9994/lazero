import re
from getCorrectList import letIt
from diffTool import diff
from fixer import snapshot
# the so-called functional programming is like a fancy shit for me.
# but that's another story.
# with presumption
# only solve local file notfound error.
# you can use difflib if you wish
# also the set, order, keyboard group theory
with open("errorLog.log","r") as fuck:
    fuckMe=list(filter((lambda x : x!= "") , fuck.read().split("\n")))[-4:]
    bird=list(enumerate(fuckMe))
    print(bird)
    nameOfSubject=fuckMe[1]
    lineOfTrouble=fuckMe[2]
    errorCode=fuckMe[3]
    extractName=re.findall(r'File "[^"]+',nameOfSubject)[0][6:]
    extractNumber=re.findall(r'", line \d*',nameOfSubject)[0][8:]
    print (extractName)
    print (extractNumber)
    extractMissingName=re.findall(r"[^']+'$",errorCode)[0][:-1]
    print (extractMissingName)
    candidateList=letIt()
    print(candidateList)
    consult=(lambda x:list(enumerate(x)))
    processFuck=list(map((lambda x: diff(x,extractMissingName)),candidateList))
    process=list(map((lambda x : max(list(map((lambda y:len(y)),x)))/len(x) ),processFuck))
    sortOfShit=list(map((lambda x:consult(x)),[processFuck,process]))
    print(sortOfShit[0])
    print(sortOfShit[1])
    getCandidateRank=list(sorted(sortOfShit[1],key=(lambda x:x[1])))
    print(getCandidateRank)
    getLastTwo=list(reversed(list(map((lambda x:x[0]),getCandidateRank[-2:]))))
    print(getLastTwo)
    getCandidate=list(map((lambda x:candidateList[x]),getLastTwo))
    print(getCandidate)
    snapshot(extractName[:-3]+"_fixed.py",extractName,extractMissingName,getCandidate[0],int(extractNumber))
#    print(processFuck)
#    print(process)
