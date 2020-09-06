import stackMe

def initBeta(a):
    if len(a)!=0:
        b=a.pop(0)
        if len(a)==0:
            return stackMe.Meta(b)
        else:
            prime=stackMe.Meta(b)
            prime.add(initBeta(a))
            for i in range(b-1):
                prime.duplicate(0)
            return prime

def initMeta(a):
    if len(a)!=0:
        b=a.pop(0)
        if len(a)==0:
            return stackMe.Meta(b)
        else:
            prime=stackMe.Meta(b)
            prime.add(initMeta(a))
            return prime

class Beta:
# need matrix.
    def __init__(self,a):
#		self.dimension=len(a)
        self.scheme=[b for b in a]
        self.core=initBeta(a)

# is this fully usable?
class Meta:
# need matrix.
    def __init__(self,a):
#		self.dimension=len(a)
        self.scheme=[b for b in a]
        self.core=initMeta(a)
		# recursively create the matrix.
		# do this ahead of everything.
		# empty shits?
