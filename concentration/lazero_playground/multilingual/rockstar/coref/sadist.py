import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 
ion=open("README","r")
## Dummy text 
txt0=ion.read() 
ion.close()
# sent_tokenize is one of instances of  
# PunktSentenceTokenizer from the nltk.tokenize.punkt module 
def jerkoff(txt):
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

    masochist=[]
    for k in tags:
        sadist=list(filter((lambda x:x[0]!="."),k))
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
#print(masochist)
    return masochist        

submarine=list(filter((lambda x:x!=""),txt0.split("\n")))
bear=[]
for penguin in submarine:
    bear.append(jerkoff(penguin))
print(bear)
