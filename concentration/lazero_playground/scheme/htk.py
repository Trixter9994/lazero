# import
import random
import string


def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

i = input("Say out your problem.\n")
print(get_random_alphaNumeric_string())
# well this is cheating.
# i don't believe whether this works or not.
# we do not have language structure, and we are told to behave like the language structure.