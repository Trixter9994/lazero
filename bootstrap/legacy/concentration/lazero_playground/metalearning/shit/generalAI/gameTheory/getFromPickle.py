import pickle

def returnList():
    return pickle.load(open("FuckingPickle.pickle","rb"))

def returnAList():
    return pickle.load(open("newFuckingPickle.pickle","rb"))
