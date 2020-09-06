def k(a):
    with open(a,"r") as d:
        return d.read()

def k0(a,b):
    with open(a,"w+") as d:
        d.write(b)

k0("peach.py",k("bitch.py")+"\n"+k("standardInsult.py")+"\n"+"print(monad(r[0],globals()))\n")
