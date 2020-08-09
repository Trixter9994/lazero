import difflib
"""
a, b = "same order words", "not same but order words matched"
thug=[a[i:i+n] for i, _, n in difflib.SequenceMatcher(None, a, b).get_matching_blocks() if n]
print(thug)"""
# i don't give a shit about time complexity.
def same_shit(superstring,throttle=0):
    gnu=[]
    # you could make something overlappy.
    # no dude you are kidding me.
    # swipe off the corner!
    for k in range(len(superstring)-2-throttle):
        a, b = superstring[2+k:],superstring[:k+1]
        thug=[a[i:i+n] for i, _, n in difflib.SequenceMatcher(None, a, b).get_matching_blocks() if n]
        gnu.append(thug)
    return gnu
shit="hell yeah i am back. oh yeah i am kidding . just kkkk"
print(same_shit(shit))
