# fuck me.
import readLikeHuman
import sys,re
import simpleStorageR
v0=sys.argv[1]
# this is string.
# 227 missing? -> CJK unified ideographs. -> fucking hell.
b0=readLikeHuman.Meta(int(v0))
s0=b0.content
# print(s0)
s1=[[],[]]
# relative position?
for r in range(len(s0)):
        s3=re.findall(r'\w*',s0[r])
        for s4 in s3:
                s5=[index for index, value in enumerate(s3) if value == s4]
                if s4 not in s1[0]:
                        l=len(s1[0])
                        s1[0].append(s4)
                        s1[1].append([])
                        for x in s5:
                                s1[1][l].append([r,x])
                else:
                        e=s1[0].index(s4)
                        for x in s5:
                                s1[1][e].append([r,x])
# for l in range(len(s1[0])):
#         print(s1[0][l],s1[1][l])
try:
        simpleStorageR.storeListF(s1,v0)
        print("#",v0,"applied.")
except:
        print("#",v0,"failed.")
