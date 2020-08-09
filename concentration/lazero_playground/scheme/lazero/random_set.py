import random
import copy
import difflib

def export_sets(a, window_size):
    # print(a)
    assert type(window_size) == int and window_size > 1
    assert type(a) in [list, str] and len(a) > 2
    return [frozenset(a[x:x+window_size]) for x in range(len(a)-window_size)]


def meta_sets(a, window_size, evolution=0):
    assert type(evolution) == int and evolution >= 0
    a0 = export_sets(a, window_size)
    if evolution == 0:
        return a0
    else:
        return meta_sets(a0, window_size, evolution-1)


def bidirection_split(a):
    b = set(a)
    c = {x: a.split(x) for x in b}
    return c


def check_common_words(a):
    a0 = copy.copy(a)
    a2 = []
    while True:
        a1 = []
        if len(a0) not in [0, 1]:
            a3 = [a0.pop(random.choice(list(range(len(a0)))))
                  for x in range(2)]
            s1, s2 = a3
            match = difflib.Differ()
            a2.append(list(match.compare(s1, s2)))
        else:
            break
    return a2


def split_common(a):
    b = bidirection_split(a)
    c = {x: check_common_words(b[x]) for x in b.keys()}
    return b, c
