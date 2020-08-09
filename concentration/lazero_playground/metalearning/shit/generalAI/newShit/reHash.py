def reHash(Grid):
    # this is for 2d arrays.
    # not sure about n-d arrays.
    Grid1=list(set([Grid.index(x) for x in Grid]))
    return [Grid[x] for x in Grid1]
