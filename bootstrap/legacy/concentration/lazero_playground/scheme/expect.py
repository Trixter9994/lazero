# connect to a graph database. anything will work.
# randomly generate data?
# import random
# must it be connected?
# must it not?
# maybe? no strong logic applied?
import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print("Random String is ", randomString())
print("Random String is ", randomString(8))
print("Random String is ", randomString(8))
# well it is the spirit.