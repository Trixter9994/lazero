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
s1=[]
# relative position?
for r in range(len(s0)):
        s3=re.findall(r'\w*',s0[r])
        l0,l1=len(s1),len(s3)
        if l0<l1:
                for i in range(l1-l0):
                        s1.append([])
        for i,m in enumerate(s3):
                s1[i].append([r,m])

# for l in range(len(s1[0])):
#         print(s1[0][l],s1[1][l])
try:
        simpleStorageR.storeListK(s1,v0)
        print("#",v0,"applied.")
except:
        print("#",v0,"failed.")