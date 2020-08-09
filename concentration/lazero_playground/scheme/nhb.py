import random

def getBuffer(x,y):
    with open(x, "r") as f:
        return f.read().split(y)

def get_random_alphaNumeric_string(core,y,stringLength=8):
    lettersAndDigits = core
    # lettersAndDigits = string.ascii_letters + string.digits
    return y.join((random.choice(lettersAndDigits) for i in range(stringLength)))

g = getBuffer("toolkit\\0.log"," ")
g0 = get_random_alphaNumeric_string(g," ")
print("Random construction:")
print(g0)
# well, beautiful.