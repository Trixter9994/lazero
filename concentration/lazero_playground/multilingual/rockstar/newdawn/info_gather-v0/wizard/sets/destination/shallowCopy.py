def mover(plist,dest):
    with open("shallowCopy.sh","w+") as fuck:
        for term in plist:
            fuck.write('cp '+term+' '+dest+'&\n")
