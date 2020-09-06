import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 
ion=open("README","r")
anion=open("SOB.log","r")
onion=list(filter((lambda x: x!=""),anion.read().split("\n")))
# two lines.
union=[]
for x in range(len(onion)):
    union.append(list(filter((lambda x: x!=""),onion[x].split(" "))))
# actually two groups.
anion.close()
# check if in the list.
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
#print(bear)
# what next?
# solving the puzzle!
# what is the pronoun?
# i define something as the puzzle: something that repeatedly appear locally.
# pronouns are of course puzzles, and other words appear frequently are also puzzles.
# general process: can solve locally -> if cannot then save session, keep unbinded pairs and lookup nearby sessions for reference -> if not solved then keep expanding the search area.
# keep doubtful even if it is solved. expand the whole thing to do the task.
# remember the matching object can either e a word, sentence, paragraph, unmentioned identity and more.
# isinstance(lst, str)
# only if the set is usable
# you would not regret.
enumerator=[0,0,0,0]
for paragraph in bear:
    enumerator[0]+=1
    print("-----paragraph: ",enumerator[0])
    for sentence in paragraph:
        enumerator[1]+=1
        print("----sentence: ",enumerator[1])
        for subsentence in sentence:
            enumerator[2]+=1
            print("---subsentence: ",enumerator[2])
            for word in subsentence:
                enumerator[3]+=1
                if word[1] in union[0]:
                    print("--word: ",enumerator[3]," pronoun: ",word)
                elif word[1] in union[1]:
                    print("word: ",enumerator[3]," determiner: ",word)
                else:
                    pass
