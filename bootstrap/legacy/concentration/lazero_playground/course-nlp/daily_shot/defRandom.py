import random
def getR(a, b):
  # a is for length. b is for limit.
  # random pop?
  # l0=len(a)
  l=list(range(a))
  if a <= b:
    return l
  else:
    for x in range(a - b):
      l.pop(random.choice(list(range(a - x))))
  return l