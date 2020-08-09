# single char spliter
# multichar spliter
# manyfold
# invisible spliter and derivatives
# mixed spliter
# length, metadata, features
from trashlot import simpleExam, spliterPos
#from statistics import sum
with open("core.log","r") as fool:
    pool=fool.read()
    with open(pool[:-1]+"holidays.txt","r") as April:
        Sunny=April.read()
        globalWarming=spliterPos(Sunny,"\n")
        s=[[],[]]
        for k in range(len(Sunny)):
            s[0].append(sum(simpleExam(k,globalWarming)))
        print(s[0])
        print("--spliter--")
        for k in range(len(Sunny)*3):
            s[1].append(sum(simpleExam(k-2*len(Sunny)*2,globalWarming)))
        print(s[1])

