def snapshot(a,b,c,d,e):
    with open(a,"w+") as ap:
        with open(b,"r") as ad:
            shit=1
            for abo in ad.readlines():
                print(shit)
                print(abo)
                if ( (c in abo) or shit == e):
                    #shit+=1
                    abo = abo.replace(c,d)
#                print(abo)
                    ap.write(abo)
                else:
                    ap.write(abo)
                shit+=1
