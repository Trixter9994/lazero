import pickle
def returnAListR(p):
    return pickle.load(open(p+"/newFuckingPickle.pickle","rb"))
def returnAList():
    return pickle.load(open("newFuckingPickle.pickle","rb"))
