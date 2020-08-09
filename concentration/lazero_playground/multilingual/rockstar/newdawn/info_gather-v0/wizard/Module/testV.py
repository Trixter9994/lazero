from verifyIfWorks import to_tables, to_columns, to_sample
from processList import simpleShit
from getFromPickle import returnAList
def theOtherDay(p):
    yankee='../'+p+'/fuckyou.db'
    jerks=list(map((lambda x:x[0]),to_tables(yankee)))
    print(jerks)
    to_sample(yankee)
    der=to_columns(jerks,yankee)
    print(der)
    pint=[simpleShit(dec) for dec in der]
    print(pint)

for jerk in returnAList():
    theOtherDay(jerk)
    print("--","spliter:",jerk,"--")
