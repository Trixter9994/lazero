from pyswip import Prolog
prolog = Prolog()
prolog.consult("playAgain.pl")
a=0
for soln in prolog.query("escape(A,B)"):
    if a<=10:
        print(soln["A"], "is escaping from", soln["B"])
    else:
        break
    a+=1
