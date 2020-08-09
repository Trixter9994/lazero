from getLinkage import reinforce
# TODO: reduce errors by making rules or hard-coded programs
with open("baidu.log") as f:
    f0 = f.read()
    m = reinforce(f0, 50)
    print(m)
