import regexgen
import re
# can this thing pass the test?
# this thing is pretty much a beast.
# match the period, match the filter.
# otherwise raise it to higher level.
r=["ee","ff","gg","hh","ii"]
r0=regexgen.to_fuzzy_regEx(r)
# print(type(r0))
# print(dir(r0))
print(r0,[re.match(r'{}'.format(r0[1:-1]),x).group()==x for x in r])
r1=["娱乐","体育"]
r2=regexgen.to_fuzzy_regEx(r1)
print(r2,[re.match(r'{}'.format(r2[1:-1]),x).group()==x for x in r1])
