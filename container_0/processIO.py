# import asyncio
# import threading
import multiprocessing
# from multiprocessing import Manager
# import time
# import termios
# import fcntl
# import tempfile
# pretend to be a terminal.
# it can do some harm on you. consider a sandbox for everything.
# {SANDBOX}
import time
import subprocess
import os
# write some env to it. both os and popen.
# three fucking python.
# send it into a pseudo terminal like some kind of .js file.
os.environ['TERM'] = 'xterm'
env=os.environ.copy()
# heck!
def run(cmd,ns):
    # await asyncio.sleep(1)
    # just render it into something else.
    # stdin=tempfile.TemporaryFile("w+b")
    proc = subprocess.Popen(
        cmd,stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,env=env)
    # proc.stdin.write(b"junk\n")
    def readline(a,b,c):
        while c.Lock:
            buff=a.readline()
            print(b+buff)
    # they seem to copy the same things several times?
    # only one fucking process when using threading.
    p=multiprocessing.Process(target=readline,args=(proc.stdout,b"stdout: ",ns))
    p0=multiprocessing.Process(target=readline,args=(proc.stderr,b"stderr: ",ns))
    # does not share information?
    p.start()
    p0.start()
    # start another shit.
    # read what?
    # when it is dead, it goes crazy. so share the namespace please?
    # not gonna start.
    proc.stdin.write(b"yes\n")
    proc.stdin.flush()
    #     ik-=1
    # yes it can be killed.
    # how to receive that signal? share the space please?
    # do it there.
    time.sleep(1)
    print("_____theStop_____")
    # not working for process.
    # globlock=False # process have a different namespace though.
    ns.Lock=False
    # but working for threads.
    time.sleep(2)
    # ik=5
    # x=["links","elinks","vim","ps","sed"]
    # while ik>0:
    #     proc.stdin.write(x[ik-1].encode()+b"\n")
    #     proc.stdin.flush()
    #     ik-=1
    #     time.sleep(1)
    proc.kill()
    # print(dir(p))
    p.kill()
    p.terminate()
    p0.kill()
    p0.terminate()
    # p0.n()
    # somehow, that's it.
    # this works.
    # not inserting shit. fuck me please?
    # does not affect?
    # how comes.
    # set the overall value into something else?
    print("_EOL_")
    # or multiprocessing works the same?
    # stdout, stderr = await proc.communicate()
    # print(f'[{cmd!r} exited with {proc.returncode}]')
    # if stdout:
    #     print(f'[stdout]\n{stdout.decode()}')
    # if stderr:
    #     print(f'[stderr]\n{stderr.decode()}')
# somewhat works.
if __name__ == "__main__":
    multiprocessing.freeze_support()
    mgr = multiprocessing.Manager()
    ns = mgr.Namespace()
    ns.Lock=True
    run('bash',ns)
    print("AHEAD OF TIME")