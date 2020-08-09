# import sys
import os
# print(sys.argv[1])
def storeFile(a=316):
    with open("legacyFuck.sh","w+") as f:
        f.write("#!/bin/bash\n")
        for i in range(a):
            f.write("python3 jerkMe.py "+str(i)+"\n")
    return

storeFile()
os.popen("chmod +x legacyFuck.sh")
# use re Match object instead?
# mother fucking slow! my program is fucking slow!
# return None if no match.
