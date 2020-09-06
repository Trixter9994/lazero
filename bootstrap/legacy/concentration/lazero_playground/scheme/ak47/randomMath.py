import random


def returnS():
    sx = ""
    s = "xyz"
    s0 = "0123456789"
    s1 = "-+=*/^"
    # s2=
    # rules? prolog?
    def x(): return random.choice(s), 0
    def y(): return random.choice(s0), 1
    def z(): return random.choice(s1), 2
    x1 = -1
    y0 = 0
    for x0 in range(10):
        if x1 == 1:
            if y0 != 0:
                y2 = random.choice([x, y, z])
            elif x1 != -1:
                y2 = random.choice([x, z])
            else:
                y2 = x
        elif x1 == 0:
            y2 = random.choice([y, z])
        else:
            y2 = random.choice([y, x])
        y0, y1 = y2()
        x1 = y1
        sx += y0
    return sx
    # return x+y+z
# print(returnS())
# random math formula?
# well, we can always delete them, make the tree clean.