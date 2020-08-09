with open("mutool.log") as f:
    f0=f.read()
    f1=f0.split("\n")
    f2=[x[0] for x in f1]
    # f3=[x[1] for x in f1]
    f3=set(f2)
    f4={x:[y for y in range(len(f2)) if f2[y]==x] for x in f3}
    # TODO: intepret meaning according to the shape of symbols