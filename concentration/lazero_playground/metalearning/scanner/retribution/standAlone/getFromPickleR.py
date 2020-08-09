import pickle
import dill
def returnList():
    return pickle.load(open("FuckingPickle.pickle","rb"))
def returnAList():
    return pickle.load(open("oldFuckingPickle.pickle","rb"))
def returnListR():
    return pickle.load(open("FuckingPickleR.pickle","rb"))
def returnListV(a):
    # check length afterwards?
    # or create a table?
    # fuck.
    return pickle.load(open("megaDatabase/"+str(a)+".pickle","rb"))
def returnListF(a):
    return pickle.load(open("coreDump/"+str(a)+".dill","rb"))
def returnListK(a):
    return pickle.load(open("goingToDie/"+str(a)+".pickle","rb"))