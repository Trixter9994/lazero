from dbM import showX, up
import pypi_get as pg

s=showX("projects",0)
for x,y in s:
    try:
        p=pg.get(y)
        print("fetching success")
        up(x,p)
    except:
        print("fetching error")
