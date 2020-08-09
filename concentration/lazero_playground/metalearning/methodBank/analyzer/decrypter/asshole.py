from tokenize import generate_tokens
from io import BytesIO

def returnTokens(thousands):
    def decistmt(s):
        tokgen = generate_tokens(s.readline)
        v=[x for x in tokgen]
        s.close()
        return v
    h=open(thousands,"r")
    return decistmt(h)
