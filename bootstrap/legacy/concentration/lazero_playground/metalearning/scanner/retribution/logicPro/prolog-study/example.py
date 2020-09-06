from pyswip import Prolog
prolog = Prolog()
prolog.consult("map-colored.pl")
a=0
for soln in prolog.query("coloring(A,B,C,D,E)"):
    if a<=10:
        print(soln)
    else:
        break
    a+=1
