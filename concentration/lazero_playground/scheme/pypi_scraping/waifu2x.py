from dbM import showX, up
import pypi_get as pg
from multiprocessing import Pool, freeze_support
from endmark import windowEndMarkEx as wex
import random
from sub2 import timeout
# not working on android, but that's fair.
# we can remote connect android via ssh!
# sweet dinner!
# TODO: switch between different mirrors so no one will block us.
# TODO: make it sound.
# TODO: tolerate missing packages.
# TODO: track new packages.

def parallel(x, v, z):
    with Pool(processes=x) as pool:
        return pool.map(v, z)


def workload(meta):
    x, y = meta
    try:
        pg_get = timeout(timeout=random.randint(13,15))(pg.get)
        # TODO: do more self-understanding like that.
        p = pg_get(y)
        print("fetching success")
        # print("fetching success")
        up_time = timeout(timeout=random.randint(7, 11))(up)
        up_time(x, p)
        # TODO: find out the cause of the freeze.
        # TODO: automatically relaunch the entire program in .cmd file.
    except:
        print("fetching error")
    return


if __name__ == "__main__":
    s = showX("projects", 0)
    if len(s) != 0:
        print("TOTAL PENDING WORK:", len(s))
    else:
        print("NO PENDING WORK, PROGRAM WILL EXIT.")
        exit()
    l = wex(s, random.randint(75, 125))
    ast = 0
    abs_limit = random.randint(650, 750)
    freeze_support()
    for meta in l:
        ast += len(meta)
        if ast <= abs_limit:
            # with parallel(len(meta), workload, meta) as locale:
            print("LOOP BEGINS HERE")
            assert len(parallel(len(meta), workload, meta)) == len(meta)
        else:
            # exit()
            break
    # exit()
    # TODO: find the real usage of exit()
        #     locale
        # TODO: find best scraping rate
        # TODO: autokill after 1500 samples
        # TODO: timeout in fetching the json
# for x,y in s:
#     try:
#         p = pg.get(y)
#         print("fetching success")
#         up(x, p)
#     except:
#         print("fetching error")
