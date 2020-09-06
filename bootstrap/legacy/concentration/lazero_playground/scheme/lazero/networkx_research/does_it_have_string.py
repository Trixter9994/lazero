# does it has string?
# how to get the string?
import random
def eat(a):
    t = type(a)
    # it must be some text somehow.
    if t == int:
        return False
        # this is not right. when at this point, problem occurs.
    elif t == str:
        return a
    # i believe these can be programs.
    elif t in [list, tuple]:
        # check the way to get it.
        return eat(random.choice(a))
    # man what will you gonna to do then, to learn shits?
    elif t in [set, frozenset]:
        return eat(random.choice(list(a)))
    elif t == dict:
        return eat(a[random.choice(list(a.keys()))])
    else:
        raise Exception("i do not know what shitty format you are using. consider learning more code and then inference.")
# how about consider understanding of python language?
# fuck! must be do with networkx?
# must be logical!
# you have memory!
def checkEval(a):
    assert type(a) == str
    if "=" not in a:
        return eval
    else:
        return exec
        # this is way too simple. I'm wondering whether this will work or not.
        # consider a parser? but inclined to read manual.
        # learn stuff?