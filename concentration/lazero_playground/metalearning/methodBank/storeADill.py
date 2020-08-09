import dill as pickle
def storeAList(a):
    pickle.dump(a, open("newFuckingDill.dill","wb"))
