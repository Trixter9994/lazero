import os
import csv
from nameParser import getAll, getX
from stackMe import queue
from sensor import chaos


def distance(a, b):
    with open(a, "a+", newline="") as f:
        # for d in b:
        #   f.write(d+"\n")
        c = csv.writer(f)
        for d in range(len(b) - 1):
            c.writerow([b[d], b[d + 1]])


def checker(a):
    return a[0] != a[1]


def readX(x, s, n, k):
    svn = getX(n)
    with open(x, "r") as csvfile:
        spamreader, sfv = csv.reader(csvfile), queue(2)
        for row in spamreader:
            sf = [int(row[0]), row[1]]
            sfx = chaos(sf)
            if not (type(sfx) is type(None)):
                if len(sfx) > 0:
                    sfv.queue([sf[0], sfx[-1], sf[1], sfx[0]])
                chk = sfv.dump()
                if len(chk) == 2:
                    if checker(chk):
                        ch0, ch1 = chk
                        ch2, ch3, ch4, ch5 = ch0[0], ch1[0], ch0[1], ch1[-1]
                        fma = str(ch2) + str(ch3)
                        s(k + "\\cross-" + "-".join(svn + [fma]) + ".csv", [ch4, ch5])
                if len(sfx) > 1:
                    s(k + "\\normal-" + "-".join(svn) + ".csv", sfx)


xv = "all\\fileShare"
xvg = getAll(xv)[0]
op = os.listdir(xv)
# o = op[0]
# print(o)
for o in op:
    readX(xv + "\\" + o, distance, o, xvg)
