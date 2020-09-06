import endmark
# TODO: unhurtful marks reserved for intervention.
# TODO: use relative visibility to get relative location of visual words.
with open("networkx_reference.txt") as f:
    f0 = f.read()
    f1 = f0.split("\n")
    for x in f1:
        e = endmark.phraseStartMark(x, ">>>")
        e4 = endmark.phraseStartMark(x, "://")
        # print(e)
        # print(e4)
        e0 = endmark.containRestrict(x, "=", 1, 3)
        e5 = endmark.containRestrict(x, ".", 1, 3)
        if e0:
            # print("has equal sign")
            # print(x)
        if e5:
            # print("has dot sign")
            # print(x)
        e1 = endmark.phraseSegment(x, "{", "}")
        e2 = endmark.phraseSegment(x, "(", ")")
        e3 = endmark.phraseSegment(x, "[", "]")
        # for x in [e1, e2, e3]:
            # print(x)