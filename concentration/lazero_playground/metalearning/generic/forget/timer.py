import signal

class Meta:
    def __init__(self,a,b,*args):
        self.a=a
        self.b=b
        self.args=args
    def main(self):
        def handler(signum,frame):
            raise Exception("end of time")
# without the exception handler
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(self.b)
        try:
            return self.a(*self.args)
        except Exception:
            return
            # nothing here