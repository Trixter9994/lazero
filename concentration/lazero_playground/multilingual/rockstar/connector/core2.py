from nltk.stem.snowball import SnowballStemmer
import re
def steam(quack):
    return SnowballStemmer("english").stem(quack)

# use readlines to create a list.
# this time we write results into csv files.

a=open("alpha.csv","r")
b=open("gamma.csv","w+")

#try:
for p in a.readlines():
#    print (p)
    p=re.sub("\n","",p)
    p0=steam(p)
    if p0!=p:
        pass
    else:
#        print (p0)
        try:
            b.write(p+"\n")
        except:
            pass
#except:
#    pass
b.write("\b")
a.close()
b.close()
