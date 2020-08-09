import re
from endmark import windowConv

# TODO: fuzzy search
# TODO: interpret user's mood and intention


def ranker(a, b):
    res = re.findall(r'{}'.format(re.escape(b)), a)
    return len(res)


def listRanker(a, b):
    return [(x, ranker(a, x)) for x in b]


def possibleRanker(a, b, window_size):
    b0 = windowConv(b, window_size)
    b1 = listRanker(a, b0)
    return b1


def possibleWindowSize(b, sigma):
    assert sigma < 1 and sigma > 0
    b0 = len(b)
    b1 = round(b0 * sigma)
    b2 = list(range(b1, b0 + 1))
    return b2


def ranky(a, sigma, window_size):
    assert sigma < 1 and sigma > 0
    assert type(window_size) == int and window_size > 3
    def flattern(x): return [z for y in x for z in y]
    return {b: [possibleRanker(a, b, x) for x in possibleWindowSize(b, sigma)] for b in flattern([windowConv(a, x) for x in possibleWindowSize([None for y in range(window_size)], sigma)])}
