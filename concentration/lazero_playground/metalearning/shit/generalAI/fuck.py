from bs4 import BeautifulSoup
from simpleStorage import storeAList
def soup(a):
    return BeautifulSoup(a)

def openShit(b):
    f=""
    with open(b,"r") as fuck:
        f=fuck.read()
    return f

def openList(b):
    return list(filter((lambda x:x!=""),openShit(b).split("\n")))

def shit(x):
    s=soup(openShit(x)).find_all(name="ul",attrs={"class":"repo-list"})[0].find_all(name="a",attrs={"class":"v-align-middle"},recursive=True)
    return [s0.get_text() for s0 in s]

# fuck you.


d=[list(filter((lambda x:x!=[]),[shit(c) for c in b])) for b in [openList(a) for a in openList("trauma.log")]]
storeAList(d)
#e=[[shit(c) for c ]]
#print(len(d))
