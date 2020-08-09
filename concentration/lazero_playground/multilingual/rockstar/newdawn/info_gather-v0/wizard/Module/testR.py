from verifyIfWorks import to_tables, to_columns, to_sample
from processList import simpleShit
from getFromPickle import returnAListR
# you simply stay put. Cannot be moved around.Right at the spot.
# If you wanna create your own function, go source code generating.
def theOtherDay(p):
    yankee='/data/data/com.termux/files/home/lazer/multilingual/rockstar/newdawn/info_gather-v0/wizard/'+p+'/fuckyou.db'
    jerks=list(map((lambda x:x[0]),to_tables(yankee)))
    print(jerks)
    to_sample(yankee)
    der=to_columns(jerks,yankee)
    print(der)
    pint=[simpleShit(dec) for dec in der]
    print(pint)

def jokeMeUp():
    for jerk in returnAListR("/data/data/com.termux/files/home/lazer/multilingual/rockstar/newdawn/info_gather-v0/wizard/Module"):
        theOtherDay(jerk)
        print("--","spliter:",jerk,"--")
