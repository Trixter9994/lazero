import pandas

# alright. now metapromramming.
# what the fuck is going on?
# what is this shit?
# what the fuck is going on?

def shitshow(x):
    p = pandas.read_csv(x)
    # print(len(p))
    # this is really strange.
    if len(p)>20000:
        p=p.sample(20000)
    # replace true?
    # print(p)
    # great.
    # print(dir(p))
    # i do not know what the fuck is going on.
    # the only thing i know the most is i am fucked up.
    p0 = p.to_numpy()
    # print(p0)
    p1 = p0[:, 0]
    p2 = p0[:, 1]
    # print(p1)
    # print(p2)
    return p1, p2
# well this is great.