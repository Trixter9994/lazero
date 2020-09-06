import pickle
import dill
def returnList():
    return pickle.load(open("FuckingPickle.pickle","rb"))
def returnAList():
    return dill.load(open("oldFuckingPickle.dill","rb"))
def returnListR():
    return pickle.load(open("FuckingPickleR.pickle","rb"))
def returnFuck():
    return pickle.load(open("FuckingFucked.pickle","rb"))
def returnFuckMe():
    return pickle.load(open("FuckingFuckedMe.pickle","rb"))
def returnWTF():
    return pickle.load(open("FuckingWTF.pickle","rb"))
def returnFuckYou():
    return pickle.load(open("FuckingFuckYou.pickle","rb"))

def returnListV(a):
    # check length afterwards?
    # or create a table?
    # fuck.
    return pickle.load(open("megaDatabase/"+str(a)+".pickle","rb"))
def returnListF(a):
    return pickle.load(open("makeLove/"+str(a)+".pickle","rb"))
def returnListK(a):
    return pickle.load(open("goingToDie/"+str(a)+".pickle","rb"))
