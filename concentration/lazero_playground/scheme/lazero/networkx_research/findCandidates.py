from getFromPickleR import returnWTF
from buildAGraph import addEdge
from does_it_have_string import eat, checkEval
import traceback
import copy
# even if donno what is going on, we have to proceed.
# GET THE FEEDBACK. REAL TIME.
r2048 = returnWTF()
# need flattern?
y = "random"
n = []
# learn different stuff? may it help?
# we are checking.
# help me with this shit.
# this is language agnostic.

def catchMyError(a, b):
    try:
        return a(b)
    except Exception as e:
        e0 = traceback.format_exc()
        print("error details:")
        print(e0)
        return e

# i have many errors, more than i can ever create one week!
# you know how I can get confused.


def findSolution(codel, reverse=False):
    solution = []
    code = copy.copy(codel)
    while code != "":
        print(code)
        c = catchMyError(checkEval(code), code)
        solution.append(c)
        # print(c, type(c))
        if reverse == False:
            code = code[:-1]
        elif reverse == True:
            code = code[1:]
        else:
            raise Exception("check the second parameter please?")
    return solution

# is it obvious to you?
# always the matrix trick.
for x in r2048:
    for z in x:
        if y in z:
            n.append(z)
            break
        # I want to speed up my programming.
        # what about just fucking parse them all?
        # what cannot be opened we just move it away.
# print(n)
# what is invalid syntax? why you complain?
# not just once.
# what you have done?
# find your fix.
for x in range(2):
    code = eat(n)
# i don't really doubt this.
# not exactly.
    # we are gonna twist them?
    # if we really want to learn, better access the dark web.
    # and that web is only avaliable after some computation.
    # find something in common.
    f = findSolution(code)
    print(f)
    f = findSolution(code, True)
    print(f)
    # that is not so helpful, isn't it?
    # try windowing, replacing?
    # find suspicious words.
    # code = code[-1:]
    # this is one way.
    # and another way.
    # detailed!
    # random dropping?
    # code = code.replace(a, "")
    # find different crap.
    # what is your method?
    # better crap.
    # the hint.
    # get different crap?
# why can you not to do anything?
# this time we do not have the traceback?
# tell me what is wrong with the code?
# it seems the calculation is mine.
# ridiculus.
# get different thing?
# addEdge(n)
# store the thing.
# run few shits?
# run them.
# well it is not about basic functions.
# you are gonna record this. and save time.
# print(r2048)
# run random craps.
# save my time to produce crap.
# custom predicates.
# get it done.
# what to search?
# query.
# learn similar words.
# many failsafe modules.
# learn what is special about those characters?
# so be it. if you want to find what is magical, better use it.
