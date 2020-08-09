import random

def chaos(a,b):
  return "".join(random.choice(a) for x in range(b))

string0 = "https://cn.bing.com/"

print("Random String is",chaos(string0,8))
print("Random String is",chaos(string0,8))
print("Random String is", chaos(string0, 8))
# yeah this is how you speak.
# get those recorded?