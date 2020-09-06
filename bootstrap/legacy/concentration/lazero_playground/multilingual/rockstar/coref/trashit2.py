#coding=utf-8
# this is for python2

# 2 unable to read pickle files created by 3 just like .doc and docx
# you can just put these things into database, like those corps.
import json #, pickle
'''with open("scavenger.pickle","rb") as _file:
    papi=pickle.load(_file)
    print papi
'''
def nothing(alist):
    for a in alist:
        for b in a:
            for c in b:
                for d in c:
                    for e in d:
                        print e
                    #print d
#                    for e,f in d:
#                        print e,"\t",f

with open("scavenger.json","r") as _file:
    # in json the tuple is the same as list.
    # some kind of minor loss.
    # neglible.
    papi=json.load(_file)
#    print papi
    nothing(papi)


