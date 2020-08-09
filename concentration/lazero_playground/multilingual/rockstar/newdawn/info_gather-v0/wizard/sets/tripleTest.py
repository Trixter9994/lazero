def trinity(arb):
    if len(arb)==1:
        return ord(arb)
    elif arb[:2]=="&#":
        return int(arb[2:-1])
    elif '-' in arb:
        a=list(map((lambda x:int(x,16)),arb.split('-')))
        return list(range(a[0],a[1]+1))
    else:
        print("--",len(arb),"brainfucked:",arb,"--")
        return ""
