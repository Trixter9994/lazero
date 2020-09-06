# import csv
# never mind.
import random
import string
from tellno import randomAnswer

# i will give you an answer.
# never the less.
# named feeling.

def nowFail(b):
    with open("collective.csv", "a+") as f:
        f.write(b+"\n")

# you will have it.

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


# for x in range(1000000):
#     g = get_random_alphaNumeric_string()
#     g0 = str(int(randomAnswer()))
#     nowFail(g+","+g0)
