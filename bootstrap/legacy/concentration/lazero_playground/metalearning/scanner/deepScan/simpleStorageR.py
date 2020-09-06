import pickle
def storeAList(a):
    pickle.dump(a, open("oldFuckingPickle.pickle","wb"))

def storeList(a):
    pickle.dump(a, open("FuckingPickle.pickle","wb"))
