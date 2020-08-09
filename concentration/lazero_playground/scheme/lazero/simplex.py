import re
def openfinder(a):
    with open(a,"rb") as f:
        return re.findall(r'[a-zA-Z0-9\-\_]+',str(f.read()))
