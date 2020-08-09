def getShit(a):
  with open(a, "r") as f:
    return f.read()

def shitter(a):
  r=a
  r0=list(set(r))
  r1 = [r.split(x) for x in r0]
  return r1

r = getShit("tensorflow.text")
r0 = shitter(r)
# able to generate infinite rubbish.
# HoTT?
for y in r0:
  # print(y)
  for x in y:
    print(shitter(x))