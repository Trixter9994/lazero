import pickle
papi=""
with open("scavenger.pickle","rb") as _file:
    papi=pickle.load(_file)
    print (papi)
#fuck
papi0=""
with open("scavenger0.pickle","rb") as _file:
    papi0=pickle.load(_file)
    print (papi0)

joker=(lambda nope0:nope0[:-1] if nope0[-1]=="\n" else nope0)
joke=(lambda nope0: list(filter((lambda x:x!=""),nope0)))

nope=""
with open("core.log","r") as tits:
    nope=tits.read()

with open(joker(nope)+"alphabets.txt","r") as dickhead:
    shit=dickhead.read().split("\n")
    shit0=joker(joke(shit))
    print(shit0)
