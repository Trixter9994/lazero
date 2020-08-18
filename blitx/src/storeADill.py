import dill as pickle


def storeAList(a):
    pickle.dump(a, open("newFuckingDill.dill", "wb"))


def storeXList(a, b):
    assert type(b) == str and len(b) > 1
    pickle.dump(a, open(b+".dill", "wb"))
