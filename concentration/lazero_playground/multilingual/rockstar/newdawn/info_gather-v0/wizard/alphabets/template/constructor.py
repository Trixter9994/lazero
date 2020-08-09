def sqlMaker(sauce,plist):
    sql = "INSERT INTO "+sauce[0]+" ( " + sauce[1] +" ) VALUES ( "+plist+" )"
    # you can pass it in pickle format.
    # do it in haskell.
    return sql

def pairMaker(a,b):
    # a and b are both lists
    k=""
    k0=[]
    for a0 in a:
        k += " " + a0 + ","
        if "Id" in a0:
            k0.append(True)
        else:
            k0.append(False)
    k= k[:-1]
    c=""
    # wait then. test.
    for b0 in range(len(b)):
        if k0[b0]== True:
            c+= " "+str(b[b0])+","
        else:
            c+= "'"+b[b0]+"',"
    c =c[:-1]
    return [k,c]

def finalPro(a,c):
    b=pairMaker(a[1],c)
    d=sqlMaker([a[0],b[0]],b[1])
    return d
