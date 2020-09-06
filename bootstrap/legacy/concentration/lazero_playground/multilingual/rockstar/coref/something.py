import re

venus=open("POS.log","r")
dog=open("SOB.log","w")
genesis=[]
for x in range(2):
    genesis.append([])
    # make sure that it would be dfferent.
x0=0
# wrong fucking syntax.
# readline() is letter by letter
for genius in venus.readlines():
    x0+=1
    fuck=(lambda x: x!=-1)
    #print(genius)
    what=fuck(genius.find("pronoun")) 
    chinese=fuck(genius.find("determiner"))
    #print(what)
    if what:
        genesis[0].append([re.match(r'[^ ]+',re.sub(r'^[ \t]+','',genius)).group(0),x0,genius])
    elif chinese:
        genesis[1].append([re.match(r'[^ ]+',re.sub(r'^[ \t]+','',genius)).group(0),x0,genius])
    else:
        pass
print(genesis)
god=["",""]
for hog in genesis[0]:
    god[0]+=(hog[0]+" ")
print(god)
for hotdog in genesis[1]:
    god[1]+=(hotdog[0]+" ")
venus.close()
dog.write(god[0][:-1]+"\n"+god[1][:-1]+"\n")
# what happened?
dog.close()


# the trailing newline is EOF.
