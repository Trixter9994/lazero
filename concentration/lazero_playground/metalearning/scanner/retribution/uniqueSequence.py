# to make sure that alike contents and seqences are detected.
from niche import Method2
from matrixPro import Maxima
# maxlength of transformed sequence
# to test alike documents?
def alike(a,b):
    i=(len(a)+0.1)/(len(b)+0.1)
    if i<1.1 and i>0.9:
        return True
    else:
        return Maxima(Method2(a,b))
def fileShare(a,b):
    return [[alike(a0,b0) for a0 in a] for b0 in b]