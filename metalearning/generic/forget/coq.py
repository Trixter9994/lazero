import time
def metaLog():
    return int(round(time.time()*10))
class Meta:
    # better use timestamp
    # shall this be a thread?
    def __init__(self,a):
#        self.birth=time
        self.death=metaLog()+a
        self.name=None
    def voke(self,a):
        self.name=a
    def revoke(self):
        if self.death<=metaLog():
            self.name=None
    def returnName(self):
        return self.name
# what the hell?
