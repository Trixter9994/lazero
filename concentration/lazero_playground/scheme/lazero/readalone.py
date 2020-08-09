# to make things simpler.
import random
def randomReadOneLine(x):
    with open(x, "r") as f:
        return random.choice(f.read().split("\n"))