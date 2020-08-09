import re
# import re
# more than three.
# deadbeef.
# must be in range.
def killThem(a,f):
    l=len(a)
    a0=[[] for r in range(l)]
    p = re.compile("[0-9A-F][0-9A-F][0-9A-F][0-9A-F]*")
# do we really need that chart detector? yes.
# anything related to unicode must be analyzed.
# range can be fetched from title (really? what if it is mixed with charts?)
# we have names for each fucking codepoint. never be worried.
    for r in range(l):
        try:
            for m in p.finditer(a[r]):
                fm=m.group()
                if f(fm):
                    a0[r].append([m.span(), fm]) # it is the charIndex.
        except Exception:
            pass
    return a0
    # what do you want to grasp?
def getFucked(a):
    l=len(a)
    a0=[[] for r in range(l)]
    p = re.compile("\w*")
# do we really need that chart detector? yes.
# anything related to unicode must be analyzed.
# range can be fetched from title (really? what if it is mixed with charts?)
# we have names for each fucking codepoint. never be worried.
    for r in range(l):
        try:
            for m in p.finditer(a[r]):
                # fm=
                # if f(fm):
                a0[r].append([m.span(), m.group()]) # it is the charIndex.
        except Exception:
            pass
    return a0
# just check the name of the following.
    # how to use along the used file?
# how to understand technical shit?