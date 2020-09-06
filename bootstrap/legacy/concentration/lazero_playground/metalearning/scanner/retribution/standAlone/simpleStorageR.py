import pickle
import dill
def storeAList(a):
    pickle.dump(a, open("oldFuckingPickle.pickle","wb"))
def storeList(a):
    pickle.dump(a, open("FuckingPickle.pickle","wb"))
def storeListR(a):
    pickle.dump(a, open("FuckingPickleR.pickle","wb"))
def storeListV(a,b):
    # b for index of original context.
    pickle.dump(a, open("megaDatabase/"+str(b)+".pickle","wb"))
def storeListF(a,b):
    dill.dump(a, open("coreDump/"+str(b)+".dill","wb"))
def storeListK(a,b):
    pickle.dump(a, open("goingToDie/"+str(b)+".pickle","wb"))
    # now what? group these shits.