from skimRead import sk
from randomMath import returnS

def sudo0():
    r1=[]
    r = returnS()
# oh we will develop some rules after this, right?
# how to speak the language?
# use eval function?
# oh fuck.
# how comes.
    r0 = sk(r, 3)
# print(r0)
# how to check a sentence is valid or not?
# i just want the fucking code.
    for x in r0:
      #print(x)
      p0=[x]
      try:
        eval(x)
        p0.append(0)
#        print("passed!")
      except:
        p0.append(1)
      r1.append(p0)
    return r1

def sudo1(x):
    x0=[sudo0() for y in range(x)]
    return [x for y in x0 for x in y]
# flattern?
#        print("failed")
      # well, this is awful. but i like it.
