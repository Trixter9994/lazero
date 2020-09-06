import multiprocessing
#import time
# time limitation versus space limitation
class Meta:
    def __init__(self,a,b,*args):
        self.a=a
        self.b=b
        self.args=args
    def main(self):
        p= multiprocessing.Process(target=self.a,args=tuple(self.args))
        p.start()
        a=p.join(self.b)
        # better be some simple sql processing.
        if p.is_alive():
            p.terminate()
            p.join()
            return
        else:
            return a
