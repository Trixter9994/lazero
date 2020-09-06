import re
r = """ Backups/            Cookies-journal             rapid_render.json
 blob_storage/       Dictionaries/              'Session Storage'/
 Cache/              GPUCache/                   storage.json
 CachedData/         languagepacks.json          TransportSecurity
 CachedExtensions/   logs/                       User/
'Code Cache'/        machineid
 Cookies            'Network Persistent State'
"""

# we need the mind.
def testif(a, b):
    c = []
    for x in a:
        d = 0
        for y in b:
            if x in y:
                d = 1
                break
        if d == 0:
            c.append(x)
    return c
# strange. really strange.

r0 = re.findall(r'[^/ \n]+', r)
r1 = re.findall(r"'[^']+'", r)
r2 = testif(r0, r1)
# y=""
for x in r1+r2:
    print("rm -rf "+x)
# print(r1)
# print(r2)
# do it now.
# have errors!
# print(r0)
# print(r1)
# print(len(r0))
# well, this cannot be blamed.
# you are well trained but this machine is not complicated enough.
# you can't blame it.
