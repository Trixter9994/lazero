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
def confusionMatrix(a,b):
    return [[a0 == b0 for a0 in a] for b0 in b]
print(confusionMatrix("group","groupChar"))
