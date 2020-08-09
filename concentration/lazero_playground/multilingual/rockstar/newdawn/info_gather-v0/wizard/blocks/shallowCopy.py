def mover(plist,dest):
    with open("shallowCopy.sh","w+") as fuck:
        fuck.write('#!/bin/bash\n')
        for term in plist:
            fuck.write('cp '+term+' '+dest+' &\n')
