import re

class Meta:
    def __init__(self,a):
        self.regex=[]
        self.content=a
        self.result=[]
    def addRegex(self,a):
        self.regex.append(a)
    def verifyAll(self):
        # raw input.
        self.result=[re.findall(a,self.content) for a in self.regex]
    def getResult(self):
        return self.result
    def getRegex(self,a):
        return [self.regex[b] for b in a]
