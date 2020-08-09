from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize
import re

list_stopWords=list(set(stopwords.words('english')))

def RemoveStopwordsReturnList(example_text):
    list_words=word_tokenize(re.sub(r"[^a-z _]"," ",example_text.lower()))
#    list_words=word_tokenize(example_text)
    return [w for w in list_words if not w in list_stopWords]

def EnglishStemmer(quack):
    return SnowballStemmer("english").stem(quack)

def ReturnSynsets(word):
    return wordnet.synsets(word)

def ProcessWordList(list0):
    k0=[]
    for k in list0:
        k0+=ReturnSynsets(k)
    return set(k0)

def ReturnExampleWithDefinition(SS):
    return [SS.definition(),SS.examples()]

def ReturnNameWithConnector(SS):
    return [SS.name(),re.match(r"^[^\.]+",SS.name())[0]]

def UberCommando(SS):
    red=ReturnExampleWithDefinition(SS)
    rnc=ReturnNameWithConnector(SS)
    red0=red[0]
    def runoob(red0):
        r1=[]
        for r0 in RemoveStopwordsReturnList(red0):
            r1.append(EnglishStemmer(r0))
        return set(r1)
    r1=runoob(red0)
    red1=red[1]
    r2=[]
    for red2 in red1:
        r2.append(runoob(red2))
    return ([r1,r2],rnc)

# use readlines to create a list.
# this time we write results into csv files.

a=open("gamma.csv","r")
b=open("delta.csv","w+")
c=open("psi.csv","w+")
d=open("epsilon.csv","w+")
#try:
wordlist=[]
for p in a.readlines():
#    print (p)
    p=re.sub("\n","",p)
#    p0=steam(p)
    if p=="":
        pass
    else:
        wordlist.append(p)

wordlist=set(wordlist)
a.close()

synet=ProcessWordList(wordlist)
synet0=[]
for s0 in synet:
    synet0.append(UberCommando(s0))
for s1 in synet0:
    s2=s1[0]
    # definition and example connections.
    s3=s1[1]
    # namespace connections.

#    b.write(s3[0])
    if s2[0]!="":
        for sk2 in s2[0]:
            b.write(s3[0]+","+sk2+"\n")
#    b.write("\n")
    # this for definition
#    c.write(s3[0])
        for sk3 in s2[1]:
            for sk4 in sk3:
                c.write(s3[0]+","+sk4+"\n")
    else:
        pass
#    c.write("\n")
    # this for examples
    d.write(s3[0]+","+s3[1]+"\n")
    # this for namespace

b.write("\b")
c.write("\b")
d.write("\b")

import time

time.sleep(5)
b.close()
c.close()
d.close()
#        print (p0)
#        try:
#            b.write(p0+","+p+"\n")
#        except:
#            pass
#except:
#    pass
#b.write("\b")
#a.close()
#b.close()
