from random_set import meta_sets

with open("baidu.log") as f:
    f0=f.read()
    m=meta_sets(f0,3,3)
    print(m)
