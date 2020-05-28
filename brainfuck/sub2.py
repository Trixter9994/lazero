from threading import Thread
import functools
# notice, you might need to write a browser?
# you draw outline for us?
# well, i can rewrite this.
def timeout(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (
                func.__name__, timeout))]
                # so-called deep understanding of python func names.
                # it is about remembering and forgetting.
                # that's learning.
            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                  # this is funny.
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as je:
                print('error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco
