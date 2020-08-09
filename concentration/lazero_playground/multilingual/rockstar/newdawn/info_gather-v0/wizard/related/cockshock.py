from newTestN import toyProject
joker=(lambda nope0:nope0[:-1] if nope0[-1]=="\n" else nope0)
greatWall2=(lambda x: "".join([p for p in x if p !=" "]))
poland=(lambda u:list(map((lambda x: greatWall2(x)),u)))
#deutschland=(lambda u:list(map((lambda x: str(int(x,16))),u)))
shit=''
bitch=[]
with open('core.log','r') as fuck:
    shit=fuck.read()
p=[]
with open(joker(shit)+'related.txt','r') as f:
    for j in f.readlines():
        if j[0]!='#' and len(j)>1:
            v0=joker(j).split(':')
            fuckFu=list(filter((lambda x: x!=''),poland(v0[1].split(','))))
            p.append([greatWall2(v0[0]),fuckFu])
            bitch.append(len(fuckFu))
'''
for a,b in enumerate(p):
    print(a,b)'''
for a in p:
    a0=str(int(a[0],16))
    for a1 in a[1]:
        if a1!='':
            toyProject(0,[a0,str(int(a1,16))])
        else:
            print('--shit happened--')
#print('\nthe extreme:',max(bitch),min(bitch))
'''for a in p:
    toyProject(0,[a[1],a[0]])'''
