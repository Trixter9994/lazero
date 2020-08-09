import dill as pickle


def returnAList():
    return pickle.load(open("newFuckingDill.dill", "rb"))


def returnXList(b):
    assert type(b) == str and len(b) > 1
    return pickle.load(open(b+".dill", "rb"))
