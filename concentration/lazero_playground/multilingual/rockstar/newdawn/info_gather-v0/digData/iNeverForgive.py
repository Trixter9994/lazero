#import sys
#print(sys.argv[0])
#print(sys.argv[1])
import pickle
#1:import pickle
def virtual(v):
    with open("scavenger"+v+".pickle","rb") as _file:
        papi=pickle.load(_file)
        print(papi)
        print("--spliter--")

v0=["","0","1"]
for v in v0:
    virtual(v)
