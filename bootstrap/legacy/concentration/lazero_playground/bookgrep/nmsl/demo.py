import unicode_charnames
# shall we concern the predefined groups?
# is there any missing alphabet or components?
# hidden candidate everywhere.
u="abcdd_saf98092134[325][436easae]"
u0=[unicode_charnames.charname(x) for x in u]
for u1 in u0:
    print(u1)
