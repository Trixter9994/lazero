from nltk.corpus import wordnet as wn
import re

def groupy(k0):
    w=wn.synsets(k0)
    r=[]
    for w0 in w:
        r.append(w0.lemma_names())
    return r

a=open("gamma.csv","r")
b=open("sigma.csv","w+")

for k in a.readlines():
    k=re.sub("\n","",k)
    try:
        g=groupy(k)
        for g0 in g:
            for g1 in g0:
                if g1==k:
                    pass
                else:
                    b.write(g1+","+k+"\n")
    except:
        pass
b.write("\n")

a.close()
b.close()
