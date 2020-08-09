from getFromPickleR import returnList
# 316 fucks
links='../../../multilingual/rockstar/unicode-standard/retribution'
link=returnList()
def openf(a):
    with open(a,'r') as ak:
        return ak.read()

def returnLength():
    return len(link)

def indexRead(a):
    return openf('/'.join([links,link[a]]))

def newLineIndex(a):
    return indexRead(a).split('\n'),link[a]
# the format -> txt + timestamp + location