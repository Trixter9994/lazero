from skimRead import sk
from randomMath import returnS

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
  print(x)
  try:
    eval(x)
    print("passed!")
  except:
    print("failed")
  # well, this is awful. but i like it.