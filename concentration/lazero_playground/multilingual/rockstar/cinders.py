import re

u = """\t hello you  mother fucker     \t     fuck you bitch      bitch      23443243234  23 42 35 23 5 26  643                        we shall split this fuck by the motherfucking newline should we?
 but you have    fucking told me that you can find that shit somewhere didn't you?
 oh calm the fuck down.          [the fucking tab is invisible here.]
"""

#verbose=re.compile(r'\b')
# print (u.split('\n'));
#print(set(u))
# the most fucking efficient way of doing this fuck.
superset=set(u)
# make it numeric.
#x="撒"
#print(ord(x))
#print(chr(ord(x)))
superlist0=list(map(lambda x: ord(x),superset))
superlist1=sorted(superlist0)
superlist2=list(map(lambda x: chr(x),superlist0))
superlist3=sorted(superlist2)
#superlist3=list(map(lambda x: chr(x),superlist1))
# superfilter=filter(lambda x: )
#print(superlist3)
# better use indexes.
print(len(u))
for index0 in range(len(superlist3)):
    item=superlist3[index0]
    location=[pos for pos, char in enumerate(u) if char == item]
    superlist3[index0]=[item,u.count(item),location]
print(superlist3)
#number is 35 here. so the max index is 35.
#print(superlist3[34])
#print(superlist3[35])
# so the range function could be safe here.

#for item in superlist3:
#    item=[item,u.count(item)]

