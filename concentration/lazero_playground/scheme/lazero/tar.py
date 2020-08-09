from random_set import split_common
with open("index.html") as f:
    f0=f.read()
    m,m0=split_common(f0)
    print(m)
    print("__________________SPLITER__________________")
    print(m0)
