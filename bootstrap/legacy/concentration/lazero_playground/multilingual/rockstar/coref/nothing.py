import re

venus=open("POS.log","r")
dog=open("SOB.log","w")
genesis=[]
x0=0
# wrong fucking syntax.
# readline() is letter by letter
for genius in venus.readlines():
    x0+=1
    fuck=(lambda x: x!=-1)
    #print(genius)
    what=(fuck(genius.find("pronoun")) or fuck(genius.find("determiner")))
    #print(what)
    if what:
        genesis.append([re.match(r'[^ ]+',re.sub(r'^[ \t]+','',genius)).group(0),x0,genius])
print(genesis)
god=""
for hog in genesis:
    god+=(hog[0]+" ")
print(god)
venus.close()
dog.write(god[:-1]+"\n")
# what happened?
dog.close()


# the trailing newline is EOF.
