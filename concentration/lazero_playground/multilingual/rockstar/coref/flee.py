# this is only for portabilization.
# to simplify the sentence for easy analyzation.

import nltk, json, pickle 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 
ion=open("README","r")
## Dummy text 
txt=ion.read() 
# sent_tokenize is one of instances of  
# PunktSentenceTokenizer from the nltk.tokenize.punkt module 
  
tokenized = sent_tokenize(txt) 

tags=[]

for i in tokenized: 
      
    # Word tokenizers is used to find the words  
    # and punctuation in a string 
    wordsList = nltk.word_tokenize(i) 
  
    # removing stop words from wordList 
#    wordsList = [w for w in wordsList if not w in stop_words]  
    # you are such a fool.

    # HOW THE FUCK CAN YOU FUCKING REMOVE THE FUCKING STOPWORDS?

    #  Using a Tagger. Which is part-of-speech  
    # tagger or POS-tagger.  
    tagged = nltk.pos_tag(wordsList) 
    tags.append(tagged)  
#    print(tagged) 
#print(tags)
# ---  [ spliter ]  --- #

#i=open("README","r")
fulltext=list(filter((lambda x: x!=""),txt.split("\n")))
for x in range(len(fulltext)):
    fulltext[x]=len(list(filter((lambda x:x!=""),[pos for pos in fulltext[x].split(".")])))
#    this is crap
    '''for y in range(len(fulltext[x])):
        fulltext[x][y]=list(filter((lambda x:x!=""),[pos for pos in fulltext[x][y].split(",")]))
        for z in range(len(fulltext[x][y])):
            fulltext[x][y][z]=list(filter((lambda x:x!=""),[pos for pos in fulltext[x][y][z].split(" ")]))'''

#print(fulltext)
# the length should be the same.

#print(len(tags),len(fulltext))

masochist=[]
for k in tags:
    sadist=list(filter((lambda x:x[0]!="." and x[0]!="?"),k))
    mark=list(reversed(sorted([pos for pos in range(len(sadist)) if sadist[pos][0]==","])))
    previous=len(sadist)
    temp=[]
    mark.append(-1)
    for m in mark:
        # you can filter out the weird things.
        temp.insert(0,sadist[m+1:previous])
        previous=m
    masochist.append(temp)
#    for d in k:

scavenger=[]
for lesbian in range(len(fulltext)):
    scavenger.append([])
# lists are the same here.
# do not use the fucking method again.
#print(scavenger)
consteller=0

for x0 in range(len(scavenger)):
    consteller+=fulltext[x0]
#    print("x=",x0)
    for y in range(fulltext[x0]):
#        print("y=",y)
        nodejs=consteller-fulltext[x0]+y
#        print("nodejs=",nodejs)
        gay=masochist[nodejs]
#        print(gay)
        scavenger[x0].append(gay)
#print(masochist)
# i plan to make a map for the mistyping shit.
"""
for guido in range(len(masochist)):
    print(masochist[guido])
print(fulltext)
print("---[fulltext spliter]---")
print(masochist)
for vessle in range(len(scavenger)):
    print("---[scavenger spliter]---")
    print(scavenger[vessle])
"""
print(scavenger)
#this list contains paragraph - sentence - subsentence - word separation with POS data inside.
# we need to store it into some sort of format for further analysis.

ion.close()

# pickle format may contains malicious code.
with open('scavenger.pickle', 'wb') as filehandle:
    # store the data as binary data stream
    pickle.dump(scavenger, filehandle)
with open('scavenger.json','w')as filehandle:
    # json format is not binary
    json.dump(scavenger,filehandle)

