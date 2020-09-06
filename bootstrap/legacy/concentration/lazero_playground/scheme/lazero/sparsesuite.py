from sparse import fixedQueue

with open("baidu.log") as f:
    f0=f.read()
    m=fixedQueue(f0,50)
    print(m)
