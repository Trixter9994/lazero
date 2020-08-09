# paste the thing right at this spot.
from tokenize import generate_tokens
from io import BytesIO
#from standardInsult import monad
def returnTokens(thousands):
    def decistmt(s):
        tokgen = generate_tokens(s.readline)
        v=[x for x in tokgen]
        s.close()
        return v
    h=open(thousands,"r")
    return decistmt(h)

name0="../stripOffPants.py"
r=returnTokens(name0)
theory=dir(r[0])
print(theory)
hypothesis=[t for t in theory if t[0] != "_"]
print(["r[0]."+g for g in hypothesis])
print(r[0])
# use ipynb?
kkp=[type(eval("r[0]."+bp)).__name__ for bp in hypothesis]
print(kkp)
print([eval("r[0]."+hypothesis[bp]) if "method" not in kkp[bp] else "blankStuff" for bp in range(len(hypothesis))])
print(r[0].exact_type)
