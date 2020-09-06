a = [0, 1, 2, 3, 4, 3, 2, 1]
x0 = len(a)
x = 0
x1 = None
while True:
    if x < x0:
        x1 = a[x]
        x += 1
    else:
        x1 = a[0]
        x = 0
    print(x1)
