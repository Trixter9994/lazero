import re
u = """\t hello you  mother fucker     \t     fuck you bitch      bitch      23443243234  23 42 35 23 5 26  643                        we shall split this fuck by the motherfucking newline should we?
 but you have    fucking told me that you can find that shit somewhere didn't you?
 oh calm the fuck down.          [the fucking tab is invisible here.]
"""
#verbose=re.compile(r'\b')
# print (u.split('\n'));
list0 = u.split('\n');

"""def func(x):
  if x == "":
    return 0
  else:
    return 1"""
# make sure the thing is configured.
# hardcore forever!

for items in list0:
  # let's extract the fucking sequence .let's extract the fucking sequence. let's extract the fucking sequence.
  # simple judgement.
  item0=items.split(" ")
  simulink0 = list(map(lambda x: (int)(x != ""), item0))
  # this is to make numerical calculations easier.
  item1 = list(filter(lambda x: x != "", item0))
  #that link is important.
  #print (simulink0)
  simulink1 = list(map(lambda x: (int)(x != "\t"), item1))
  print(simulink0)
  #very damn important.
  # you may consider other shits.
  item2 = list(filter(lambda x: x != "\t", item1))
  # we could make it multithreaded.
  # after counting the fucking newlines
  # it could be better if making some recursive functions.
# print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))