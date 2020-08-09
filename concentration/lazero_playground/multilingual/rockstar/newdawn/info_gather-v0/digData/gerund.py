import re
# four version.
shit="aaaaaargh fuck!"
nope="\w+"
mobile=list(re.findall(r'{}'.format(nope),shit))
print(mobile)
