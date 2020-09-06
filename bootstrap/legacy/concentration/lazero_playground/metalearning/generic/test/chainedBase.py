from getFromPickle import returnAList
# if passed the test, then onward to next
# if not passed, slice and move to next test.
# return the sum of all successful test.
# the integrity is defined as the biggest clogged group found in test.
# better use keyboard tolerance mechanism.
# straight line mechanism, nearst neighbor mechanism.

#group groupChar
# group -> g_roup <delay>
# group -> gloup <replace>
# group -> ggroup <repeat>
# if it isn't the end, do not stop.
# group -> roupg <swap>
#group groupCharGroup
# WARNING WE HAVEN'T BEEN USING A STENOTYPE SO BE CAREFUL OF ARRANGEMENTS.
# better use the real keyboard to do this job.

def confusionMatrixBoost(a,b,c):
    return [[c(a0,b0) for a0 in a] for b0 in b]

d=(lambda x:[f for g in x for f in g])
f=returnAList() # actually a dict
vr=confusionMatrixBoost("group","groupChar",(lambda x,y: [x==y, y in f[x],y in [f1 for f1 in d([f[f0] for f0 in f[x]]) if f1 not in f[x]+[x]]]))
print(vr)
