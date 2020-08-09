import re
#from getCorrectList import letIt
#from diffTool import diff
from fixerv0 import snapshot
# the so-called functional programming is like a fancy shit for me.
# but that's another story.
# with presumption
# only solve local file notfound error.
# you can use difflib if you wish
# also the set, order, keyboard group theory
with open("AnotherStory.log","r") as fuck:
    fuckMe=list(filter((lambda x : x!= "") , fuck.read().split("\n")))[:3]
    bird=list(enumerate(fuckMe))
    print(bird)
    nameOfSubject=re.findall(r'^[^:]+',fuckMe[0])[0]
    print(nameOfSubject)
    lineOfTrouble=re.findall(r"^\d*",fuckMe[0].replace(nameOfSubject+":",""))[0]
    print(lineOfTrouble)
    errorCode=re.findall(r"[^ ]+$",fuckMe[1])[0][1:-1]
    print(errorCode)
#    extractName=re.findall(r'File "[^"]+',nameOfSubject)[0][6:]
#    extractNumber=re.findall(r'", line \d*',nameOfSubject)[0][8:]
#    print (extractName)
#    print (extractNumber)
# death to all lawyers
    extractMissingName=re.findall(r"Perhaps you meant [^ ]+",fuckMe[2])[0][(7+4+6+1):]
#    print(extractMissingName)
# conclution is simple.
# it is nothing.
    print (extractMissingName)
    snapshot(nameOfSubject[:-3]+"_fixed.hs",nameOfSubject,errorCode,extractMissingName,int(lineOfTrouble))
# you are hitting a fake target.
#    print(processFuck)
#    print(process)
