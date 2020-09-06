from sparse import checkUnique
with open("baidu.log") as f:
    f0=f.read()
    m=checkUnique(f0)
    print(m)
